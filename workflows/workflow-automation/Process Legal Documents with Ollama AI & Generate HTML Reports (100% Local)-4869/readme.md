## 简介
**Process Legal Documents with Ollama AI & Generate HTML Reports (100% Local)**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/4869

---

# Process Legal Documents with Ollama AI & Generate HTML Reports (100% Local)


## 节点清单

| 节点 | 类型 |
|------|------|
| Extract from File | 从文件提取 |
| Local File Trigger | localFileTrigger |
| Read/Write Files from Disk | 读写文件 |
| AI Agent | AI Agent |
| OpenAI Chat Model | OpenAI Chat Model |
| Convert to File | 转换为文件 |
| Read/Write Files from Disk1 | 读写文件 |



## 功能说明

Process Legal Documents with Ollama AI & Generate （AI 增强)手动或子流程调用，通过 n8n 内置节点实现自动化。

手动触发，通过 工作流编排 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：7
- 触发方式：手动或子流程调用

## 触发方式
- Local File Trigger 触发

## 统计
- 节点总数：7
- 触发节点：1
- 处理节点：6
- 输出节点：0
- 分类：workflow-automation
