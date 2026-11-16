# 操作参考

以下参数以本版本 Schema 为准，调用前使用 connection_describe 读取完整契约。

## list_top

按官方热门榜顺序返回消息 ID。

性质：read。
- `limit`（可选）：条数。约束：`{"type": "integer", "default": 10, "minimum": 1, "maximum": 100}`。

最小参数示例：`{}`。

## list_new

按官方最新榜顺序返回消息 ID。

性质：read。
- `limit`（可选）：条数。约束：`{"type": "integer", "default": 10, "minimum": 1, "maximum": 100}`。

最小参数示例：`{}`。

## get_item

根据消息 ID 获取标题、链接、评分与评论等真实内容。

性质：read。
- `id`（必填）：消息 ID。约束：`{"type": "integer", "minimum": 1}`。

## discussion

输入 HN 帖子 ID 或链接，读取真实评论树。limit 为最多评论请求数，depth 为层级；正文为 HTML。

性质：read。
- `target`（必填）：帖子 ID 或链接。约束：`{"type": "string", "pattern": "^(?:https://news\\.ycombinator\\.com/item\\?id=)?[1-9][0-9]*$"}`。
- `limit`（可选）：limit。约束：`{"type": "integer", "default": 30, "minimum": 1, "maximum": 50}`。
- `depth`（可选）：depth。约束：`{"type": "integer", "default": 3, "minimum": 1, "maximum": 5}`。
