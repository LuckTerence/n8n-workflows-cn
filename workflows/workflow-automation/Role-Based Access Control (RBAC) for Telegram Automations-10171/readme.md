## 简介
**Role-Based Access Control (RBAC) for Telegram Automations**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Notion/Google Sheets/Slack)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/10171

---

# Role-Based Access Control (RBAC) for Telegram Automations


## 节点清单

| 节点 | 类型 |
|------|------|
| Telegram Trigger | Telegram 触发器 |
| No Operation, do nothing | 空操作 |
| No Operation, do nothing1 | 空操作 |
| No Operation, do nothing2 | 空操作 |
| Switch | Switch 路由 |
| Employee database | 数据表 |
| No Operation, do nothing3 | 空操作 |
| No Operation, do nothing4 | 空操作 |
| Choose Position | Switch 路由 |
| Slack Trigger | slackTrigger |
| Get row(s) in sheet | Google Sheets |
| Get a record | Airtable |
| Get a database page | Notion |
| If | IF 判断 |
| Filter | 过滤器 |
| On form submission | 表单触发器 |
| Schedule Trigger | 定时触发器 |



## 功能说明

Telegram 机器人，消息驱动自动化流程，定时执行。

定时触发、Telegram 消息触发，通过 Telegram 通知 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- Telegram Bot Token → @BotFather 创建

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：17
- 触发方式：Telegram 消息触发, 表单提交触发, 定时触发

## 触发方式
- Telegram Trigger 触发
- Slack Trigger 触发
- On form submission 触发
- Schedule Trigger 触发

## 统计
- 节点总数：17
- 触发节点：4
- 处理节点：13
- 输出节点：0
- 分类：workflow-automation
