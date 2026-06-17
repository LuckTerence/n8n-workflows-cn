## 简介
**Automated QuickBooks Sales Anomaly Detector with Professional Email Alerts**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/10486

---

# Automated QuickBooks Sales Anomaly Detector with Professional Email Alerts


## 节点清单

| 节点 | 类型 |
|------|------|
| Create_Date_Range | 数据设置 |
| Fetch_30Day_Invoices | QuickBooks |
| Filter_Paid_30Day_Invoices | 过滤器 |
| Fetch_30Day_Sales_Receipts | HTTP Request |
| Sum_30Day_Totals | 文本摘要 |
| Calculate_30Day_Average | 数据设置 |
| Calculate_Deviation | 数据设置 |
| Check_If_Anomaly | IF 判断 |
| Prepare_Email_Content | 数据设置 |
| Send_Alert_Email | Email 发送 |
| Fetch_Yesterday_Invoices | QuickBooks |
| Fetch_Yesterday_Sales_Receipts | HTTP Request |
| Filter_Paid_Yesterday_Invoices | 过滤器 |
| Total_30Day_Sales_Receipts | Code |
| Merging_30Day_Invoices_Sales_Receipts | 数据合并 |
| Merging_Yesterday_Invoices_Sales_Receipts | 数据合并 |
| Sum_Yesterday_Totals | 文本摘要 |
| Combining_Overall_Invoices_Sales_Receipts | Code |
| Run_Every_Morning | 定时触发器 |
| Extract_Yesterday_Sales_Receipts | Code |
| Combine_Final_Totals | 数据合并 |

## 触发方式
- Run_Every_Morning 触发

## 统计
- 节点总数：21
- 触发节点：1
- 处理节点：17
- 输出节点：3
- 分类：workflow-automation
