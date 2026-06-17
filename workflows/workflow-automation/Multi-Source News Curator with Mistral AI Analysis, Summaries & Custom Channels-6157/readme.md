## 简介
**Multi-Source News Curator with Mistral AI Analysis, Summaries & Custom Channels**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：83 | 难度：⭐⭐⭐ 高级
> 原始来源：https://n8nworkflows.xyz/workflows/6157

---

# Multi-Source News Curator with Mistral AI Analysis, Summaries & Custom Channels


## 节点清单

| 节点 | 类型 |
|------|------|
| Merge | 数据合并 |
| Aggregate | 数据聚合 |
| Filter by Datetime | 过滤器 |
| Limit Number of Articles | 数据限制 |
| Mistral Cloud Chat Model | Mistral Chat Model |
| News Analyzer | AI Agent |
| Split Out News Data | 数据拆分 |
| Remove Certain Content | 过滤器 |
| Schedule | 定时触发器 |
| Join Outputs | 数据合并 |
| Final Aggregate | 数据聚合 |
| Website Summarizer | AI Agent |
| Results to Text | Code |
| JSON Output Parser 2 | 结构化输出解析器 |
| JSON Output Parser | 结构化输出解析器 |
| Final Markdown Conversion | Markdown |
| Call Get Webpage Content to Data | 执行工作流 |
| Remove Elements with Empty Content | 过滤器 |
| Custom RSS Feed List | Code |
| Call Loop Over Custom RSS Feed News List | 执行工作流 |
| Loop Over Items | 分批处理 |
| Remove Elements with Empty Content  (Custom Feed) | 过滤器 |
| If | IF 判断 |
| Call Get Webpage Content to Data (Custom Feed) | 执行工作流 |
| Custom Feed | RSS Feed |
| Final Edit Fields | 数据设置 |
| Configure Workflow Args | globalConstants |
| Configure Workflow Args (Alternative) | 数据设置 |
| HTTP Request | HTTP Request |
| Markdown Conversion | Markdown |
| Rejoin Data | 数据设置 |
| Filter Fields for Custom Feed | 数据设置 |
| Combine General Summary with Specific Summaries | 数据合并 |
| Final Join Outputs | 数据合并 |
| If Not Empty | IF 判断 |
| Stop and Error | 停止并报错 |
| Switch | Switch 路由 |
| Telegram | Telegram |
| Loop Over Items (Search) | 分批处理 |
| Split Out | 数据拆分 |
| If1 | IF 判断 |
| Remove Duplicates | 去重 |
| Sending Step Prep | 数据设置 |
| Custom Feed Test | RSS Feed |
| Quality Assurance | AI Agent |
| If QA isn't Needed | IF 判断 |
| Aggregate for QA | 数据聚合 |
| Loop for QA | 分批处理 |
| JSON Output Parser (QA) | 结构化输出解析器 |
| Split Out QA Results | 数据拆分 |
| Prep QA Results | 数据设置 |
| Clean Content | 数据设置 |
| When clicking ‘Execute workflow’ | 手动触发 |
| Configure Workflow Args (Custom Credentials) | globalConstants |
| Custom Credentials | Code |
| Email Trigger (IMAP) | Email 读取 |
| Webhook: Call Workflow Activation | Webhook |
| Respond to Webhook: JSON with Result | 响应 Webhook |
| Write contents to disk | 读写文件 |
| Create a binary data for the Latest News | Function |
| Setting Email Body | 数据设置 |
| Send email | Email 发送 |
| Content Translator | AI Agent |
| Determine Language & Tone | Code |
| If Tone isn't Empty | IF 判断 |
| If Not English | IF 判断 |
| If Video Search is Enabled | IF 判断 |
| No Operation, do nothing | 空操作 |
| WhatsApp message | WhatsApp |
| Shuffle News | 数据排序 |
| Confirmation | 数据设置 |
| Remove Empty | 过滤器 |
| Remove Video Info with Empty Content | 过滤器 |
| Custom Video Feed List | Code |
| Video Filter by Datetime | 过滤器 |
| XML | XML |
| Edit Video Fields | 数据设置 |
| HTTP Request to XML Feed | HTTP Request |
| Split Out Videos | 数据拆分 |
| Process Video Feed Searches | 数据设置 |
| Google_news search | serpApi |
| Remove Elements with Empty Links | 过滤器 |
| Filter Fields for Loop | 数据设置 |
| Split Out News Results | 数据拆分 |
| Call Search Queries with SerpAPI | 执行工作流 |
| Call Video News - Get the Descriptions of Video Found through Feeds and Theme Search | 执行工作流 |

## 触发方式
- Schedule 触发
- Custom Feed 触发
- Custom Feed Test 触发
- When clicking ‘Execute workflow’ 触发
- Webhook: Call Workflow Activation 触发

## 统计
- 节点总数：86
- 触发节点：5
- 处理节点：74
- 输出节点：7
- 分类：workflow-automation
