## 简介
**Create a Lookio RAG assistant from a CSV text corpus**

（待补充中文描述）

> 分类：知识库 RAG | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/11877

---

# Create a Lookio RAG assistant from a CSV text corpus


## 节点清单

| 节点 | 类型 |
|------|------|
| Convert to txt | 转换为文件 |
| Loop Over Items | 分批处理 |
| Convert CSV to JSON | 从文件提取 |
| Upload a CSV | 表单触发器 |
| Aggregate success messages | 数据聚合 |
| Convert IDs into an Array | 数据设置 |
| Success message form ending | 表单 |
| Create Lookio assistant | HTTP Request |
| Import resource to Lookio | HTTP Request |



## 功能说明

RAG 检索增强生成系统，基于文档向量库的知识问答（Lookio)表单提交触发，通过 HTTP API 实现自动化。

，通过 HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

无需额外 API Key，导入即可运行。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：9
- 触发方式：表单提交触发

## 触发方式
- Upload a CSV 触发

## 统计
- 节点总数：9
- 触发节点：1
- 处理节点：6
- 输出节点：2
- 分类：knowledge-rag
