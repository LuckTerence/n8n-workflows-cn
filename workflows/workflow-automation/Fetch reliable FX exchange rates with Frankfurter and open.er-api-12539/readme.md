## 简介
**Fetch reliable FX exchange rates with Frankfurter and open.er-api**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/12539

---

# Fetch reliable FX exchange rates with Frankfurter and open.er-api


## 节点清单

| 节点 | 类型 |
|------|------|
| Set Currencies | 数据设置 |
| If Valid Data | IF 判断 |
| Stop and Error | 停止并报错 |
| Frankfurter | HTTP Request |
| Normalize Frankfurter | Code |
| open.er-api.com | HTTP Request |
| If base correct 1 | IF 判断 |
| If base correct 2 | IF 判断 |
| Fetch FX Rates | 执行工作流触发器 |
| Stop and Error3 | 停止并报错 |
| Normalize open.er-api.com | Code |
| Handle Wrong Base 1 | Code |
| Handle Wrong Base 2 | Code |
| Trim | Code |
| If Trim | IF 判断 |
| Manual Trigger (Example) | 手动触发 |
| Validate & Normalize Inputs | Code |
| Initialize FX State + Static Rates | Code |
| Initialize Coverage Tracking | Code |
| Merge Rates & Check Coverage (1) | Code |
| Merge Rates & Check Coverage (2) | Code |
| Coverage Complete 1? | IF 判断 |
| Coverage Complete 2? | IF 判断 |
| Final Output | 空操作 |



## 功能说明

API 集成接口，连接和编排多个第三方服务。

手动触发，通过 HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

无需额外 API Key，导入即可运行。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：24
- 触发方式：手动触发

## 触发方式
- Fetch FX Rates 触发
- Manual Trigger (Example) 触发

## 统计
- 节点总数：24
- 触发节点：2
- 处理节点：20
- 输出节点：2
- 分类：workflow-automation
