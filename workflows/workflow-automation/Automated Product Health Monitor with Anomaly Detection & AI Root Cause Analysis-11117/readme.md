## 简介
**Automated Product Health Monitor with Anomaly Detection & AI Root Cause Analysis**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Notion/Slack/Supabase/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/11117

---

# Automated Product Health Monitor with Anomaly Detection & AI Root Cause Analysis


## 节点清单

| 节点 | 类型 |
|------|------|
| log incident | PostgreSQL |
| daily usage metrics | PostgreSQL |
| anomalies | Code |
| insert incidents | PostgreSQL |
| select open incident | PostgreSQL |
| revenue by country | PostgreSQL |
| revenue by plan | PostgreSQL |
| sum up/ hypothesis | OpenAI |
| root cause summary | Slack |
| update incident status | PostgreSQL |
| daily report trigger | 定时触发器 |
| sum up | Code |
| email alert | Email 发送 |
| daily report email | Email 发送 |
| root cause summary email | Email 发送 |
| log system | PostgreSQL |
| Execute the SQL query | PostgreSQL |
| Trigger RH | 定时触发器 |
| Update notions | Notion |
| slack notification | Slack |
| Condition incident | IF 判断 |
| Merge data | 数据合并 |
| log system final | PostgreSQL |
| anomalies check | Code |
| Slack notification | Slack |
| usage health email | Email 发送 |
| Trigger CS | 定时触发器 |
| Trigger UH | 定时触发器 |
| log system UH | PostgreSQL |
| Execute SQL query incident check | PostgreSQL |
| Notions database creation | Notion |
| log system final1 | PostgreSQL |



## 功能说明

监控告警系统，异常检测并发送通知，定时执行。

定时触发，通过 邮箱 + 在线表格 + 数据库 + Slack + HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com
- 邮箱 SMTP/IMAP 账号密码
- 数据库连接信息

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：32
- 触发方式：定时触发

## 触发方式
- daily report trigger 触发
- Trigger RH 触发
- Trigger CS 触发
- Trigger UH 触发

## 统计
- 节点总数：32
- 触发节点：4
- 处理节点：21
- 输出节点：7
- 分类：workflow-automation
