## 简介
**Automate Video Translation from Multiple Sources with Rask AI**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Drive)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/11496

---

# Automate Video Translation from Multiple Sources with Rask AI


## 节点清单

| 节点 | 类型 |
|------|------|
| When Executed by Another Workflow | 执行工作流触发器 |
| Upload media | HTTP Request |
| Get media | HTTP Request |
| Switch media status | Switch 路由 |
| Create project | HTTP Request |
| Get project | HTTP Request |
| Wait media processing | 等待 |
| Switch project status | Switch 路由 |
| Wait project processing | 等待 |
| Uploading failed | 停止并报错 |
| Processing failed | 停止并报错 |



## 功能说明

AI 视频生成工作流，自动创作视频内容。

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

- 节点总数：11
- 触发方式：手动或子流程调用

## 触发方式
- When Executed by Another Workflow 触发

## 统计
- 节点总数：11
- 触发节点：1
- 处理节点：6
- 输出节点：4
- 分类：workflow-automation
