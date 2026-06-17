## 简介
**Convert PDF to PNG with PDF.co API (Multi-Page Support)**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3847

---

# Convert PDF to PNG with PDF.co API (Multi-Page Support)


## 节点清单

| 节点 | 类型 |
|------|------|
| Pass through binary | 数据设置 |
| Get Presigned Upload URL (PDF.co) | HTTP Request |
| Combine binary and json data | 数据合并 |
| Upload PDF to Presigned URL | HTTP Request |
| Strip binary data | 数据设置 |
| Combine data | 数据合并 |
| Convert PDF to PNG (PDF.co) | HTTP Request |
| Download PNG from PDF.co | HTTP Request |
| When clicking ‘Test workflow’ | 手动触发 |
| Split multipage PDF files | HTTP Request |
| Compress into zip file | compression |
| Combine binaries | 数据聚合 |
| GET example PDF files | HTTP Request |
| Extract PDF links | HTML |
| Split links into items | 数据拆分 |
| Use two relevant PDF examples | 数据限制 |
| Download example PDF Files | HTTP Request |
| Split out urls | 数据拆分 |
| Loop over pdf files | 分批处理 |



## 功能说明

PDF 文档处理，解析或生成 PDF 文件。

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

- 节点总数：19
- 触发方式：手动触发

## 触发方式
- When clicking ‘Test workflow’ 触发

## 统计
- 节点总数：19
- 触发节点：1
- 处理节点：11
- 输出节点：7
- 分类：workflow-automation
