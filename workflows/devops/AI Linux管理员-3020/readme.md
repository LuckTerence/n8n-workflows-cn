## 简介
**AI Linux管理员**

用AI管理Linux VPS实例

> 分类：DevOps | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3020

---

# AI Linux 管理员


通过 Webhook 接收管理指令，AI Agent 连接 SSH 在目标服务器上执行运维操作。

## 节点

| 节点 | 类型 |
|------|------|
| Webhook Trigger | Webhook 触发器 |
| AI Agent | AI Agent |
| SSH | SSH 连接 |
| Code | 数据处理 |
| Webhook Response | 响应输出 |

## 触发方式

HTTP Webhook 触发

## 统计

