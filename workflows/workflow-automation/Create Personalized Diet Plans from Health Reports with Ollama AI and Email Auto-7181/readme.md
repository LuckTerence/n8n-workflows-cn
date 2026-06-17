## 简介
**Create Personalized Diet Plans from Health Reports with Ollama AI and Email Automation**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/7181

---

# Create Personalized Diet Plans from Health Reports with Ollama AI and Email Automation


## 节点清单

| 节点 | 类型 |
|------|------|
| Receive Health Report Email | Email 读取 |
| Process Report with AI Nutrition Engine | LLM Chain |
| AI Nutrition Model | lmOllama |
| Wait Before Sending Plan  | 等待 |
| Send Personalized Diet Plan  | Email 发送 |

## 触发方式
- 手动触发

## 统计
- 节点总数：5
- 触发节点：0
- 处理节点：3
- 输出节点：2
- 分类：workflow-automation
