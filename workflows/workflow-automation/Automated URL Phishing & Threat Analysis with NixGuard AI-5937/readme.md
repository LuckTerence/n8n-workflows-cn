## 简介
**Automated URL Phishing & Threat Analysis with NixGuard AI**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Slack)（基本改完，配置 API Key 应该就能跑）
> 节点数：4 | 难度：⭐ 入门
> 原始来源：https://n8nworkflows.xyz/workflows/5937

---

# Automated URL Phishing & Threat Analysis with NixGuard AI


## 节点清单

| 节点 | 类型 |
|------|------|
| Execute NixGuard & Wazuh Workflow | 执行工作流 |
| Format NixGuard AI Summary & Wazuh Insights | 数据设置 |
| (Optional) Send Slack Alert for High-Risk Events | Slack |
| Webhook Trigger
(REAL-WORLD USE)1 | Webhook |
| Set API Key & Initial Prompt | 数据设置 |

## 触发方式
- Webhook Trigger
(REAL-WORLD USE)1 触发

## 统计
- 节点总数：5
- 触发节点：1
- 处理节点：3
- 输出节点：1
- 分类：workflow-automation
