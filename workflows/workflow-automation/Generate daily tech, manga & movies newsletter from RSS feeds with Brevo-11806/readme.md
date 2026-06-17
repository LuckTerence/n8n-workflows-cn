## 简介
**Generate daily tech, manga & movies newsletter from RSS feeds with Brevo**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Gmail)（基本改完，配置 API Key 应该就能跑）
> 节点数：21 | 难度：⭐⭐⭐ 高级
> 原始来源：https://n8nworkflows.xyz/workflows/11806

---

# Generate daily tech, manga & movies newsletter from RSS feeds with Brevo


## 节点清单

| 节点 | 类型 |
|------|------|
| Split Out2 | 数据拆分 |
| Schedule Trigger | 定时触发器 |
| RSS Read1 | RSS Feed |
| Loop Over Items3 | 分批处理 |
| Rss database | Google Sheets |
| Switch | Switch 路由 |
| Code in Python (Beta) | Code |
| RSS Read2 | RSS Feed |
| Loop Over Items4 | 分批处理 |
| Code in Python (Beta)1 | Code |
| RSS Read3 | RSS Feed |
| Loop Over Items5 | 分批处理 |
| Code in Python (Beta)2 | Code |
| Aggregate | 数据聚合 |
| Merge | 数据合并 |
| Send a Mail | Email 发送 |
| Mail Campaign | sendInBlue |
| HTML Template | HTML |
| Category Rss | 数据设置 |
| Jeu video | Code |
| Movie | Code |
| Manga | Code |

## 触发方式
- Schedule Trigger 触发
- RSS Read1 触发
- RSS Read2 触发
- RSS Read3 触发

## 统计
- 节点总数：22
- 触发节点：4
- 处理节点：17
- 输出节点：1
- 分类：workflow-automation
