## 简介
**RSS to Social: Automated Content Generation with Llama 3 & GetLate Publishing**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：B（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/9147

---

# RSS to Social: Automated Content Generation with Llama 3 & GetLate Publishing


## 节点清单

| 节点 | 类型 |
|------|------|
| Groq Chat Model | Groq Chat Model |
| Structured Output Parser | 结构化输出解析器 |
| Set Post Schedule | 定时触发器 |
| Markdown: Convert Article Content | Markdown |
| Groq Chat Model1 | Groq Chat Model |
| Structured Output Parser1 | 结构化输出解析器 |
| LinkedIn SMCG | LLM Chain |
| Bluesky SMCG | LLM Chain |
| Convert Image to Base64 (Bluesky) | Code |
| Generate Post Image (Bluesky) | HTTP Request |
| Store Image on Imgbb (Bluesky) | HTTP Request |
| Post/Draft via GetLate API (Bluesky) | HTTP Request |
| Store Generated Post Content (Bluesky) | Airtable |
| Post/Draft via GetLate API (No Image, Bluesky) | HTTP Request |
| Store Generated Post Content (No Image, Bluesky) | Airtable |
| Check For Image Generation Prompt (Bluesky) | IF 判断 |
| Check For Image Generation Prompt (LinkedIn) | IF 判断 |
| Post/Draft via GetLate API (No Image, LinkedIn)) | HTTP Request |
| Generate Post Image (LinkedIn) | HTTP Request |
| Convert Image to Base64 (LinkedIn) | Code |
| Store Image on Imgbb (LinkedIn) | HTTP Request |
| Post/Draft via GetLate API (LinkedIn) | HTTP Request |
| Store Generated Post Content (LinkedIn) | Airtable |
| Store Generated Post Content (No Image, LinkedIn) | Airtable |
| Check Platform | Switch 路由 |
| Bluesky SMCG Prompt | 数据设置 |
| Pull New Article | Airtable |
| Set SMCG Custom Prompt Parameters | 数据设置 |
| Markdown: Convert Article Content1 | Markdown |
| RSS Feed Trigger: '#to-share-bluesky' | rssFeedReadTrigger |
| Set Platform (Bluesky) | 数据设置 |
| Store Article Content (LinkedIn) | Airtable |
| Set Platform (LinkedIn) | 数据设置 |
| RSS Feed Trigger: '#to-share-linkedin' | rssFeedReadTrigger |
| Store Article Content | Airtable |
| LinkedIn SMCG Prompt | 数据设置 |

## 触发方式
- Set Post Schedule 触发
- RSS Feed Trigger: '#to-share-bluesky' 触发
- RSS Feed Trigger: '#to-share-linkedin' 触发

## 统计
- 节点总数：36
- 触发节点：3
- 处理节点：25
- 输出节点：8
- 分类：workflow-automation
