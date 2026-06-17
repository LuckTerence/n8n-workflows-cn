## 简介
**Extend and Merge UGC Viral Videos Using Kling 2.1, Then Publish on Social Media**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Google Drive)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/11710

---

# Extend and Merge UGC Viral Videos Using Kling 2.1, Then Publish on Social Media


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Execute workflow’ | 手动触发 |
| Completed?1 | IF 判断 |
| Get Last frame | HTTP Request |
| Update video url | Google Sheets |
| Extract last frame | HTTP Request |
| Wait 10 sec. | 等待 |
| Get status Extract Frame | HTTP Request |
| Set params | 数据设置 |
| Completed?5 | IF 判断 |
| Upload Video2 | Google Drive |
| Generate clip | HTTP Request |
| Get status clip | HTTP Request |
| Wait 60 sec. | 等待 |
| Completed? | IF 判断 |
| Set VideoUrls Json | Code |
| Get videos to merge | Google Sheets |
| Get final video file | HTTP Request |
| Get status | HTTP Request |
| Get final video url | HTTP Request |
| Update video url2 | Google Sheets |
| Wait 30 sec. | 等待 |
| Merge Videos | HTTP Request |
| Upload to Postiz | HTTP Request |
| Upload to Social | postiz |
| Upload to Youtube | HTTP Request |
| Get video | Google Sheets |



## 功能说明

AI 视频生成工作流，自动创作视频内容。

手动触发，通过 HTTP API 实现自动化。

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
- 触发方式：手动触发

## 触发方式
- When clicking ‘Execute workflow’ 触发

## 统计
- 节点总数：26
- 触发节点：1
- 处理节点：14
- 输出节点：11
- 分类：workflow-automation
