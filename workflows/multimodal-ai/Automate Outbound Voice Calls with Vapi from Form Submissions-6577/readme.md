## 简介
**Automate Outbound Voice Calls with Vapi from Form Submissions**

（待补充中文描述）

> 分类：多模态 AI | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/6577

---

# Automate Outbound Voice Calls with Vapi from Form Submissions


## 节点清单

| 节点 | 类型 |
|------|------|
| Start outbound Vapi call | HTTP Request |
| Set fields | 数据设置 |
| On form submission | 表单触发器 |
| Wait 2min | 等待 |



## 功能说明

AI 语音处理工作流，语音合成或转录（Outbound)表单提交触发，通过 HTTP API 实现自动化。

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

- 节点总数：4
- 触发方式：表单提交触发

## 触发方式
- On form submission 触发

## 统计
- 节点总数：4
- 触发节点：1
- 处理节点：2
- 输出节点：1
- 分类：multimodal-ai
