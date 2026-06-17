# n8n-workflows-cn

> 一些整理过的 n8n 工作流模板，加上中文说明和本地化标注。
>
> 源数据来自 [nusquama/n8nworkflows.xyz](https://github.com/nusquama/n8nworkflows.xyz)，感谢原作者的收集。

---

## 为什么要做这个

用 n8n 的时候碰到一些小麻烦：
- 社区模板里很多服务（Gmail、Google Sheets、Slack 等）在国内访问不方便
- 官方文档和模板都是英文，看起来比较吃力
- 想用国内服务（飞书、企业微信、钉钉）替换，但不太确定怎么改

所以就从这个仓库里筛了一批模板，标了一下哪些可以直接用、哪些需要换一换。

---

## 分类

| 分类 | 说明 |
|------|------|
| [🤖 AI Agent](workflows/ai-agent/) | AI Agent、多 Agent 协作、MCP |
| [⚙️ DevOps](workflows/devops/) | Webhook、API、监控告警 |
| [📈 金融分析](workflows/finance-analysis/) | 加密货币、股票数据 |
| [🧠 知识库/RAG](workflows/knowledge-rag/) | Ollama、向量数据库、RAG |
| [🎨 多模态AI](workflows/multimodal-ai/) | 图像、语音、视频 |
| [🔧 工作流自动化](workflows/workflow-automation/) | 飞书通知、消息推送、数据同步 |

---

## 如何使用

每个 `.json` 文件就是一个 n8n 工作流，可以直接导入：

1. 打开 n8n 编辑器
2. 点击 **Import from File**（或粘贴剪贴板）
3. 选择下载的 `.json` 文件就行

JSON 文件末尾有个 `_cn_meta` 字段，里面写了一些中文备注（标题、描述、需要注意的地方）。

### 安装 n8n（如果还没装）

```bash
docker run -d --name n8n -p 5678:5678 -v n8n_data:/home/node/.n8n n8nio/n8n
```

---

## 服务替换参考

有些模板里用到的服务在国内不太好用，整理了一些常见的替换思路：

| 原来的服务 | 可以试试 | 怎么改 |
|------|------|------|
| Gmail | QQ邮箱 / 网易企业邮箱 | 改用 Email (IMAP) 节点 |
| Google Sheets | 飞书多维表格 / 腾讯文档 | 改用 HTTP Request 调 API |
| Slack | 飞书群机器人 / 企业微信群机器人 | 改用 Webhook 节点 |
| OpenAI | DeepSeek / 通义千问 | 改 OpenAI 节点的 Base URL |
| Notion | 飞书文档 / 语雀 | 改用 HTTP Request |
| Twilio | 腾讯云短信 / 阿里云短信 | 改用 HTTP Request |

更详细的替换方案见 [docs/replacement-guide.md](docs/replacement-guide.md)。

---

## 模板标注说明

每个模板都标了一个简单的适配等级：

| 标记 | 意思 |
|:---:|------|
| 🟢 A | 不依赖海外服务，可以直接用 |
| 🟡 B | 有一两个地方需要换成国内服务 |
| 🟠 C | 需要改动的地方比较多 |
| 🔴 D | 不太适合国内直接用 |

---

## 贡献

如果有觉得好用的模板、或者发现了更好的替换方案，欢迎提 PR 或者 Issue。

---

## 许可

模板来自 [nusquama/n8nworkflows.xyz](https://github.com/nusquama/n8nworkflows.xyz)，MIT 许可。

---
