## 简介
**Bitrix24 Chatbot Application Workflow example with Webhook Integration**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2923

---

# Bitrix24 Chatbot Application Workflow example with Webhook Integration


## 节点清单

| 节点 | 类型 |
|------|------|
| Bitrix24 Handler | Webhook |
| Credentials | 数据设置 |
| Validate Token | IF 判断 |
| Route Event | Switch 路由 |
| Process Message | Function |
| Process Join | Function |
| Process Install | Function |
| Register Bot | HTTP Request |
| Send Message | HTTP Request |
| Send Join Message | HTTP Request |
| Process Delete | 空操作 |
| Success Response | 响应 Webhook |
| Error Response | 响应 Webhook |

## 触发方式
- Bitrix24 Handler 触发

## 统计
- 节点总数：13
- 触发节点：1
- 处理节点：7
- 输出节点：5
- 分类：workflow-automation
