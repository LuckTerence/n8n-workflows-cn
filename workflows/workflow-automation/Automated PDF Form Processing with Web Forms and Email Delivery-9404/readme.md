## 简介
**Automated PDF Form Processing with Web Forms and Email Delivery**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/9404

---

# Automated PDF Form Processing with Web Forms and Email Delivery


## 节点清单

| 节点 | 类型 |
|------|------|
| HTTP Request | HTTP Request |
| PDF Form Fill (Fill PDF Fields) | PdfFormFill |
| Get PDF Form Fields | GetFormFieldNames |
| Send email | Email 发送 |
| FormData Endpoint | Webhook |
| HTML for Landingpage | HTML |
| Landingpage Endpoint | Webhook |
| Respond to Webhook | 响应 Webhook |
| Set Form Endpoint | 数据设置 |

## 触发方式
- FormData Endpoint 触发
- Landingpage Endpoint 触发

## 统计
- 节点总数：9
- 触发节点：2
- 处理节点：4
- 输出节点：3
- 分类：workflow-automation
