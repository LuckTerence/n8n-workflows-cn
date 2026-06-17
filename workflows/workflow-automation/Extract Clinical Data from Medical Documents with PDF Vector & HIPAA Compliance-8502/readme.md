## 简介
**Extract Clinical Data from Medical Documents with PDF Vector & HIPAA Compliance**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Drive)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/8502

---

# Extract Clinical Data from Medical Documents with PDF Vector & HIPAA Compliance


## 节点清单

| 节点 | 类型 |
|------|------|
| Manual Trigger | 手动触发 |
| Google Drive - Get Medical Record | Google Drive |
| PDF Vector - Extract Medical Data | pdfVector |
| Process & Validate Data | Code |
| Valid Record? | IF 判断 |
| Store in Secure Database | PostgreSQL |



## 功能说明

数据采集工具，自动抓取网页或 API 数据。

手动触发，通过 数据库 + HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- 数据库连接信息

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：6
- 触发方式：手动触发

## 触发方式
- Manual Trigger 触发

## 统计
- 节点总数：6
- 触发节点：1
- 处理节点：5
- 输出节点：0
- 分类：workflow-automation
