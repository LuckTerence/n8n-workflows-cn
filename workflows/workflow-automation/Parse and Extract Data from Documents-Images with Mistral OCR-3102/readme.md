## 简介
**Parse and Extract Data from Documents-Images with Mistral OCR**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Drive)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3102

---

# Parse and Extract Data from Documents-Images with Mistral OCR


## 节点清单

| 节点 | 类型 |
|------|------|
| Mistral Upload | HTTP Request |
| When clicking ‘Test workflow’ | 手动触发 |
| Mistral Signed URL | HTTP Request |
| Import PDF | Google Drive |
| Import Image | Google Drive |
| Mistral Upload1 | HTTP Request |
| Mistral Signed URL1 | HTTP Request |
| Mistral DOC OCR | HTTP Request |
| Mistral IMAGE OCR | HTTP Request |
| Document URL | 数据设置 |
| Image URL | 数据设置 |
| Mistral DOC OCR1 | HTTP Request |
| Mistral IMAGE OCR1 | HTTP Request |
| Document URL1 | 数据设置 |
| Document Understanding | HTTP Request |
| Image URL1 | 数据设置 |
| Document Mis-Understanding? | HTTP Request |



## 功能说明

数据采集工具，自动抓取网页或 API 数据。

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

- 节点总数：17
- 触发方式：手动触发

## 触发方式
- When clicking ‘Test workflow’ 触发

## 统计
- 节点总数：17
- 触发节点：1
- 处理节点：6
- 输出节点：10
- 分类：workflow-automation
