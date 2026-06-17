## 简介
**Automate n8n Updates with Version Checking and Portainer Webhook**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/7061

---

# Automate n8n Updates with Version Checking and Portainer Webhook


## 节点清单

| 节点 | 类型 |
|------|------|
| Portainer Webhook | HTTP Request |
| Schedule Trigger | 定时触发器 |
| Get the latest n8n version | HTTP Request |
| If | IF 判断 |
| local n8n version | Code |
| Get local n8n metrics | HTTP Request |

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：6
- 触发节点：1
- 处理节点：2
- 输出节点：3
- 分类：workflow-automation
