# 操作参考

以下参数以本版本 Schema 为准，调用前使用 connection_describe 读取完整契约。

## read

读取标题、频道、发布日期、简介和统计，不下载视频。

性质：read。
- `target`（必填）：视频 ID 或 HTTPS YouTube 链接。约束：`{"type": "string"}`。

## search

搜索公开 YouTube 视频。

性质：read。
- `query`（必填）：关键词。约束：`{"type": "string"}`。
- `limit`（可选）：条数。约束：`{"type": "integer", "default": 5, "minimum": 1, "maximum": 20}`。

## subtitle

读取人工或自动字幕，按语言优先级选择一份。无字幕明确报错，不做语音转写。

性质：read。
- `target`（必填）：视频 ID 或 HTTPS YouTube 链接。约束：`{"type": "string"}`。
- `lang`（可选）：逗号分隔，最多六种语言，如 zh-Hans,en。。约束：`{"type": "string", "default": "zh-Hans,zh,zh-CN,zh-TW,en,en-orig"}`。
