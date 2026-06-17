# n8n-workflows-cn

> 让中国开发者和企业零门槛使用 n8n — 1480+ 工作流模板已全面适配国内服务

[![Workflows](https://img.shields.io/badge/Workflows-1480-brightgreen)](INDEX.md)
[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)](CONTRIBUTING.md)
[![n8n](https://img.shields.io/badge/n8n-%3E%3D1.0-red)](https://n8n.io)

---

## 一句话说清

把 n8n 开源生态中 1480+ 个现成工作流模板中的海外服务（OpenAI、Slack、Google Workspace 等）**全部替换为国内可用方案**。导入即用，无需翻墙，无需海外账号。

## 解决什么问题

中国开发者和企业在使用 n8n 官方工作流模板时，会遇到三个核心痛点：

| 痛点 | 具体问题 | 解决方案 |
|------|----------|----------|
| **AI 不可用** | OpenAI、Claude、Gemini 需要海外账号和支付方式 | 替换为 DeepSeek / 通义千问 |
| **服务不通** | Slack、Gmail、Google Sheets 等在国内无法访问 | 替换为飞书 / QQ邮箱 / 飞书多维表格 |
| **水土不服** | 全英文文档和节点说明，上手门槛高 | 每个工作流附带中文说明 |

## 30 秒快速体验

```bash
# 1. 启动 n8n（Docker）
docker run -d --name n8n -p 5678:5678 -v n8n_data:/home/node/.n8n n8nio/n8n

# 2. 打开 http://localhost:5678，点击 Import from File

# 3. 导入任意 workflow.json，填入 API Key，开始使用
```

> 推荐从 `workflows/ai-agent/AI Agent聊天-1954/workflow.json` 开始体验 — 一个基础 AI 聊天 Agent，5 个节点，导入即用。

## 工作流分类

| 分类 | 数量 | 适用场景 |
|------|:----:|----------|
| [Workflow Automation](workflows/workflow-automation/) | 1110 | 业务流程自动化、邮件处理、数据采集、社交媒体、CRM 集成 |
| [DevOps](workflows/devops/) | 153 | 服务器管理、API 开发、MCP Server 构建、监控告警、自动部署 |
| [AI Agent](workflows/ai-agent/) | 93 | AI 智能体、聊天机器人、多代理系统、MCP 协议集成 |
| [Multimodal AI](workflows/multimodal-ai/) | 52 | 图像生成、语音合成、视频生成、音频转录、3D 内容生成 |
| [Knowledge RAG](workflows/knowledge-rag/) | 47 | 向量数据库、检索增强生成、文档问答、语义缓存 |
| [Finance Analysis](workflows/finance-analysis/) | 25 | 股票分析、加密货币、交易信号、欺诈检测、市场数据 |

[查看完整索引（1480 个工作流列表）](INDEX.md)

## 服务替换对照

n8n 的专用节点本质上是 HTTP Request 的封装。大部分替换方案通过将专用节点改为 HTTP Request 节点并配置对应国内服务的 API 实现。

| 原始服务 | 替换方案 | 修改方式 |
|----------|----------|----------|
| OpenAI (GPT-4/GPT-4o) | **DeepSeek** | 修改 Base URL 为 `https://api.deepseek.com`，Model 为 `deepseek-chat` |
| Anthropic (Claude) | **DeepSeek** | 将 Anthropic Chat Model 节点替换为 OpenAI Chat Model，同上配置 |
| Google Gemini | **通义千问** | 替换为 OpenAI Chat Model，Base URL 为 `https://dashscope.aliyuncs.com/compatible-mode/v1` |
| Slack | **飞书群机器人** | 修改 Webhook URL 为飞书机器人地址，调整消息体格式 |
| Gmail | **QQ邮箱 / 网易企业邮箱** | 替换为 Email (IMAP/SMTP) 节点 |
| Google Sheets | **飞书多维表格** | 替换为 HTTP Request 节点，调用飞书 Bitable API |
| Google Drive | **阿里云 OSS / 腾讯云 COS** | 替换为 HTTP Request 节点 |
| Google Calendar | **飞书日历** | 替换为 HTTP Request 节点 |
| Notion | **飞书文档 / 语雀** | 替换为 HTTP Request 节点 |
| Twilio | **腾讯云短信 / 阿里云短信** | 替换为 HTTP Request 节点 |
| Stripe / PayPal | **微信支付 / 支付宝** | 替换为 HTTP Request 节点 |
| GitHub | **Gitee** | HTTP Request 节点调用 Gitee API |
| Supabase | **腾讯云 CloudBase** | HTTP Request 节点 |
| Zoom | **腾讯会议** | HTTP Request 节点 |

## 工作流质量标记

每个 `workflow.json` 中包含 `_cn_meta` 字段，记录了适配信息：

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

- **Tier A** — 完全适配，导入即可使用（只需配置 API Key）
- **Tier B** — 核心功能可用，部分高级功能需自行调整
- **Tier C** — 框架适配，具体节点需根据实际场景配置

## 目录结构

```
workflows/
  {分类}/
    {工作流名称}-{ID}/
      workflow.json    # 工作流定义（含 _cn_meta 适配元数据）
      readme.md        # 节点说明、触发方式与适配记录
```

## 使用方式

在 n8n 编辑器中通过 **Import from File** 导入 `workflow.json` 即可。

n8n 安装（Docker）：

```bash
docker run -d --name n8n -p 5678:5678 -v n8n_data:/home/node/.n8n n8nio/n8n
```

## 路线图

- [ ] **CI/CD 自动验证** — GitHub Actions 自动检查工作流与最新 n8n 版本兼容性
- [ ] **工作流搜索站** — GitHub Pages 搭建可搜索、可筛选的浏览站点
- [ ] **精选合集** — 按场景（智能客服、自动化日报、财务报表等）打包推荐
- [ ] **视频教程** — 典型工作流的配置与使用教程
- [ ] **社区排行榜** — 贡献者榜单与热门工作流排名

## 贡献

欢迎贡献！无论是提交新的工作流适配、修复已有问题，还是完善文档，都请参考 [CONTRIBUTING.md](CONTRIBUTING.md)。

**主要贡献方向：**

1. 新增国内服务的替换方案（如替换其他海外 SaaS）
2. 修复已有工作流的兼容性问题
3. 补充中文说明和使用示例
4. 完善分类和索引

## 许可

模板来源：[nusquama/n8nworkflows.xyz](https://github.com/nusquama/n8nworkflows.xyz)，MIT 许可。

本项目同样采用 MIT 许可。
