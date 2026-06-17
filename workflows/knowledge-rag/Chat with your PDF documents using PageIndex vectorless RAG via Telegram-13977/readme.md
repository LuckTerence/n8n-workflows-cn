## 简介
**Chat with your PDF documents using PageIndex vectorless RAG via Telegram**

（待补充中文描述）

> 分类：知识库 RAG | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/13977

---

# Chat with your PDF documents using PageIndex vectorless RAG via Telegram


## 节点清单

| 节点 | 类型 |
|------|------|
| Receive PDF Document | Telegram 触发器 |
| Download PDF File | Telegram |
| Index PDF on PageIndex | HTTP Request |
| Receive User Question | Telegram 触发器 |
| Fetch All Indexed Documents | HTTP Request |
| Extract Document IDs | 数据设置 |
| LLM Reasoning over Document Tree | HTTP Request |
| Send Answer to User | Telegram |



## 功能说明

RAG 检索增强生成系统，基于文档向量库的知识问答。

Telegram 消息触发，通过 Telegram 通知 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- Telegram Bot Token → @BotFather 创建

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：8
- 触发方式：Telegram 消息触发

## 触发方式
- Receive PDF Document 触发
- Receive User Question 触发

## 统计
- 节点总数：8
- 触发节点：2
- 处理节点：1
- 输出节点：5
- 分类：knowledge-rag
