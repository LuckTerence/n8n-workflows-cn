## 简介
**Extract Product Info from Website Screenshots with Dumpling AI + Sheets**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/5169

---

# Extract Product Info from Website Screenshots with Dumpling AI + Sheets


## 节点清单

| 节点 | 类型 |
|------|------|
| Watch for New Screenshot URLs in Google Sheets | Google Sheets 触发器 |
| Create Screenshot File via Dumpling AI | HTTP Request |
| Download Screenshot Image File from Dumpling AI | HTTP Request |
| Extract Text from Screenshot with Dumpling AI | HTTP Request |
| Convert Image File to Base64 | 从文件提取 |
| Format Extracted Data for Google Sheets | 数据设置 |
| Save extracted data to Google Sheets | Google Sheets |



## 功能说明

数据采集工具，自动抓取网页或 API 数据。

手动触发，通过 在线表格 + HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- 通义万相 API Key → https://dashscope.aliyun.com

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：7
- 触发方式：手动或子流程调用

## 触发方式
- Watch for New Screenshot URLs in Google Sheets 触发

## 统计
- 节点总数：7
- 触发节点：1
- 处理节点：3
- 输出节点：3
- 分类：workflow-automation
