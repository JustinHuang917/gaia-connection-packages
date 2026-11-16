# 操作参考

以下参数以本版本 Schema 为准，调用前使用 connection_describe 读取完整契约。

## read

无登录态浏览器渲染 HTTPS 公网页面，返回标题、正文和链接。不会读取其他连接的账号状态，不绕过登录或验证码。

性质：read。
- `url`（必填）：网页地址。约束：`{"type": "string", "pattern": "^https://"}`。
- `max_chars`（可选）：最多正文字符。约束：`{"type": "integer", "default": 12000, "minimum": 100, "maximum": 30000}`。

## find

在当前渲染页面的可见正文中查找字面关键词（不区分大小写），返回字符位置和上下文。不自动展开或翻页。

性质：read。
- `url`（必填）：网页地址。约束：`{"type": "string", "pattern": "^https://"}`。
- `keyword`（必填）：关键词。约束：`{"type": "string", "pattern": "\\S"}`。
- `limit`（可选）：最多匹配条数。约束：`{"type": "integer", "default": 20, "minimum": 1, "maximum": 100}`。
- `context_chars`（可选）：匹配词前后各保留多少个 Unicode 字符；0 只返回匹配词。。约束：`{"type": "integer", "default": 100, "minimum": 0, "maximum": 2000}`。
