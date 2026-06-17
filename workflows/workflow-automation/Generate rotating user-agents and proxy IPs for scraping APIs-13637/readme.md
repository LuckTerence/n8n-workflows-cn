## 简介
**Generate rotating user-agents and proxy IPs for scraping APIs**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/13637

---

# Generate rotating user-agents and proxy IPs for scraping APIs


## 节点清单

| 节点 | 类型 |
|------|------|
| user-agents | HTTP Request |
| clean the return to line in user-agent | 数据设置 |
| random sort | 数据排序 |
| Extract user-agent values | HTML |
| Split Out | 数据拆分 |
| Check used IP/user-agent with cloudflare | HTTP Request |
| Manual trigger | 手动触发 |
| SET your proxy connection details here | 数据设置 |
| Merge | 数据合并 |
| Take X random user-agents | 数据限制 |
| Targeted API | HTTP Request |
| IP address and user-agent used | 数据设置 |

## 触发方式
- Manual trigger 触发

## 统计
- 节点总数：12
- 触发节点：1
- 处理节点：8
- 输出节点：3
- 分类：workflow-automation
