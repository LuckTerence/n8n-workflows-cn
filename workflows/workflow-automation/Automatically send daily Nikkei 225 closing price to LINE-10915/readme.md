## 简介
**Automatically send daily Nikkei 225 closing price to LINE**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：4 | 难度：⭐ 入门
> 原始来源：https://n8nworkflows.xyz/workflows/10915

---

# Automatically send daily Nikkei 225 closing price to LINE


## 节点清单

| 节点 | 类型 |
|------|------|
| Every Weekday at 4 PM JST | 定时触发器 |
| Get Nikkei 225 Data | HTTP Request |
| Format Message | 数据设置 |
| Prepare LINE API Payload | Code |
| Send to LINE via HTTP | HTTP Request |

## 触发方式
- Every Weekday at 4 PM JST 触发

## 统计
- 节点总数：5
- 触发节点：1
- 处理节点：2
- 输出节点：2
- 分类：workflow-automation
