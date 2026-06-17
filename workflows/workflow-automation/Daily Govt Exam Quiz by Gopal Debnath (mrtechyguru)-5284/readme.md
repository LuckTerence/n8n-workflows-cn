## 简介
**Daily Govt Exam Quiz by Gopal Debnath (mrtechyguru)**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Twilio/Google Sheets)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/5284

---

# Daily Govt Exam Quiz by Gopal Debnath (mrtechyguru)


## 节点清单

| 节点 | 类型 |
|------|------|
| Daily Trigger | 定时触发器 |
| Fetch Question | Google Sheets |
| Format Quiz | Function |
| Send Email | Email 发送 |
| Send to Telegram | Telegram |
| Send via Twilio | twilio |



## 功能说明

Daily Govt Exam Quiz by Gopal Debnath (mrtechyguru。

手动触发，通过 Telegram 通知 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- Telegram Bot Token → @BotFather 创建
- 邮箱 SMTP/IMAP 账号密码

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：6
- 触发方式：手动或子流程调用

## 触发方式
- Daily Trigger 触发

## 统计
- 节点总数：6
- 触发节点：1
- 处理节点：3
- 输出节点：2
- 分类：workflow-automation
