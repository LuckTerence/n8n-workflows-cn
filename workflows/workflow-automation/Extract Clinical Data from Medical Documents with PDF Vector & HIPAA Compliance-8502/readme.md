## 简介
**Extract Clinical Data from Medical Documents with PDF Vector & HIPAA Compliance**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Drive)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/8502

---

# Extract Clinical Data from Medical Documents with PDF Vector & HIPAA Compliance


## 节点清单

| 节点 | 类型 |
|------|------|
| Manual Trigger | 手动触发 |
| Google Drive - Get Medical Record | Google Drive |
| PDF Vector - Extract Medical Data | pdfVector |
| Process & Validate Data | Code |
| Valid Record? | IF 判断 |
| Store in Secure Database | PostgreSQL |

## 触发方式
- Manual Trigger 触发

## 统计
- 节点总数：6
- 触发节点：1
- 处理节点：5
- 输出节点：0
- 分类：workflow-automation
