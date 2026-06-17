## 简介
**Run bulk RAG queries from CSV with Lookio**

（待补充中文描述）

> 分类：知识库 RAG | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/9908

---

# Run bulk RAG queries from CSV with Lookio


## 节点清单

| 节点 | 类型 |
|------|------|
| On form submission | 表单触发器 |
| Valid Query column? | IF 判断 |
| Error message | 表单 |
| Isolate the Query column | 数据设置 |
| Lookio API call | HTTP Request |
| Prepare output | 数据设置 |
| Generate enriched CSV | 转换为文件 |
| Form ending and file download | 表单 |
| Loop Over Queries | 分批处理 |
| Split Out | 数据拆分 |
| Aggregate rows | 数据聚合 |
| Extract all rows | 从文件提取 |



## 功能说明

RAG 检索增强生成系统，基于文档向量库的知识问答（Bulk)表单提交触发，通过 HTTP API 实现自动化。

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

- 节点总数：12
- 触发方式：表单提交触发

## 触发方式
- On form submission 触发

## 统计
- 节点总数：12
- 触发节点：1
- 处理节点：10
- 输出节点：1
- 分类：knowledge-rag
