## 简介
**Analyze, Interpret & Visualize Data from Multiple Sources with Ada AI**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/9605

---

# Analyze, Interpret & Visualize Data from Multiple Sources with Ada AI


## 节点清单

| 节点 | 类型 |
|------|------|
| Start | 手动触发 |
| Get data from database | MySQL |
| Process Data | 数据聚合 |
| Get data from Google Sheets | Google Sheets |
| Get data from local file | 读写文件 |
| Extract JSON from xlsx file | 从文件提取 |
| DataAnalysis | HTTP Request |
| DataInterpretation | HTTP Request |
| DataVisualization | HTTP Request |
| Convert to HTML File | 转换为文件 |
| Convert markdown to HTML | Markdown |
| Convert markdown to HTML 2 | Markdown |
| Send DataAnalysis message | Email 发送 |
| Send DataInterpretation message | Email 发送 |
| Send DataVisualization | Email 发送 |
| Sample Data | Code |
| Process Visualization Data | 数据设置 |



## 功能说明

Analyze、Interpret & Visualize Data from Multiple。

手动触发，通过 邮箱 + 在线表格 + HTTP API 实现自动化。

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

- 节点总数：17
- 触发方式：手动触发

## 触发方式
- Start 触发

## 统计
- 节点总数：17
- 触发节点：1
- 处理节点：10
- 输出节点：6
- 分类：workflow-automation
