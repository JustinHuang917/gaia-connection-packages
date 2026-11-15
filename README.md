# Gaia Connection Packages

Gaia 独立数据连接服务的公开连接包目录。每个连接包拥有独立目录、版本、操作定义、配置 Schema 和依赖声明；凭据、Cookie、浏览器状态及运行数据不进入仓库。

## 服务配置

```dotenv
ADAPTER_CATALOG_URL=https://github.com/JustinHuang917/gaia-connection-packages
```

服务拉取仓库 HEAD 的固定 commit，读取根目录 `catalog.json`。用户检查更新后，选择包并安装，再审阅批准。更新目录不会自动替换现有连接使用的版本。

## 包目录

| 目录 | 能力 |
| --- | --- |
| bilibili | Bilibili CLI 登录、视频、分 P 与字幕 |
| coros | COROS MCP 登录及运动数据 |
| finance-market | 无 Key 的财经行情与数据 |
| hacker-news | Hacker News 消息及讨论 |
| instagram | Instagram 浏览器访问 |
| public-web | 公开网页读取与页面关键词查找 |
| reddit | Reddit 浏览器访问 |
| x-twitter | X / Twitter 浏览器访问 |
| xiaohongshu | 小红书浏览器登录与访问 |
| youtube | YouTube 搜索、视频与字幕 |

具体操作以各包 `schemas/operations.json` 为准。部分 CLI 和浏览器操作由数据连接 Worker 的原生运行器提供，需要服务端支持相应运行器；此目录不将它们伪装为独立 Python 实现。CLI 依赖随包声明，不要求预装到基础镜像。

## 发布连接包

1. 修改对应目录的代码、Schema、依赖与 `adapter.yaml`，变更时递增 `version`。
2. 在仓库根目录运行（需要 Python 3.10+）：

   ```sh
   python3 -m pip install -r tools/requirements.txt
   python3 tools/catalog.py
   python3 tools/catalog.py --check
   ```

3. 将包内容与生成的 `catalog.json` 一并提交、推送。
4. 在 Gaia 数据连接管理中检查更新、安装并审阅批准。

目录格式：

```json
{
  "schema": "gaia.connection-catalog/v1",
  "packages": [
    {"id": "hacker-news", "version": "1.1.0", "path": "hacker-news", "sha256": "<generated content SHA-256>"}
  ]
}
```

`sha256` 是包内容摘要，与 ZIP 压缩实现无关。对按路径排序的每个文件，依次写入 UTF-8 相对路径、NUL、文件字节数的十进制 ASCII、NUL、原始文件字节，再计算整个流的 SHA-256。不要使用 Git commit 或 ZIP 文件摘要替代。服务端安装时对解包后的文件执行相同校验。

包目录只存放发布内容，不加入缓存、ZIP、可执行文件或符号链接。

可生成临时 ZIP 用于服务端包校验：

```sh
python3 tools/catalog.py --check --out-dir /tmp/gaia-connection-packages
```

此目录采用内容摘要协议，服务端需包含对应的 catalog 内容摘要校验更新。
