## 简介
**Send Telegram notifications for new Feedspace testimonials**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/12152

---

# Send Telegram notifications for new Feedspace testimonials


## 节点清单

| 节点 | 类型 |
|------|------|
| Receive Feedspace Webhook | Webhook |
| Send Telegram Notification | Telegram |
| Has Error? | IF 判断 |
| Success Response | 响应 Webhook |
| Format Error Details | Code |
| Error Response | 响应 Webhook |



## 功能说明

Telegram 机器人，消息驱动自动化流程，Webhook 触发。

Webhook触发，通过 Telegram 通知 实现自动化。

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

- 节点总数：6
- 触发方式：Webhook 触发

## 触发方式
- Receive Feedspace Webhook 触发

## 统计
- 节点总数：6
- 触发节点：1
- 处理节点：2
- 输出节点：3
- 分类：workflow-automation
