# 操作参考

以下参数以本版本 Schema 为准，调用前使用 connection_describe 读取完整契约。

## analyst_targets

第三方分析师数据，不是本平台预测。

性质：read。
- `market`（必填）：市场。约束：`{"type": "string", "default": "HK", "enum": ["HK", "US"]}`。
- `symbol`（必填）：只填代码：SH600519 / 00700 / NVDA。约束：`{"type": "string"}`。
- `provider`（可选）：公开数据源。约束：`{"type": "string", "default": "auto", "enum": ["auto", "yfinance"]}`。
- `limit`（可选）：最多返回行数。约束：`{"type": "integer", "default": 20, "minimum": 1, "maximum": 100}`。

## board_members

查询已知行业或概念名称的成分股。

性质：read。
- `market`（必填）：市场。约束：`{"type": "string", "default": "CN", "enum": ["CN"]}`。
- `provider`（可选）：公开数据源。约束：`{"type": "string", "default": "auto", "enum": ["auto", "akshare"]}`。
- `limit`（可选）：最多返回行数。约束：`{"type": "integer", "default": 20, "minimum": 1, "maximum": 100}`。
- `board_type`（可选）：板块类型。约束：`{"type": "string", "default": "industry", "enum": ["industry", "concept"]}`。
- `board`（必填）：板块名称。约束：`{"type": "string"}`。

## capital_flow

东方财富资金流口径。

性质：read。
- `market`（必填）：市场。约束：`{"type": "string", "default": "CN", "enum": ["CN"]}`。
- `symbol`（必填）：只填代码：SH600519 / 00700 / NVDA。约束：`{"type": "string"}`。
- `provider`（可选）：公开数据源。约束：`{"type": "string", "default": "auto", "enum": ["auto", "akshare"]}`。
- `limit`（可选）：最多返回行数。约束：`{"type": "integer", "default": 20, "minimum": 1, "maximum": 100}`。

## chip_distribution

提供商估计模型，不是实际账户持仓。

性质：read。
- `market`（必填）：市场。约束：`{"type": "string", "default": "CN", "enum": ["CN"]}`。
- `symbol`（必填）：只填代码：SH600519 / 00700 / NVDA。约束：`{"type": "string"}`。
- `provider`（可选）：公开数据源。约束：`{"type": "string", "default": "auto", "enum": ["auto", "akshare"]}`。
- `limit`（可选）：最多返回行数。约束：`{"type": "integer", "default": 20, "minimum": 1, "maximum": 100}`。

## concept_rankings

按提供商涨跌幅降序。

性质：read。
- `market`（必填）：市场。约束：`{"type": "string", "default": "CN", "enum": ["CN"]}`。
- `provider`（可选）：公开数据源。约束：`{"type": "string", "default": "auto", "enum": ["auto", "akshare"]}`。
- `limit`（可选）：最多返回行数。约束：`{"type": "integer", "default": 20, "minimum": 1, "maximum": 100}`。

## dividends

提供商原始字段，CN可能包含预案，HK/US为Yahoo分红序列，不视为同一口径。

性质：read。
- `market`（必填）：市场。约束：`{"type": "string", "default": "CN", "enum": ["CN", "HK", "US"]}`。
- `symbol`（必填）：只填代码：SH600519 / 00700 / NVDA。约束：`{"type": "string"}`。
- `provider`（可选）：公开数据源。约束：`{"type": "string", "default": "auto", "enum": ["auto", "akshare", "yfinance"]}`。
- `limit`（可选）：最多返回行数。约束：`{"type": "integer", "default": 20, "minimum": 1, "maximum": 100}`。

## dragon_tiger

指定日期区间的龙虎榜数据。

性质：read。
- `market`（必填）：市场。约束：`{"type": "string", "default": "CN", "enum": ["CN"]}`。
- `provider`（可选）：公开数据源。约束：`{"type": "string", "default": "auto", "enum": ["auto", "akshare"]}`。
- `limit`（可选）：最多返回行数。约束：`{"type": "integer", "default": 20, "minimum": 1, "maximum": 100}`。
- `start_date`（必填）：开始日期。约束：`{"type": "string"}`。
- `end_date`（必填）：结束日期。约束：`{"type": "string"}`。

## earnings

提供商财报日历，含预测日期的可能性。

