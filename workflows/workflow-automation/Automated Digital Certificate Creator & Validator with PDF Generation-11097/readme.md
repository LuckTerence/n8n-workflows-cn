# Automated Digital Certificate Creator & Validator with PDF Generation

https://n8nworkflows.xyz/workflows/11097

## 节点清单

| 节点 | 类型 |
|------|------|
| Insert_Certificaton | 数据表 |
| Generate_Certification_ID | Code |
| Find_Certification_By_ID | 数据表 |
| Certification_ID_Exists | IF 判断 |
| Generate_PDF | pdfGeneratorApi |
| Email_Certification | Email 发送 |
| Webhook_Check | Webhook |
| Find_Certification_By_ID1 | 数据表 |
| Certification_Exists | IF 判断 |
| Respond_Found | 响应 Webhook |
| Respond_NotFound | 响应 Webhook |
| Webhook_Creation | Webhook |

## 触发方式
- Webhook_Check 触发
- Webhook_Creation 触发

## 统计
- 节点总数：12
- 触发节点：2
- 处理节点：7
- 输出节点：3
- 分类：workflow-automation
