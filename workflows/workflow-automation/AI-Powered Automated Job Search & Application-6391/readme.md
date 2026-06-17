## 简介
**AI-Powered Automated Job Search & Application**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：B（需替换Google Sheets/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/6391

---

# AI-Powered Automated Job Search & Application


## 节点清单

| 节点 | 类型 |
|------|------|
| 3️⃣Set Job Title | 数据设置 |
| 4️⃣Get Jobs from Adzuna | HTTP Request |
| OpenRouter Chat Model | OpenRouter Chat Model |
| 7️⃣Extract Skills from Job Description | AI Agent |
| 📤 Split Jobs  | 数据拆分 |
| 🧪 Extract Job Info | 数据设置 |
| Filter Duplicates | Code |
| Webhook | Webhook |
| OpenRouter Chat Model1 | OpenRouter Chat Model |
| 📈 IF Score ≥ 3 | IF 判断 |
| 9️⃣Resume Match Score  | AI Agent |
| OpenRouter Chat Model3 | OpenRouter Chat Model |
| 🔥Write Cover Letter | AI Agent |
| 8️⃣Rewrite Resume | AI Agent |
| OpenRouter Chat Model2 | OpenRouter Chat Model |
| Upate sheets | Google Sheets |
| 📧Gmail | Email 发送 |
| Respond to Webhook | 响应 Webhook |
| Extract from File | 从文件提取 |

## 触发方式
- Webhook 触发

## 统计
- 节点总数：19
- 触发节点：1
- 处理节点：15
- 输出节点：3
- 分类：workflow-automation
