## 简介
**Automated RSS to Telegram Publisher with Groq AI Rewriting**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：10 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/11566

---

# Automated RSS to Telegram Publisher with Groq AI Rewriting


## 节点清单

| 节点 | 类型 |
|------|------|
| Groq Chat Model | Groq Chat Model |
| Every 30 minutes | 定时触发器 |
| Read RSS links | RSS Feed |
| Add link | 数据表 |
| Rewrite Post | AI Agent |
| Send post to user | Telegram |
| If link not in table | 数据表 |
| For each RSS | 分批处理 |
| Finish workflow | 空操作 |
| Get RSS list | 数据表 |
| Get only latest link | 数据限制 |

## 触发方式
- Every 30 minutes 触发
- Read RSS links 触发

## 统计
- 节点总数：11
- 触发节点：2
- 处理节点：8
- 输出节点：1
- 分类：workflow-automation
