## 简介
**Index your website using IndexNow and your XML sitemap**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：7 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/13775

---

# Index your website using IndexNow and your XML sitemap


## 节点清单

| 节点 | 类型 |
|------|------|
| Read Sitemap | HTTP Request |
| Parse XML | XML |
| Split Out URLs | 数据拆分 |
| Filter Last Modified Pages | 过滤器 |
| Aggregate URLs | 数据聚合 |
| Send URLs to IndexNow | HTTP Request |
| Configuration | 数据设置 |
| Run Daily Indexing | 定时触发器 |

## 触发方式
- Run Daily Indexing 触发

## 统计
- 节点总数：8
- 触发节点：1
- 处理节点：5
- 输出节点：2
- 分类：workflow-automation
