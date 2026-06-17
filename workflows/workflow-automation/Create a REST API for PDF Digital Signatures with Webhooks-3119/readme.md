## 简介
**Create a REST API for PDF Digital Signatures with Webhooks**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3119

---

# Create a REST API for PDF Digital Signatures with Webhooks


## 节点清单

| 节点 | 类型 |
|------|------|
| Validate Key Gen Params | Code |
| Validate PDF Sign Params | Code |
| Validate PDF Upload | Code |
| Validate Key Upload | Code |
| Generate Keys | Code |
| Sign PDF | Code |
| Prepare Success Response | 数据设置 |
| Switch Operation | Switch 路由 |
| Switch Upload Type | Switch 路由 |
| Prepare input params | 数据设置 |
| set file path | 数据设置 |
| Convert PDF to File | 转换为文件 |
| Write PDF File to Disk | 读写文件 |
| Read PDF File from Disk | 读写文件 |
| Convert PFX to File | 转换为文件 |
| Write PFX File to Disk | 读写文件 |
| Read PFX File from Disk | 读写文件 |
| Check PDF file is OK | 数据设置 |
| Check PFX file is OK | 数据设置 |
| check success | IF 判断 |
| set downlowd file info | 数据设置 |
| Read download file from Disk | 读写文件 |
| API POST Endpoint | Webhook |
| API GET Endpoint | Webhook |
| POST Success Response | 响应 Webhook |
| POST Error Response | 响应 Webhook |
| GET Respond to Webhook | 响应 Webhook |



## 功能说明

PDF 文档处理，解析或生成 PDF 文件，Webhook 触发。

Webhook触发，通过 HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

无需额外 API Key，导入即可运行。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：27
- 触发方式：Webhook 触发

## 触发方式
- API POST Endpoint 触发
- API GET Endpoint 触发

## 统计
- 节点总数：27
- 触发节点：2
- 处理节点：22
- 输出节点：3
- 分类：workflow-automation
