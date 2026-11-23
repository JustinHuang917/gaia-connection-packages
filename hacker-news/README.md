# Hacker News 2.0.0：声明式浏览器包

与小红书采用同一 browser runtime，仅通过 adapter.yaml 与 schemas/operations.json 描述操作，无站点专属 Python/JavaScript 代码。公开网页，无需登录，配置 {}，只允许 news.ycombinator.com。

- list_top / list_new：分别读取首页与 /newest，使用 records 提取最多 30 条完整新闻。返回 data={url,items,state,coverage}；每个 item 有 id/title/url/comments_url/score/descendants/by/time。应用读取 result.data.items，不再逐条 get_item。
- get_item(id)：读取 /item?id={id}，返回 data.items 中的帖子详情。
- discussion(id)：同一页面提取帖子和前 50 条已加载评论，按 DOM 顺序平铺；评论位于 items[0].raw.comments，并提供 comments_loaded/comments_state，不保证完整评论树，不自动翻页。

缺失的网页元数据返回 null，不伪造评分、作者、时间或评论数。页面结构改变、必填字段缺失、整数解析失败均明确报错，不作为空榜单。浏览器处理提供方页面脚本，页面内容仍是不可信数据。

本版为破坏性升级：旧版榜单返回 ID 数组，现为标准浏览器 records 包装。discussion 参数改为 id，不保留旧 Firebase、target/limit/depth 或 HTTP 解析回退。更新包、重新发布连接契约、重新构建应用。

Worker 的通用字段规则：scope=next_sibling 从相邻 DOM 元素提取，:scope 读取元素自身；attribute 获取属性，pattern 提取首个捕获组，type=integer 严格转安全整数，values 进行显式文本映射，nullable 保留缺失值，required 缺失时报错。既有选择器和字符串字段无需修改。
