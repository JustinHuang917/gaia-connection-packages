# 操作参考

以下参数以本版本 Schema 为准，调用前使用 connection_describe 读取完整契约。

## search

搜索实际可见的推文，返回正文、作者、时间和链接。

性质：read。
- `query`（必填）：搜索词。约束：`{"type": "string"}`。
- `limit`（可选）：最多条数。约束：`{"type": "integer", "default": 5, "minimum": 1, "maximum": 20}`。

## profile

读取用户简介、位置、网站、加入时间和关注信息；未展示字段省略。

性质：read。
- `username`（必填）：X 用户名（不带 @）。约束：`{"type": "string", "pattern": "^[A-Za-z0-9_]{1,15}$"}`。

## tweets

读取指定用户当前可加载的最近推文；含正文，不承诺完整历史。

性质：read。
- `username`（必填）：X 用户名（不带 @）。约束：`{"type": "string", "pattern": "^[A-Za-z0-9_]{1,15}$"}`。
- `limit`（可选）：最多条数。约束：`{"type": "integer", "default": 5, "minimum": 1, "maximum": 20}`。

## thread

读取目标推文及当前可加载的回复，不保证完整评论流。

性质：read。
- `target`（必填）：推文 ID 或 X/Twitter 链接。约束：`{"type": "string", "pattern": "^(?:[0-9]+|https://(?:www\\.)?(?:x\\.com|twitter\\.com)/(?:[A-Za-z0-9_]+/status|i/status)/[0-9]+/?(?:\\?[^#]*)?)$"}`。
