## 简介
**Research SEO keywords from a seed term with Keupera and n8n data tables**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/15921

---

# Research SEO keywords from a seed term with Keupera and n8n data tables


## 节点清单

| 节点 | 类型 |
|------|------|
| Wait 10s | 等待 |
| Start workflow | 表单触发器 |
| Create a data table | 数据表 |
| Set Seed Keyword | 数据设置 |
| Perform Keyword Research | HTTP Request |
| Poll Keyword Results | HTTP Request |
| Insert row | 数据表 |
| Split Keywords | Code |
| Completed? | IF 判断 |



## 功能说明

SEO 优化工具，关键词分析和内容优化（Research)表单提交触发，通过 HTTP API 实现自动化。

，通过 HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- 搜索 API Key（如 SerpAPI / Brave Search）

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：9
- 触发方式：表单提交触发

## 触发方式
- Start workflow 触发

## 统计
- 节点总数：9
- 触发节点：1
- 处理节点：6
- 输出节点：2
- 分类：workflow-automation
