## 简介
**Nano Banana AI Image Editor via Telegram**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：7 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/8082

---

# Nano Banana AI Image Editor via Telegram


## 节点清单

| 节点 | 类型 |
|------|------|
| Photo Message Receiver | Telegram 触发器 |
| Download Telegram Photo | Telegram |
| Convert Photo to Base64 | 从文件提取 |
| Format Image Data URL | Code |
| Parse AI Response Data | 数据设置 |
| Base64 to Binary File | 转换为文件 |
| Send Processed Photo | Telegram |
| Nano Banana Image Processor | HTTP Request |

## 触发方式
- Photo Message Receiver 触发

## 统计
- 节点总数：8
- 触发节点：1
- 处理节点：4
- 输出节点：3
- 分类：workflow-automation
