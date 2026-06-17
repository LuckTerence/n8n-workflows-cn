## 简介
**Automate Student Admission Process with Excel, Validation & Email Notifications**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/6996

---

# Automate Student Admission Process with Excel, Validation & Email Notifications


## 节点清单

| 节点 | 类型 |
|------|------|
| Validate Application Data | IF 判断 |
| Process Application Data | Code |
| Update Student Database | microsoftExcel |
| Prepare Welcome Email | Code |
| Success Response | 响应 Webhook |
| Error Response | 响应 Webhook |
| Read Student Data | microsoftExcel |
| Send email | Email 发送 |
| Trigger at Every Day 7 am | 定时触发器 |

## 触发方式
- Trigger at Every Day 7 am 触发

## 统计
- 节点总数：9
- 触发节点：1
- 处理节点：5
- 输出节点：3
- 分类：workflow-automation
