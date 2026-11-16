# 操作参考

以下参数以本版本 Schema 为准，调用前使用 connection_describe 读取完整契约。

## search

搜索 Reddit 公开帖子；平台限制时明确报错。

性质：read。
- `query`（必填）：搜索词。约束：`{"type": "string"}`。
- `limit`（可选）：最多条数。约束：`{"type": "integer", "default": 5, "minimum": 1, "maximum": 20}`。

## read

读取指定帖子及最多20条已加载评论，合并正文并保留原始帖子/评论结构。

性质：read。
- `target`（必填）：Reddit 帖子链接或 ID。约束：`{"type": "string", "pattern": "^(?:https://(?:(?:www\\.|old\\.)?reddit\\.com/(?:r/[A-Za-z0-9_]+/)?comments/|redd\\.it/))?([A-Za-z0-9]+)(?:/[^?]*)?(?:\\?.*)?$"}`。

## subreddit

读取社区最新帖子；社区名称可带 r/ 前缀。

性质：read。
- `name`（必填）：社区名称。约束：`{"type": "string", "pattern": "^(?:r/)?[A-Za-z0-9_]{2,21}$"}`。
- `limit`（可选）：最多条数。约束：`{"type": "integer", "default": 5, "minimum": 1, "maximum": 20}`。
