## 简介
**Generate AI camera moves with Seedance and build a previs review board**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Slack/Google Drive)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/14891

---

# Generate AI camera moves with Seedance and build a previs review board


## 节点清单

| 节点 | 类型 |
|------|------|
| Extract & Map Form Fields | Code |
| AI Agent: Generate Camera Options | AI Agent |
| Azure OpenAI: GPT-4o Mini | Azure OpenAI Chat Model |
| Parse AI Response → Seedance Items | Code |
| Build Seedance API Request | Code |
| Seedance: Submit Camera Move Job | HTTP Request |
| Store Job ID + Move Metadata | Code |
| Poll: Check Move Render Status | HTTP Request |
| Move Render Complete? | IF 判断 |
| Wait 20s Before Retry | 等待 |
| Collect Move + Tag Key Frames | Code |
| Download Lighting Reference Video | HTTP Request |
| Google Drive: Archive Lighting Ref | Google Drive |
| Jira: Create Previs Review Task | jira |
| ClickUp: Create Previs Production Record | clickUp |
| Telegram: Deliver Previs to Supervisor | Telegram |
| Telegram: Alert on AI Agent Failure | Telegram |
| Form: Previs Brief Input1 | 表单触发器 |
| Compile Previs Board Package1 | Code |
| Slack: Publish Previs Board1 | Slack |
| On Workflow Error | 错误触发器 |
| Slack: Error Alert | Slack |



## 功能说明

Generate AI camera moves with Seedance and build a（AI 增强)表单提交触发，通过 Telegram + Slack + HTTP API 实现自动化。

，通过 Telegram 通知 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com
- Telegram Bot Token → @BotFather 创建
- 通义万相 API Key → https://dashscope.aliyun.com

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：22
- 触发方式：表单提交触发

## 触发方式
- Form: Previs Brief Input1 触发
- On Workflow Error 触发

## 统计
- 节点总数：22
- 触发节点：2
- 处理节点：13
- 输出节点：7
- 分类：workflow-automation
