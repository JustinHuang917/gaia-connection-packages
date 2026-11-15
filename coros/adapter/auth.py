"""Real COROS gateway protocol adapted from the repository Skill. No host cache access."""
import base64
import hashlib
import json
import secrets
import time
from urllib.parse import urlencode, urlsplit, parse_qs

HOSTS={'mcp.coros.com','mcpcn.coros.com','mcpeu.coros.com','mcpus.coros.com'}
REDIRECT='http://127.0.0.1:43123/callback'
SCOPE='openid offline_access mcp.tools'

def start_auth(ctx,args):
    discovery=ctx.request('https://mcp.coros.com/.well-known/openid-configuration')
    issuer=discovery['issuer'].rstrip('/')
    u=urlsplit(issuer)
    if u.scheme!='https' or u.hostname not in HOSTS or u.path or u.query or u.port:raise ValueError('Unapproved issuer')
    client=ctx.request(issuer+'/connect/register','POST',{'client_name':'Gaia Connection PoC','redirect_uris':[REDIRECT],'grant_types':['authorization_code','refresh_token'],'response_types':['code'],'scope':SCOPE,'token_endpoint_auth_method':'none'})['client_id']
    verifier=secrets.token_urlsafe(48);state=secrets.token_urlsafe(24)
    challenge=base64.urlsafe_b64encode(hashlib.sha256(verifier.encode()).digest()).decode().rstrip('=')
    authorize=issuer+'/oauth2/authorize?'+urlencode({'response_type':'code','client_id':client,'redirect_uri':REDIRECT,'scope':SCOPE,'code_challenge':challenge,'code_challenge_method':'S256','resource':issuer+'/mcp','state':state})
    session=ctx.request(issuer+'/api/v1/cli/login-sessions','POST',{'clientId':client})
    login=session['loginUrl'];host=urlsplit(login)
    if host.scheme!='https' or host.hostname not in HOSTS:raise ValueError('Unexpected login URL')
    ctx.save_state({'issuer':issuer,'client_id':client,'verifier':verifier,'state':state,'authorize':authorize,'session_id':session['sessionId'],'poll_token':session['pollToken']})
    return {'state':'waiting','action':{'type':'open_url','url':login}}

def save_token(ctx,payload,issuer,client,old=None):
    if not payload.get('access_token'):raise ValueError('Token response missing access token')
    ctx.save_credential({'access_token':payload['access_token'],'refresh_token':payload.get('refresh_token',(old or {}).get('refresh_token','')),'token_type':payload.get('token_type','Bearer'),'expires_at':time.time()+int(payload.get('expires_in',3600)),'issuer':issuer,'client_id':client})

def poll_auth(ctx,args):
    s=ctx.state();issuer=s['issuer']
    claim=ctx.request(issuer+'/api/v1/cli/login-sessions/'+s['session_id']+'/claim','POST',headers={'X-Poll-Token':s['poll_token']})
    if claim.get('status')=='pending':return {'state':'waiting'}
    if claim.get('status')!='authorized':raise ValueError('Login not authorized or expired')
    response=ctx.http_response(s['authorize']+'&'+urlencode({'login_ticket':claim['loginTicket']}))
    location=next((v for k,v in response['headers'].items() if k.lower()=='location'),'')
    if response['status'] not in (302,303):raise ValueError('Authorization redirect missing')
    callback=urlsplit(location)
    if callback.scheme!='http' or callback.hostname!='127.0.0.1' or callback.port!=43123 or callback.path!='/callback':raise ValueError('Unexpected callback')
    query=parse_qs(callback.query)
    if query.get('state',[''])[0]!=s['state']:raise ValueError('Authorization state mismatch')
    payload=ctx.request(issuer+'/oauth2/token','POST',{'grant_type':'authorization_code','client_id':s['client_id'],'code':query['code'][0],'redirect_uri':REDIRECT,'code_verifier':s['verifier']},{'Content-Type':'application/x-www-form-urlencoded'})
    save_token(ctx,payload,issuer,s['client_id']);ctx.save_state({});return {'state':'completed'}

def refresh_auth(ctx,args):
    c=ctx.credential()
    payload=ctx.request(c['issuer']+'/oauth2/token','POST',{'grant_type':'refresh_token','client_id':c['client_id'],'refresh_token':c['refresh_token']},{'Content-Type':'application/x-www-form-urlencoded'})
    save_token(ctx,payload,c['issuer'],c['client_id'],c);return {'state':'completed'}

def rpc(ctx,method,params):
    c=ctx.credential();headers={'Authorization':c.get('token_type','Bearer')+' '+c['access_token'],'Accept':'application/json, text/event-stream'}
    response=ctx.request(c['issuer']+'/mcp','POST',{'jsonrpc':'2.0','id':1,'method':method,'params':params},headers)
    if response.get('error'):raise ValueError('MCP request rejected')
    return response.get('result',{})

def initialize(ctx):
    return rpc(ctx,'initialize',{'protocolVersion':'2025-06-18','capabilities':{},'clientInfo':{'name':'gaia-connection-poc','version':'1.0'}})

def test_connection(ctx,args):
    initialize(ctx);catalog=rpc(ctx,'tools/list',{})
    if not isinstance(catalog.get('tools'),list):raise ValueError('MCP tools discovery failed')
    return {'verified':True,'identity':'COROS · '+urlsplit(ctx.credential()['issuer']).hostname,'tool_count':len(catalog['tools'])}

def invoke(ctx,args):
    initialize(ctx)
    if args['operation']=='list_tools':return rpc(ctx,'tools/list',{})
    name={'query_user':'queryUserInfo','query_sport_records':'querySportRecords'}[args['operation']]
    return rpc(ctx,'tools/call',{'name':name,'arguments':args['arguments']})
