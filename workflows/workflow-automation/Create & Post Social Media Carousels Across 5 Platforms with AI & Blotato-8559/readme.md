## 简介
**Create & Post Social Media Carousels Across 5 Platforms with AI & Blotato**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/8559

---

# Create & Post Social Media Carousels Across 5 Platforms with AI & Blotato


## 节点清单

| 节点 | 类型 |
|------|------|
| Error Report | 数据合并 |
| Tiktok [BLOTATO] | Blotato |
| Facebook [BLOTATO] | Blotato |
| Instagram [BLOTATO] | Blotato |
| Twitter [BLOTATO] | Blotato |
| Get carousel | Blotato |
| When chat message received | Chat 触发器 |
| Simple Memory | 记忆缓冲区 |
| Respond to Chat | 聊天 |
| Wait | 等待 |
| If quotes ready | IF 判断 |
| AI Agent Carousel Maker | AI Agent |
| Simple tweet cards monocolor | blotatoTool |
| Quote cards monocolor paper | blotatoTool |
| Tweet cards with photo background | blotatoTool |
| Quote cards with highlight on paper | blotatoTool |
| ChatGPT | OpenAI Chat Model |
| Pinterest [BLOTATO] | Blotato |
| If carousel ready | IF 判断 |



## 功能说明

社交媒体管理，多平台内容发布和监听。

Chat 消息触发，通过 工作流编排 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：19
- 触发方式：Chat 消息触发

## 触发方式
- When chat message received 触发

## 统计
- 节点总数：19
- 触发节点：1
- 处理节点：17
- 输出节点：1
- 分类：workflow-automation
