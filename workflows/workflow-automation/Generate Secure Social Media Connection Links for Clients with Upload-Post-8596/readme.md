## 简介
**Generate Secure Social Media Connection Links for Clients with Upload-Post**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Gmail)（基本改完，配置 API Key 应该就能跑）
> 节点数：4 | 难度：⭐ 入门
> 原始来源：https://n8nworkflows.xyz/workflows/8596

---

# Generate Secure Social Media Connection Links for Clients with Upload-Post


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Execute workflow’ | 手动触发 |
| Create user | uploadPost |
| Generate jwt for platform integration | uploadPost |
| Send a text message | Telegram |
| On form submission | 表单触发器 |
| Upload a video | uploadPost |

## 触发方式
- When clicking ‘Execute workflow’ 触发
- On form submission 触发

## 统计
- 节点总数：6
- 触发节点：2
- 处理节点：3
- 输出节点：1
- 分类：workflow-automation
