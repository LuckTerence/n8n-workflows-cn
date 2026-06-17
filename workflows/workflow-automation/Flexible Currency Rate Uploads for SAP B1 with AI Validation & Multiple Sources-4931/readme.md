## 简介
**Flexible Currency Rate Uploads for SAP B1 with AI Validation & Multiple Sources**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：B（需替换Google Sheets)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/4931

---

# Flexible Currency Rate Uploads for SAP B1 with AI Validation & Multiple Sources


## 节点清单

| 节点 | 类型 |
|------|------|
| Webhook | Webhook |
| Switch | Switch 路由 |
| Enviar SAP (JSON) | HTTP Request |
| Conectar SAP | HTTP Request |
| Microsoft SQL | microsoftSql |
| Extraer Query | 数据设置 |
| Enviar SAP (SQL) | HTTP Request |
| Limit | 数据限制 |
| Enviar SAP (MANUAL) | HTTP Request |
| OpenAI | OpenAI |
| Split Out | 数据拆分 |
| Google Sheets | Google Sheets |
| Enviar SAP (SHEET) | HTTP Request |
| Success | Google Sheets |
| Fallo | Google Sheets |
| Success1 | Google Sheets |
| Comprobar Fecha | OpenAI |
| Fallo1 | Google Sheets |
| Success2 | Google Sheets |
| Fallo2 | Google Sheets |
| Success3 | Google Sheets |
| Fallo3 | Google Sheets |

## 触发方式
- Webhook 触发

## 统计
- 节点总数：22
- 触发节点：1
- 处理节点：16
- 输出节点：5
- 分类：workflow-automation
