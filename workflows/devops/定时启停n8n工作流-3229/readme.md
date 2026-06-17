## 简介
**定时启停n8n工作流**

n8n API自动启停

> 分类：DevOps | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3229

---

# 定时启停n8n工作流


## 节点清单

| 节点 | 类型 |
|------|------|
| n8n Activate | n8n |
| n8n Deactivate | n8n |
| Workflow ID | 数据设置 |
| Merge in Workflow ID for deactivation | 数据合并 |
| Merge in Workflow ID for activation | 数据合并 |
| Activate at 08:00 daily | 定时触发器 |
| Deactivate at 20:00 daily | 定时触发器 |



## 功能说明

n8n 工作流管理工具，编排控制工作流的启停，定时执行（定时启停n8n工作流)定时触发，通过 n8n 内置节点实现自动化。

定时触发，通过 工作流编排 实现自动化。

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
- 触发方式：定时触发

## 触发方式
- Activate at 08:00 daily 触发
- Deactivate at 20:00 daily 触发

## 统计
- 节点总数：7
- 触发节点：2
- 处理节点：5
- 输出节点：0
- 分类：devops
