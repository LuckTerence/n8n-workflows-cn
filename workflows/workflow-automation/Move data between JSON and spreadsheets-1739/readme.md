## 简介
**Move data between JSON and spreadsheets**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/1739

---

# Move data between JSON and spreadsheets


## 节点清单

| 节点 | 类型 |
|------|------|
| HTTP Request | HTTP Request |
| Google Sheets | Google Sheets |
| Set | 数据设置 |
| Spreadsheet File | 电子表格文件 |
| Spreadsheet File1 | 电子表格文件 |
| Write Binary File | 写入二进制文件 |
| Move Binary Data1 | moveBinaryData |
| Gmail1 | Email 发送 |
| Google Sheets2 | Google Sheets |
| Move Binary Data2 | moveBinaryData |



## 功能说明

Move data between JSON and spreadsheets。

手动触发，通过 邮箱 + 在线表格 + HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- 邮箱 SMTP/IMAP 账号密码

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：10
- 触发方式：手动或子流程调用

## 触发方式
- 手动触发

## 统计
- 节点总数：10
- 触发节点：0
- 处理节点：8
- 输出节点：2
- 分类：workflow-automation
