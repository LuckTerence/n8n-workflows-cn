## 简介
**Generate Interactive Wall Quantity Reports from Revit Models to HTML**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/5869

---

# Generate Interactive Wall Quantity Reports from Revit Models to HTML


## 节点清单

| 节点 | 类型 |
|------|------|
| Start - Click to begin | 手动触发 |
| Setup - Define file paths | 数据设置 |
| Extract - Run Revit converter | 执行命令 |
| Check - Did extraction succeed? | IF 判断 |
| Success - Create Excel filename | 数据设置 |
| Error - Show what went wrong | 数据设置 |
| Extract - Read Excel file from disk | 读取二进制文件 |
| Extract - Parse Excel to data | 电子表格文件 |
| Transform - Filter only OST_Walls | IF 判断 |
| Transform - Clean wall data | 数据设置 |
| Transform - Group by Type Name & sum Volume | Function |
| Transform - Generate HTML Report | Function |
| Load - Save HTML Report | 写入二进制文件 |
| Success - Final results | 数据设置 |



## 功能说明

Generate Interactive Wall Quantity Reports from Re。

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

- 节点总数：14
- 触发方式：手动触发

## 触发方式
- Start - Click to begin 触发

## 统计
- 节点总数：14
- 触发节点：1
- 处理节点：13
- 输出节点：0
- 分类：workflow-automation
