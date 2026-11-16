# 操作参考

以下参数以本版本 Schema 为准，调用前使用 connection_describe 读取完整契约。

## search

按关键词读取公开视频搜索结果；可能受平台风控限制。

性质：read。
- `query`（必填）：关键词。约束：`{"type": "string"}`。
- `limit`（可选）：条数。约束：`{"type": "integer", "default": 5, "minimum": 1, "maximum": 20}`。

## read

通过 bili-cli video 读取视频详情。输入 BV 号或 HTTPS Bilibili 视频链接。

性质：read。
- `target`（必填）：BV 号或 Bilibili 视频链接。约束：`{"type": "string", "pattern": "^(?:https://(?:www\\.)?bilibili\\.com/video/)?BV[0-9A-Za-z]{10}/?(?:\\?[^\\s]*)?$"}`。

## hot

读取 Bilibili 第一页热门视频。

性质：read。
- `limit`（可选）：条数。约束：`{"type": "integer", "default": 10, "minimum": 1, "maximum": 20}`。

最小参数示例：`{}`。

## subtitle

读取指定分 P 的字幕，默认第 1 P。复用 bili-cli 原生登录状态；无字幕明确报错。

性质：read。
- `target`（必填）：BV 号或 Bilibili 视频链接。约束：`{"type": "string", "pattern": "^(?:https://(?:www\\.)?bilibili\\.com/video/)?BV[0-9A-Za-z]{10}/?(?:\\?[^\\s]*)?$"}`。
- `part`（可选）：分 P 编号。约束：`{"type": "integer", "default": 1, "minimum": 1, "maximum": 10000}`。

## parts

列出同一 BV 视频的所有分 P：编号、CID、标题与时长。

性质：read。
- `target`（必填）：BV 号或 Bilibili 视频链接。约束：`{"type": "string", "pattern": "^(?:https://(?:www\\.)?bilibili\\.com/video/)?BV[0-9A-Za-z]{10}/?(?:\\?[^\\s]*)?$"}`。
