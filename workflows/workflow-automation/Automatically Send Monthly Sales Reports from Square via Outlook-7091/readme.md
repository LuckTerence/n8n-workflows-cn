## 简介
**Automatically Send Monthly Sales Reports from Square via Outlook**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/7091

---

# Automatically Send Monthly Sales Reports from Square via Outlook


## 节点清单

| 节点 | 类型 |
|------|------|
| Get Square Locations | HTTP Request |
| Turn Locations Into List | 数据拆分 |
| Ignore Locations w/o Sales | IF 判断 |
| Get Sales from Square | HTTP Request |
| Compile Sales Reports | Code |
| Schedule Trigger | 定时触发器 |
| Convert Sales Summary to CSV File | 转换为文件 |
| Get Dates From Last Month | Code |
| Send Report | Outlook |

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：9
- 触发节点：1
- 处理节点：5
- 输出节点：3
- 分类：workflow-automation
