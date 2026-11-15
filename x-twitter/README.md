# X / Twitter 浏览器连接 1.1.0

对齐 Agent-Reach `agent_reach/channels/twitter.py` 的四个只读操作：

| 操作 | 参数 | 返回 |
|---|---|---|
| search | query、limit（默认5，最多20） | 搜索结果推文 |
| profile | username（不带@） | 简介、网站、加入时间、关注与粉丝信息等实际展示字段 |
| tweets | username、limit（默认5，最多20） | 最近可加载推文，含正文 |
| thread | target（推文ID或X/Twitter链接） | 目标页面的推文与可加载回复 |

推文字段包括 url、text、author、published_at，以及页面实际展示的 replies/reposts/likes 描述。未展示字段省略，不猜测数值。结果标识 `coverage: visible`，不保证完整历史或完整评论流。最多滚动三次；线程最多取30条记录。

Agent-Reach 本身不实现 Twitter API：它调用 OpenCLI，经浏览器扩展和本地守护进程控制已登录浏览器，再把结果转成统一 item。当前 PoC 对齐其操作语义，继续使用已验证的租户 Chromium + 显式 Playwright 读取阶段，没有安装 OpenCLI 扩展或读取个人浏览器 Cookie。

页面异步加载必须等到实际记录出现；未加载成功报 CONTENT_NOT_READY，不能把空壳页面当作成功。仅观察到包中声明的空状态元素时，才返回 state=empty。

登录和平台挑战由用户手动完成。连接共用租户浏览器目录，授权信息不进入返回结果。只读测试：`.venv/bin/python linux/verify_x.py`，需要已批准的新包与有效登录。
