## 简介
**Build a Telegram Subscription Gate with Lead Magnet and Upsell Sequence**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/10598

---

# Build a Telegram Subscription Gate with Lead Magnet and Upsell Sequence


## 节点清单

| 节点 | 类型 |
|------|------|
| ❌ Subscription Check Failed | Перевірка підписки не вдалася2 | Telegram |
| 🔧 Extract User & Callback Data | Витяг даних користувача2 | Code |
| 🌐 Check Telegram Subscription | Перевірка підписки в Телеграм2 | HTTP Request |
| ✅ Acknowledge Button Click | Підтвердження натискання кнопки2 | HTTP Request |
| ❓ Is Subscription Check Request? | Запит на перевірку підписки?2 | IF 判断 |
| 🔔 Telegram Message Trigger | Тригер повідомлень Телеграм2 | Telegram 触发器 |
| 📈 Upsell/CrossSell/DownSell System | Система допродажів2 | Telegram |
| 🎁 Premium Offer Message | Повідомлення преміум пропозиції2 | Telegram |
| 🔒 Lock Permissions | Блокування дозволів2 | Telegram |
| ✅ Subscription Confirmed - Send Lead Magnet | Підписка підтверджена2 | Telegram |
| ✅ Is User Subscribed? | Користувач підписаний?2 | IF 判断 |
| Closed Channel | HTTP Request |
| Wait | 等待 |
| HTTP typing...1 | HTTP Request |
| 📈 Upsell/CrossSell/DownSell System | Система допродажів | Telegram |
| Wait1 | 等待 |
| ❓ Is /ok Command? | Команда /more?2 | IF 判断 |
| HTTP typing... | HTTP Request |



## 功能说明

Telegram 机器人，消息驱动自动化流程。

Telegram 消息触发，通过 Telegram 通知 实现自动化。

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

- 节点总数：18
- 触发方式：Telegram 消息触发

## 触发方式
- 🔔 Telegram Message Trigger | Тригер повідомлень Телеграм2 触发

## 统计
- 节点总数：18
- 触发节点：1
- 处理节点：6
- 输出节点：11
- 分类：workflow-automation
