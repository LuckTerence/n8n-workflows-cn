## 简介
**Obsidian Notes Read Aloud using AI: Available as a Podcast Feed**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets)（基本改完，配置 API Key 应该就能跑）
> 节点数：13 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/2699

---

# Obsidian Notes Read Aloud using AI: Available as a Podcast Feed


## 节点清单

| 节点 | 类型 |
|------|------|
| OpenAI1 | OpenAI |
| Webhook GET Note | Webhook |
| Webhook GET Podcast Feed | Webhook |
| Upload Audio to Cloudinary | HTTP Request |
| OpenAI | OpenAI |
| Merge | 数据合并 |
| Aggregate | 数据聚合 |
| Give Audio Unique Name | 数据设置 |
| Send Audio to Obsidian | 响应 Webhook |
| Rename Fields | 数据设置 |
| Append Item to Google Sheet | Google Sheets |
| Get Items from Google Sheets | Google Sheets |
| Write RSS Feed | Code |
| Return Podcast Feed to Webhook | 响应 Webhook |
| Manually Enter Other Data for Podcast Feed | 数据设置 |

## 触发方式
- Webhook GET Note 触发
- Webhook GET Podcast Feed 触发

## 统计
- 节点总数：15
- 触发节点：2
- 处理节点：10
- 输出节点：3
- 分类：workflow-automation
