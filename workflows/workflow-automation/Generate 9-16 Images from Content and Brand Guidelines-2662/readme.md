## 简介
**Generate 9:16 Images from Content and Brand Guidelines**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：B（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2662

---

# Generate 9:16 Images from Content and Brand Guidelines


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Test workflow’ | 手动触发 |
| Set Guidelines | 数据设置 |
| Get Brand Guidelines | Airtable |
| Get SEO Keywords | Airtable |
| Remove Duplicates | 去重 |
| Keyword Filter | 过滤器 |
| Get Content | Airtable |
| Split Out Content | 数据拆分 |
| Split Out Keywords | 数据拆分 |
| Limit | 数据限制 |
| Script Prep | OpenAI |
| Split Out Scenes | 数据拆分 |
| Split Out TN Prompt | 数据拆分 |
| Leo - Improve Prompt1 | HTTP Request |
| Leo - Get imageId1 | HTTP Request |
| Prompt Settings | 数据设置 |
| Leo - Generate Image1 | HTTP Request |
| Wait 30 Seconds | 等待 |
| Leo - Improve Prompt | HTTP Request |
| Leo - Get imageId | HTTP Request |
| Prompt Settings1 | 数据设置 |
| Leo - Generate Image | HTTP Request |
| Wait 30 Seconds1 | 等待 |
| Loop Over Items | 分批处理 |
| Add Asset Info | Airtable |
| Add Asset Info1 | Airtable |
| Wikipedia | Wikipedia 工具 |

## 触发方式
- When clicking ‘Test workflow’ 触发

## 统计
- 节点总数：27
- 触发节点：1
- 处理节点：20
- 输出节点：6
- 分类：workflow-automation
