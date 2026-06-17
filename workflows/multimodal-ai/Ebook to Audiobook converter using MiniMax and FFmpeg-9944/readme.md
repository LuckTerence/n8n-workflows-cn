## 简介
**Ebook to Audiobook converter using MiniMax and FFmpeg**

（待补充中文描述）

> 分类：多模态 AI | 适配等级：A（需替换Google Drive)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/9944

---

# Ebook to Audiobook converter using MiniMax and FFmpeg


## 节点清单

| 节点 | 类型 |
|------|------|
| Save Audio Chucks | 读写文件 |
| Generate `concat_list.txt` | Code |
| Save concat_list | 读写文件 |
| Join audio chucks and delete all files | 执行命令 |
| read final_merged | 读写文件 |
| FORM | 表单触发器 |
| EXTRACT TEXT | 从文件提取 |
| SPLITS THE TEXT ACCORGING TO RULES | Code |
| Loop Over Text chunks (5) at a time | 分批处理 |
| WAITS FOR 5 SECONDS | 等待 |
| CONVERTS URL TO AUDIO FILES | HTTP Request |
| GIVES INDEXES TO AUDIO FILES | Code |
| Uploads Ebook | Google Drive |
| MINIMAX TTS | HTTP Request |



## 功能说明

AI 语音处理工作流，语音合成或转录（Ebook)表单提交触发，通过 HTTP API 实现自动化。

，通过 HTTP API 实现自动化。

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
- 触发方式：表单提交触发

## 触发方式
- FORM 触发

## 统计
- 节点总数：14
- 触发节点：1
- 处理节点：11
- 输出节点：2
- 分类：multimodal-ai
