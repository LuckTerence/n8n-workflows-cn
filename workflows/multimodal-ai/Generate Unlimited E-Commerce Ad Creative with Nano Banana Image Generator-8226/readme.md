## 简介
**Generate Unlimited E-Commerce Ad Creative with Nano Banana Image Generator**

（待补充中文描述）

> 分类：多模态 AI | 适配等级：A（需替换Google Drive)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/8226

---

# Generate Unlimited E-Commerce Ad Creative with Nano Banana Image Generator


## 节点清单

| 节点 | 类型 |
|------|------|
| form_trigger | 表单触发器 |
| list_influencer_images | Google Drive |
| iterate_influencer_images | 分批处理 |
| download_influencer_image | Google Drive |
| product_image_to_base64 | 从文件提取 |
| influencer_image_to_base_64 | 从文件提取 |
| generate_image | HTTP Request |
| get_image | 转换为文件 |
| upload_image | Google Drive |
| set_result | 数据设置 |



## 功能说明

AI 图像生成工作流，文生图或图生图（Unlimited)表单提交触发，通过 HTTP API 实现自动化。

，通过 HTTP API 实现自动化。

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

- 节点总数：10
- 触发方式：表单提交触发

## 触发方式
- form_trigger 触发

## 统计
- 节点总数：10
- 触发节点：1
- 处理节点：8
- 输出节点：1
- 分类：multimodal-ai
