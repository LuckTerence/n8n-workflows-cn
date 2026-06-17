## 简介
**Currency Conversion Workflow**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2691

---

# Currency Conversion Workflow


## 节点清单

| 节点 | 类型 |
|------|------|
| Fetch Exchange Rate | HTTP Request |
| Extract Conversion Data | HTML |
| Format Currency Response | 数据设置 |
| Capture Conversion Query | Webhook |
| Send Conversion Response | 响应 Webhook |

## 触发方式
- Capture Conversion Query 触发

## 统计
- 节点总数：5
- 触发节点：1
- 处理节点：2
- 输出节点：2
- 分类：workflow-automation
