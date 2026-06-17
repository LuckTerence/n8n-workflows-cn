## 简介
**Scrape Latest 20 TechCrunch Articles**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：8 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/2832

---

# Scrape Latest 20 TechCrunch Articles


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Test workflow’ | 手动触发 |
| Request Techcrunsh Latest Page | HTTP Request |
| Parse a posts box | HTML |
| Parse all posts | HTML |
| split out the posts | 数据拆分 |
| Parse each post in detail | HTML |
| Request a post detail page | HTTP Request |
| Parse a post's content and metadata | HTML |
| Save the values | 数据设置 |

## 触发方式
- When clicking ‘Test workflow’ 触发

## 统计
- 节点总数：9
- 触发节点：1
- 处理节点：6
- 输出节点：2
- 分类：workflow-automation
