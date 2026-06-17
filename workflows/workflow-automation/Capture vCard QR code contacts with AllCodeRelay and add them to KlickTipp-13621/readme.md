# Capture vCard QR code contacts with AllCodeRelay and add them to KlickTipp

https://n8nworkflows.xyz/workflows/13621

## 节点清单

| 节点 | 类型 |
|------|------|
| Filter: vCard Only | 过滤器 |
| Parse: vCard → Contact Fields | Code |
| AllCodeRelay: Scan Webhook | Webhook |
| KlickTipp: Add Contact with DOI | Klicktipp |

## 触发方式
- AllCodeRelay: Scan Webhook 触发

## 统计
- 节点总数：4
- 触发节点：1
- 处理节点：3
- 输出节点：0
- 分类：workflow-automation
