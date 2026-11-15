# 公开财经数据组合包 v2

本包只收录**免 API Key、免用户登录**的公开只读数据。一个连接提供多种业务能力，内部按市场和操作选择公开数据源；不同来源仍独立适配。代码独立编写，不导入 daily_stock_analysis，不依赖 OpenBB。

## 与授权数据连接的边界

| 类型 | 本包 |
|---|---|
| 腾讯公开行情、AKShare公开接口、Yahoo公开数据 | 收录在能力矩阵中的已适配接口 |
| Tushare、Finnhub、Alpha Vantage、TickFlow等需要Key的接口 | 不收录，应单独创建授权数据连接包 |
| Longbridge OAuth、Futu OpenD等授权/专用网关 | 不收录，不与公开包共用凭据 |

公开不代表无限流、永久免费授权、数据全市场覆盖或永久可用。平台拦截、限流、网络失败如实返回，不要求用户为此包输入密钥。Yahoo可能内部使用匿名会话Cookie，不使用用户登录凭据。

## 操作目录（23项）

- 基础：`sources`、`quote`、`history`、`profile`。
- 财务：`financials`（HK/US原始三张报表）、`financial_indicators`（CN指标）。
- 公司事件：`dividends`、`splits`、`earnings`。
- 研究：`holders`、`recommendations`、`analyst_targets`、`news`。
- 个股市场：`capital_flow`、`chip_distribution`。
- 全市场：`indices`、`market_stats`、`sector_rankings`、`concept_rankings`、`hot_stocks`。
- 专题：`limit_up_pool`、`dragon_tiger`、`board_members`。

UI按操作和市场过滤数据源。`sources`返回完整静态支持矩阵；不是全源健康检查。

## 使用

在适配包点击「导入公开财经数据包」，审核后创建连接；租户A现有「财经股票」连接已升级到本包。

代码规则：CN使用SH600519/SZ000001/BJ开头，HK使用00700，US使用NVDA。只填写代码，不带“港股”等说明文字。

`provider=auto`按支持能力尝试来源，并记录实际来源和失败尝试；手工指定数据源后失败不换源。历史日线最多366天、含首尾，不跨数据源拼接，复权方式显式声明。表格最多100行，默认20行。

财务报表和财务指标明确分开；指标按报告期或单季度获取。分红记录各源含义不同：CN可能包括预案，不与Yahoo已记录分红混为同一口径。原始表格保持列名和数据结构，标识`provider_native`；不会把不同单位自动混成统一数值。`currency`只用于行情和历史价格，其他数据集为null，不能据市场推断财务报告币种。缺失数值为null，不伪装为0。

## 当前范围与未覆盖项

本版不是AKShare/Yahoo的所有SDK方法自动暴露。仅允许目录中明确登记、验证参数和网络边界的23个只读操作，不提供任意函数调用。

目前indices仅上证系列；机构持仓仅Yahoo机构持有人；筹码是第三方模型估计。ETF、基金、台股法人、期货、期权、分钟线、行业归属反查及其他提供商冗余接入暂未实现。需要Key或登录的包后续独立开发，本次没有创建虚假授权入口。

## 实现与验证

能力唯一事实源：`native/finance/catalog.py`。运行`scripts/build_finance_catalog.py`生成包的操作Schema和市场/数据源联动约束。

独立Linux Node的finance环境，依赖锁定在`native/finance/requirements.lock`。固定工具注册表、固定公开域名和请求子进程截止时间，不开放任意SDK调用或安装命令。节点全局代理继续生效。

2026-11-09真实链路已验证：腾讯CN/HK行情、CN名称、AKShare CN日线、财务指标、行业排行、新闻、上证指数、资金流成功。Yahoo当前出口曾返回YFRateLimitError；不能标记为美股真实验收通过。详见测试记录。
