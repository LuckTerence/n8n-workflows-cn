## 简介
**Get Daily Exercise Plan with Flex Message via LINE**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2988

---

# Get Daily Exercise Plan with Flex Message via LINE


## 节点清单

| 节点 | 类型 |
|------|------|
| Azure OpenAI Chat Model2 | Azure OpenAI Chat Model |
| YogaLog | Google Sheets |
| Azure OpenAI Chat Model3 | Azure OpenAI Chat Model |
| Auto-fixing Output Parser | 自动修复输出解析器 |
| Azure OpenAI Chat Model1 | Azure OpenAI Chat Model |
| Structured Output Parser | 结构化输出解析器 |
| AI Agent | AI Agent |
| PosesDatabase1 | Google Sheets 工具 |
| YogaLog2 | Google Sheets |
| Split Out | 数据拆分 |
| Trigger 2130 YogaPosesToday | 定时触发器 |
| Azure OpenAI Chat Model5 | Azure OpenAI Chat Model |
| Get PoseName | Google Sheets |
| WritePosesToday | LLM Chain |
| RewritePosesToday | LLM Chain |
| Azure OpenAI Chat Model | Azure OpenAI Chat Model |
| WriteJSONflex | LLM Chain |
| Structured Output Parser1 | 结构化输出解析器 |
| Auto-fixing Output Parser1 | 自动修复输出解析器 |
| Azure OpenAI Chat Model6 | Azure OpenAI Chat Model |
| Azure OpenAI Chat Model4 | Azure OpenAI Chat Model |
| Code | Code |
| Line Push with Flex Bubble | HTTP Request |
| CombineAll | 数据设置 |
| Fix JSON | LLM Chain |



## 功能说明

Get Daily Exercise Plan with Flex Message via LINE（AI 增强)定时触发，通过 HTTP API 实现自动化。

定时触发，通过 HTTP API 实现自动化。

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

- 节点总数：25
- 触发方式：定时触发

## 触发方式
- Trigger 2130 YogaPosesToday 触发

## 统计
- 节点总数：25
- 触发节点：1
- 处理节点：23
- 输出节点：1
- 分类：workflow-automation
