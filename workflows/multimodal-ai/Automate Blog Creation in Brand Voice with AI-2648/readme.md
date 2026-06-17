## 简介
**Automate Blog Creation in Brand Voice with AI**

（待补充中文描述）

> 分类：多模态 AI | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2648

---

# Automate Blog Creation in Brand Voice with AI


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Test workflow’ | 手动触发 |
| OpenAI Chat Model | OpenAI Chat Model |
| OpenAI Chat Model1 | OpenAI Chat Model |
| OpenAI Chat Model2 | OpenAI Chat Model |
| Extract Voice Characteristics | 信息提取器 |
| Get Blog | HTTP Request |
| Get Article | HTTP Request |
| Extract Article URLs | HTML |
| Split Out URLs | 数据拆分 |
| Latest Articles | 数据限制 |
| Extract Article Content | HTML |
| Combine Articles | 数据聚合 |
| Article Style & Brand Voice | 数据合并 |
| Save as Draft | wordpress |
| Capture Existing Article Structure | LLM Chain |
| Markdown | Markdown |
| Content Generation Agent | 信息提取器 |
| New Article Instruction | 数据设置 |



## 功能说明

AI 语音处理工作流，语音合成或转录。

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

- 节点总数：18
- 触发方式：手动触发

## 触发方式
- When clicking ‘Test workflow’ 触发

## 统计
- 节点总数：18
- 触发节点：1
- 处理节点：15
- 输出节点：2
- 分类：multimodal-ai
