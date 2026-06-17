## 简介
**Generate AI images using Havis AI Seedream 5 Lite**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/15761

---

# Generate AI images using Havis AI Seedream 5 Lite


## 节点清单

| 节点 | 类型 |
|------|------|
| Form - Seedream 5 Lite | 表单触发器 |
| Build Payload | Code |
| Submit - Havis API | HTTP Request |
| Wait 8s | 等待 |
| Check Task Status | HTTP Request |
| Is Completed? | IF 判断 |
| Is Failed? | IF 判断 |
| Wait 8s (loop) | 等待 |
| Return Result | 数据设置 |
| Return Error | 数据设置 |



## 功能说明

AI 图像生成工作流，文生图或图生图（Images)表单提交触发，通过 HTTP API 实现自动化。

，通过 HTTP API 实现自动化。

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
- 触发方式：表单提交触发

## 触发方式
- Form - Seedream 5 Lite 触发

## 统计
- 节点总数：10
- 触发节点：1
- 处理节点：7
- 输出节点：2
- 分类：workflow-automation
