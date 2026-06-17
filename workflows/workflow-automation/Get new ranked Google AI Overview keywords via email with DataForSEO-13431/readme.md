## 简介
**Get new ranked Google AI Overview keywords via email with DataForSEO**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/13431

---

# Get new ranked Google AI Overview keywords via email with DataForSEO


## 节点清单

| 节点 | 类型 |
|------|------|
| Aggregate | 数据聚合 |
| Get ranked keywords | dataForSeoLabsApi |
| Get previous keywords | Google Sheets |
| Get targets | Google Sheets |
| Append keyword in sheet | Google Sheets |
| Run every Monday | 定时触发器 |
| Aggregate1 | 数据聚合 |
| Clear sheet | Google Sheets |
| Send a message | Email 发送 |
| Initialize "items" field | 数据设置 |
| Set "items" field | 数据设置 |
| Merge "items" with DFS response | 数据设置 |
| Has more pages? | IF 判断 |
| Merge "items" with last response | 数据设置 |
| Filter (has new AIO keywords) | 过滤器 |
| Find new AIO keywords | Code |
| Split out (items) | 数据拆分 |
| Loop over targets | 分批处理 |

## 触发方式
- Run every Monday 触发

## 统计
- 节点总数：18
- 触发节点：1
- 处理节点：16
- 输出节点：1
- 分类：workflow-automation
