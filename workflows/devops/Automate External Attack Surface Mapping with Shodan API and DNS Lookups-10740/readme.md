## 简介
**Automate External Attack Surface Mapping with Shodan API and DNS Lookups**

（待补充中文描述）

> 分类：DevOps | 适配等级：B（需替换Google Sheets)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/10740

---

# Automate External Attack Surface Mapping with Shodan API and DNS Lookups


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking 'Test workflow' | 手动触发 |
| Set Target Domain1 | 数据设置 |
| DNS Lookup (Google)1 | HTTP Request |
| Extract DNS Records1 | Code |
| Filter: Only IP records1 | IF 判断 |
| Prepare IP Item1 | 数据设置 |
| Delay (rate-limit) | 等待 |
| Shodan Search by IP | HTTP Request |
| Parse Shodan Data | Code |
| Log to Google Sheets1 | Google Sheets |
| Notify: Results (console log) | 数据设置 |
| Error Handler (catch) | 空操作 |

## 触发方式
- When clicking 'Test workflow' 触发

## 统计
- 节点总数：12
- 触发节点：1
- 处理节点：9
- 输出节点：2
- 分类：devops
