## 简介
**Chinese Translator via Line x OpenRouter (Text & Image)**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3211

---

# Chinese Translator via Line x OpenRouter (Text & Image)


## 节点清单

| 节点 | 类型 |
|------|------|
| Line Webhook | Webhook |
| Line Loading Animation | HTTP Request |
| Switch | Switch 路由 |
| Get Image | HTTP Request |
| OpenRouter : qwen/qwen2.5-vl-72b-instruct:free | HTTP Request |
| OpenRouter: qwen/qwen-2.5-72b-instruct:free | HTTP Request |
| Extract from File | 从文件提取 |
| Line Reply (image) | HTTP Request |
| Line Reply (Text) | HTTP Request |
| Line Reply (Not Supported 2) | HTTP Request |
| Line Reply (Not Supported 1) | HTTP Request |



## 功能说明

AI 图像生成工作流，文生图或图生图，Webhook 触发。

Webhook触发，通过 HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- 通义万相 API Key → https://dashscope.aliyun.com

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：11
- 触发方式：Webhook 触发

## 触发方式
- Line Webhook 触发

## 统计
- 节点总数：11
- 触发节点：1
- 处理节点：2
- 输出节点：8
- 分类：workflow-automation