性质：read。
- `market`（必填）：市场。约束：`{"type": "string", "default": "HK", "enum": ["HK", "US"]}`。
- `symbol`（必填）：只填代码：SH600519 / 00700 / NVDA。约束：`{"type": "string"}`。
- `provider`（可选）：公开数据源。约束：`{"type": "string", "default": "auto", "enum": ["auto", "yfinance"]}`。
- `limit`（可选）：最多返回行数。约束：`{"type": "integer", "default": 20, "minimum": 1, "maximum": 100}`。

## financial_indicators

A股东方财富财务指标；不等同于三张原始报表。

性质：read。
- `market`（必填）：市场。约束：`{"type": "string", "default": "CN", "enum": ["CN"]}`。
- `symbol`（必填）：只填代码：SH600519 / 00700 / NVDA。约束：`{"type": "string"}`。
- `provider`（可选）：公开数据源。约束：`{"type": "string", "default": "auto", "enum": ["auto", "akshare"]}`。
- `limit`（可选）：最多返回行数。约束：`{"type": "integer", "default": 20, "minimum": 1, "maximum": 100}`。
- `basis`（可选）：指标口径。约束：`{"type": "string", "default": "report", "enum": ["report", "single_quarter"]}`。

## financials

Yahoo原始利润表、资产负债表或现金流，保留原始字段与报告期。

性质：read。
- `market`（必填）：市场。约束：`{"type": "string", "default": "HK", "enum": ["HK", "US"]}`。
- `symbol`（必填）：只填代码：SH600519 / 00700 / NVDA。约束：`{"type": "string"}`。
- `provider`（可选）：公开数据源。约束：`{"type": "string", "default": "auto", "enum": ["auto", "yfinance"]}`。
- `limit`（可选）：最多返回行数。约束：`{"type": "integer", "default": 20, "minimum": 1, "maximum": 100}`。
- `period`（可选）：报告周期。约束：`{"type": "string", "default": "yearly", "enum": ["yearly", "quarterly"]}`。
- `statement`（可选）：报表类型。约束：`{"type": "string", "default": "income", "enum": ["income", "balance", "cashflow"]}`。

## history

含首尾，最多366天，单源序列不拼接。

性质：read。
- `market`（必填）：市场。约束：`{"type": "string", "default": "CN", "enum": ["CN", "HK", "US"]}`。
- `symbol`（必填）：只填代码：SH600519 / 00700 / NVDA。约束：`{"type": "string"}`。
- `provider`（可选）：公开数据源。约束：`{"type": "string", "default": "auto", "enum": ["auto", "akshare", "yfinance"]}`。
- `limit`（可选）：最多返回行数。约束：`{"type": "integer", "default": 20, "minimum": 1, "maximum": 100}`。
- `start_date`（必填）：开始日期。约束：`{"type": "string"}`。
- `end_date`（必填）：结束日期。约束：`{"type": "string"}`。
- `adjust`（可选）：复权方式。约束：`{"type": "string", "default": "none", "enum": ["none", "forward"]}`。

## holders

Yahoo机构持有人数据，不代表所有股东。

性质：read。
- `market`（必填）：市场。约束：`{"type": "string", "default": "HK", "enum": ["HK", "US"]}`。
- `symbol`（必填）：只填代码：SH600519 / 00700 / NVDA。约束：`{"type": "string"}`。
- `provider`（可选）：公开数据源。约束：`{"type": "string", "default": "auto", "enum": ["auto", "yfinance"]}`。
- `limit`（可选）：最多返回行数。约束：`{"type": "integer", "default": 20, "minimum": 1, "maximum": 100}`。

## hot_stocks

东方财富人气排行。

性质：read。
- `market`（必填）：市场。约束：`{"type": "string", "default": "CN", "enum": ["CN"]}`。
- `provider`（可选）：公开数据源。约束：`{"type": "string", "default": "auto", "enum": ["auto", "akshare"]}`。
- `limit`（可选）：最多返回行数。约束：`{"type": "integer", "default": 20, "minimum": 1, "maximum": 100}`。

## indices

当前提供上证系列指数快照。

性质：read。
- `market`（必填）：市场。约束：`{"type": "string", "default": "CN", "enum": ["CN"]}`。
- `provider`（可选）：公开数据源。约束：`{"type": "string", "default": "auto", "enum": ["auto", "akshare"]}`。
- `limit`（可选）：最多返回行数。约束：`{"type": "integer", "default": 20, "minimum": 1, "maximum": 100}`。

## limit_up_pool

指定交易日涨停池。

