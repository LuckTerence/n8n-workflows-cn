## 简介
**Automated Digital Certificate Creator & Validator with PDF Generation**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/11097

---

# Automated Digital Certificate Creator & Validator with PDF Generation


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
