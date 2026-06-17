## 简介
**Scrape Books from URL with Dumpling AI, Clean HTML, Save to Sheets, Email as CSV**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3701

---

# Scrape Books from URL with Dumpling AI, Clean HTML, Save to Sheets, Email as CSV


## 节点清单

| 节点 | 类型 |
|------|------|
| Convert to CSV File | 转换为文件 |
| Extract all books from the page | HTML |
| Sort by price | 数据排序 |
| Extract individual book price | HTML |
| Send CSV via e-mail | Email 发送 |
| Trigger- Watches For new URL in Spreadsheet | Google Sheets 触发器 |
| Scrape Website Content with Dumpling AI | HTTP Request |
| Split HTML Array into Individual Books | 数据拆分 |



## 功能说明

邮件自动化处理，AI 分类整理或。

定时触发、手动触发，通过 邮箱 + HTTP API 实现自动化。

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

- 节点总数：8
- 触发方式：手动或子流程调用

## 触发方式
- Trigger- Watches For new URL in Spreadsheet 触发

## 统计
- 节点总数：8
- 触发节点：1
- 处理节点：5
- 输出节点：2
- 分类：workflow-automation
