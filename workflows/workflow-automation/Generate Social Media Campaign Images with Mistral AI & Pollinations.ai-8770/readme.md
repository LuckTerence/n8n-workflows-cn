## 简介
**Generate Social Media Campaign Images with Mistral AI & Pollinations.ai**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Drive)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/8770

---

# Generate Social Media Campaign Images with Mistral AI & Pollinations.ai


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Test workflow’ | 手动触发 |
| Mistral Cloud Chat Model4 | Mistral Chat Model |
| Structured Output Parser1 | 结构化输出解析器 |
| pollinations.ai | HTTP Request |
| pollinations.ai2 | HTTP Request |
| pollinations.ai3 | HTTP Request |
| pollinations.ai4 | HTTP Request |
| pollinations.ai5 | HTTP Request |
| Send as 1 merged file1 | Code |
| Change name to photo 1 | Code |
| Change name to photo 2 | Code |
| Change name to photo 3 | Code |
| Change name to photo 4 | Code |
| Change name to photo 5 | Code |
| Campaign Goal generator | AI Agent |
| image prompt generator base on the goal | AI Agent |
| brand goals | Google Drive |
| brand profile | Google Drive |
| clean retrived data | Code |
| Merge profile and goals | 数据合并 |
| separate each Prompts | 数据设置 |
| Merge image into one item | 数据合并 |
| Upload file | Google Drive |



## 功能说明

AI 图像生成工作流，文生图或图生图。

手动触发，通过 HTTP API 实现自动化。

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

- 节点总数：23
- 触发方式：手动触发

## 触发方式
- When clicking ‘Test workflow’ 触发

## 统计
- 节点总数：23
- 触发节点：1
- 处理节点：17
- 输出节点：5
- 分类：workflow-automation
