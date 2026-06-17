## 简介
**Convert PDF Articles to Audio Podcasts with Google TTS & Cloudflare R2**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/9521

---

# Convert PDF Articles to Audio Podcasts with Google TTS & Cloudflare R2


## 节点清单

| 节点 | 类型 |
|------|------|
| ⚙️ Workflow Config | 数据设置 |
| Upload PDF for Podcast | 表单触发器 |
| Extract PDF Text | readPDF |
| Clean & Process Text | Code |
| Detect Sections & Split | Code |
| Check TTS Usage Limit | Code |
| Google TTS API | HTTP Request |
| Convert Audio to Binary | Code |
| Stitch All Mp3 Together | Code |
| Upload MP3 to R2 | cloudflareR2Storage |
| Build RSS XML | Code |
| Upload RSS to R2 | cloudflareR2Storage |
| Update Monthly Usage | Code |
| Aggregate for Email | Code |
| Send Email | Email 发送 |
| Merge | 数据合并 |



## 功能说明

AI 语音处理工作流，语音合成或转录（Pdf)表单提交触发，通过 邮箱 + HTTP API 实现自动化。

，通过 邮箱 + HTTP API 实现自动化。

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

- 节点总数：16
- 触发方式：表单提交触发

## 触发方式
- Upload PDF for Podcast 触发

## 统计
- 节点总数：16
- 触发节点：1
- 处理节点：13
- 输出节点：2
- 分类：workflow-automation
