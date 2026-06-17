## 简介
**Create High Quality UGC Images with Nano Banana (Cheaper & Faster)**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Drive)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/8644

---

# Create High Quality UGC Images with Nano Banana (Cheaper & Faster)


## 节点清单

| 节点 | 类型 |
|------|------|
| Mistral Cloud Chat Model | Mistral Chat Model |
| Generate Image | HTTP Request |
| Google Drive Trigger | Google Drive 触发器 |
| Loop Over Items | 分批处理 |
| Upload file | Google Drive |
| Structured Output Parser | 结构化输出解析器 |
| No Operation, do nothing | 空操作 |
| Retrieve Image | HTTP Request |
| Setup | 数据设置 |
| Generate Prompts | LLM Chain |
| Split Out | 数据拆分 |



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

- 节点总数：11
- 触发方式：手动或子流程调用

## 触发方式
- Google Drive Trigger 触发

## 统计
- 节点总数：11
- 触发节点：1
- 处理节点：8
- 输出节点：2
- 分类：workflow-automation
