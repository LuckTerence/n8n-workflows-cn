## 简介
**Daily Company Online Presence Monitor with AI Sentiment Analysis & Multi-platform Tracking**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/6668

---

# Daily Company Online Presence Monitor with AI Sentiment Analysis & Multi-platform Tracking


## 节点清单

| 节点 | 类型 |
|------|------|
| Daily Morning Trigger (9 AM) | 定时触发器 |
| Set Company Details | 数据设置 |
| Fetch Google News RSS | rssFeed |
| Prepare News for Merge | Function |
| Search Reddit Posts | reddit |
| Prepare Reddit for Merge | Function |
| Search YouTube Videos | youTube |
| Prepare YouTube for Merge | Function |
| Merge All Mentions | 列表操作 |
| SQLite: Ensure Table Exists | sqlite |
| Filter New Mentions (Deduplication) | Function |
| SQLite: Check If Processed | sqlite |
| AI: Analyze Sentiment & Summarize | OpenAI |
| Process AI Results & Categorize | Function |
| SQLite: Record Processed Mentions | sqlite |
| Format Report Email | Function |
| Send Report Email | Email 发送 |



## 功能说明

监控告警系统，异常检测并发送通知。

手动触发，通过 邮箱 + 数据库 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com
- 邮箱 SMTP/IMAP 账号密码
- 数据库连接信息
- 通义万相 API Key → https://dashscope.aliyun.com

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：17
- 触发方式：手动或子流程调用

## 触发方式
- Daily Morning Trigger (9 AM) 触发

## 统计
- 节点总数：17
- 触发节点：1
- 处理节点：15
- 输出节点：1
- 分类：workflow-automation
