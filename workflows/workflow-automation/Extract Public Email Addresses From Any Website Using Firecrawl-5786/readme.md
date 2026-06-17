# Extract Public Email Addresses From Any Website Using Firecrawl

https://n8nworkflows.xyz/workflows/5786

## 节点清单

| 节点 | 类型 |
|------|------|
| form_trigger | 表单触发器 |
| map_website | HTTP Request |
| start_batch_scrape | HTTP Request |
| check_retry_count | IF 判断 |
| too_many_attempts_error | 停止并报错 |
| rate_limit_wait | 等待 |
| set_result | 数据设置 |
| check_scrape_completed | IF 判断 |
| fetch_scrape_results | HTTP Request |

## 触发方式
- form_trigger 触发

## 统计
- 节点总数：9
- 触发节点：1
- 处理节点：5
- 输出节点：3
- 分类：workflow-automation
