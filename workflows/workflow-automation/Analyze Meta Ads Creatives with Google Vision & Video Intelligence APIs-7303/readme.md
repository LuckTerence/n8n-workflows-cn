## 简介
**Analyze Meta Ads Creatives with Google Vision & Video Intelligence APIs**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/7303

---

# Analyze Meta Ads Creatives with Google Vision & Video Intelligence APIs


## 节点清单

| 节点 | 类型 |
|------|------|
| Run Daily at 9 AM | 定时触发器 |
| Get Active Ads | facebookGraphApi |
| Is it a Video? | IF 判断 |
| Get Video Source URL | facebookGraphApi |
| Download Video File | HTTP Request |
| Set Campaign ID | 数据设置 |
| Split Out | 数据拆分 |
| Start Video Annotation | HTTP Request |
| If Ready | IF 判断 |
| Parse data | Code |
| Download Image File | HTTP Request |
| Video to Base64 String | 从文件提取 |
| Image to Base64 String | 从文件提取 |
| Start Image Annotation | HTTP Request |
| Set id data for Static | 数据设置 |
| Set id data for Video | 数据设置 |
| Parse data from images | Code |
| Has image_url? | IF 判断 |
| Loop for videos | 分批处理 |
| Add errors | Google Sheets |
| Check Operation Status | HTTP Request |
| Add Segments data | Google Sheets |
| Set (Video Error Row) | 数据设置 |
| Wait 3s | 等待 |
| Wait 30s | 等待 |
| Set (Error Row) | 数据设置 |



## 功能说明

AI 视频生成工作流，自动创作视频内容，定时执行。

定时触发，通过 在线表格 + HTTP API 实现自动化。

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

- 节点总数：26
- 触发方式：定时触发

## 触发方式
- Run Daily at 9 AM 触发

## 统计
- 节点总数：26
- 触发节点：1
- 处理节点：20
- 输出节点：5
- 分类：workflow-automation
