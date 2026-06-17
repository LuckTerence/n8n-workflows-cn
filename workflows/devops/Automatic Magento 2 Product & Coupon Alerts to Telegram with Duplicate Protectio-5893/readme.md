# Automatic Magento 2 Product & Coupon Alerts to Telegram with Duplicate Protection

https://n8nworkflows.xyz/workflows/5893

## 节点清单

| 节点 | 类型 |
|------|------|
| Schedule Trigger | 定时触发器 |
| Get Rule Info | HTTP Request |
| Coupon Status | IF 判断 |
| Post to Telegram1 | Telegram |
| Product Alert to Telegram | Telegram |
| Init Database | MySQL |
| Fetch New Product | HTTP Request |
| Get Product Info | HTTP Request |
| Set Coupon as Posted | MySQL |
| Set Product as Posted | MySQL |
| Get Latest Offer | HTTP Request |
| Product Message Format | Code |
| Voucher Message Format | Code |
| New Voucher Entry | MySQL |
| New Product Entry | MySQL |
| Product Status | IF 判断 |
| Voucher to X | Twitter |
| Product X Post | Twitter |
| Voucher Duplication Protection | IF 判断 |
| Product Duplication Protection | IF 判断 |

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：20
- 触发节点：1
- 处理节点：13
- 输出节点：6
- 分类：devops
