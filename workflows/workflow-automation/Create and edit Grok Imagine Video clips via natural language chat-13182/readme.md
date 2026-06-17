## 简介
**Create and edit Grok Imagine Video clips via natural language chat**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/13182

---

# Create and edit Grok Imagine Video clips via natural language chat


## 节点清单

| 节点 | 类型 |
|------|------|
| Run text to video | 工作流工具 |
| Run Text-to-Video1 | 执行工作流触发器 |
| When chat message received | Chat 触发器 |
| Simple Memory | 记忆缓冲区 |
| Get status | HTTP Request |
| Completed? | IF 判断 |
| Switch1 | Switch 路由 |
| Get status1 | HTTP Request |
| Completed?1 | IF 判断 |
| Run image to video | 工作流工具 |
| Get status2 | HTTP Request |
| Completed?2 | IF 判断 |
| Run video to video | 工作流工具 |
| Grok 4.1 Fast | OpenRouter Chat Model |
| Binary? | IF 判断 |
| Set Image Url | 数据设置 |
| Grok Imagine Video Agent | AI Agent |
| Edit Video | HTTP Request |
| Text to Video | HTTP Request |
| Image to Video | HTTP Request |
| Get final text to video url | HTTP Request |
| Get final edit video url | HTTP Request |
| Get final image to video url | HTTP Request |
| Wait 10 sec. | 等待 |
| Wait 10 sec.1 | 等待 |
| Wait 10 sec.2 | 等待 |
| Upload image | FTP |



## 功能说明

AI 视频生成工作流，自动创作视频内容。

Chat 消息触发，通过 HTTP API 实现自动化。

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
- 触发方式：Chat 消息触发

## 触发方式
- Run Text-to-Video1 触发
- When chat message received 触发

## 统计
- 节点总数：27
- 触发节点：2
- 处理节点：16
- 输出节点：9
- 分类：workflow-automation
