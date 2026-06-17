## 简介
**Run automated SEO audits with Screaming Frog CLI, PageSpeed, PDF and Excel fixes**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：B（需替换Google Sheets/Slack/Google Drive)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/15252

---

# Run automated SEO audits with Screaming Frog CLI, PageSpeed, PDF and Excel fixes


## 节点清单

| 节点 | 类型 |
|------|------|
| Wait | 等待 |
| Wait1 | 等待 |
| Compression | compression |
| PSI Parser | Code |
| Page Speed Insights | HTTP Request |
| Input Cleaner | 数据设置 |
| Switch | Switch 路由 |
| Start Crawl | HTTP Request |
| Check Crawl | HTTP Request |
| Fetch | HTTP Request |
| SEO Audit Parser | Code |
| Full Data Parser | Code |
| Tab Builder | Code |
| Upload file | Google Drive |
| Data | 数据设置 |
| Excel File Builder | Code |
| HTML TO PDF | HTTP Request |
| Upload to Drive | Google Drive |
| Downlaod PDF | HTTP Request |
| Slack Trigger | slackTrigger |
| If | IF 判断 |
| Append row in sheet | Google Sheets |
| Aggregate | 数据聚合 |
| Merge | 数据合并 |
| Arrange Data | 数据设置 |
| Send Failed Message | Slack |
| Send Report | Slack |
| Extract URL | Code |
| Report Builder | Code |

## 触发方式
- Slack Trigger 触发

## 统计
- 节点总数：29
- 触发节点：1
- 处理节点：20
- 输出节点：8
- 分类：workflow-automation
