## 简介
**Cold Outreach Automation: Scrape Local Leads with Dumpling AI & Call via Vapi**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/4031

---

# Cold Outreach Automation: Scrape Local Leads with Dumpling AI & Call via Vapi


## 节点清单

| 节点 | 类型 |
|------|------|
| Start Workflow Manually | 手动触发 |
| Get Search Keywords from Google Sheets | Google Sheets |
| Scrape Google Map Businesses using Dumpling AI | HTTP Request |
| Split Each Business Result | 数据拆分 |
| Extract Business Name, Phone and website | 数据设置 |
| Filter Valid Phone Numbers Only | 过滤器 |
| Format Phone Number for Calling | 数据设置 |
| Initiate Vapi AI Call to Business | HTTP Request |
| Log Called Business Info to Sheet | Google Sheets |

## 触发方式
- Start Workflow Manually 触发

## 统计
- 节点总数：9
- 触发节点：1
- 处理节点：6
- 输出节点：2
- 分类：workflow-automation
