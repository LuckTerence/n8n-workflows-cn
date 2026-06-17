## 简介
**Daily Insight Email from Structured Web Data with Firecrawl**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/4654

---

# Daily Insight Email from Structured Web Data with Firecrawl


## 节点清单

| 节点 | 类型 |
|------|------|
| Schedule Trigger | 定时触发器 |
| POST Request | HTTP Request |
| Wait 60 Seconds | 等待 |
| Gmail | Email 发送 |
| Edit Fields | 数据设置 |
| If | IF 判断 |
| Wait 30 seconds | 等待 |
| HTTP GET Request | HTTP Request |
| Formatting AI | OpenAI |

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：9
- 触发节点：1
- 处理节点：5
- 输出节点：3
- 分类：workflow-automation
