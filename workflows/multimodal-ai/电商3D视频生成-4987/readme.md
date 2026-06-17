## 简介
**电商3D视频生成**

2D图片生成3D产品展示视频

> 分类：多模态 AI | 适配等级：A（需替换Google Sheets/Google Drive/Gmail)（AI模型已适配，部分外服节点需手动替换为国内服务）
> 原始来源：https://n8nworkflows.xyz/workflows/4987

---

# 电商3D视频生成


## 节点清单

| 节点 | 类型 |
|------|------|
| Wait | 等待 |
| On Form Submission | 表单触发器 |
| Give Access to folder | Google Drive |
| Get Image File | Code |
| Upload Remove BG image | Google Drive |
| Extract Image ID from URL | Code |
| Upload Video | Google Drive |
| Create Folder | Google Drive |
| Create Slug | Code |
| Create Video | HTTP Request |
| Check Video Status | HTTP Request |
| Get Video Link | HTTP Request |
| Remove Image Background | HTTP Request |
| Upload Original Image | Google Drive |
| Insert New Product | Google Sheets |
| Update Remove BG URL | Google Sheets |
| Is In Progress | IF 判断 |
| Convert to Binary File | HTTP Request |
| Update Video Link | Google Sheets |
| Send E-Mail Notification | Gmail |



## 功能说明

AI 视频生成工作流，自动创作视频内容（电商3D视频生成)表单提交触发，通过 邮箱 + HTTP API 实现自动化。

，通过 邮箱 + HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- 邮箱 SMTP/IMAP 账号密码
- 通义万相 API Key → https://dashscope.aliyun.com

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：20
- 触发方式：表单提交触发

## 触发方式
- On Form Submission 触发

## 统计
- 节点总数：20
- 触发节点：1
- 处理节点：14
- 输出节点：5
- 分类：multimodal-ai
