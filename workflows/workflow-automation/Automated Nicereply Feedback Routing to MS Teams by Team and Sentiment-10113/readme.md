## 简介
**Automated Nicereply Feedback Routing to MS Teams by Team and Sentiment**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/10113

---

# Automated Nicereply Feedback Routing to MS Teams by Team and Sentiment


## 节点清单

| 节点 | 类型 |
|------|------|
| Schedule Trigger | 定时触发器 |
| Filter | 过滤器 |
| Send to Support | Teams |
| Split Out | 数据拆分 |
| Send to Support1 | Teams |
| Get Feedback | HTTP Request |
| Edit Feedbacks | 数据设置 |
| Without Comment | IF 判断 |
| Happiness Value | Switch 路由 |
| Switch - Type of Team | Switch 路由 |
| Switch - Type of Team1 | Switch 路由 |
| Happiness Value2 | Switch 路由 |
| Send to Team Lead | Teams |
| Send to Team Lead1 | Teams |
| Change survey ID according Nicereply | aiTransform |
| Change happiness value | aiTransform |
| Set Empty Respondent to "Unknown Client" | Code |



## 功能说明

表单问卷工具，自动收集和处理用户反馈，定时执行。

定时触发，通过 HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

无需额外 API Key，导入即可运行。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：17
- 触发方式：定时触发

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：17
- 触发节点：1
- 处理节点：11
- 输出节点：5
- 分类：workflow-automation
