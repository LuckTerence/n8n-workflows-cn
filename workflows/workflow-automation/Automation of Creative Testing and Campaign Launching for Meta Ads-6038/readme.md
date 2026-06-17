## 简介
**Automation of Creative Testing and Campaign Launching for Meta Ads**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Google Drive)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/6038

---

# Automation of Creative Testing and Campaign Launching for Meta Ads


## 节点清单

| 节点 | 类型 |
|------|------|
| Schedule Trigger | 定时触发器 |
| Files search | Google Drive |
| Download Files | Google Drive |
| Upload Video to FB | HTTP Request |
| Create Video Creative | HTTP Request |
| Is it a Video? | IF 判断 |
| Upload Image to FB | HTTP Request |
| Create Image Creative | HTTP Request |
| Merge Creatives | 数据合并 |
| Create Campaign | HTTP Request |
| Run Once | Function |
| Create Ad Set | HTTP Request |
| Create Ad | HTTP Request |
| Set Video ID | 数据设置 |
| Set Image Hash | 数据设置 |
| Set Image Packet | 数据设置 |
| Set Video Packet | 数据设置 |
| Merge | 数据合并 |
| Save Adset Id | 数据设置 |
| Save Full Report to Sheet | Google Sheets |
| Configuration Meta Ads | 数据设置 |



## 功能说明

Automation of Creative Testing and Campaign Launch。

定时触发，通过 HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- 搜索 API Key（如 SerpAPI / Brave Search）
- 通义万相 API Key → https://dashscope.aliyun.com

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：21
- 触发方式：定时触发

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：21
- 触发节点：1
- 处理节点：13
- 输出节点：7
- 分类：workflow-automation
