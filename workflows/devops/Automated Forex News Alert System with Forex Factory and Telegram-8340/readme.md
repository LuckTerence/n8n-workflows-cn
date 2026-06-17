## 简介
**Automated Forex News Alert System with Forex Factory and Telegram**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：16 | 难度：⭐⭐⭐ 高级
> 原始来源：https://n8nworkflows.xyz/workflows/8340

---

# Automated Forex News Alert System with Forex Factory and Telegram


## 节点清单

| 节点 | 类型 |
|------|------|
| Google Calendar Trigger | googleCalendarTrigger |
| If | IF 判断 |
| To Number | 数据设置 |
| Get Actual Data? | IF 判断 |
| Actual, Forecast Value | 数据设置 |
| Delete %KMBT, To Number | 数据设置 |
| 'Actual' less than 'Forecast' is good for currency? | IF 判断 |
| IF Has Forecast | IF 判断 |
| No Operation, do nothing1 | 空操作 |
| Get News Details | 数据设置 |
| Scrape News Link | Airtop |
| Wait 10s | 等待 |
| Wait 5s | 等待 |
| Less Good | Telegram |
| Greater Good | Telegram |
| No Operation, do nothing | 空操作 |

## 触发方式
- Google Calendar Trigger 触发

## 统计
- 节点总数：16
- 触发节点：1
- 处理节点：13
- 输出节点：2
- 分类：devops
