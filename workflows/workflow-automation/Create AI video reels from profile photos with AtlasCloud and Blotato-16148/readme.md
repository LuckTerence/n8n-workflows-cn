## 简介
**Create AI video reels from profile photos with AtlasCloud and Blotato**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/16148

---

# Create AI video reels from profile photos with AtlasCloud and Blotato


## 节点清单

| 节点 | 类型 |
|------|------|
| Webhook Trigger | Webhook |
| Config | 数据设置 |
| Wait Image | 等待 |
| Poll Image | HTTP Request |
| Generate Video | HTTP Request |
| Wait Video | 等待 |
| Poll Video | HTTP Request |
| Generate Image with GPT Image 2 Model | HTTP Request |
| Extract Image URL | Code |
| Extract Video URL | Code |
| Create post Tiktok | Blotato |
| Create post Instagram | Blotato |
| Image Status | Switch 路由 |
| Stop and Error | 停止并报错 |
| Video Status | Switch 路由 |
| Stop and Error II | 停止并报错 |



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

- 节点总数：16
- 触发方式：Webhook 触发

## 触发方式
- Webhook Trigger 触发

## 统计
- 节点总数：16
- 触发节点：1
- 处理节点：11
- 输出节点：4
- 分类：workflow-automation
