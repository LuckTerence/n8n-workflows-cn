## 简介
**Assign Requests Using AI and Send Reminders Based On NocoDB Kanban Board Status**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3784

---

# Assign Requests Using AI and Send Reminders Based On NocoDB Kanban Board Status


## 节点清单

| 节点 | 类型 |
|------|------|
| Incident Form | 表单触发器 |
| Assign Category | AI Agent |
| OpenAI Chat Model1 | OpenAI Chat Model |
| Structure Output Todoist Ready1 | 结构化输出解析器 |
| Get incident definitions | NocoDB |
| Insert Incident | NocoDB |
| Aggregate for AI parsing | 数据聚合 |
| On schedule or during flow | 空操作 |
| When clicking ‘Test workflow’ | 手动触发 |
| Task is not picked up after expected response | IF 判断 |
| Send email to client | Email 发送 |
| Check status every day | 定时触发器 |
| Send email to asignee | Email 发送 |
| Get Unpicked Tasks | NocoDB |
| Get Unfinished Tasks | NocoDB |
| Task is not complete in expected time | IF 判断 |
| Send email to client1 | Email 发送 |
| If there is asignee email | IF 判断 |
| If there is assignee slack | IF 判断 |
| Slack to assignee | Slack |
| Send another email to asignee | Email 发送 |
| Format for Noco | 数据设置 |



## 功能说明

Assign Requests Using AI and Send Reminders Based （AI 增强)表单提交触发、手动触发、定时触发，通过 邮箱 + Slack + HTTP API 实现自动化。

定时触发、手动触发，通过 邮箱 + Slack + HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com
- 邮箱 SMTP/IMAP 账号密码

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：22
- 触发方式：表单提交触发, 手动触发, 定时触发

## 触发方式
- Incident Form 触发
- When clicking ‘Test workflow’ 触发
- Check status every day 触发

## 统计
- 节点总数：22
- 触发节点：3
- 处理节点：14
- 输出节点：5
- 分类：workflow-automation
