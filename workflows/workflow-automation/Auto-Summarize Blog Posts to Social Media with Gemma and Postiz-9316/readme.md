## 简介
**Auto-Summarize Blog Posts to Social Media with Gemma and Postiz**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/9316

---

# Auto-Summarize Blog Posts to Social Media with Gemma and Postiz


## 节点清单

| 节点 | 类型 |
|------|------|
| Postiz (Create Post) | postiz |
| Split RSS Feed URLs into Items | 数据拆分 |
| Fetch Latest RSS Feed Content | RSS Feed |
| Normalize RSS Fields (Content & Link) | 数据设置 |
| Select Latest RSS Item by Date | Code |
| Generate Summary and Hashtags with LLM | LLM Chain |
| Configure Local LLM Model (Ollama) | lmOllama |
| Calculate Summary Character Limit | Code |
| Set RSS Feed URLs | 数据设置 |
| Read Last Posted Hash from File | Code |
| Save Posted Hash to File | Code |
| Calculate Link Hash for Duplication Check | Code |
| Compare Hashes for Duplicate Check | Code |
| Conditional Check for New Post | Code |
| Extract Image URL from Post HTML | Code |
| Fetch Blog Post HTML Content | HTTP Request |
| Download Post Image | HTTP Request |
| Transform/Resize Image for Upload | 图片编辑 |
| Upload Image to Postiz | postiz |
| Filter Latest Item for Image Processing | Code |
| Loop Over RSS Items for Processing | 分批处理 |
| Merge Processed Data Streams | 数据合并 |
| Create and Post Content via Postiz API | HTTP Request |
| Validate Inputs for Postiz API | Code |
| Schedule: Check RSS Every 10 Minutes | 定时触发器 |
| Process LLM Output for Postiz (Extract Text/Hashtags/Link) | Code |
| Save Temporary Link Hash to File | Code |



## 功能说明

社交媒体管理，多平台内容发布和监听，定时执行。

定时触发，通过 HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com
- 通义万相 API Key → https://dashscope.aliyun.com

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：27
- 触发方式：定时触发

## 触发方式
- Fetch Latest RSS Feed Content 触发
- Schedule: Check RSS Every 10 Minutes 触发

## 统计
- 节点总数：27
- 触发节点：2
- 处理节点：22
- 输出节点：3
- 分类：workflow-automation
