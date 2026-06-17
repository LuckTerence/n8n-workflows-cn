## 简介
**N8N for Beginners: Looping over Items**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2896

---

# N8N for Beginners: Looping over Items


## 节点清单

| 节点 | 类型 |
|------|------|
| Result1 | 空操作 |
| Result2 | 空操作 |
| Split Array of Strings into Array of Objects | 数据拆分 |
| Result3 | 空操作 |
| Result4 | 空操作 |
| Result5 | 空操作 |
| Paste JSON into this node | 手动触发 |
| Add param1 to output5 | Code |
| Add param1 to output1 | Code |
| Loop over Items 2 | 分批处理 |
| Loop over Items 1 | 分批处理 |
| Add param1 to output2 | Code |
| Add param1 to output3 | Code |
| Add param1 to output4 | Code |
| Wait one second(just for show) | 等待 |



## 功能说明

N8N for Beginners- Looping over Items。

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

- 节点总数：15
- 触发方式：手动触发

## 触发方式
- Paste JSON into this node 触发

## 统计
- 节点总数：15
- 触发节点：1
- 处理节点：14
- 输出节点：0
- 分类：workflow-automation
