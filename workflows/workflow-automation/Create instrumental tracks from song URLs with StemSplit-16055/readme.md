## 简介
**Create instrumental tracks from song URLs with StemSplit**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Drive/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/16055

---

# Create instrumental tracks from song URLs with StemSplit


## 节点清单

| 节点 | 类型 |
|------|------|
| On karaoke form submission | 表单触发器 |
| Normalize form data | 数据设置 |
| Is song URL valid? | IF 判断 |
| StemSplit: check credits | stemSplit |
| Enough StemSplit credits? | IF 判断 |
| StemSplit: create instrumental | stemSplit |
| Download instrumental MP3 | HTTP Request |
| Upload to Google Drive | Google Drive |
| Gmail: send download link | Email 发送 |
| Gmail: invalid URL notice | Email 发送 |
| Gmail: insufficient credits | Email 发送 |



## 功能说明

Create instrumental tracks from song URLs with Ste（自动化)表单提交触发，通过 邮箱 + HTTP API 实现自动化。

，通过 邮箱 + HTTP API 实现自动化。

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

- 节点总数：11
- 触发方式：表单提交触发

## 触发方式
- On karaoke form submission 触发

## 统计
- 节点总数：11
- 触发节点：1
- 处理节点：6
- 输出节点：4
- 分类：workflow-automation
