## 简介
**Generate High-Quality Audio with Voxtral Small 24B 2507**

（待补充中文描述）

> 分类：多模态 AI | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/6890

---

# Generate High-Quality Audio with Voxtral Small 24B 2507


## 节点清单

| 节点 | 类型 |
|------|------|
| On clicking 'execute' | 手动触发 |
| Set API Key | 数据设置 |
| Create Prediction | HTTP Request |
| Extract Prediction ID | Code |
| Wait | 等待 |
| Check Prediction Status | HTTP Request |
| Check If Complete | IF 判断 |
| Process Result | Code |



## 功能说明

AI 语音处理工作流，语音合成或转录。

手动触发，通过 HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

无需额外 API Key，导入即可运行。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：8
- 触发方式：手动触发

## 触发方式
- On clicking 'execute' 触发

## 统计
- 节点总数：8
- 触发节点：1
- 处理节点：5
- 输出节点：2
- 分类：multimodal-ai
