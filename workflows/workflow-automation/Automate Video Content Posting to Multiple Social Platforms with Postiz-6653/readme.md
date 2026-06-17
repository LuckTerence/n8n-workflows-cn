## 简介
**Automate Video Content Posting to Multiple Social Platforms with Postiz**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Drive/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/6653

---

# Automate Video Content Posting to Multiple Social Platforms with Postiz


## 节点清单

| 节点 | 类型 |
|------|------|
| Google Drive Trigger | Google Drive 触发器 |
| Download file | Google Drive |
| Extract datetime | 信息提取器 |
| Schedule on TikTok | postiz |
| Upload to Postiz | HTTP Request |
| Get integrations | postiz |
| Schedule on Youtube | postiz |
| Schedule on Facebook | postiz |
| Schedule on Instagram | postiz |
| Schedule on Threads | postiz |
| Send email and wait for reply | Email 发送 |
| Set fields | 数据设置 |
| Split Out | 数据拆分 |
| Filter | 过滤器 |
| Filter1 | 过滤器 |
| Filter2 | 过滤器 |
| Filter3 | 过滤器 |
| Filter4 | 过滤器 |
| OpenAI Chat Model | OpenAI Chat Model |



## 功能说明

AI 视频生成工作流，自动创作视频内容。

手动触发，通过 邮箱 + HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com
- 邮箱 SMTP/IMAP 账号密码

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：19
- 触发方式：手动或子流程调用

## 触发方式
- Google Drive Trigger 触发

## 统计
- 节点总数：19
- 触发节点：1
- 处理节点：16
- 输出节点：2
- 分类：workflow-automation
