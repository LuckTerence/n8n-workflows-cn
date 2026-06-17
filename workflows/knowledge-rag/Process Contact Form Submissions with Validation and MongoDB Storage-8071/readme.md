## 简介
**Process Contact Form Submissions with Validation and MongoDB Storage**

（待补充中文描述）

> 分类：知识库 RAG | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/8071

---

# Process Contact Form Submissions with Validation and MongoDB Storage


## 节点清单

| 节点 | 类型 |
|------|------|
| Validate Pattern | Code |
| On form submission | 表单触发器 |
| Insert documents | MongoDB |
| Edit Fields | 数据设置 |
| Form Ending | 表单 |



## 功能说明

RAG 检索增强生成系统，基于文档向量库的知识问答（Contact)表单提交触发，通过 n8n 内置节点实现自动化。

，通过 工作流编排 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

无需额外 API Key，导入即可运行。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：5
- 触发方式：表单提交触发

## 触发方式
- On form submission 触发

## 统计
- 节点总数：5
- 触发节点：1
- 处理节点：4
- 输出节点：0
- 分类：knowledge-rag
