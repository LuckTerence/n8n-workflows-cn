## 简介
**3D手办生成**

Midjourney+GPT-4o生成3D模型多视角图

> 分类：多模态 AI | 适配等级：A-adapted（AI模型已适配，部分外服节点需手动替换为国内服务）
> 原始来源：https://n8nworkflows.xyz/workflows/3628

---

# 3D手办生成


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Test workflow’ | 手动触发 |
| Midjourney Generator | HTTP Request |
| Get Midjourney URL | HTTP Request |
| Verify URL Acquisition | IF 判断 |
| Wait for Generation | 等待 |
| Get Random Image URL | Code |
| Generation 3-view Image with GPT-4o-Image | HTTP Request |
| Check if the URL is obtained | IF 判断 |
| Get Final Output | Code |
| Get Image | Code |

## 触发方式
- When clicking ‘Test workflow’ 触发

## 统计
- 节点总数：10
- 触发节点：1
- 处理节点：6
- 输出节点：3
- 分类：multimodal-ai
