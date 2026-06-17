## 简介
**MFA Multi-factor authentication (Voice call and Email) with ClickSend and SMTP**

（待补充中文描述）

> 分类：多模态 AI | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：12 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/3142

---

# MFA Multi-factor authentication (Voice call and Email) with ClickSend and SMTP


## 节点清单

| 节点 | 类型 |
|------|------|
| Send Voice | HTTP Request |
| On form submission | 表单触发器 |
| Send Email | Email 发送 |
| Code for voice | Code |
| Set voice code | 数据设置 |
| Verify voice code | 表单 |
| Fail voice code | 表单 |
| Set email code | 数据设置 |
| Verify email code | 表单 |
| Is email code correct? | IF 判断 |
| Is voice code correct? | IF 判断 |
| Success | 表单 |
| Fail email code | 表单 |

## 触发方式
- On form submission 触发

## 统计
- 节点总数：13
- 触发节点：1
- 处理节点：10
- 输出节点：2
- 分类：multimodal-ai
