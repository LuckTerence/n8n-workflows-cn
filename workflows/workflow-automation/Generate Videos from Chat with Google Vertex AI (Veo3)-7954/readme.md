## 简介
**Generate Videos from Chat with Google Vertex AI (Veo3)**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Slack/Google Drive)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/7954

---

# Generate Videos from Chat with Google Vertex AI (Veo3)


## 节点清单

| 节点 | 类型 |
|------|------|
| Wait | 等待 |
| Poll for Video | HTTP Request |
| Edit Fields | 数据设置 |
| Convert to File | 转换为文件 |
| Post Veo3 Fast | HTTP Request |
| If | IF 判断 |
| Wait1 | 等待 |
| When chat message received | Chat 触发器 |

## 触发方式
- When chat message received 触发

## 统计
- 节点总数：8
- 触发节点：1
- 处理节点：5
- 输出节点：2
- 分类：workflow-automation
