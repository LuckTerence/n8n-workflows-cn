## 简介
**Extract Text from Images & PDFs via Telegram with Mistral OCR to Markdown**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/6209

---

# Extract Text from Images & PDFs via Telegram with Mistral OCR to Markdown


## 节点清单

| 节点 | 类型 |
|------|------|
| Image / PDF | IF 判断 |
| Mistral OCR | HTTP Request |
| Settings | 数据设置 |
| Telegram Event Handler | Switch 路由 |
| Status “Typing…” | Telegram |
| Notification about correct commands | Telegram |
| Maximum file size exceeded | Telegram |
| Checking file size | IF 判断 |
| File classifier | Code |
| Generating temporary file link | Telegram |
| Invalid file | Telegram |
| Markdown converter | Code |
| Converting Markdown to File | 转换为文件 |
| Manual Webhook Setup Trigger | 手动触发 |
| Telegram Webhook Configuration | 数据设置 |
| Check Production Mode | IF 判断 |
| Set Production Webhook | HTTP Request |
| Set Development Webhook | HTTP Request |
| Return Webhook Status | HTTP Request |
| Check Whitelist Status | IF 判断 |
| Whitelist Logic | Code |
| Access Denied | Telegram |
| Determine Message Type | Switch 路由 |
| Inform Bot Capabilities | Telegram |
| Command Router | Switch 路由 |
| Send Markdown File to Telegram | Telegram |
| Respond with attachment | 响应 Webhook |
| Determine Incoming Request Source Type | Switch 路由 |
| Is Whitelist Disabled? | IF 判断 |
| Get a file | Telegram |
| Incoming request | Webhook |
| Problem with file recognition | Telegram |



## 功能说明

Telegram 机器人，消息驱动自动化流程，Webhook 触发。

Webhook触发、手动触发，通过 Telegram 通知 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- Telegram Bot Token → @BotFather 创建
- 通义万相 API Key → https://dashscope.aliyun.com

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：32
- 触发方式：手动触发, Webhook 触发

## 触发方式
- Manual Webhook Setup Trigger 触发
- Incoming request 触发

## 统计
- 节点总数：32
- 触发节点：2
- 处理节点：15
- 输出节点：15
- 分类：workflow-automation
