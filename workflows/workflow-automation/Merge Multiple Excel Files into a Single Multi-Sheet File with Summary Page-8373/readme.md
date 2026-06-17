## 简介
**Merge Multiple Excel Files into a Single Multi-Sheet File with Summary Page**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/8373

---

# Merge Multiple Excel Files into a Single Multi-Sheet File with Summary Page


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Execute workflow’ | 手动触发 |
| Read each XLXS | 分批处理 |
| Read XLXS Files from Disk | 读写文件 |
| Create Multi-Sheet Excel | Code |
| Collect and Process Data | Code |
| Save XLXS to Disk | 读写文件 |
| XLSX to Json List | 从文件提取 |
| Mulipte Json to Single Json | 数据聚合 |



## 功能说明

AI 内容摘要工具，自动提炼长文关键信息。

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

- 节点总数：8
- 触发方式：手动触发

## 触发方式
- When clicking ‘Execute workflow’ 触发

## 统计
- 节点总数：8
- 触发节点：1
- 处理节点：7
- 输出节点：0
- 分类：workflow-automation
