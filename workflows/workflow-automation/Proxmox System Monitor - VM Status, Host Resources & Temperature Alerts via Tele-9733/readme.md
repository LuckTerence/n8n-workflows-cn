## 简介
**Proxmox System Monitor - VM Status, Host Resources & Temperature Alerts via Telegram**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/9733

---

# Proxmox System Monitor - VM Status, Host Resources & Temperature Alerts via Telegram


## 节点清单

| 节点 | 类型 |
|------|------|
| Schedule Every 15min | 定时触发器 |
| Set Variables | 数据设置 |
| Proxmox Login | HTTP Request |
| Prepare Auth | 数据设置 |
| API - VM List | HTTP Request |
| API - Node Tasks | HTTP Request |
| API - Node Status | HTTP Request |
| SSH - Get Sensors | SSH |
| Process Data | Code |
| Generate Formatted Message | Code |
| Send Telegram Report | Telegram |

## 触发方式
- Schedule Every 15min 触发

## 统计
- 节点总数：11
- 触发节点：1
- 处理节点：5
- 输出节点：5
- 分类：workflow-automation
