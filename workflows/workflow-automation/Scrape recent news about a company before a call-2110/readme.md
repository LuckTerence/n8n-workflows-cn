## 简介
**Scrape recent news about a company before a call**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2110

---

# Scrape recent news about a company before a call


## 节点清单

| 节点 | 类型 |
|------|------|
| Setup | 数据设置 |
| Extract company name | 数据设置 |
| Every morning @ 7 | 定时触发器 |
| Filter meetings | IF 判断 |
| Get latest news | HTTP Request |
| Format for email | Code |
| Send news | Email 发送 |
| No meetings today | 空操作 |
| Get meetings for today | Google Calendar |

## 触发方式
- Every morning @ 7 触发

## 统计
- 节点总数：9
- 触发节点：1
- 处理节点：6
- 输出节点：2
- 分类：workflow-automation
