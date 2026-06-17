## 简介
**Score and route pre-trip vehicle inspections with local AI and alerts**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/15448

---

# Score and route pre-trip vehicle inspections with local AI and alerts


## 节点清单

| 节点 | 类型 |
|------|------|
| HTTP Request | HTTP Request |
| Parse Input | Code |
| Score Calculator | Code |
| Flag Rules | Code |
| Ollama AI | HTTP Request |
| Parse AI Response | Code |
| Final Score | Code |
| Route by Status | Switch 路由 |
| Respond OK | 响应 Webhook |
| Respond Flagged | 响应 Webhook |
| Webhook3 | Webhook |
| Send an Email2 | Email 发送 |



## 功能说明

监控告警系统，异常检测并发送通知，Webhook 触发。

Webhook触发，通过 邮箱 + HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- 邮箱 SMTP/IMAP 账号密码

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：12
- 触发方式：Webhook 触发

## 触发方式
- Webhook3 触发

## 统计
- 节点总数：12
- 触发节点：1
- 处理节点：6
- 输出节点：5
- 分类：devops
