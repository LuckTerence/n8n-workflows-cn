# Automated Sonarr Missing Episode Finder with Quality & Language Filtering

https://n8nworkflows.xyz/workflows/5927

## 节点清单

| 节点 | 类型 |
|------|------|
| info | 数据设置 |
| Edit Fields | 数据设置 |
| Split Out | 数据拆分 |
| Schedule Trigger | 定时触发器 |
| Override and add to download queue | HTTP Request |
| Interactive search for all episodes in this season | HTTP Request |
| Check for Missing Episodes | HTTP Request |
| Validate Quality and Language Match | IF 判断 |
| Filter Series | Code |
| Loop Over Items | 分批处理 |

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：10
- 触发节点：1
- 处理节点：6
- 输出节点：3
- 分类：workflow-automation
