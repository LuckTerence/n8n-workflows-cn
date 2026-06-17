# Analyze Email Headers for IP Reputation and Spoofing Detection - Outlook

https://n8nworkflows.xyz/workflows/2676

## 节点清单

| 节点 | 类型 |
|------|------|
| Trigger on New Email | microsoftOutlookTrigger |
| Retrieve Headers of Email | HTTP Request |
| Extract Received Headers | Code |
| Remove Extra Received Headers | 数据限制 |
| Extract Original From IP | 数据设置 |
| Query IP Quality Score API | HTTP Request |
| Query IP API | HTTP Request |
| Authentication-Results Header? | IF 判断 |
| Extract Authentication-Results Header | Code |
| Received-SPF Header? | IF 判断 |
| DKIM-Signature Header? | IF 判断 |
| Set SPF Value | 数据设置 |
| Extract Received-SPF Header | Code |
| DKIM Signature Found | 数据设置 |
| DMARC Header? | IF 判断 |
| No DMARC Header | 数据设置 |
| Extract DMARC Header | Code |
| Set DMARC Value | 数据设置 |
| Original IP Found? | IF 判断 |
| No DKIM Signature Found | 数据设置 |
| Determine Auth Values | 数据设置 |
| No SPF Found | 数据设置 |
| Merge | 数据合并 |
| Aggregate | 数据聚合 |
| No Operation, do nothing | 空操作 |
| Format Webhook Output | 数据设置 |
| Format Individual Auth Outputs | 数据设置 |
| Format Combined Auth Output | 数据设置 |
| Respond to Webhook | 响应 Webhook |
| Webhook1 | Webhook |
| Set Headers | 数据设置 |
| Aggregate Received-SPF Headers | 数据聚合 |
| Set Headers Here | 数据设置 |
| Set Webhook Headers Here | 数据设置 |

## 触发方式
- Trigger on New Email 触发
- Webhook1 触发

## 统计
- 节点总数：34
- 触发节点：2
- 处理节点：28
- 输出节点：4
- 分类：workflow-automation
