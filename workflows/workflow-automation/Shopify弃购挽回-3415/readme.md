## 简介
**Shopify弃购挽回**

Gmail+Sheets+Twilio自动挽回弃购

> 分类：工作流自动化 | 适配等级：A（需替换Twilio/Google Sheets/Gmail)（AI模型已适配，部分外服节点需手动替换为国内服务）
> 原始来源：https://n8nworkflows.xyz/workflows/3415

---

# Shopify弃购挽回


## 节点清单

| 节点 | 类型 |
|------|------|
| Fetch Cart | HTTP Request |
| Send Email (Gmail) | Gmail |
| Wait 24 Hours | 等待 |
| Send SMS (Twilio) | twilio |
| Log to Google Sheet | Google Sheets |
| Shopify Trigger | shopifyTrigger |
| GET Checkout Status | HTTP Request |
| Completed Checkout? | IF 判断 |
| Mark as "Recovered Naturally" | Google Sheets |
| Extract Key Values | 数据设置 |
| Webhook | Webhook |
| Airtable | Airtable |
| Apply Global Discount Code | 数据设置 |
| Wait some hours | 等待 |
| Wait some days | 等待 |
| Loop Over Items | 分批处理 |
| GET Checkout Status1 | HTTP Request |
| Ready to take this to the next level? We at Innovatio are cheering for you!!! Best of luck and great successes to you all <3 Velebit from Innovatio | 空操作 |



## 功能说明

电商自动化，订单处理或商品管理，Webhook 触发。

Webhook触发，通过 邮箱 + 在线表格 + HTTP API 实现自动化。

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

- 节点总数：18
- 触发方式：Webhook 触发

## 触发方式
- Shopify Trigger 触发
- Webhook 触发

## 统计
- 节点总数：18
- 触发节点：2
- 处理节点：13
- 输出节点：3
- 分类：workflow-automation
