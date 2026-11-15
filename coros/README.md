# COROS gateway
真实网络连接。协议来源：本仓库 skills/coros_mcp_login_gateway/scripts/coros_mcp_login.py。
不读取用户 HOME 或旧授权缓存。用户在 COROS 官方页面登录；凭据经宿主专用 IPC 加密存储。
必须审阅批准包摘要后再创建连接，配置 JSON 为 {}。
list_tools 真实发现目录；query_user 调用 queryUserInfo；query_sport_records 依据工具协议查询。
不宣称未经实际调用的接口已通过。退出登录只清除本平台凭据，不代表撤销提供方授权。
