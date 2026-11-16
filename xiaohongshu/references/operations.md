# 操作参考

以下参数以本版本 Schema 为准，调用前使用 connection_describe 读取完整契约。

## search

使用登录浏览器搜索，最多返回20条已加载笔记，保留笔记访问参数。

性质：read。
- `query`（必填）：关键词。约束：`{"type": "string"}`。
- `limit`（可选）：最多条数。约束：`{"type": "integer", "default": 5, "minimum": 1, "maximum": 20}`。

## read

读取正文与已加载评论；页面限制或尚未加载时明确报错，不导出完整评论历史。

性质：read。
- `target`（必填）：优先粘贴搜索结果的完整URL，保留xsec_token；支持xhslink.com短链接。。约束：`{"type": "string", "pattern": "^https://(?:(?:www\\.)?(?:xiaohongshu|rednote)\\.com/(?:explore|search_result)/[A-Za-z0-9_-]+|xhslink\\.com/[A-Za-z0-9/_-]+)(?:\\?[^\\s#]*)?(?:#[^\\s]*)?$"}`。

## comments

读取页面已加载评论及回复，不展开未加载的回复，不代表全部评论。最多50条。

性质：read。
- `target`（必填）：优先粘贴搜索结果的完整URL，保留xsec_token；支持xhslink.com短链接。。约束：`{"type": "string", "pattern": "^https://(?:(?:www\\.)?(?:xiaohongshu|rednote)\\.com/(?:explore|search_result)/[A-Za-z0-9_-]+|xhslink\\.com/[A-Za-z0-9/_-]+)(?:\\?[^\\s#]*)?(?:#[^\\s]*)?$"}`。
- `limit`（可选）：最多条数。约束：`{"type": "integer", "default": 20, "minimum": 1, "maximum": 50}`。