性质：read。
- `market`（必填）：市场。约束：`{"type": "string", "default": "CN", "enum": ["CN"]}`。
- `provider`（可选）：公开数据源。约束：`{"type": "string", "default": "auto", "enum": ["auto", "akshare"]}`。
- `limit`（可选）：最多返回行数。约束：`{"type": "integer", "default": 20, "minimum": 1, "maximum": 100}`。
- `date`（必填）：交易日期。约束：`{"type": "string"}`。

## market_stats

从A股快照计算涨跌平数量，缺失单列。

性质：read。
- `market`（必填）：市场。约束：`{"type": "string", "default": "CN", "enum": ["CN"]}`。
- `provider`（可选）：公开数据源。约束：`{"type": "string", "default": "auto", "enum": ["auto", "akshare"]}`。
- `limit`（可选）：最多返回行数。约束：`{"type": "integer", "default": 20, "minimum": 1, "maximum": 100}`。

## news

提供商原始新闻内容与链接。

性质：read。
- `market`（必填）：市场。约束：`{"type": "string", "default": "CN", "enum": ["CN", "HK", "US"]}`。
- `symbol`（必填）：只填代码：SH600519 / 00700 / NVDA。约束：`{"type": "string"}`。
- `provider`（可选）：公开数据源。约束：`{"type": "string", "default": "auto", "enum": ["auto", "akshare", "yfinance"]}`。
- `limit`（可选）：最多返回行数。约束：`{"type": "integer", "default": 20, "minimum": 1, "maximum": 100}`。

## profile

各源字段不同，缺失不补造。

性质：read。
- `market`（必填）：市场。约束：`{"type": "string", "default": "CN", "enum": ["CN", "HK", "US"]}`。
- `symbol`（必填）：只填代码：SH600519 / 00700 / NVDA。约束：`{"type": "string"}`。
- `provider`（可选）：公开数据源。约束：`{"type": "string", "default": "auto", "enum": ["auto", "tencent", "akshare", "yfinance"]}`。
- `limit`（可选）：最多返回行数。约束：`{"type": "integer", "default": 20, "minimum": 1, "maximum": 100}`。

## quote

提供商报告值，数据时间缺失时明确标注。

性质：read。
- `market`（必填）：市场。约束：`{"type": "string", "default": "CN", "enum": ["CN", "HK", "US"]}`。
- `symbol`（必填）：只填代码：SH600519 / 00700 / NVDA。约束：`{"type": "string"}`。
- `provider`（可选）：公开数据源。约束：`{"type": "string", "default": "auto", "enum": ["auto", "tencent", "akshare", "yfinance"]}`。
- `limit`（可选）：最多返回行数。约束：`{"type": "integer", "default": 20, "minimum": 1, "maximum": 100}`。

## recommendations

提供商评级汇总。

性质：read。
- `market`（必填）：市场。约束：`{"type": "string", "default": "HK", "enum": ["HK", "US"]}`。
- `symbol`（必填）：只填代码：SH600519 / 00700 / NVDA。约束：`{"type": "string"}`。
- `provider`（可选）：公开数据源。约束：`{"type": "string", "default": "auto", "enum": ["auto", "yfinance"]}`。
- `limit`（可选）：最多返回行数。约束：`{"type": "integer", "default": 20, "minimum": 1, "maximum": 100}`。

## sector_rankings

按提供商涨跌幅降序。

性质：read。
- `market`（必填）：市场。约束：`{"type": "string", "default": "CN", "enum": ["CN"]}`。
- `provider`（可选）：公开数据源。约束：`{"type": "string", "default": "auto", "enum": ["auto", "akshare"]}`。
- `limit`（可选）：最多返回行数。约束：`{"type": "integer", "default": 20, "minimum": 1, "maximum": 100}`。

## sources

仅列免Key、免用户登录能力；不代表实时健康检查。

性质：read。

最小参数示例：`{}`。

## splits

提供商拆股比率序列。

性质：read。
- `market`（必填）：市场。约束：`{"type": "string", "default": "HK", "enum": ["HK", "US"]}`。
- `symbol`（必填）：只填代码：SH600519 / 00700 / NVDA。约束：`{"type": "string"}`。
- `provider`（可选）：公开数据源。约束：`{"type": "string", "default": "auto", "enum": ["auto", "yfinance"]}`。
- `limit`（可选）：最多返回行数。约束：`{"type": "integer", "default": 20, "minimum": 1, "maximum": 100}`。
