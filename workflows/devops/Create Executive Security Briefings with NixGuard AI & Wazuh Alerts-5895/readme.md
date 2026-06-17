## 简介
**Create Executive Security Briefings with NixGuard AI & Wazuh Alerts**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/5895

---

# Create Executive Security Briefings with NixGuard AI & Wazuh Alerts


## 节点清单

| 节点 | 类型 |
|------|------|
| Run Daily at 8 AM | 定时触发器 |
| Parse Alert Array | Code |
| Set Prompt for Summary | 数据设置 |
| Set API Key & Initial Prompt | 数据设置 |
| Set Final Briefing | 数据设置 |
| Execute: Get Daily Events as JSON (Get Real-Time Security Insights with NixGuard RAG and Wazuh Integration) | 执行工作流 |
| Execute: Generate Executive Summary (Get Real-Time Security Insights with NixGuard RAG and Wazuh Integration) | 执行工作流 |
| If | IF 判断 |
| Send Email | Email 发送 |
| Convert Markdown to HTML | Code |



## 功能说明

监控告警系统，异常检测并发送通知，定时执行。

定时触发，通过 邮箱 实现自动化。

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

- 节点总数：10
- 触发方式：定时触发

## 触发方式
- Run Daily at 8 AM 触发

## 统计
- 节点总数：10
- 触发节点：1
- 处理节点：8
- 输出节点：1
- 分类：devops
