## 简介
**Automate GoDaddy Subdomain Management via Email Requests**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：B（需替换Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/5401

---

# Automate GoDaddy Subdomain Management via Email Requests


## 节点清单

| 节点 | 类型 |
|------|------|
| Create Subdomain | HTTP Request |
| Delete Subdomain | HTTP Request |
| Start Workflow (GET Request) | Email 读取 |
| Extract Data from Email | Code |
| Validate Action Type | IF 判断 |
| Send Email Response | Email 发送 |

## 触发方式
- 手动触发

## 统计
- 节点总数：6
- 触发节点：0
- 处理节点：2
- 输出节点：4
- 分类：workflow-automation
