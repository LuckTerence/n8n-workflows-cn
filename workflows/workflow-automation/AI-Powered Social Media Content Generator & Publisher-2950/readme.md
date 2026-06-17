## 简介
**AI-Powered Social Media Content Generator & Publisher**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2950

---

# AI-Powered Social Media Content Generator & Publisher


## 节点清单

| 节点 | 类型 |
|------|------|
| On form submission | 表单触发器 |
| AI Agent | AI Agent |
| Google Gemini Chat Model | OpenAI Chat Model |
| Structured Output Parser | 结构化输出解析器 |
| Split Form Input | 数据设置 |
| Upload Image | 表单 |
| Split Data | 数据设置 |
| Data for AI | 数据设置 |
| Aggregate | 数据聚合 |
| Form | 表单 |
| Nest Top Meta | 数据设置 |
| Rename Image Binary Top Image | Code |
| Publish to Facebook | facebookGraphApi |
| Publish to LinkedIn | linkedIn |
| X | Twitter |
| Edit Fields | 数据设置 |
| Image for Instagram | HTTP Request |
| Publish to Instagram | facebookGraphApi |
| Merge1 | 数据合并 |
| Upload Image to imgbb.com | HTTP Request |



## 功能说明

社交媒体管理，多平台内容发布和监听（Powered)表单提交触发，通过 HTTP API 实现自动化。

，通过 HTTP API 实现自动化。

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

- 节点总数：20
- 触发方式：表单提交触发

## 触发方式
- On form submission 触发

## 统计
- 节点总数：20
- 触发节点：1
- 处理节点：17
- 输出节点：2
- 分类：workflow-automation
