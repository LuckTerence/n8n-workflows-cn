## 简介
**Automated Meta Token Renewal System with Graph API and Data Storage**

（待补充中文描述）

> 分类：知识库 RAG | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/9604

---

# Automated Meta Token Renewal System with Graph API and Data Storage


## 节点清单

| 节点 | 类型 |
|------|------|
| Schedule Trigger | 定时触发器 |
| No Operation, do nothing | 空操作 |
| Get token expiration date | 数据表 |
| Needs renewal? | IF 判断 |
| Carry ID & Token | 数据设置 |
| User Exchange | HTTP Request |
| Compute new expiry | 数据设置 |
| Update Record | 数据表 |
| When clicking "Execute workflow" | 手动触发 |



## 功能说明

RAG 检索增强生成系统，基于文档向量库的知识问答，定时执行。

定时触发、手动触发，通过 HTTP API 实现自动化。

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
- 触发方式：定时触发, 手动触发

## 触发方式
- Schedule Trigger 触发
- When clicking "Execute workflow" 触发

## 统计
- 节点总数：9
- 触发节点：2
- 处理节点：6
- 输出节点：1
- 分类：knowledge-rag
