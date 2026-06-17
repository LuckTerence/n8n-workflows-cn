## 简介
**Comprehensive LLM Usage Tracker & Cost Monitor with Node-Level Analytics**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/7398

---

# Comprehensive LLM Usage Tracker & Cost Monitor with Node-Level Analytics


## 节点清单

| 节点 | 类型 |
|------|------|
| Get an execution | n8n |
| When Exc. | 执行工作流触发器 |
| Extract all model names | Code |
| model prices | 数据设置 |
| Standardize names | 数据设置 |
| Check correctly defined | Code |
| Stop and Error | 停止并报错 |
| If not passed | IF 判断 |
| Merge | 数据合并 |
| Smart Extract LLM data | Code |
| Calculate cost | Code |
| Test id | 手动触发 |



## 功能说明

监控告警系统，异常检测并发送通知。

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

- 节点总数：12
- 触发方式：手动触发

## 触发方式
- When Exc. 触发
- Test id 触发

## 统计
- 节点总数：12
- 触发节点：2
- 处理节点：10
- 输出节点：0
- 分类：workflow-automation
