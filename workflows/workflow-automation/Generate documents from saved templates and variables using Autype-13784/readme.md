## 简介
**Generate documents from saved templates and variables using Autype**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/13784

---

# Generate documents from saved templates and variables using Autype


## 节点清单

| 节点 | 类型 |
|------|------|
| Certificate Form | 表单触发器 |
| Set Form Variables | 数据设置 |
| Get Document Variables | autype |
| Render Document with Variables | autype |
| Create Project | autype |
| Create Document | autype |
| When clicking ‘Execute workflow’ | 手动触发 |



## 功能说明

Generate documents from saved templates and variab（自动化)表单提交触发、手动触发，通过 n8n 内置节点实现自动化。

手动触发，通过 工作流编排 实现自动化。

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
- 触发方式：表单提交触发, 手动触发

## 触发方式
- Certificate Form 触发
- When clicking ‘Execute workflow’ 触发

## 统计
- 节点总数：7
- 触发节点：2
- 处理节点：5
- 输出节点：0
- 分类：workflow-automation
