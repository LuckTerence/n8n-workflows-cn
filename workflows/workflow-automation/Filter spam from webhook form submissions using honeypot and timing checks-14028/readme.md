# Filter spam from webhook form submissions using honeypot and timing checks

https://n8nworkflows.xyz/workflows/14028

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
