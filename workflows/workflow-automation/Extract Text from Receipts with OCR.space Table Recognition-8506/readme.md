## 简介
**Extract Text from Receipts with OCR.space Table Recognition**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/8506

---

# Extract Text from Receipts with OCR.space Table Recognition


## 节点清单

| 节点 | 类型 |
|------|------|
| Trigger • Upload image for OCR | 表单触发器 |
| Prepare • Normalize inputs | 数据设置 |
| OCR.space • Parse image | HTTP Request |
| Display • Show OCR text | 表单 |



## 功能说明

数据采集工具，自动抓取网页或 API 数据（Text)表单提交触发，通过 HTTP API 实现自动化。

，通过 HTTP API 实现自动化。

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

- 节点总数：4
- 触发方式：表单提交触发

## 触发方式
- Trigger • Upload image for OCR 触发

## 统计
- 节点总数：4
- 触发节点：1
- 处理节点：2
- 输出节点：1
- 分类：workflow-automation
