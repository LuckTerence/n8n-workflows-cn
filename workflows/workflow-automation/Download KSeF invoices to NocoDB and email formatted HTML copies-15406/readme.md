## 简介
**Download KSeF invoices to NocoDB and email formatted HTML copies**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：30 | 难度：⭐⭐⭐ 高级
> 原始来源：https://n8nworkflows.xyz/workflows/15406

---

# Download KSeF invoices to NocoDB and email formatted HTML copies


## 节点清单

| 节点 | 类型 |
|------|------|
| ⚙️ Config | 数据设置 |
| Get Public Key | HTTP Request |
| Get Challenge | HTTP Request |
| Encrypt Token | Code |
| Init Auth | HTTP Request |
| Check Auth Status | HTTP Request |
| Redeem Token | HTTP Request |
| Extract Invoices | Code |
| Send an Email | Email 发送 |
| Convert to File | 转换为文件 |
| Covert to Base64 | Code |
| Query Cost Invoices | HTTP Request |
| Query Issued Invoices | HTTP Request |
| Process only new invoices | 数据合并 |
| For each invoice | 分批处理 |
| Get invoice details | HTTP Request |
| to JSON | XML |
| Convert to HTML | Code |
| Created row with file input to be sent | 数据合并 |
| Insert new invoice details | NocoDB |
| Process both types | 数据合并 |
| Get existing invoices | NocoDB |
| Mark as "issued" invoice | 数据设置 |
| Mark as "cost" invoice | 数据设置 |
| Combine HTML with base invoice data | 数据合并 |
| Monitor Every Day for new invoices | 定时触发器 |
| Wait | 等待 |
| Terminate Auth Session | HTTP Request |
| Wait 2s | 等待 |
| Create Tables | 手动触发 |
| NocoDB Config | 数据设置 |
| Create NocoDB KSeF Invoices Table | HTTP Request |

## 触发方式
- Monitor Every Day for new invoices 触发
- Create Tables 触发

## 统计
- 节点总数：32
- 触发节点：2
- 处理节点：19
- 输出节点：11
- 分类：workflow-automation
