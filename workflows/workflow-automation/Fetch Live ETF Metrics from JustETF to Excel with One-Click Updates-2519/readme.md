## 简介
**Fetch Live ETF Metrics from JustETF to Excel with One-Click Updates**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2519

---

# Fetch Live ETF Metrics from JustETF to Excel with One-Click Updates


## 节点清单

| 节点 | 类型 |
|------|------|
| Loop Over Items | 分批处理 |
| Logs the date & time | microsoftExcel |
| Gets rows from table | microsoftExcel |
| Forge a Get request with ISIN Values | HTTP Request |
| Extracts defined values with css selector | HTML |
| Extracts defined values in better format | Code |
| Updates my table | microsoftExcel |
| When called by Excel Macro | Webhook |
| Edit Fields | 数据设置 |
| When clicking ‘Test workflow’ | 手动触发 |

## 触发方式
- When called by Excel Macro 触发
- When clicking ‘Test workflow’ 触发

## 统计
- 节点总数：10
- 触发节点：2
- 处理节点：7
- 输出节点：1
- 分类：workflow-automation
