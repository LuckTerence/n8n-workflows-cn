# n8n-workflows-cn

> n8n 工作流模板的本地化笔记 — 记录一些替换海外服务的尝试，希望对有类似需求的朋友有帮助

[![Workflows](https://img.shields.io/badge/Workflows-1480-brightgreen)](INDEX.md)
[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)](CONTRIBUTING.md)
[![n8n](https://img.shields.io/badge/n8n-%3E%3D1.0-red)](https://n8n.io)

---

## 这个项目是什么

这是 [nusquama/n8nworkflows.xyz](https://github.com/nusquama/n8nworkflows.xyz) 的一个分支项目。原项目收集了大量 n8n 工作流模板，但因为很多模板依赖 OpenAI、Slack、Google 等服务，在国内使用时不太方便。于是我把这些模板里用到的海外服务，逐个试着替换成了自己常用的国内方案。

目前整理了一千多个工作流，替换了十几种服务。不一定每个都完美适配，但大部分核心功能应该是可以跑通的。

## 起因

自己在用 n8n 的时候，经常遇到这样的问题：

- 看到一个不错的模板，点进去发现全是 OpenAI / Claude 的节点，没有相关账号就很尴尬
- Slack、Google Sheets 这些服务平时也不用，模板里的这些部分基本用不上
- 每次都要手动改 Base URL、换节点类型、调消息体格式，时间长了觉得不如顺手整理一下

所以就做了这个仓库，算是个人的学习记录，也希望能帮到有同样困扰的朋友。

## 快速体验

```bash
# 1. 启动 n8n（Docker）
docker run -d --name n8n -p 5678:5678 -v n8n_data:/home/node/.n8n n8nio/n8n

# 2. 打开 http://localhost:5678，点击 Import from File

# 3. 导入任意 workflow.json，填入 API Key，开始使用
```

> 推荐从 `workflows/ai-agent/AI Agent聊天-1954/workflow.json` 开始试试，一个基础的 AI 聊天 Agent，只有 5 个节点。

## 工作流分类

需要先说明一下：这些工作流的质量参差不齐，有些适配得比较完整，有些只改了核心节点。具体可以在每个工作流目录下的 `readme.md` 里看到适配记录。

| 分类 | 数量 | 大概包含哪些 |
|------|:----:|----------|
| [Workflow Automation](workflows/workflow-automation/) | 1110 | 业务流程自动化、邮件处理、数据采集、CRM 集成 |
| [DevOps](workflows/devops/) | 153 | 服务器管理、API 开发、MCP Server、监控告警 |
| [AI Agent](workflows/ai-agent/) | 93 | AI 智能体、聊天机器人、多代理系统 |
| [Multimodal AI](workflows/multimodal-ai/) | 52 | 图像生成、语音合成、视频生成、音频转录 |
| [Knowledge RAG](workflows/knowledge-rag/) | 47 | 向量数据库、RAG 检索、文档问答 |
| [Finance Analysis](workflows/finance-analysis/) | 25 | 股票分析、加密货币、交易信号 |

[完整索引（1480 个工作流）](INDEX.md)

## 我做了哪些替换

主要思路是：n8n 的专用节点本质上是对 HTTP API 的封装，所以大部分可以通过换成 HTTP Request + 国内服务 API 来实现。也有少数情况可以直接复用 n8n 内置节点（比如 Email 节点替换 Gmail）。

| 原始服务 | 替换方案 | 修改方式 |
|----------|----------|----------|
| OpenAI (GPT-4/GPT-4o) | DeepSeek | 修改 Base URL 为 `https://api.deepseek.com`，Model 为 `deepseek-chat` |
| Anthropic (Claude) | DeepSeek | Anthropic Chat Model 替换为 OpenAI Chat Model，同上配置 |
| Google Gemini | 通义千问 | 替换为 OpenAI Chat Model，Base URL 改为通义千问兼容地址 |
| Slack | 飞书群机器人 | 修改 Webhook URL 为飞书机器人地址，调整消息体格式 |
| Gmail | QQ邮箱 / 网易企业邮箱 | 替换为 Email (IMAP/SMTP) 节点 |
| Google Sheets | 飞书多维表格 | 替换为 HTTP Request 节点，调用飞书 Bitable API |
| Google Drive | 阿里云 OSS / 腾讯云 COS | 替换为 HTTP Request 节点 |
| Google Calendar | 飞书日历 | 替换为 HTTP Request 节点 |
| Notion | 飞书文档 / 语雀 | 替换为 HTTP Request 节点 |
| Twilio | 腾讯云短信 / 阿里云短信 | 替换为 HTTP Request 节点 |
| Stripe / PayPal | 微信支付 / 支付宝 | 替换为 HTTP Request 节点 |
| GitHub | Gitee | HTTP Request 节点调用 Gitee API |
| Supabase | 腾讯云 CloudBase | HTTP Request 节点 |
| Zoom | 腾讯会议 | HTTP Request 节点 |

> 这些替换方案可能不是最优解，如果你有更好的想法，欢迎提 issue 或 PR 一起讨论。

## 适配程度的说明

每个 `workflow.json` 里加了一个 `_cn_meta` 字段，记录适配情况：

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

- **Tier A** — 基本上改完了，导入后配置 API Key 应该就能跑
- **Tier B** — 核心链路通了，边边角角的节点可能还要自己调一下
- **Tier C** — 只搭了个框架，具体参数需要根据实际场景来配

## 目录结构

```
workflows/
  {分类}/
    {工作流名称}-{ID}/
      workflow.json    # 工作流定义（含 _cn_meta 适配元数据）
      readme.md        # 节点说明与适配记录
```

## 使用方式

在 n8n 编辑器里用 **Import from File** 导入 `workflow.json` 就行。

n8n 安装（Docker）：

```bash
docker run -d --name n8n -p 5678:5678 -v n8n_data:/home/node/.n8n n8nio/n8n
```

## 接下来想做的事

- [ ] CI/CD 自动验证 — 用 GitHub Actions 检查工作流和新版本 n8n 的兼容性
- [ ] 工作流浏览站点 — 搭个简单的 GitHub Pages，方便搜索和筛选
- [ ] 精选合集 — 按场景整理一些推荐的工作流组合
- [ ] 完善适配 — 把更多 Tier C 的工作流提升到 Tier A

## 参与进来

不管是提 bug、给建议还是直接改代码，都非常欢迎。具体怎么做可以参考 [CONTRIBUTING.md](CONTRIBUTING.md)。

**如果你有兴趣，可以帮忙：**

1. 试试某个工作流能不能正常跑，遇到问题提个 issue
2. 把自己常用的服务替换方案加进来
3. 把英文说明翻译成中文，或补充使用示例
4. 帮忙整理 INDEX.md，让分类更好找

## 许可

原始模板来自 [nusquama/n8nworkflows.xyz](https://github.com/nusquama/n8nworkflows.xyz)，MIT 许可。

本项目同样采用 MIT 许可。
