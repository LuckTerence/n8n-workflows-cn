## 简介
**Daily Crypto Yield Monitor: Track Top Binance Earn APY Rates with Earnings Calculator**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/11426

---

# Daily Crypto Yield Monitor: Track Top Binance Earn APY Rates with Earnings Calculator


## 节点清单

| 节点 | 类型 |
|------|------|
| Daily Trigger1 | 定时触发器 |
| Prepare Data1 | Code |
| Sign Request1 | 加密 |
| Get Earn Rates1 | HTTP Request |
| Filter & Analyze1 | Code |
| Send Email1 | Email 发送 |
| Split Out1 | 数据拆分 |
| Edit Fields1 | 数据设置 |
| Sort1 | 数据排序 |
| Limit1 | 数据限制 |
| Set Credentials1 | 数据设置 |



## 功能说明

金融数据分析系统，市场行情采集与 AI 分析告警，定时执行。

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

- 节点总数：11
- 触发方式：定时触发

## 触发方式
- Daily Trigger1 触发

## 统计
- 节点总数：11
- 触发节点：1
- 处理节点：8
- 输出节点：2
- 分类：workflow-automation
