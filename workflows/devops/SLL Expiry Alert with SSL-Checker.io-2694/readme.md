## 简介
**SLL Expiry Alert with SSL-Checker.io**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（需替换Google Sheets/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2694

---

# SLL Expiry Alert with SSL-Checker.io


## 节点清单

| 节点 | 类型 |
|------|------|
| URLs to Monitor | Google Sheets |
| Weekly Trigger | 定时触发器 |
| Fetch URLs | Google Sheets |
| Check SSL | HTTP Request |
| Expiry Alert | IF 判断 |
| Send Alert Email | Email 发送 |

## 触发方式
- Weekly Trigger 触发

## 统计
- 节点总数：6
- 触发节点：1
- 处理节点：3
- 输出节点：2
- 分类：devops
