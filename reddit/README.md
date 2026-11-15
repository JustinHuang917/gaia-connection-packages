# Reddit 浏览器连接 1.0.2

对齐 Agent-Reach RedditChannel 的三个只读操作：

| 操作 | 参数 | 行为 |
|---|---|---|
| search | query、limit（默认5，最多20） | 搜索公开帖子 |
| read | target（帖子ID、reddit.com链接或redd.it链接） | 返回帖子及最多20条实际加载的评论，合并正文，同时保留raw.post/raw.comments |
| subreddit | name（可带r/）、limit（默认5，最多20） | 社区最新帖子 |

当前采用 Reddit 官方旧版 HTML 页面（old.reddit.com），不调用匿名 JSON 接口，不自动绕过登录、验证码或平台限制。公开操作不强制登录。手动登录使用 www.reddit.com，同租户浏览器目录保存网站会话。

Agent-Reach 的实际后端是 OpenCLI；本包对齐其操作语义，复用现有租户 Chromium 与显式页面读取阶段，没有另行安装 OpenCLI。

结果字段按页面实际展示返回：title/url/author/text/published_at/score/subreddit/comments，缺失省略。coverage=visible，不承诺完整评论历史；comments_state=not_observed 表示没有观察到评论，不能解释为帖子没有评论。平台403或429会报错，不会伪装成空数据成功。

2026-11-08 当前测试出口访问公开搜索和社区页受到平台限制，返回 PLATFORM_BLOCKED；真实登录后的数据读取需用户验收。包契约、参数解析、公开路径无需登录和正文评论合并已自动化验证。

授权探测访问 `/login/`，识别该地址上明确的“你已登录”文案；主页则展开用户菜单后检查设置链接。不以“欢迎回来”或仅有头像判定登录。2026-11-08 真实容器会话检测返回 completed / ready；此结论仅验证授权，不代表公开帖子读取已通过。
