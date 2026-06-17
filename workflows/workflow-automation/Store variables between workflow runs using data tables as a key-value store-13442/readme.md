## 简介
**Store variables between workflow runs using data tables as a key-value store**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/13442

---

# Store variables between workflow runs using data tables as a key-value store


## 节点清单

| 节点 | 类型 |
|------|------|
| Create Globals table | 数据表 |
| Stop and Error | 停止并报错 |
| If not the expected error | IF 判断 |
| Global found | IF 判断 |
| When clicking ‘Execute workflow’ | 手动触发 |
| Get Global "your_variable_name" | 数据表 |
| Set default value | 数据设置 |
| Format value | 数据设置 |
| Do something | 空操作 |
| Upsert Global "your_variable_name" | 数据表 |



## 功能说明

n8n 工作流管理工具，编排控制工作流的启停。

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

- 节点总数：10
- 触发方式：手动触发

## 触发方式
- When clicking ‘Execute workflow’ 触发

## 统计
- 节点总数：10
- 触发节点：1
- 处理节点：9
- 输出节点：0
- 分类：workflow-automation
