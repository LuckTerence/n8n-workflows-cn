## 简介
**Gmail智能分类归档**

AI自动分类邮件并归档

> 分类：工作流自动化 | 适配等级：A（需替换Gmail)（AI模型已替换为DeepSeek，部分边角节点可能仍需手动调整）
> 原始来源：https://n8nworkflows.xyz/workflows/3686

---

# Gmail智能分类归档


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Test workflow’ | 手动触发 |
| OpenRouter Chat Model | OpenRouter Chat Model |
| Telegram Trigger | Telegram 触发器 |
| mail_label_setter | Gmail 工具 |
| mail_archiver | Gmail 工具 |
| Aggregate | 数据聚合 |
| Telegram | Telegram |
| OpenRouter Chat Model1 | OpenRouter Chat Model |
| Reporter | AI Agent |
| Get mails in INBOX | Gmail |
| Filter processed | 过滤器 |
| Categoriser | AI Agent |



## 功能说明

邮件自动化处理，AI 分类整理或。

定时触发、Telegram 消息触发、手动触发，通过 Telegram 通知 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com
- Telegram Bot Token → @BotFather 创建
- 邮箱 SMTP/IMAP 账号密码

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：12
- 触发方式：手动触发, Telegram 消息触发

## 触发方式
- When clicking ‘Test workflow’ 触发
- Telegram Trigger 触发

## 统计
- 节点总数：12
- 触发节点：2
- 处理节点：9
- 输出节点：1
- 分类：workflow-automation
