## 简介
**Extract Company Data and Calculate ICP Score with Airtop**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/4260

---

# Extract Company Data and Calculate ICP Score with Airtop


## 节点清单

| 节点 | 类型 |
|------|------|
| On form submission | 表单触发器 |
| When Executed by Another Workflow | 执行工作流触发器 |
| Merge | 数据合并 |
| Extract company LinkedIn url | 执行工作流 |
| Extract Company Information | 执行工作流 |
| Calclate ICP | 执行工作流 |
| LinkedIn link exists? | IF 判断 |
| Is valid LinkedIn link? | 过滤器 |
| Unify Params | 数据设置 |



## 功能说明

数据采集工具，自动抓取网页或 API 数据（Company)表单提交触发，通过 n8n 内置节点实现自动化。

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

- 节点总数：9
- 触发方式：表单提交触发

## 触发方式
- On form submission 触发
- When Executed by Another Workflow 触发

## 统计
- 节点总数：9
- 触发节点：2
- 处理节点：7
- 输出节点：0
- 分类：workflow-automation
