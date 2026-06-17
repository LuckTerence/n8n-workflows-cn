## 简介
**SSL Certificate Expiry Notifier (No Paid APIs)**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Gmail)（基本改完，配置 API Key 应该就能跑）
> 节点数：5 | 难度：⭐ 入门
> 原始来源：https://n8nworkflows.xyz/workflows/4643

---

# SSL Certificate Expiry Notifier (No Paid APIs)


## 节点清单

| 节点 | 类型 |
|------|------|
| URLs to Monitor | Google Sheets |
| Fetch URLs | Google Sheets |
| Check SSL | HTTP Request |
| Expiry Alert | IF 判断 |
| Send Email | Email 发送 |
| Daily Trigger | 定时触发器 |

## 触发方式
- Daily Trigger 触发

## 统计
- 节点总数：6
- 触发节点：1
- 处理节点：3
- 输出节点：2
- 分类：workflow-automation
