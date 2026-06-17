## 简介
**Send Indian tender email reports from TendersInfo.net results**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/15886

---

# Send Indian tender email reports from TendersInfo.net results


## 节点清单

| 节点 | 类型 |
|------|------|
| Webhook Trigger1 | Webhook |
| Parse Tender Response1 | Code |
| Select Email Fields1 | 数据设置 |
| Fetch Tender Data from API1 | HTTP Request |
| Filter GEM Tenders Only1 | 过滤器 |
| Respond to Webhook1 | 响应 Webhook |
| Build HTML Table | Code |



## 功能说明

邮件自动化处理，AI 分类整理或。

定时触发、Webhook触发，通过 邮箱 + HTTP API 实现自动化。

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

- 节点总数：7
- 触发方式：Webhook 触发

## 触发方式
- Webhook Trigger1 触发

## 统计
- 节点总数：7
- 触发节点：1
- 处理节点：4
- 输出节点：2
- 分类：workflow-automation
