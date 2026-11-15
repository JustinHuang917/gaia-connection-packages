# Instagram 浏览器连接
通过平台管理的 Linux Chromium 浏览器运行。用户在受控远程窗口完成真实登录；验证码和 MFA 不由 Agent 处理。
操作：profile 读取主页标题与简介，posts 读取当前页面已展示的帖子链接。
本包采用平台 Playwright 引擎，不依赖 OpenCLI 扩展，保持声明式操作入口。未来引入 OpenCLI 应新增经过验证的引擎适配，不执行任意 shell。
浏览器 profile 为连接独占，不导出 Cookie。网站风控、登录失败和页面改版均真实报错。PoC 不是生产网络隔离验收。
