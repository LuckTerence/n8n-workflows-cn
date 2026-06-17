## 简介
**Get enriched location, weather, and timezone data using free APIs**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：7 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/13411

---

# Get enriched location, weather, and timezone data using free APIs


## 节点清单

| 节点 | 类型 |
|------|------|
| Merge | 数据合并 |
| OpenWeatherMap | openWeatherMap |
| HTTP Request (Nominatim) | HTTP Request |
| Webhook - Accepts Coordinates | Webhook |
| HTTP Request (TimezoneDB) | HTTP Request |
| HTTP Request (Sunrise-Sunset) | HTTP Request |
| Edit Fields - Format & Structure Output | 数据设置 |
| Respond to Webhook - Return JSON Response | 响应 Webhook |

## 触发方式
- Webhook - Accepts Coordinates 触发

## 统计
- 节点总数：8
- 触发节点：1
- 处理节点：3
- 输出节点：4
- 分类：workflow-automation
