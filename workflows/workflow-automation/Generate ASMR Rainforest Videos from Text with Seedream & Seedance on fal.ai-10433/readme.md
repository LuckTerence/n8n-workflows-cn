## 简介
**Generate ASMR Rainforest Videos from Text with Seedream & Seedance on fal.ai**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/10433

---

# Generate ASMR Rainforest Videos from Text with Seedream & Seedance on fal.ai


## 节点清单

| 节点 | 类型 |
|------|------|
| manual-workflow | 手动触发 |
| create-image | HTTP Request |
| wait-10s | 等待 |
| get-status-image | HTTP Request |
| is-image-complete | IF 判断 |
| create-video | HTTP Request |
| wait-30s | 等待 |
| get-status-video | HTTP Request |
| is-video-complete | IF 判断 |
| link-video | HTTP Request |
| prompt | 数据设置 |
| download-video | HTTP Request |
| link-image | HTTP Request |



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

- 节点总数：13
- 触发方式：手动触发

## 触发方式
- manual-workflow 触发

## 统计
- 节点总数：13
- 触发节点：1
- 处理节点：5
- 输出节点：7
- 分类：workflow-automation
