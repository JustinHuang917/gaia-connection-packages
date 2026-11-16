# 操作参考

以下参数以本版本 Schema 为准，调用前使用 connection_describe 读取完整契约。

## list_tools

list_tools：读取当前连接提供的数据；具体参数见操作契约。

性质：read。

最小参数示例：`{}`。

## query_user

query_user：读取当前连接提供的数据；具体参数见操作契约。

性质：read。

最小参数示例：`{}`。

## query_sport_records

query_sport_records：读取当前连接提供的数据；具体参数见操作契约。

性质：read。
- `startDate`（必填）：startDate。约束：`{"type": "string", "pattern": "^[0-9]{8}$"}`。
- `endDate`（必填）：endDate。约束：`{"type": "string", "pattern": "^[0-9]{8}$"}`。
- `sportTypeCodes`（可选）：sportTypeCodes。约束：`{"type": "array"}`。
- `limit`（可选）：limit。约束：`{"type": "integer", "minimum": 1, "maximum": 100}`。
