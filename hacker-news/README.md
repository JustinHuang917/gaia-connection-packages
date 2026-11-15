# Hacker News
独立只读适配包。官方 Firebase API，公开访问，无需登录。配置为 {}。
list_top/list_new 返回消息 ID，get_item 读取详情。不使用模拟数据。

## 1.1.0 讨论读取

`discussion(target, limit=30, depth=3)`：target 为帖子 ID 或 `https://news.ycombinator.com/item?id=50410107`。使用官方 Firebase item/kids API，按提供方顺序读取嵌套评论；返回作者、时间、HTML 正文、父 ID、children。跳过 deleted/dead 条目，但仍计入请求预算。`comments_loaded` 为实际评论数，`truncated` 表示预算或深度限制，不能据此视为全部讨论。limit 最大 50，depth 最大 5。
