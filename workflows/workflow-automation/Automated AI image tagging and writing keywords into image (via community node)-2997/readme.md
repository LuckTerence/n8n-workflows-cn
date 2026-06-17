## 简介
**Automated AI image tagging and writing keywords into image (via community node)**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Drive)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2997

---

# Automated AI image tagging and writing keywords into image (via community node)


## 节点清单

| 节点 | 类型 |
|------|------|
| Trigger: New file added to Google Drive Folder | Google Drive 触发器 |
| Download Image File | Google Drive |
| Analyze Image Content | OpenAI |
| Merge Metadata and Image File | 数据合并 |
| Write Metadata into Image | exifData |
| Update Image File | Google Drive |



## 功能说明

AI 图像生成工作流，文生图或图生图。

手动触发，通过 HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com
- 通义万相 API Key → https://dashscope.aliyun.com

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：6
- 触发方式：手动或子流程调用

## 触发方式
- Trigger: New file added to Google Drive Folder 触发

## 统计
- 节点总数：6
- 触发节点：1
- 处理节点：5
- 输出节点：0
- 分类：workflow-automation
