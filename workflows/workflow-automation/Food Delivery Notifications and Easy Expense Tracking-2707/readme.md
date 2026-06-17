## 简介
**Food Delivery Notifications and Easy Expense Tracking**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Slack/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2707

---

# Food Delivery Notifications and Easy Expense Tracking


## 节点清单

| 节点 | 类型 |
|------|------|
| Loop Over Items | 分批处理 |
| Click to Test Flow | 手动触发 |
| Get emails from Gmail with certain subject | Email 发送 |
| Receive certain keyword Gmail Trigger | Gmail 触发器 |
| Extract Price, Shop, Date, TIme | 数据设置 |
| Send to Slack with Block | Slack |



## 功能说明

通知推送系统，多渠道消息分发。

手动触发，通过 邮箱 + Slack + HTTP API 实现自动化。

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

- 节点总数：6
- 触发方式：手动触发

## 触发方式
- Click to Test Flow 触发
- Receive certain keyword Gmail Trigger 触发

## 统计
- 节点总数：6
- 触发节点：2
- 处理节点：2
- 输出节点：2
- 分类：workflow-automation
