# n8n-workflows-cn

[English](README_EN.md) | 中文

[![Workflows](https://img.shields.io/badge/Workflows-1480-brightgreen)](INDEX.md)
[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)](CONTRIBUTING.md)
[![n8n](https://img.shields.io/badge/n8n-%3E%3D1.0-red)](https://n8n.io)

---

> **1480 个 n8n 工作流模板 · 全部替换为 DeepSeek / 飞书 / 微信支付 / 阿里云 · 1479 个开箱即用**

[在线浏览站点](https://luckterence.github.io/n8n-workflows-cn/) · [完整索引](INDEX.md) · [精选合集](CURATED.md) · [快速开始](#快速试试)

---

## 这是什么

把 [nusquama/n8nworkflows.xyz](https://github.com/nusquama/n8nworkflows.xyz) 社区收集的 1480 个 n8n 模板里的海外服务（OpenAI、Slack、Google Workspace 等），逐个替换成了国内常用服务（DeepSeek、通义千问、飞书、微信支付、阿里云等），并给每个工作流加了中文说明。

**适合谁：用 n8n 做自动化，但不想折腾海外账号和支付的开发者。**

## 5 分钟上手

**第 1 步** — 一行命令启动 n8n：
```bash
docker run -d --name n8n -p 5678:5678 -v n8n_data:/home/node/.n8n n8nio/n8n
```

**第 2 步** — 打开 `http://localhost:5678`，点 **Import from File**，导入任意 `workflow.json`

**第 3 步** — 填 API Key（DeepSeek / 千问 / 飞书），点 **Execute Workflow**

> 新手建议从标记为「新手」的工作流入手，只需 DeepSeek Key 就能跑。

**推荐从这几个开始：**

| 工作流 | 说明 | 适合 | 入口 |
|--------|------|:--:|------|
| AI Agent 聊天 | 基础 AI 对话，配 DeepSeek Key 直接跑 | 新手 | [打开](workflows/ai-agent/AI%20Agent聊天-1954/) |
| 定时启停 n8n 工作流 | 用 n8n 管理 n8n 本身 | 新手 | [打开](workflows/devops/定时启停n8n工作流-3229/) |
| AI 客服中心 Telegram | 完整 Telegram 客服机器人 | 进阶 | [打开](workflows/ai-agent/AI客服中心Telegram呼入-4044/) |
| Gmail 智能分类 | AI 自动给邮件打标签归档 | 进阶 | [打开](workflows/workflow-automation/Gmail智能分类归档-3686/) |
| AI 股票基本面分析 | 多维度股票基本面分析 | 进阶 | [打开](workflows/finance-analysis/AI股票基本面分析-2183/) |


> **需要切回海外节点？** 部分工作流的 Gmail/Slack/Google Sheets 等节点已替换为飞书/阿里云方案。如果你有海外账号想用原始节点：
> ```bash
> python scripts/toggle_region.py overseas  # 恢复海外原始节点
> python scripts/toggle_region.py cn        # 切回国内方案
> python scripts/toggle_region.py status    # 查看当前状态
> ```

## 工作流分类

需要说明一下：这些模板的适配程度不一样，有的改得比较完整，有的只动了核心节点。具体可以看每个工作流目录下的 `readme.md`。

> 点击查看 [完整索引（按子分类折叠浏览）](INDEX.md) · [精选合集（场景推荐）](CURATED.md) · [在线浏览站点](https://luckterence.github.io/n8n-workflows-cn/)

### AI Agent（93 个）

智能体相关的工作流，从入门到多智能体协作都有。

| 子分类 | 数量 | 包含内容 |
|--------|:----:|----------|
| [对话机器人](https://luckterence.github.io/n8n-workflows-cn/?cat=ai-agent&sub=对话机器人) | 26 | 各类 AI 聊天机器人、多轮对话、情感支持 |
| [MCP 工具 & 集成](https://luckterence.github.io/n8n-workflows-cn/?cat=ai-agent&sub=MCP%20工具%20%26%20集成) | 19 | 为 AI Agent 暴露各种 API 工具的 MCP Server |
| [其他](https://luckterence.github.io/n8n-workflows-cn/?cat=ai-agent&sub=其他) | 26 | 客服/金融/HR/代码/日程等垂直场景 Agent |
| [消息平台机器人](https://luckterence.github.io/n8n-workflows-cn/?cat=ai-agent&sub=消息平台机器人) | 5 | Telegram、WhatsApp、LINE 上的 AI 机器人 |
| [多智能体](https://luckterence.github.io/n8n-workflows-cn/?cat=ai-agent&sub=多智能体) | 5 | 多个 Agent 协作、辩论、编排 |
| [个人助理](https://luckterence.github.io/n8n-workflows-cn/?cat=ai-agent&sub=个人助理) | 3 | AI 驱动的个人效率助手 |
| [入门教程](https://luckterence.github.io/n8n-workflows-cn/?cat=ai-agent&sub=入门教程) | 2 | Build Your First AI Agent 系列 |
| [金融 Agent](https://luckterence.github.io/n8n-workflows-cn/?cat=ai-agent&sub=金融%20Agent) | 2 | 金融分析、投资 Agent |
| [Agent 框架](https://luckterence.github.io/n8n-workflows-cn/?cat=ai-agent&sub=Agent%20框架) | 2 | LangChain、自定义 Agent 框架 |
| [搜索 & 研究 Agent](https://luckterence.github.io/n8n-workflows-cn/?cat=ai-agent&sub=搜索%20%26%20研究%20Agent) | 2 | 联网搜索、信息检索 |
| [多模态 Agent](https://luckterence.github.io/n8n-workflows-cn/?cat=ai-agent&sub=多模态%20Agent) | 1 | 支持图像/语音的多模态 Agent |

### DevOps（153 个）

面向开发运维的自动化工作流，监控、部署、API 集成为主。

| 子分类 | 数量 | 包含内容 |
|--------|:----:|----------|
| [API 集成 & Webhook](https://luckterence.github.io/n8n-workflows-cn/?cat=devops&sub=API%20集成%20%26%20Webhook) | 78 | 各种第三方服务的 API 连接器、Webhook 转发 |
| [监控 & 告警](https://luckterence.github.io/n8n-workflows-cn/?cat=devops&sub=监控%20%26%20告警) | 25 | 服务器监控、日志分析、异常告警通知 |
| [其他](https://luckterence.github.io/n8n-workflows-cn/?cat=devops&sub=其他) | 15 | 安全、网络、成本等场景 |
| [MCP Server 构建](https://luckterence.github.io/n8n-workflows-cn/?cat=devops&sub=MCP%20Server%20构建) | 10 | 构建各类工具 MCP Server |
| [服务器 & 云](https://luckterence.github.io/n8n-workflows-cn/?cat=devops&sub=服务器%20%26%20云) | 9 | 云资源管理、SSH 运维 |
| [CI/CD & 部署](https://luckterence.github.io/n8n-workflows-cn/?cat=devops&sub=CI/CD%20%26%20部署) | 6 | 自动构建、测试、部署流水线 |
| [备份 & 恢复](https://luckterence.github.io/n8n-workflows-cn/?cat=devops&sub=备份%20%26%20恢复) | 5 | 数据库备份、快照管理 |
| [安全 & 认证](https://luckterence.github.io/n8n-workflows-cn/?cat=devops&sub=安全%20%26%20认证) | 3 | 安全扫描、OAuth 集成 |
| [代码管理](https://luckterence.github.io/n8n-workflows-cn/?cat=devops&sub=代码管理) | 2 | Git 操作、代码同步 |

### Finance Analysis（25 个）

金融相关的分析工作流，以股票和加密货币为主。

| 子分类 | 数量 | 包含内容 |
|--------|:----:|----------|
| [股票 & 市场](https://luckterence.github.io/n8n-workflows-cn/?cat=finance-analysis&sub=股票%20%26%20市场) | 20 | A 股/美股分析、技术指标、市场数据采集 |
| [AI 投顾](https://luckterence.github.io/n8n-workflows-cn/?cat=finance-analysis&sub=AI%20投顾) | 2 | AI 驱动的投资建议 |
| [其他](https://luckterence.github.io/n8n-workflows-cn/?cat=finance-analysis&sub=其他) | 2 | 其他金融场景 |
| [风控 & 合规](https://luckterence.github.io/n8n-workflows-cn/?cat=finance-analysis&sub=风控%20%26%20合规) | 1 | 欺诈检测、合规检查 |

### Knowledge RAG（47 个）

检索增强生成相关，适合搭建知识库问答系统。

| 子分类 | 数量 | 包含内容 |
|--------|:----:|----------|
| [RAG 检索问答](https://luckterence.github.io/n8n-workflows-cn/?cat=knowledge-rag&sub=RAG%20检索问答) | 36 | 基于文档的知识库问答 |
| [向量数据库](https://luckterence.github.io/n8n-workflows-cn/?cat=knowledge-rag&sub=向量数据库) | 8 | Qdrant、Milvus、Pinecone 集成 |
| [其他](https://luckterence.github.io/n8n-workflows-cn/?cat=knowledge-rag&sub=其他) | 3 | 其他 RAG 场景 |

### Multimodal AI（52 个）

多模态 AI 工作流，语音、图像、视频生成。

| 子分类 | 数量 | 包含内容 |
|--------|:----:|----------|
| [语音 & 音频](https://luckterence.github.io/n8n-workflows-cn/?cat=multimodal-ai&sub=语音%20%26%20音频) | 25 | TTS 语音合成、Whisper 转录、配音 |
| [图像生成](https://luckterence.github.io/n8n-workflows-cn/?cat=multimodal-ai&sub=图像生成) | 14 | Stable Diffusion、DALL-E、Flux |
| [视频生成](https://luckterence.github.io/n8n-workflows-cn/?cat=multimodal-ai&sub=视频生成) | 5 | 文生视频、动画制作 |
| [图像分析](https://luckterence.github.io/n8n-workflows-cn/?cat=multimodal-ai&sub=图像分析) | 4 | 图片识别、OCR、内容审核 |
| [3D 生成](https://luckterence.github.io/n8n-workflows-cn/?cat=multimodal-ai&sub=3D%20生成) | 3 | 三维模型生成 |
| [其他](https://luckterence.github.io/n8n-workflows-cn/?cat=multimodal-ai&sub=其他) | 1 | 翻译/数字人/音乐等 |

### Workflow Automation（1110 个）

最大的分类，覆盖日常业务自动化的方方面面。

| 子分类 | 数量 | 包含内容 |
|--------|:----:|----------|
| [AI 增强工作流](https://luckterence.github.io/n8n-workflows-cn/?cat=workflow-automation&sub=AI%20增强工作流) | 119 | 嵌入 AI 能力的业务流程 |
| [消息平台 & Bot](https://luckterence.github.io/n8n-workflows-cn/?cat=workflow-automation&sub=消息平台%20%26%20Bot) | 116 | Telegram/WhatsApp/Discord 消息机器人 |
| [邮件 & 通讯](https://luckterence.github.io/n8n-workflows-cn/?cat=workflow-automation&sub=邮件%20%26%20通讯) | 112 | 邮件自动发送、收件箱处理、Newsletter |
| [文件 & 存储](https://luckterence.github.io/n8n-workflows-cn/?cat=workflow-automation&sub=文件%20%26%20存储) | 70 | 文件处理、存储管理、格式转换 |
| [社交媒体 & 内容](https://luckterence.github.io/n8n-workflows-cn/?cat=workflow-automation&sub=社交媒体%20%26%20内容) | 68 | 多平台内容发布、社交监听 |
| [API 集成 & 自动化](https://luckterence.github.io/n8n-workflows-cn/?cat=workflow-automation&sub=API%20集成%20%26%20自动化) | 65 | 通用自动化流程、定时任务、数据同步 |
| [数据采集 & 爬虫](https://luckterence.github.io/n8n-workflows-cn/?cat=workflow-automation&sub=数据采集%20%26%20爬虫) | 54 | 网页抓取、新闻聚合、SEO 内容生成 |
| [CRM & 客服](https://luckterence.github.io/n8n-workflows-cn/?cat=workflow-automation&sub=CRM%20%26%20客服) | 50 | 客户管理、销售漏斗、工单系统 |
| [ERP & 财务](https://luckterence.github.io/n8n-workflows-cn/?cat=workflow-automation&sub=ERP%20%26%20财务) | 37 | 发票处理、费用报销、交易分析 |
| [其他](https://luckterence.github.io/n8n-workflows-cn/?cat=workflow-automation&sub=其他) | 334 | 日程/营销/HR/教育/合规等各类场景 |
| [表单 & 问卷](https://luckterence.github.io/n8n-workflows-cn/?cat=workflow-automation&sub=表单%20%26%20问卷) | 27 | 表单收集、问卷调查 |
| [电商 & 营销](https://luckterence.github.io/n8n-workflows-cn/?cat=workflow-automation&sub=电商%20%26%20营销) | 18 | 订单处理、营销自动化、库存管理 |
| [通知 & 告警](https://luckterence.github.io/n8n-workflows-cn/?cat=workflow-automation&sub=通知%20%26%20告警) | 15 | 推送通知、异常告警、状态监控 |
| [日历 & 日程](https://luckterence.github.io/n8n-workflows-cn/?cat=workflow-automation&sub=日历%20%26%20日程) | 13 | 日历事件、日程安排 |
| [项目管理](https://luckterence.github.io/n8n-workflows-cn/?cat=workflow-automation&sub=项目管理) | 12 | 任务跟踪、Bug 管理、开发流程 |

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

- **Tier A**（1479 个）— 外服节点已替换，配 API Key 就能跑
- **Tier B**（1 个）— 含 Gmail/Google Sheets 等国内用不了的服务，需手动替换（[升级指南](UPGRADE_GUIDE.md)）

> 注意：Tier 标准基于代码审查，标注为 A 不代表在所有 n8n 版本中都能 100% 跑通。欢迎实测后提 issue 或 PR 帮忙完善。

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

> **[工作流浏览站点](https://luckterence.github.io/n8n-workflows-cn/)** — 可搜索、可按分类筛选的在线浏览器，暗色主题。

启用方式：仓库 Settings > Pages > Source 选 `Deploy from a branch`，分支 `main`，目录 `/docs`，保存后等几分钟即可访问。

## 接下来想做的

- [x] CI/CD 自动验证 — GitHub Actions 检查工作流合法性
- [x] 工作流浏览站点 — 搭个 GitHub Pages，方便搜索筛选
- [x] 精选合集 — 按场景整理推荐组合
- [x] 完善适配 — 全部 1480 个已达 A/A-adapted，B/C 清零

## 参与进来

提 bug、给建议、直接改代码，都欢迎。参考 [CONTRIBUTING.md](CONTRIBUTING.md)。

可以帮忙的事：

1. 试试某个工作流能不能跑，遇到问题提 issue
2. 把自己用的服务替换方案加进来
3. 翻译英文说明、补使用示例
4. 帮忙完善工作流索引（index/ 目录）的分类

## 许可

原始模板来自 [nusquama/n8nworkflows.xyz](https://github.com/nusquama/n8nworkflows.xyz)，MIT 许可。本项目同样采用 MIT 许可。
