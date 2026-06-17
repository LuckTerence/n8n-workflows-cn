## 简介
**Auto-clip long videos into viral short clips with Vizard AI and social publishing**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets)（基本改完，配置 API Key 应该就能跑）
> 节点数：12 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/12054

---

# Auto-clip long videos into viral short clips with Vizard AI and social publishing


## 节点清单

| 节点 | 类型 |
|------|------|
| Configuration | 数据设置 |
| Get Status | HTTP Request |
| Wait | 等待 |
| Check Status | Switch 路由 |
| Split Clips | 数据拆分 |
| On form submission | 表单触发器 |
| Filter by Viral Score | 过滤器 |
| Append Source (Success) | Google Sheets |
| Append Source (Failed) 2 | Google Sheets |
| Append Source (Failed)  | Google Sheets |
| AI Clipper | HTTP Request |
| Success? | IF 判断 |
| Post to Tiktok | HTTP Request |

## 触发方式
- On form submission 触发

## 统计
- 节点总数：13
- 触发节点：1
- 处理节点：9
- 输出节点：3
- 分类：workflow-automation
