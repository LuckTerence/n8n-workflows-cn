## 简介
**Orchestrate Web Crawls with Scrapyd and Automated Data Enrichment**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/8552

---

# Orchestrate Web Crawls with Scrapyd and Automated Data Enrichment


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Execute workflow’ | 手动触发 |
| job_list | HTTP Request |
| filter_job | Code |
| check_job_status | IF 判断 |
| Wait3 | 等待 |
| check_items | HTTP Request |
| run_job | HTTP Request |
| screenshots | HTTP Request |
| job_log | HTTP Request |
| DL-html | HTTP Request |
| HTML | HTTP Request |
| loop-html | 分批处理 |
| DL-screenshots | HTTP Request |
| loop-screenshots | 分批处理 |
| combine-screenshots | 数据聚合 |
| combine-html | 数据聚合 |
| Split HTML | 数据拆分 |
| Split-screenshot | 数据拆分 |
| Respond to Webhook | 响应 Webhook |
| If-job-check | IF 判断 |
| Filter-result | Code |

## 触发方式
- When clicking ‘Execute workflow’ 触发

## 统计
- 节点总数：21
- 触发节点：1
- 处理节点：11
- 输出节点：9
- 分类：workflow-automation
