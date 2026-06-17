# Auto-clip long videos into viral short clips with Vizard AI and social publishing

https://n8nworkflows.xyz/workflows/12054

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
