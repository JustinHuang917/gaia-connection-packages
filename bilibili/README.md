# Bilibili 2.1.0 — bili-cli

独立声明式适配包，复用节点安装的 bili-cli 0.6.2（bilibili-api-python 17.4.2）。旧版直接 HTTP 实现已移除，无 API 回退。

操作：search(query,limit=5)、read(target)、hot(limit=10)、parts(target)、subtitle(target,part=1)。target 支持 BV 号或 HTTPS bilibili.com/video/BV 链接；limit 1–20。返回 data 为上游 CLI JSON，backend=bili-cli。parts 返回所有分 P 的编号、CID、标题和时长。subtitle 按 1 开始的编号读取指定 P，默认第 1 P；越界明确报 PART_NOT_FOUND。需要有效登录与可用字幕，缺失时明确报错。搜索/详情/热门调用原生 CLI；parts/指定 P 字幕复用同环境的 SDK 与原生登录，不修改上游完整 CLI 分支。

页面点击登录，执行真实 `bili login` 同一 CLI 入口；展示原生终端二维码转换的 SVG，用户用 Bilibili App 扫码确认，再点击检查授权。只有原生登录成功且 `bili status --json` 确认身份后才标记已登录。退出执行 bili logout。凭据保存在 Linux 节点连接私有 HOME 的 .bilibili-cli/credential.json（权限600），不回传到 UI。服务端仅存原生登录标记，不伪造凭据到期时间；身份验证以 CLI 实际结果为准。

Node 仅允许上述固定命令，不执行包内 shell/Python 命令。bwrap 挂载独立 HOME，CLI 使用库的公开代理设置和平台域名出口白名单，不访问用户宿主浏览器目录。与现有浏览器 PoC 相同，当前 share-net 加应用代理不是内核级网络隔离，生产节点仍需更强网络隔离。

2026-11-08：真实 CLI search、read、hot 成功；原生登录二维码生成成功。扫码和登录后字幕仍需用户完成验收，未冒充通过。

## 扫码解析修订

bilibili-api-python 17.4.2 的 WEB 扫码实现只解析 redirect URL query，并将未知状态当作 DONE。PoC 固定版本启动适配在保留上游二维码生成、bili login 流程和凭据写入器的前提下，校验轮询 code=0 且非空 SESSDATA，并从公开 BiliAPIResponse.cookies 或 query 提取。未知状态、缺失会话不得保存为成功。修订覆盖 Cookie/query/未知状态/空会话测试；真实扫码需用户再次确认，未宣称通过。

后续修正：严格解析层仍使用固定版本 Api._prepare_request 保留原生请求头与自动 Cookie；不能直接裸调用 get_client.request，否则可能在扫码前触发412。失败仅回传白名单 BILI_QR_* 错误码，不记录原始响应或凭据。当前真实未扫码轮询连续返回 waiting，完整扫码仍待用户确认。

原生登录状态契约：CLI poll_auth 返回 completed + verified + identity，控制面保存身份元数据，不走要求 access_token 的 OAuth 密钥保存流程。节点重启后可用 bili status 核验持久会话，避免要求重复扫码。控制面完整流程回归已覆盖无 Token 完成和重复检查。

## 运行器目录

平台实现统一在 `native/bilibili/`：launcher.py（原生 CLI 和扩展入口）、login.py（固定版本扫码解析修订）、worker.py（命令与登录生命周期）、video.py（分 P 和指定字幕）。cli_node.py 负责沙箱监督，镜像 COPY 和挂载均使用新目录；旧根目录入口已删除。

2026-11-08 真实验证：BV1ABcsztEcY 返回 1 P；BV1wD4y1o7AS 返回 200 P，第二 P 字幕 2511 字符，CID 与列表第二项一致。39项测试通过。当前 tenant-a 连接已升级2.1.0，保留原有登录。
