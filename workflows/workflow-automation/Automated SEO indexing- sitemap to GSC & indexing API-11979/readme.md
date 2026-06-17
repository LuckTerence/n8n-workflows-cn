# Automated SEO indexing: sitemap to GSC & indexing API

https://n8nworkflows.xyz/workflows/11979

## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Execute workflow’ | 手动触发 |
| Configuration | 数据设置 |
| Fetch Sitemap XML | HTTP Request |
| Convert XML to JSON | XML |
| Parse Sitemap Structure | Code |
| Is Sitemap Index? | IF 判断 |
| Format URL Data | 数据设置 |
| Filter: Recent URLs Only | 过滤器 |
| Check Submission History | Code |
| GSC: Inspect URL Status | HTTP Request |
| Logic: Should Index? | Code |
| Filter: Only Not Indexed | 过滤器 |
| Batch Processing | 分批处理 |
| Delay (Rate Limiting) | 等待 |
| Schedule Trigger | 定时触发器 |
| Filter: Valid for Submission | 过滤器 |
| GSC: Request Indexing | HTTP Request |

## 触发方式
- When clicking ‘Execute workflow’ 触发
- Schedule Trigger 触发

## 统计
- 节点总数：17
- 触发节点：2
- 处理节点：12
- 输出节点：3
- 分类：workflow-automation
