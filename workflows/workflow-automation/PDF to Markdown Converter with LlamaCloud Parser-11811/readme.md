## 简介
**PDF to Markdown Converter with LlamaCloud Parser**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Drive)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/11811

---

# PDF to Markdown Converter with LlamaCloud Parser


## 节点清单

| 节点 | 类型 |
|------|------|
| Wait1 | 等待 |
| Check Status1 | HTTP Request |
| Send Data To Llama Cloud1 | HTTP Request |
| Download File From Drive1 | Google Drive |
| Check Job Status1 | IF 判断 |
| Wait3 | 等待 |
| Get Data1 | HTTP Request |



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

- 节点总数：7
- 触发方式：手动或子流程调用

## 触发方式
- 手动触发

## 统计
- 节点总数：7
- 触发节点：0
- 处理节点：4
- 输出节点：3
- 分类：workflow-automation
