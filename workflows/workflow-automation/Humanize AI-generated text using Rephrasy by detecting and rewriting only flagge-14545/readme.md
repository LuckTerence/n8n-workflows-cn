## 简介
**Humanize AI-generated text using Rephrasy by detecting and rewriting only flagged sentences**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/14545

---

# Humanize AI-generated text using Rephrasy by detecting and rewriting only flagged sentences


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Execute workflow’ | 手动触发 |
| Split Out | 数据拆分 |
| Loop Over Items | 分批处理 |
| Set text | 数据设置 |
| AI Detector | HTTP Request |
| AI Humanizer | HTTP Request |
| Get sentences | Code |
| > 50? | IF 判断 |
| Text | 数据设置 |
| Continue... | 空操作 |
| Text 2 | 数据设置 |
| Aggregate Text | 数据聚合 |



## 功能说明

AI 招聘助手，简历筛选或面试流程自动化。

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

- 节点总数：12
- 触发方式：手动触发

## 触发方式
- When clicking ‘Execute workflow’ 触发

## 统计
- 节点总数：12
- 触发节点：1
- 处理节点：9
- 输出节点：2
- 分类：workflow-automation
