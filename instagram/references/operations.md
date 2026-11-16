# 操作参考

以下参数以本版本 Schema 为准，调用前使用 connection_describe 读取完整契约。

## profile

读取指定用户主页的标题与公开简介。

性质：read。
- `username`（必填）：Instagram 用户名。约束：`{"type": "string", "pattern": "^[A-Za-z0-9_.]{1,30}$"}`。

## posts

读取页面实际展示的帖子链接；未加载的数据不会补造。

性质：read。
- `username`（必填）：Instagram 用户名。约束：`{"type": "string", "pattern": "^[A-Za-z0-9_.]{1,30}$"}`。
- `limit`（可选）：最多条数。约束：`{"type": "integer", "default": 6, "minimum": 1, "maximum": 20}`。
