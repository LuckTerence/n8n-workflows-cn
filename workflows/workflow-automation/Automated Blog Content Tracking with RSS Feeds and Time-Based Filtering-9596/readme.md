# Automated Blog Content Tracking with RSS Feeds and Time-Based Filtering

https://n8nworkflows.xyz/workflows/9596

## 节点清单

| 节点 | 类型 |
|------|------|
| Split RSS Feeds | 分批处理 |
| RSS → Items | RSS Feed |
| When clicking ‘Execute workflow’ | 手动触发 |
| Merge3 | 数据合并 |
| Client ID + Max Content Age + Blogs | 数据合并 |
| Find Date & Time of Blogs | 日期时间 |
| Filter Out Old Blogs | IF 判断 |
| max_content_age_days | 数据设置 |
| Split Out | 数据拆分 |
| blogs to track | 数据设置 |
| Rss feed link | 数据设置 |
| rss feed links + blogs | 数据合并 |

## 触发方式
- RSS → Items 触发
- When clicking ‘Execute workflow’ 触发

## 统计
- 节点总数：12
- 触发节点：2
- 处理节点：10
- 输出节点：0
- 分类：workflow-automation
