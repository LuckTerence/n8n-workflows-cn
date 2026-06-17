## 简介
**Clone Voices from Text to Speech with Zyphra Zonos API**

（待补充中文描述）

> 分类：多模态 AI | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/5448

---

# Clone Voices from Text to Speech with Zyphra Zonos API


## 节点清单

| 节点 | 类型 |
|------|------|
| Webhook Trigger | Webhook |
| Set Clone Parameters | 数据设置 |
| Read Sample Voice | 读写文件 |
| Check File Loaded | IF 判断 |
| Call Zyphra Clone API | HTTP Request |
| Save Cloned Audio | 读写文件 |
| Success Response | 数据设置 |
| File Error Response | 数据设置 |
| API Error Response | 数据设置 |
| Webhook Response | 响应 Webhook |
| Base64 convertor | Code |

## 触发方式
- Webhook Trigger 触发

## 统计
- 节点总数：11
- 触发节点：1
- 处理节点：8
- 输出节点：2
- 分类：multimodal-ai
