# Generate and verify email patterns from chat input with Reoon Email Verifier

https://n8nworkflows.xyz/workflows/16102

## 节点清单

| 节点 | 类型 |
|------|------|
| Loop Over Email Variations | 分批处理 |
| If Score Above 70 | IF 判断 |
| Check Email Status | IF 判断 |
| Notify Chat Success | 聊天 |
| Notify No Email Result | 聊天 |
| Query First Name | 聊天 |
| Query Last Name | 聊天 |
| Query Domain Name | 聊天 |
| Create Email Variations | Code |
| Verify Email with Reoon | HTTP Request |
| Normalize Verification Data | Code |

## 触发方式
- 手动触发

## 统计
- 节点总数：11
- 触发节点：0
- 处理节点：5
- 输出节点：6
- 分类：workflow-automation
