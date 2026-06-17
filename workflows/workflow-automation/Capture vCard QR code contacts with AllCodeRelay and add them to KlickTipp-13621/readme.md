## 简介
**Capture vCard QR code contacts with AllCodeRelay and add them to KlickTipp**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：3 | 难度：⭐ 入门
> 原始来源：https://n8nworkflows.xyz/workflows/13621

---

# Capture vCard QR code contacts with AllCodeRelay and add them to KlickTipp


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
