## 简介
**AI Chatbot Call Center: Demo Call Back (Production-Ready, Part 6)**

（待补充中文描述）

> 分类：AI Agent | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/4050

---

# AI Chatbot Call Center: Demo Call Back (Production-Ready, Part 6)


## 节点清单

| 节点 | 类型 |
|------|------|
| Media Switch | Switch 路由 |
| Flow Trigger | 执行工作流触发器 |
| Input | 数据设置 |
| Test Trigger | Chat 触发器 |
| Test Fields | 数据设置 |
| Download Minimax Audio | HTTP Request |
| Telegram Voice Output | Telegram |
| If Provider No | IF 判断 |
| Provider Cache | Redis |
| Save Provider Cache | Redis |
| If Provider Cache | IF 判断 |
| Provider | 数据设置 |
| Load Provider Data | PostgreSQL |
| If Provider Voice | IF 判断 |
| Switch | Switch 路由 |
| Create Chat Log Output | PostgreSQL |
| Create Chat Log Input | PostgreSQL |
| If Input | IF 判断 |
| Output | 数据设置 |
| Media Switch1 | Switch 路由 |
| Chinese,Yue | 数据设置 |
| Minimax TTS | HTTP Request |
| Chinese | 数据设置 |
| Japanese | 数据设置 |
| English | 数据设置 |
| If Reply | IF 判断 |
| Telegram Reply Output | Telegram |
| Telegram Output | Telegram |
| Parse Cache | Code |

## 触发方式
- Flow Trigger 触发
- Test Trigger 触发

## 统计
- 节点总数：29
- 触发节点：2
- 处理节点：22
- 输出节点：5
- 分类：ai-agent
