## 简介
**AI-Powered Vendor Policy & RSS Feed Analysis with Integrated Risk Scoring**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Gmail)（基本改完，配置 API Key 应该就能跑）
> 节点数：21 | 难度：⭐⭐⭐ 高级
> 原始来源：https://n8nworkflows.xyz/workflows/5103

---

# AI-Powered Vendor Policy & RSS Feed Analysis with Integrated Risk Scoring


## 节点清单

| 节点 | 类型 |
|------|------|
| HTTP Request | HTTP Request |
| AI Agent | AI Agent |
| RSS Feed List | Code |
| Splitting the Feeds | 数据拆分 |
| Vendor RSS Feed Read | RSS Feed |
| Vendor URLs | Code |
| AI Agent1 | AI Agent |
| Google Gemini Chat Model1 | OpenAI Chat Model |
| Gmail | Email 发送 |
| Gmail1 | Email 发送 |
| Google Gemini Chat Model | OpenAI Chat Model |
| Filtering last 24hrs feed | 过滤器 |
| Formatting the Content for Mail | Code |
| Sort the feeds | 数据排序 |
| Merge the content for AI | Code |
| Merge | 数据合并 |
| Format the Summary for Email | Code |
| Scrapping inside the Webpage content | Code |
| Cleaning up the code | Code |
| Daily Trigger | 定时触发器 |
| Splitting the Urls | 数据拆分 |
| Check the headers | IF 判断 |

## 触发方式
- Vendor RSS Feed Read 触发
- Daily Trigger 触发

## 统计
- 节点总数：22
- 触发节点：2
- 处理节点：17
- 输出节点：3
- 分类：workflow-automation
