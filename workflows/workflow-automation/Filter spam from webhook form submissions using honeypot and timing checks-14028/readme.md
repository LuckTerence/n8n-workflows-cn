## 简介
**Filter spam from webhook form submissions using honeypot and timing checks**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/14028

---

# Filter spam from webhook form submissions using honeypot and timing checks


## 节点清单

| 节点 | 类型 |
|------|------|
| Receive Form Submission | Webhook |
| Configure Spam Rules | 数据设置 |
| Detect Spam | Code |
| Is Spam? | IF 判断 |
| Silent OK (Spam Blocked) | 响应 Webhook |
| Forward & Respond (Legit) | 响应 Webhook |

## 触发方式
- Receive Form Submission 触发

## 统计
- 节点总数：6
- 触发节点：1
- 处理节点：3
- 输出节点：2
- 分类：workflow-automation
