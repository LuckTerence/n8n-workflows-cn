## 简介
**Monitor website performance with Google PageSpeed, Sheets and multi-channel alerts**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/13009

---

# Monitor website performance with Google PageSpeed, Sheets and multi-channel alerts


## 节点清单

| 节点 | 类型 |
|------|------|
| Schedule Trigger | 定时触发器 |
| Get Data Form Sheet | Google Sheets |
| PageSpeed Test | HTTP Request |
| Save Results | Google Sheets |
| Process Results | Code |
| Update data | Google Sheets |
| Loop Over Items | 分批处理 |
| If3 | IF 判断 |
| PageSpeed Test2 | HTTP Request |
| Send a message | Discord |
| Rapiwa | rapiwa |
| Send a message2 | Email 发送 |
| Code (Calculate Days) | Code |
| Limit (10) | 数据限制 |
| If (check empty response) | IF 判断 |
| Wait 10s | 等待 |



## 功能说明

监控告警系统，异常检测并发送通知，定时执行。

定时触发，通过 邮箱 + HTTP API 实现自动化。

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

- 节点总数：16
- 触发方式：定时触发

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：16
- 触发节点：1
- 处理节点：11
- 输出节点：4
- 分类：workflow-automation
