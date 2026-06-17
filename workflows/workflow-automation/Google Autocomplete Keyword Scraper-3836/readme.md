## 简介
**Google Autocomplete Keyword Scraper**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Drive)（基本改完，配置 API Key 应该就能跑）
> 节点数：7 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/3836

---

# Google Autocomplete Keyword Scraper


## 节点清单

| 节点 | 类型 |
|------|------|
| Generate A-Z Queries | Code |
| Google Autocomplete | HTTP Request |
| Loop Over Items | 分批处理 |
| Wait 1s | 等待 |
| Code | Code |
| Get Keyword | Chat 触发器 |
| Extract Keywords | Code |
| Return Keywords | 响应 Webhook |

## 触发方式
- Get Keyword 触发

## 统计
- 节点总数：8
- 触发节点：1
- 处理节点：5
- 输出节点：2
- 分类：workflow-automation
