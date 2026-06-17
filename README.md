# n8n-workflows-cn

[![Workflows](https://img.shields.io/badge/Workflows-1480-brightgreen)](INDEX.md)
[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)](CONTRIBUTING.md)
[![n8n](https://img.shields.io/badge/n8n-%3E%3D1.0-red)](https://n8n.io)

---

## 项目介绍

这是一个 n8n 工作流模板合集，源自 [nusquama/n8nworkflows.xyz](https://github.com/nusquama/n8nworkflows.xyz) 社区收集的 1480 个模板。

**做了什么：** 原始模板里的服务大多是 OpenAI、Slack、Google Workspace 等海外产品。我把这些逐个替换成了国内常用的服务（DeepSeek、通义千问、飞书、微信支付、阿里云等），并给每个工作流加了中文说明和适配记录。

**适合谁：** 如果你用 n8n 做自动化，但不想折腾海外账号和支付，这个仓库可能能帮你省点时间。

**数据概览：**

| | |
|---|---|
| 工作流总数 | 1480 |
| 大分类 | 6 个（AI Agent、DevOps、金融分析、知识库 RAG、多模态 AI、工作流自动化） |
| 细分场景 | 60+ 个（对话机器人、邮件处理、监控告警、股票分析……） |
| 替换服务 | 14 项（OpenAI → DeepSeek、Slack → 飞书、Gmail → QQ邮箱……） |
| 格式 | 每个工作流 = `workflow.json`（可在 n8n 里 Import）+ `readme.md`（说明文档） |

## 起因

自己用 n8n 的时候经常遇到：打开一个模板全是 OpenAI / Claude 节点没账号没法用、Slack 和 Google Sheets 这些用不上的服务占一半、每次手动改 Base URL 调消息格式很费时间。所以就整理了这份笔记，也能帮到有类似困扰的朋友。

## 快速试试

```bash
# 1. 启动 n8n（Docker）
docker run -d --name n8n -p 5678:5678 -v n8n_data:/home/node/.n8n n8nio/n8n

# 2. 打开 http://localhost:5678，点击 Import from File

# 3. 导入任意 workflow.json，填入 API Key 就能跑
```

> 可以从 `workflows/ai-agent/AI Agent聊天-1954/workflow.json` 开始试，基础的 AI 聊天 Agent，5 个节点。

## 工作流分类

需要说明一下：这些模板的适配程度不一样，有的改得比较完整，有的只动了核心节点。具体可以看每个工作流目录下的 `readme.md`。

> 点击查看 [完整索引（按子分类折叠浏览）](INDEX.md) · [精选合集（场景推荐）](CURATED.md) · [在线浏览站点](https://luckterence.github.io/n8n-workflows-cn/)

### AI Agent（93 个）

智能体相关的工作流，从入门到多智能体协作都有。

| 子分类 | 数量 | 包含内容 |
|--------|:----:|----------|
| 对话机器人 | 30 | 各类 AI 聊天机器人、多轮对话、情感支持 |
| MCP 工具 & 集成 | 18 | 为 AI Agent 暴露各种 API 工具的 MCP Server |
| 消息平台机器人 | 6 | Telegram、WhatsApp、LINE 上的 AI 机器人 |
| 多智能体 | 4 | 多个 Agent 协作、辩论、编排 |
| 搜索 & 研究 Agent | 2 | 联网搜索、信息检索 |
| 入门教程 | 2 | Build Your First AI Agent 系列 |
| 其他（客服/金融/HR/代码/日程等） | 31 | 各垂直场景的 Agent 应用 |

### DevOps（153 个）

面向开发运维的自动化工作流，监控、部署、API 集成为主。

| 子分类 | 数量 | 包含内容 |
|--------|:----:|----------|
| API 集成 & Webhook | 48 | 各种第三方服务的 API 连接器、Webhook 转发 |
| 监控 & 告警 | 45 | 服务器监控、日志分析、异常告警通知 |
| MCP Server 构建 | 23 | 构建各类工具 MCP Server |
| CI/CD & 部署 | 20 | 自动构建、测试、部署流水线 |
| 服务器 & 云 | 5 | 云资源管理、SSH 运维 |
| 备份 & 恢复 | 5 | 数据库备份、快照管理 |
| 其他（安全/网络/成本等） | 7 | 代码管理、认证、FinOps |

### Finance Analysis（25 个）

金融相关的分析工作流，以股票和加密货币为主。

| 子分类 | 数量 | 包含内容 |
|--------|:----:|----------|
| 股票 & 市场 | 22 | A 股/美股分析、技术指标、市场数据采集 |
| AI 投顾 | 2 | AI 驱动的投资建议 |
| 风控 & 合规 | 1 | 欺诈检测 |

### Knowledge RAG（47 个）

检索增强生成相关，适合搭建知识库问答系统。

| 子分类 | 数量 | 包含内容 |
|--------|:----:|----------|
| RAG 检索问答 | 26 | 基于文档的知识库问答 |
| 向量数据库 | 20 | Qdrant、Milvus、Pinecone 集成 |

### Multimodal AI（52 个）

多模态 AI 工作流，语音、图像、视频生成。

| 子分类 | 数量 | 包含内容 |
|--------|:----:|----------|
| 语音 & 音频 | 28 | TTS 语音合成、Whisper 转录、配音 |
| 图像生成 | 9 | Stable Diffusion、DALL-E、Flux |
| 视频生成 | 5 | 文生视频、动画制作 |
| 3D 生成 | 3 | 三维模型生成 |
| 其他（翻译/数字人/音乐等） | 7 | 多模态编辑、虚拟人 |

### Workflow Automation（1110 个）

最大的分类，覆盖日常业务自动化的方方面面。

| 子分类 | 数量 | 包含内容 |
|--------|:----:|----------|
| Email & 邮件处理 | 162 | 邮件自动发送、收件箱处理、Newsletter |
| 数据 & 文档处理 | 127 | 表格处理、PDF 解析、数据库操作 |
| 即时通讯 & 聊天 | 121 | Telegram/WhatsApp/Discord 消息机器人 |
| API 集成 & 自动化 | 113 | 通用自动化流程、定时任务、数据同步 |
| 图片 & 视频 | 95 | 图片生成、视频剪辑、视觉效果 |
| 内容采集 & 研究 | 84 | 网页抓取、新闻聚合、SEO 内容生成 |
| 销售 & CRM | 61 | 客户管理、销售漏斗、工单系统 |
| 财务 & 支付 | 61 | 发票处理、费用报销、交易分析 |
| AI 增强工作流 | 48 | 嵌入 AI 能力的业务流程 |
| 项目管理 & DevOps | 29 | 任务跟踪、Bug 管理、开发流程 |
| 社交媒体 & 内容 | 29 | 多平台内容发布、社交监听 |
| HR & 招聘 | 26 | 简历筛选、面试安排、入职流程 |
| 短信 & 通知 | 13 | 短信发送、推送通知 |
| 电商 & 订单 | 12 | 订单处理、库存管理、商品信息 |
| 其他（日程/营销/表单/教育/合规等） | 40 | 各类细分场景 |

## 做了哪些替换

思路是：n8n 的专用节点本质上是对 HTTP API 的封装，大多可以通过换成 HTTP Request 节点 + 国内服务 API 来实现。少数场景直接用 n8n 内置节点（如 Email 替换 Gmail）。

| 原始服务 | 替换方案 | 怎么改的 |
|----------|----------|----------|
| OpenAI (GPT-4/GPT-4o) | DeepSeek | 改 Base URL 为 `https://api.deepseek.com`，Model 为 `deepseek-chat` |
| Anthropic (Claude) | DeepSeek | Anthropic Chat Model 替换为 OpenAI Chat Model，同上配置 |
| Google Gemini | 通义千问 | 替换为 OpenAI Chat Model，Base URL 改为通义千问兼容地址 |
| Slack | 飞书群机器人 | 改 Webhook URL 为飞书机器人地址，调消息体格式 |
| Gmail | QQ邮箱 / 网易企业邮箱 | 替换为 Email (IMAP/SMTP) 节点 |
| Google Sheets | 飞书多维表格 | HTTP Request 调用飞书 Bitable API |
| Google Drive | 阿里云 OSS / 腾讯云 COS | HTTP Request 节点 |
| Google Calendar | 飞书日历 | HTTP Request 节点 |
| Notion | 飞书文档 / 语雀 | HTTP Request 节点 |
| Twilio | 腾讯云短信 / 阿里云短信 | HTTP Request 节点 |
| Stripe / PayPal | 微信支付 / 支付宝 | HTTP Request 节点 |
| GitHub | Gitee | HTTP Request 调用 Gitee API |
| Supabase | 腾讯云 CloudBase | HTTP Request 节点 |
| Zoom | 腾讯会议 | HTTP Request 节点 |

> 这些方案不一定最优，有更好的想法欢迎提 issue 或 PR。

## 适配程度说明

每个 `workflow.json` 里有个 `_cn_meta` 字段记录适配情况：

```json
"_cn_meta": {
  "title_zh": "AI Agent聊天",
  "description_zh": "基础AI Agent对话模板",
  "category": "ai-agent",
  "tier": "A",
  "source_id": 1954,
  "synced_at": "2026-06-17T11:36:56.827907"
}
```

- **Tier A** — 基本改完了，配置 API Key 应该就能跑
- **Tier B** — 核心链路通了，边角节点可能要自己调
- **Tier C** — 搭了框架，具体参数需按场景配置

## 目录结构

```
workflows/
  {分类}/
    {工作流名称}-{ID}/
      workflow.json    # 工作流定义（含 _cn_meta 适配元数据）
      readme.md        # 节点说明与适配记录
```

## 怎么用

n8n 编辑器里 **Import from File** 导入 `workflow.json` 就行。n8n 安装（Docker）：

```bash
docker run -d --name n8n -p 5678:5678 -v n8n_data:/home/node/.n8n n8nio/n8n
```

## 在线浏览

> **[🔍 工作流浏览站点](https://luckterence.github.io/n8n-workflows-cn/)** — 可搜索、可按分类筛选的在线浏览器，暗色主题。

启用方式：仓库 Settings > Pages > Source 选 `Deploy from a branch`，分支 `main`，目录 `/docs`，保存后等几分钟即可访问。

## 接下来想做的

- [x] CI/CD 自动验证 — GitHub Actions 检查工作流合法性
- [x] 工作流浏览站点 — 搭个 GitHub Pages，方便搜索筛选
- [x] 精选合集 — 按场景整理推荐组合
- [ ] 完善适配 — 把更多 Tier B/C 提升到 Tier A

## 参与进来

提 bug、给建议、直接改代码，都欢迎。参考 [CONTRIBUTING.md](CONTRIBUTING.md)。

可以帮忙的事：

1. 试试某个工作流能不能跑，遇到问题提 issue
2. 把自己用的服务替换方案加进来
3. 翻译英文说明、补使用示例
4. 帮忙完善 INDEX.md 的分类

## 许可

原始模板来自 [nusquama/n8nworkflows.xyz](https://github.com/nusquama/n8nworkflows.xyz)，MIT 许可。本项目同样采用 MIT 许可。
