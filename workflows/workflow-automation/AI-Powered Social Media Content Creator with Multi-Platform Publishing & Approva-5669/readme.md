## 简介
**AI-Powered Social Media Content Creator with Multi-Platform Publishing & Approval**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Drive/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/5669

---

# AI-Powered Social Media Content Creator with Multi-Platform Publishing & Approval


## 节点清单

| 节点 | 类型 |
|------|------|
| When chat message received | Chat 触发器 |
| X-Twiter | 工作流工具 |
| Instagram | 工作流工具 |
| Window Buffer Memory | 记忆缓冲区 |
| Facebook | 工作流工具 |
| LinkedIn | 工作流工具 |
| Short | 工作流工具 |
| YouTube Short | 工作流工具 |
| Instagram Image | HTTP Request |
| X Post | Twitter |
| Instragram Post | facebookGraphApi |
| Facebook Post | facebookGraphApi |
| LinkedIn Post | linkedIn |
| Gmail User for Approval | Email 发送 |
| Get Social Post Image | HTTP Request |
| gpt-40-mini1 | OpenAI Chat Model |
| Social Media Publishing Router | Switch 路由 |
| Prepare Email Contents | AI Agent |
| Is Approved? | IF 判断 |
| File Id | 数据设置 |
| Get Social Post from Google Drive | Google Drive |
| Extract as JSON | 从文件提取 |
| Merge Image and Post Contents | 数据合并 |
| Implement Threads Here | 空操作 |
| Implement YouTube Shorts Here | 空操作 |
| X Response | 数据设置 |
| Instagram Response | 数据设置 |
| Facebook Response | 数据设置 |
| LinkedIn Response | 数据设置 |
| 🤖Social Media Router Agent | AI Agent |
| gpt-4o | OpenAI Chat Model |



## 功能说明

社交媒体管理，多平台内容发布和监听。

Chat 消息触发，通过 邮箱 + HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com
- 邮箱 SMTP/IMAP 账号密码
- 通义万相 API Key → https://dashscope.aliyun.com

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：31
- 触发方式：Chat 消息触发

## 触发方式
- When chat message received 触发

## 统计
- 节点总数：31
- 触发节点：1
- 处理节点：27
- 输出节点：3
- 分类：workflow-automation
