# YouTube 连接包

独立包，使用节点内固定版本的 yt-dlp，支持节点 Chromium 登录，将 YouTube Cookie 保存到租户下该连接的私有目录；yt-dlp 仅在节点本地读取 Cookie，不向 Agent、App 或控制端返回凭据。未登录时仍可尝试公开访问。

在「适配包」导入 YouTube 包，审核后创建连接，再在连接测试中选择操作：

- `search(query, limit=5)`：搜索视频，最多 20 条。
- `read(target)`：读取视频标题、简介、作者、发布时间、时长和统计信息。
- `subtitle(target, lang="zh-Hans,zh,zh-CN,zh-TW,en,en-orig")`：优先读取指定语言的人工或自动字幕，返回纯文本；不下载视频，不进行语音转写。

`target` 接受视频 ID 或 YouTube 视频链接。字幕不可用会返回 `SUBTITLE_UNAVAILABLE`；平台验证、限流和超时分别报告，不将失败包装为空数据。

Linux 浏览器节点镜像包含 yt-dlp 及 Deno。代理沿用节点全局代理设置。`transcribe` 不在本包中。

点击连接的「登录」，打开远程浏览器并完成 YouTube 登录，然后返回「检查授权」。检测到头像按钮后导出 Cookie；Cookie 文件权限为 600。点击退出授权删除此连接保存的 Cookie；浏览器网站会话仍保留，要彻底退出需在 YouTube 网站操作。Cookie 失效或遇到平台验证时重新登录。
