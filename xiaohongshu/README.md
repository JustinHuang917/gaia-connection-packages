# 小红书浏览器连接包

参考 Agent-Reach 的 `channels/xiaohongshu.py` 操作边界；`xiaoyuzhou.py` 实际为小宇宙播客，并非小红书。

复用现有租户浏览器机制：用户在普通 Chromium 里手动扫码/登录，账号状态保留在节点租户浏览器私有目录。检查授权及操作阶段通过现有浏览器检查器读取页面，不导出Cookie给Agent/App，不增加逆向签名API或写操作。

## 操作

- `search(query, limit=5)`：最多20条已加载笔记，返回标题、作者、点赞与完整链接。
- `read(target)`：读取正文及最多20条已加载评论，保留正文/评论原始结构。
- `comments(target, limit=20)`：最多50条已加载评论/回复；不自动展开隐藏回复，不是完整评论导出。

阅读请优先使用搜索返回的完整链接，保留 `xsec_token` 等访问参数。也接受 `https://xhslink.com/…` 分享链接，节点出口仍限制在声明域名。该包不实现发布、点赞、收藏、关注、下载。

## 验收

1. 刷新PoC，适配包中导入「小红书浏览器包」，审核并创建连接。
2. 点击登录，在远程浏览器完成小红书登录，再返回检查授权。
3. 搜索“咖啡”，复制结果中的完整笔记URL，依次测试read/comments。

当前实现的是可见DOM读取。页面加载失败不返回虚构空列表；登录标识或DOM发生变化会明确报告待登录/内容未就绪。验证码、站点风控需用户在浏览器处理。必须完成一次真实用户登录，才能完成搜索/正文/评论的真实业务验收。允许站点官方重定向到国际版rednote.com，使用当前页面的实际登录状态；支持两种域名的完整笔记URL，不跨域复制Cookie。

登录与授权检查统一访问 `https://www.xiaohongshu.com/explore`，搜索访问 `https://www.xiaohongshu.com/search_result`。以 `li.user.side-bar-component` 内指向 `/user/profile/` 的 `a.link-wrapper` 判断登录，不固定账号ID。站点自身重定向仍受允许域名策略约束。
