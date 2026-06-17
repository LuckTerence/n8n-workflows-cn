## 简介
**Create a Dynamic Telegram Bot Menu System with Multi-Level Navigation**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/8844

---

# Create a Dynamic Telegram Bot Menu System with Multi-Level Navigation


## 节点清单

| 节点 | 类型 |
|------|------|
| Telegram Trigger4 | Telegram 触发器 |
| Load Menu Config2 | Function |
| Extract Command4 | Function |
| Merge Config & Command2 | 数据合并 |
| Process Command2 | Function |
| Needs Action?2 | IF 判断 |
| Action Router2 | Switch 路由 |
| Rating Handler2 | Function |
| Language Handler2 | Function |
| Analytics Handler2 | Function |
| Statistics Handler3 | Function |
| Feedback Handler3 | Function |
| Settings Handler3 | Function |
| Default Handler2 | Function |
| Build Response2 | Function |
| Prepare Telegram2 | Function |
| Set Bot Token4 | 数据设置 |
| Is Callback?4 | IF 判断 |
| Send to Telegram4 | HTTP Request |
| Answer Callback4 | HTTP Request |

## 触发方式
- Telegram Trigger4 触发

## 统计
- 节点总数：20
- 触发节点：1
- 处理节点：17
- 输出节点：2
- 分类：workflow-automation
