## 简介
**Create Social Media Videos with Sora 2 AI for Marketing & Content Creation**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/9337

---

# Create Social Media Videos with Sora 2 AI for Marketing & Content Creation


## 节点清单

| 节点 | 类型 |
|------|------|
| Obtain the generated status | HTTP Request |
| Convert to JSON | Code |
| Format and Display Results | 数据设置 |
| Send Sora 2 Generation Request to Defapi.org API | HTTP Request |
| Wait for Processing Completion | 等待 |
| On form submission | 表单触发器 |
| Check if Generation is Complete | IF 判断 |



## 功能说明

AI 视频生成工作流，自动创作视频内容（Social)表单提交触发，通过 HTTP API 实现自动化。

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

- 节点总数：7
- 触发方式：表单提交触发

## 触发方式
- On form submission 触发

## 统计
- 节点总数：7
- 触发节点：1
- 处理节点：4
- 输出节点：2
- 分类：workflow-automation
