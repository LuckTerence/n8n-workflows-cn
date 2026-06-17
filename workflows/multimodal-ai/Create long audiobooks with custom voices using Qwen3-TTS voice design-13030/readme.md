## 简介
**Create long audiobooks with custom voices using Qwen3-TTS voice design**

（待补充中文描述）

> 分类：多模态 AI | 适配等级：A（需替换Google Sheets/Google Drive)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/13030

---

# Create long audiobooks with custom voices using Qwen3-TTS voice design


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Execute workflow’ | 手动触发 |
| Loop Over Items | 分批处理 |
| Get status | HTTP Request |
| Wait 30 sec. | 等待 |
| Get scripts | Google Sheets |
| Update Temp URL | Google Sheets |
| Set AudioUrls Json | Code |
| Merge Audios | HTTP Request |
| Wait 10 sec. | 等待 |
| Completed? | IF 判断 |
| Get final audio url | HTTP Request |
| Get File | HTTP Request |
| Upload Audiobook | Google Drive |
| Voice Design | HTTP Request |



## 功能说明

AI 语音处理工作流，语音合成或转录。

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

- 节点总数：14
- 触发方式：手动触发

## 触发方式
- When clicking ‘Execute workflow’ 触发

## 统计
- 节点总数：14
- 触发节点：1
- 处理节点：8
- 输出节点：5
- 分类：multimodal-ai
