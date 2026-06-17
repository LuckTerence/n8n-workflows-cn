## 简介
**Bulk AI Video Generation with Freepik Minimax Hailuo & Google Suite Integration**

（待补充中文描述）

> 分类：多模态 AI | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/7335

---

# Bulk AI Video Generation with Freepik Minimax Hailuo & Google Suite Integration


## 节点清单

| 节点 | 类型 |
|------|------|
| Download Video as Base64 | HTTP Request |
| Upload to Google Drive1 | Google Drive |
| Create Video | HTTP Request |
| Get Video URL | HTTP Request |
| Switch | Switch 路由 |
| Wait | 等待 |
| Duplicate Rows2 | Code |
| Loop Over Items | 分批处理 |
| Get prompt from google sheet | Google Sheets |

## 触发方式
- 手动触发

## 统计
- 节点总数：9
- 触发节点：0
- 处理节点：6
- 输出节点：3
- 分类：multimodal-ai
