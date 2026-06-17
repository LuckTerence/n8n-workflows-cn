## 简介
**Birthday and Ephemeris Notification (Google Contact, Telegram & Home Assistant)**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/4462

---

# Birthday and Ephemeris Notification (Google Contact, Telegram & Home Assistant)


## 节点清单

| 节点 | 类型 |
|------|------|
| Google Contacts | googleContacts |
| Get One first name list | 数据设置 |
| First names | 数据聚合 |
| Nominis - Saints du jour | HTTP Request |
| Combine Firstname & Saints | 数据合并 |
| No Saint Today ? | IF 判断 |
| Compose Message | 数据设置 |
| Single list Birthday | 数据设置 |
| Get Nominis URL | 数据设置 |
| Sent Telegram Message | Telegram |
| Birthday Today? | IF 判断 |
| Set Date Offset | 数据设置 |
| Everyday at 7am | 定时触发器 |
| List of Saints of the day | 数据设置 |
| Check if any firstname match a Saints of the day | Code |
| Aggregate Birthdays | 数据聚合 |
| Aggregate No Birthday | 数据聚合 |
| "Bonne fête" celebration message | 数据设置 |
| Birthday celebration message | 数据设置 |
| Merge Birthday + Fête Messages | 数据合并 |
| Check if any celebration to make | IF 判断 |
| Send to Google Home Speaker | homeAssistant |



## 功能说明

Telegram 机器人，消息驱动自动化流程，定时执行。

定时触发，通过 Telegram 通知 实现自动化。

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

- 节点总数：22
- 触发方式：定时触发

## 触发方式
- Everyday at 7am 触发

## 统计
- 节点总数：22
- 触发节点：1
- 处理节点：19
- 输出节点：2
- 分类：workflow-automation
