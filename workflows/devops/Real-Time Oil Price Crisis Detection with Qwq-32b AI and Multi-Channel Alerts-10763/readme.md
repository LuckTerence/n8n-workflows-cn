## 简介
**Real-Time Oil Price Crisis Detection with Qwq-32b AI and Multi-Channel Alerts**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（需替换Slack/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/10763

---

# Real-Time Oil Price Crisis Detection with Qwq-32b AI and Multi-Channel Alerts


## 节点清单

| 节点 | 类型 |
|------|------|
| Schedule Every 5 Minutes | 定时触发器 |
| Workflow Configuration | 数据设置 |
| Fetch Oil Price Data (API) | HTTP Request |
| Fetch OPEC Reports | HTTP Request |
| Fetch Shipping Data | HTTP Request |
| Fetch News Feed | HTTP Request |
| Merge All Data Sources | 数据合并 |
| Data Cleaning & Preprocessing | Code |
| Statistical Anomaly Detection | Code |
| AI Trend & Geopolitical Analyzer | AI Agent |
| Calculate Crisis Risk Score | Code |
| Route by Alert Level | Switch 路由 |
| Format Info Alert | 数据设置 |
| Format Warning Alert | 数据设置 |
| Format Critical Alert | 数据设置 |
| Send Email Alert | Email 发送 |
| Send Slack Alert | Slack |
| Store Alert History | PostgreSQL |
| Send to Dashboard API | HTTP Request |
| OpenRouter Chat Model | OpenRouter Chat Model |



## 功能说明

监控告警系统，异常检测并发送通知，定时执行。

定时触发，通过 邮箱 + 数据库 + Slack + HTTP API 实现自动化。

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

- 节点总数：20
- 触发方式：定时触发

## 触发方式
- Schedule Every 5 Minutes 触发

## 统计
- 节点总数：20
- 触发节点：1
- 处理节点：12
- 输出节点：7
- 分类：devops
