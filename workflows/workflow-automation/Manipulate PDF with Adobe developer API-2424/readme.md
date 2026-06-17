## 简介
**Manipulate PDF with Adobe developer API**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2424

---

# Manipulate PDF with Adobe developer API


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Test workflow’ | 手动触发 |
| Create Asset | HTTP Request |
| Execute Workflow Trigger | 执行工作流触发器 |
| Adobe API Query | 数据设置 |
| Load a test pdf file | dropbox |
| Query + File | 数据合并 |
| Query + File + Asset information | 数据合并 |
| Process Query | HTTP Request |
| Wait 5 second | 等待 |
| Try to download the result | HTTP Request |
| Switch | Switch 路由 |
| Forward response to origin workflow | 数据设置 |
| Authenticartion (get token) | HTTP Request |
| Upload PDF File (asset) | HTTP Request |



## 功能说明

PDF 文档处理，解析或生成 PDF 文件。

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

- 节点总数：14
- 触发方式：手动触发

## 触发方式
- When clicking ‘Test workflow’ 触发
- Execute Workflow Trigger 触发

## 统计
- 节点总数：14
- 触发节点：2
- 处理节点：7
- 输出节点：5
- 分类：workflow-automation
