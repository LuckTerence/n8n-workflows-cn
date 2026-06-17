## 简介
**Smart Email Draft Generator**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/5196

---

# Smart Email Draft Generator


## 节点清单

| 节点 | 类型 |
|------|------|
| Check New Email (IMAP) | Email 读取 |
| Process Email with AI | LLM Chain |
| Custom AI Model | lmOllama |
| Prepare Email Content | 数据设置 |
| Save as Gmail Draft | Email 发送 |

## 触发方式
- 手动触发

## 统计
- 节点总数：5
- 触发节点：0
- 处理节点：3
- 输出节点：2
- 分类：workflow-automation
