## 简介
**Call Center Analytics with Dual-AI Verification using DeepSeek Models**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Gmail)（基本改完，配置 API Key 应该就能跑）
> 节点数：6 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/5658

---

# Call Center Analytics with Dual-AI Verification using DeepSeek Models


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Test workflow’ | 手动触发 |
| HTTP Request | HTTP Request |
| Report | LLM Chain |
| DeepSeek Reasonning | lmChatDeepSeek |
| DeepSeek Chat | lmChatDeepSeek |
| Example data | Code |
| Webhook | Webhook |
| Recheck | LLM Chain |

## 触发方式
- When clicking ‘Test workflow’ 触发
- Webhook 触发

## 统计
- 节点总数：8
- 触发节点：2
- 处理节点：5
- 输出节点：1
- 分类：workflow-automation
