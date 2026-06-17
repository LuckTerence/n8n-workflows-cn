# Scrape recent news about a company before a call

https://n8nworkflows.xyz/workflows/2110

## 节点清单

| 节点 | 类型 |
|------|------|
| Setup | 数据设置 |
| Extract company name | 数据设置 |
| Every morning @ 7 | 定时触发器 |
| Filter meetings | IF 判断 |
| Get latest news | HTTP Request |
| Format for email | Code |
| Send news | Email 发送 |
| No meetings today | 空操作 |
| Get meetings for today | Google Calendar |

## 触发方式
- Every morning @ 7 触发

## 统计
- 节点总数：9
- 触发节点：1
- 处理节点：6
- 输出节点：2
- 分类：workflow-automation
