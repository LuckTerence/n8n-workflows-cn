## 简介
**Get your website indexed by Google automatically**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：14 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/2210

---

# Get your website indexed by Google automatically


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking "Test workflow" | 手动触发 |
| Split Out | 数据拆分 |
| Check status | HTTP Request |
| Loop Over Items | 分批处理 |
| Wait | 等待 |
| URL Updated | HTTP Request |
| Schedule Trigger | 定时触发器 |
| is new? | IF 判断 |
| Get content-specific sitemaps | 数据拆分 |
| Convert sitemap to JSON | XML |
| Force urlset.url to array | 数据设置 |
| Assign mandatiry sitemap fields | 数据设置 |
| convert page data to JSON | XML |
| Get sitemap.xml | HTTP Request |
| Get content of each sitemap | HTTP Request |
| Sort | 数据排序 |

## 触发方式
- When clicking "Test workflow" 触发
- Schedule Trigger 触发

## 统计
- 节点总数：16
- 触发节点：2
- 处理节点：10
- 输出节点：4
- 分类：workflow-automation
