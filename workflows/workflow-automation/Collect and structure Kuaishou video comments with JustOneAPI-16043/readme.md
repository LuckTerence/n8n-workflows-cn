## 简介
**Collect and structure Kuaishou video comments with JustOneAPI**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/16043

---

# Collect and structure Kuaishou video comments with JustOneAPI


## 节点清单

| 节点 | 类型 |
|------|------|
| Start Workflow Execution | 手动触发 |
| Set API Request Parameters | 数据设置 |
| Fetch Kuaishou Video Comments API | HTTP Request |
| Output Raw Comment Data | 数据设置 |
| Process Comment Data Collection | Code |
| Output Final Comment Collection | 数据设置 |



## 功能说明

AI 视频生成工作流，自动创作视频内容。

手动触发，通过 HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- 通义万相 API Key → https://dashscope.aliyun.com

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：6
- 触发方式：手动触发

## 触发方式
- Start Workflow Execution 触发

## 统计
- 节点总数：6
- 触发节点：1
- 处理节点：4
- 输出节点：1
- 分类：workflow-automation
