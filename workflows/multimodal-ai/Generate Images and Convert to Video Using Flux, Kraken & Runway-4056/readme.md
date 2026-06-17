## 简介
**Generate Images and Convert to Video Using Flux, Kraken & Runway**

（待补充中文描述）

> 分类：多模态 AI | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/4056

---

# Generate Images and Convert to Video Using Flux, Kraken & Runway


## 节点清单

| 节点 | 类型 |
|------|------|
| Wait | 等待 |
| get_image_url | HTTP Request |
| get_image | HTTP Request |
| upload to kraken | HTTP Request |
| When clicking ‘Test workflow’ | 手动触发 |
| Get Image3 | HTTP Request |
| upload to kraken1 | HTTP Request |
| Get Video Generation Status1 | HTTP Request |
| Confirm Generation Status | Switch 路由 |
| 1 minute3 | 等待 |
| 1 minute2 | 等待 |
| Download Video | HTTP Request |
| generate image (flux) | HTTP Request |
| generate image (flux-rapid-api) | HTTP Request |
| image to video (runway-rapid-api) | HTTP Request |
| image to video (runway) | HTTP Request |



## 功能说明

AI 图像生成工作流，文生图或图生图。

手动触发，通过 HTTP API 实现自动化。

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

- 节点总数：16
- 触发方式：手动触发

## 触发方式
- When clicking ‘Test workflow’ 触发

## 统计
- 节点总数：16
- 触发节点：1
- 处理节点：4
- 输出节点：11
- 分类：multimodal-ai
