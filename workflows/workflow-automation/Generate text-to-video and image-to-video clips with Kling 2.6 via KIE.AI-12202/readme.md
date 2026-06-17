## 简介
**Generate text-to-video and image-to-video clips with Kling 2.6 via KIE.AI**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Google Drive/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/12202

---

# Generate text-to-video and image-to-video clips with Kling 2.6 via KIE.AI


## 节点清单

| 节点 | 类型 |
|------|------|
| Submit Video Generation Request | HTTP Request |
| Switch Video Generation Status | Switch 路由 |
| Check Video Generation Status | HTTP Request |
| Wait for Video Generation | 等待 |
| Extract Video URL | Code |
| Download Video File | HTTP Request |
| When clicking ‘Execute workflow’ | 手动触发 |
| Set Prompt & Image Url | 数据设置 |
| Wait for Image-to-Video Generation | 等待 |
| Switch | Switch 路由 |
| Check Video Status | HTTP Request |
| Download Video1 | HTTP Request |
| Submit Video Generation1 | HTTP Request |
| Video URL | Code |
| Set Text to Video Parameters | 数据设置 |



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

- 节点总数：15
- 触发方式：手动触发

## 触发方式
- When clicking ‘Execute workflow’ 触发

## 统计
- 节点总数：15
- 触发节点：1
- 处理节点：8
- 输出节点：6
- 分类：workflow-automation
