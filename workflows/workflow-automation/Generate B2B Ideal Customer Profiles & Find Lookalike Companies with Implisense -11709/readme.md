# Generate B2B Ideal Customer Profiles & Find Lookalike Companies with Implisense API

https://n8nworkflows.xyz/workflows/11709

## 节点清单

| 节点 | 类型 |
|------|------|
| Manual Trigger | 手动触发 |
| set_f2 | 数据设置 |
| Filter term.en | Function |
| Filter term.de | Function |
| parse_term_features | Function |
| merge_terms | 数据合并 |
| Configuration | 数据设置 |
| Authorization | 数据设置 |
| serialize_ids | Function |
| trim | 数据设置 |
| get_lookalikes | HTTP Request |
| lookalikes_or_icp | Switch 路由 |
| get_companies | 数据拆分 |
| sort_desc | Function |
| digest_terms_en | Function |
| digest_terms_de | Function |
| sort_desc2 | Function |
| generate_icp_report | OpenAI |
| icp_report | 数据设置 |
| list_of_companies | 数据设置 |
| Mock ICP Companies based on Implisense-ID | Code |

## 触发方式
- Manual Trigger 触发

## 统计
- 节点总数：21
- 触发节点：1
- 处理节点：19
- 输出节点：1
- 分类：workflow-automation
