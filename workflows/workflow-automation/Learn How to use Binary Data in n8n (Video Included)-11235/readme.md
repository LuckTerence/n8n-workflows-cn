## 简介
**Learn How to use Binary Data in n8n (Video Included)**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Drive)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/11235

---

# Learn How to use Binary Data in n8n (Video Included)


## 节点清单

| 节点 | 类型 |
|------|------|
| Edit Fields | 数据设置 |
| Edit Fields1 | 数据设置 |
| Extract from File | 从文件提取 |
| Extract text | mistralAi |
| Analyze an image | OpenAI Chat Model |
| Convert to File | 转换为文件 |
| Google Drive Trigger | Google Drive 触发器 |
| Convert to File2 | 转换为文件 |
| Edit Fields2 | 数据设置 |
| On form submission1 | 表单触发器 |
| FTP | FTP |
| Upload file | Google Drive |
| Edit Image | 图片编辑 |
| When clicking ‘Execute workflow’ | 手动触发 |
| On form submission | 表单触发器 |



## 功能说明

AI 视频生成工作流，自动创作视频内容（Learn)表单提交触发、手动触发，通过 HTTP API 实现自动化。

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

- 节点总数：15
- 触发方式：表单提交触发, 手动触发

## 触发方式
- Google Drive Trigger 触发
- On form submission1 触发
- When clicking ‘Execute workflow’ 触发
- On form submission 触发

## 统计
- 节点总数：15
- 触发节点：4
- 处理节点：11
- 输出节点：0
- 分类：workflow-automation
