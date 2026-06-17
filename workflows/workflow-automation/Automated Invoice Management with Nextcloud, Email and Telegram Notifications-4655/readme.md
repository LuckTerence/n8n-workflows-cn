## 简介
**Automated Invoice Management with Nextcloud, Email and Telegram Notifications**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/4655

---

# Automated Invoice Management with Nextcloud, Email and Telegram Notifications


## 节点清单

| 节点 | 类型 |
|------|------|
| Start | 定时触发器 |
| List Incoming Invoices | NextCloud |
| File Exists? | IF 判断 |
| Download Invoice | NextCloud |
| Send Email | Email 发送 |
| Archive File | NextCloud |
| Notify Telegram | Telegram |
| Set Parameters | 数据设置 |



## 功能说明

邮件自动化处理，AI 分类整理或。

定时触发，通过 Telegram 通知 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- Telegram Bot Token → @BotFather 创建
- 邮箱 SMTP/IMAP 账号密码
- 通义万相 API Key → https://dashscope.aliyun.com

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：8
- 触发方式：定时触发

## 触发方式
- Start 触发

## 统计
- 节点总数：8
- 触发节点：1
- 处理节点：5
- 输出节点：2
- 分类：workflow-automation
