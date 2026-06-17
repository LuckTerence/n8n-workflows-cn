## 简介
**Convert boring images to stunning photos and videos**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：8 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/4275

---

# Convert boring images to stunning photos and videos


## 节点清单

| 节点 | 类型 |
|------|------|
| Telegram Bot Trigger | Telegram 触发器 |
| Edit Image (OpenAI) | HTTP Request |
| Convert to Binary Image | 转换为文件 |
| Send Edited Image | Telegram |
| Generate Variation (Replicate) | HTTP Request |
| Retrieve Generated Image | HTTP Request |
| Send Variation Image | Telegram |
| Get File Path | HTTP Request |
| Wait for Processing | 等待 |

## 触发方式
- Telegram Bot Trigger 触发

## 统计
- 节点总数：9
- 触发节点：1
- 处理节点：2
- 输出节点：6
- 分类：workflow-automation
