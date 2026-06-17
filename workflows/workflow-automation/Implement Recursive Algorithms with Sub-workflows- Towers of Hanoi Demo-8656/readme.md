## 简介
**Implement Recursive Algorithms with Sub-workflows: Towers of Hanoi Demo**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/8656

---

# Implement Recursive Algorithms with Sub-workflows: Towers of Hanoi Demo


## 节点清单

| 节点 | 类型 |
|------|------|
| Set number of discs | 数据设置 |
| Max 1 disc | IF 判断 |
| A B C | 执行工作流 |
| X Y Z | 执行工作流触发器 |
| X to Z | Code |
| X to Z | Code |
| Update | Code |
| Update | Code |
| Create stacks | Code |
| X Z Y | 执行工作流 |
| Y X Z | 执行工作流 |
| Solution | Code |
| Start | 手动触发 |



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

- 节点总数：13
- 触发方式：手动触发

## 触发方式
- X Y Z 触发
- Start 触发

## 统计
- 节点总数：13
- 触发节点：2
- 处理节点：11
- 输出节点：0
- 分类：workflow-automation
