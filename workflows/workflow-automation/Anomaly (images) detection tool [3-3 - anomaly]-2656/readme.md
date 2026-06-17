## 简介
**Anomaly (images) detection tool [3-3 - anomaly]**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2656

---

# Anomaly (images) detection tool [3-3 - anomaly]


## 节点清单

| 节点 | 类型 |
|------|------|
| Embed image | HTTP Request |
| Get similarity of medoids | HTTP Request |
| Compare scores | Code |
| Variables for medoids | 数据设置 |
| Info About Crop Labeled Clusters | 数据设置 |
| Total Points in Collection | HTTP Request |
| Each Crop Counts | HTTP Request |
| Image URL hardcode | 数据设置 |
| Execute Workflow Trigger | 执行工作流触发器 |



## 功能说明

AI 图像生成工作流，文生图或图生图。

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

- 节点总数：9
- 触发方式：手动或子流程调用

## 触发方式
- Execute Workflow Trigger 触发

## 统计
- 节点总数：9
- 触发节点：1
- 处理节点：4
- 输出节点：4
- 分类：workflow-automation
