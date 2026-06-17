## 简介
**Convert Revit Projects to Database with Drawings & Specifications using DDC Toolkit**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/7649

---

# Convert Revit Projects to Database with Drawings & Specifications using DDC Toolkit


## 节点清单

| 节点 | 类型 |
|------|------|
| Form UI | 表单触发器 |
| Manual Trigger (Optional) | 手动触发 |
| Set the conversion variables | 数据设置 |
| Converting the project into a structured form1 | 执行命令 |



## 功能说明

数据库操作工具，自动查询或写入数据库（Revit)表单提交触发、手动触发，通过 n8n 内置节点实现自动化。

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

- 节点总数：4
- 触发方式：表单提交触发, 手动触发

## 触发方式
- Form UI 触发
- Manual Trigger (Optional) 触发

## 统计
- 节点总数：4
- 触发节点：2
- 处理节点：2
- 输出节点：0
- 分类：workflow-automation
