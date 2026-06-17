## 简介
**Automatically document and backup N8N workflows**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3354

---

# Automatically document and backup N8N workflows


## 节点清单

| 节点 | 类型 |
|------|------|
| Set fields | 数据设置 |
| Get notion page with workflow id | HTTP Request |
| Map fields | 数据设置 |
| Add to Notion | Notion |
| Update in Notion | Notion |
| Notify internal-infra of push | Slack |
| Notify internal-infra of update | Slack |
| Notify on workflow setup error | Slack |
| Summarize what the Workflow does | OpenAI |
| Upload changes to repo | github |
| Create new file in repo | github |
| Notify on create file in repo fail | Slack |
| Is this a new workflow (to Notion) ? | IF 判断 |
| Every Monday at 1am | 定时触发器 |
| Check if updated in last 7 days | IF 判断 |
| Get active workflows with internal-infra tag | n8n |
| Check that error workflow has been configured | IF 判断 |



## 功能说明

自动备份系统，定时备份数据或配置，定时执行。

定时触发，通过 在线表格 + Git + HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：17
- 触发方式：定时触发

## 触发方式
- Every Monday at 1am 触发

## 统计
- 节点总数：17
- 触发节点：1
- 处理节点：11
- 输出节点：5
- 分类：devops
