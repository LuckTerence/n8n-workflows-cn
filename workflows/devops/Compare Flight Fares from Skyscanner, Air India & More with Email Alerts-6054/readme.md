## 简介
**Compare Flight Fares from Skyscanner, Air India & More with Email Alerts**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（需替换Gmail)（基本改完，配置 API Key 应该就能跑）
> 节点数：10 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/6054

---

# Compare Flight Fares from Skyscanner, Air India & More with Email Alerts


## 节点清单

| 节点 | 类型 |
|------|------|
| Skyscanner API | HTTP Request |
| Air India API | HTTP Request |
| IndiGo API | HTTP Request |
| Akasa Air API | HTTP Request |
| Set Schedule | 定时触发器 |
| Set Input Data | 数据设置 |
| Merge API Data | 数据合并 |
| Merge Both API Data | 数据合并 |
| Merge All API Results | 数据合并 |
| Compare Data and Sorting Price | Function |
| Send Response via Email | Email 发送 |

## 触发方式
- Set Schedule 触发

## 统计
- 节点总数：11
- 触发节点：1
- 处理节点：5
- 输出节点：5
- 分类：devops
