## 简介
**Automate E-commerce Return Guides with Email Verification, PDF-Image Generation & QR Codes**

（待补充中文描述）

> 分类：多模态 AI | 适配等级：A（需替换Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/8942

---

# Automate E-commerce Return Guides with Email Verification, PDF-Image Generation & QR Codes


## 节点清单

| 节点 | 类型 |
|------|------|
| Webhook | Webhook |
| Verifi Email | verifiEmail |
| Switch | Switch 路由 |
| Stop and Error | 停止并报错 |
| Edit Fields | 数据设置 |
| Code in JavaScript | Code |
| Merge | 数据合并 |
| Remove Duplicates | 去重 |
| HTML to PDF | htmlcsstopdf |
| HTML/CSS to Image | htmlCssToImage |
| Loop Over Items | 分批处理 |
| Merge1 | 数据合并 |
| Send a message | Email 发送 |



## 功能说明

邮件自动化处理，AI 分类整理或。

定时触发、Webhook触发，通过 邮箱 + HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- 邮箱 SMTP/IMAP 账号密码
- 通义万相 API Key → https://dashscope.aliyun.com

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：13
- 触发方式：Webhook 触发

## 触发方式
- Webhook 触发

## 统计
- 节点总数：13
- 触发节点：1
- 处理节点：11
- 输出节点：1
- 分类：multimodal-ai
