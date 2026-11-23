# 操作参考

包使用 browser runtime，与小红书采用相同声明式执行器，所有结果均为浏览器标准包装。

## list_top / list_new

参数 limit：整数，1–30，默认 10。返回 data.items，完整新闻条目按提供方页面顺序排列，不包含自动详情请求。元数据不存在时为 null。

## get_item

参数 id：正整数，必填。返回 data.items 中的帖子详情，不加载评论树。

## discussion

参数 id：正整数，必填。返回帖子与已加载前 50 条评论；items[0].raw.comments 为平铺评论，comments_loaded/comments_state 表示本次读取覆盖范围。不自动翻页、不返回完整树，也不推断未加载的评论内容。
