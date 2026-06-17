# Build a Telegram Subscription Gate with Lead Magnet and Upsell Sequence

https://n8nworkflows.xyz/workflows/10598

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

## 触发方式
- 🔔 Telegram Message Trigger | Тригер повідомлень Телеграм2 触发

## 统计
- 节点总数：18
- 触发节点：1
- 处理节点：6
- 输出节点：11
- 分类：workflow-automation
