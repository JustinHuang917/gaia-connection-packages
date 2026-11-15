"""Public Hacker News Firebase API; no authentication or simulated data."""
BASE='https://hacker-news.firebaseio.com/v0/'
def test_connection(ctx,args):
    value=ctx.request(BASE+'topstories.json')
    if not isinstance(value,list):raise ValueError('Expected story ID array')
    return {'verified':True,'identity':'Hacker News public API','item_count':len(value)}
def invoke(ctx,args):
    operation=args['operation'];values=args['arguments']
    if operation in {'list_top','list_new'}:
        data=ctx.request(BASE+{'list_top':'topstories.json','list_new':'newstories.json'}[operation])
        if not isinstance(data,list):raise ValueError('Expected story ID array')
        return data[:values.get('limit',10)]
    if operation=='discussion':return discussion(ctx,values)
    if operation=='get_item':return ctx.request(BASE+'item/'+str(values['id'])+'.json')
    raise ValueError('Unknown operation')

def discussion(ctx,values):
    import re
    target=str(values['target'])
    match=re.fullmatch(r'(?:https://news\.ycombinator\.com/item\?id=)?([1-9][0-9]*)',target)
    if not match:raise ValueError('Expected Hacker News item ID or HTTPS item link')
    item=ctx.request(BASE+'item/'+match.group(1)+'.json')
    if not isinstance(item,dict):raise ValueError('Hacker News item not found')
    limit=values.get('limit',30);depth=values.get('depth',3)
    count=0;requests=0;truncated=False;seen=set()
    def children(ids,level):
        nonlocal count,requests,truncated
        rows=[]
        for ident in ids:
            if level>depth or requests>=limit:
                truncated=True;break
            if ident in seen:continue
            seen.add(ident);requests+=1
            comment=ctx.request(BASE+'item/'+str(ident)+'.json')
            if not isinstance(comment,dict):raise ValueError('Comment unavailable during discussion read')
            if comment.get('deleted') or comment.get('dead'):
                rows.extend(children(comment.get('kids',[]),level));continue
            count+=1
            row={k:comment[k] for k in ('id','parent','by','time','text') if k in comment}
            row['children']=children(comment.get('kids',[]),level+1);rows.append(row)
        return rows
    comments=children(item.get('kids',[]),1)
    return {'item':{k:v for k,v in item.items() if k!='kids'},'comments':comments,
            'comments_loaded':count,'requests':requests,'truncated':truncated,'depth':depth,
            'text_format':'html','order':'provider'}
