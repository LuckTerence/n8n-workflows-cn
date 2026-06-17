# Manage SMC Screener analyses with n8n forms and HTTP API

https://n8nworkflows.xyz/workflows/16153

## 节点清单

| 节点 | 类型 |
|------|------|
| SMC_Analysis_Form | 表单触发器 |
| Manual Trigger | 手动触发 |
| Manual Test Payload | Code |
| Normalize Analysis Input | Code |
| Input Valid? | Switch 路由 |
| Build Input Error | Code |
| Example API Key? | Switch 路由 |
| Example Output | Code |
| Action Router | Switch 路由 |
| GET User Analyses | HTTP Request |
| Build Analyses List Summary | Code |
| GET Analysis Detail | HTTP Request |
| Build Analysis Detail Summary | Code |
| POST Create Analysis | HTTP Request |
| Build Create Summary | Code |
| PATCH Update Analysis | HTTP Request |
| Build Update Summary | Code |
| POST Reanalyze Analysis | HTTP Request |
| Build Reanalysis Queue Summary | Code |
| POST Clear Analysis | HTTP Request |
| Build Clear Summary | Code |
| DELETE Analysis | HTTP Request |
| Build Delete Summary | Code |
| GET Runtime Status | HTTP Request |
| Build Runtime Status Summary | Code |

## 触发方式
- SMC_Analysis_Form 触发
- Manual Trigger 触发

## 统计
- 节点总数：25
- 触发节点：2
- 处理节点：15
- 输出节点：8
- 分类：workflow-automation
