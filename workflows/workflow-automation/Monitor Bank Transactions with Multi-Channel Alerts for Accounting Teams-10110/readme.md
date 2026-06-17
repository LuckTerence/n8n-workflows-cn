## 简介
**Monitor Bank Transactions with Multi-Channel Alerts for Accounting Teams**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Slack)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/10110

---

# Monitor Bank Transactions with Multi-Channel Alerts for Accounting Teams


## 节点清单

| 节点 | 类型 |
|------|------|
| Schedule Trigger | 定时触发器 |
| Fetch Transactions | HTTP Request |
| API Error? | IF 判断 |
| Handle API Error | Code |
| Send Error Alert | Email 发送 |
| Enrich & Transform Data | Code |
| Critical Alert? | IF 判断 |
| High Priority? | IF 判断 |
| Medium Priority? | IF 判断 |
| Log Critical to Sheet | Google Sheets |
| Log High Priority to Sheet | Google Sheets |
| Log Medium Priority to Sheet | Google Sheets |
| Send Critical Email | Email 发送 |
| Send High Priority Email | Email 发送 |
| Send Critical Slack Alert | Slack |
| Send High Priority Slack | Slack |
| Merge All Alerts | 数据合并 |
| Generate Summary Stats | Code |
| Log Summary to Sheet | Google Sheets |



## 功能说明

监控告警系统，异常检测并发送通知，定时执行。

定时触发，通过 邮箱 + Slack + HTTP API 实现自动化。

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

- 节点总数：19
- 触发方式：定时触发

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：19
- 触发节点：1
- 处理节点：12
- 输出节点：6
- 分类：workflow-automation
