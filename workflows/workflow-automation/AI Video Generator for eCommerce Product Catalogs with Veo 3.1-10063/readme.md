## 简介
**AI Video Generator for eCommerce Product Catalogs with Veo 3.1**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Drive)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/10063

---

# AI Video Generator for eCommerce Product Catalogs with Veo 3.1


## 节点清单

| 节点 | 类型 |
|------|------|
| form_trigger | 表单触发器 |
| scrape_catalog_collection | Firecrawl |
| split_products | 数据拆分 |
| limit_products | 数据限制 |
| iterate_products | 分批处理 |
| fetch_image | HTTP Request |
| generate_video | HTTP Request |
| set_prompt | 数据设置 |
| fetch_status | HTTP Request |
| wait | 等待 |
| check_response | IF 判断 |
| download_video | HTTP Request |
| convert_to_base64 | 从文件提取 |
| upload_source_image | Google Drive |
| upload_output_video | Google Drive |
| convert_to_binary | 转换为文件 |



## 功能说明

AI 视频生成工作流，自动创作视频内容（Video)表单提交触发，通过 HTTP API 实现自动化。

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

- 节点总数：16
- 触发方式：表单提交触发

## 触发方式
- form_trigger 触发

## 统计
- 节点总数：16
- 触发节点：1
- 处理节点：11
- 输出节点：4
- 分类：workflow-automation
