## 简介
**Automated Video Translation & Distribution with DubLab to Multiple Platforms**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/4751

---

# Automated Video Translation & Distribution with DubLab to Multiple Platforms


## 节点清单

| 节点 | 类型 |
|------|------|
| Init Dubbing | HTTP Request |
| Upload Video | HTTP Request |
| Start Dubbing | HTTP Request |
| Fetch Projects | HTTP Request |
| Combine Videos and Languages | Code |
| Proxy Videos | 数据合并 |
| Proxy Ids | 数据合并 |
| Webhook | Webhook |
| Original Video | HTTP Request |
| Dubbed Video | HTTP Request |
| Telegram | Telegram |
| Box | box |
| Dropbox | dropbox |
| YouTube | youTube |
| Postiz | HTTP Request |
| Start | 表单触发器 |

## 触发方式
- Webhook 触发
- Start 触发

## 统计
- 节点总数：16
- 触发节点：2
- 处理节点：6
- 输出节点：8
- 分类：workflow-automation
