## 简介
**Aggregate News Articles from NewsAPI, Mediastack & CurrentsAPI into Database**

（待补充中文描述）

> 分类：DevOps | 适配等级：B（需替换Google Sheets)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/11572

---

# Aggregate News Articles from NewsAPI, Mediastack & CurrentsAPI into Database


## 节点清单

| 节点 | 类型 |
|------|------|
| Split Out 1 | 数据拆分 |
| Split Out 2 | 数据拆分 |
| Split Out 3 | 数据拆分 |
| Set Mediastack | 数据设置 |
| Add Mediastack item | NocoDB |
| Add NewsAPI item | NocoDB |
| call mediastack | HTTP Request |
| call currentsapi | HTTP Request |
| currentsapi config | 数据设置 |
| MediaStack | 定时触发器 |
| CurrentsAPI | 定时触发器 |
| call newsapi.org - Top Headlines | HTTP Request |
| Set CurrentsAPI | 数据设置 |
| NewsAPI - Top Headlines | 定时触发器 |
| Split Out  | 数据拆分 |
| Add NewsAPI item1 | NocoDB |
| mediastack categories | 数据设置 |
| newsapi.org categories | 数据设置 |
| Itemize Newsapi Categories | Code |
| Itemize Mediastack Categories | Code |
| call newsapi.org - categories | HTTP Request |
| NewsAPI - Categories | 定时触发器 |
| Wait | 等待 |
| Wait1 | 等待 |
| Loop Over NewsAPI | 分批处理 |
| Loop Over Mediastack | 分批处理 |
| Set Newsapi.org top headlines | 数据设置 |
| Set Newsapi.org categories | 数据设置 |
| Add CurrentsAPI item | NocoDB |

## 触发方式
- MediaStack 触发
- CurrentsAPI 触发
- NewsAPI - Top Headlines 触发
- NewsAPI - Categories 触发

## 统计
- 节点总数：29
- 触发节点：4
- 处理节点：21
- 输出节点：4
- 分类：devops
