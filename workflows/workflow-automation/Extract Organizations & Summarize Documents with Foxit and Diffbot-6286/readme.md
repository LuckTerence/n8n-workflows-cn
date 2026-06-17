## 简介
**Extract Organizations & Summarize Documents with Foxit and Diffbot**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Drive/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/6286

---

# Extract Organizations & Summarize Documents with Foxit and Diffbot


## 节点清单

| 节点 | 类型 |
|------|------|
| Fire on New File in Google Drive Folder | Google Drive 触发器 |
| Download File | Google Drive |
| Upload to Foxit | HTTP Request |
| Kick off Foxit Extract | HTTP Request |
| Check Task | HTTP Request |
| Is the job done? | IF 判断 |
| Wait | 等待 |
| Download Extracted Text | HTTP Request |
| Get Diffbot Entities | HTTP Request |
| Shape Data | Code |
| Gmail | Email 发送 |
| Make Email Contents | Code |



## 功能说明

数据采集工具，自动抓取网页或 API 数据。

手动触发，通过 邮箱 + HTTP API 实现自动化。

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

- 节点总数：12
- 触发方式：手动或子流程调用

## 触发方式
- Fire on New File in Google Drive Folder 触发

## 统计
- 节点总数：12
- 触发节点：1
- 处理节点：5
- 输出节点：6
- 分类：workflow-automation
