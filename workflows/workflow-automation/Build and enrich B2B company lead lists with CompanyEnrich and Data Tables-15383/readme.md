## 简介
**Build and enrich B2B company lead lists with CompanyEnrich and Data Tables**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：11 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/15383

---

# Build and enrich B2B company lead lists with CompanyEnrich and Data Tables


## 节点清单

| 节点 | 类型 |
|------|------|
| Batch Process Companies | 分批处理 |
| Trigger Search Form | 表单触发器 |
| Post to Company Search API | HTTP Request |
| Split Company Listings | 数据拆分 |
| Post to Company Enrich API | HTTP Request |
| Wait 1 Second | 等待 |
| If Company Duplicate Exists | IF 判断 |
| Skip Processing | 空操作 |
| Filter Enriched Companies | 过滤器 |
| Add Company to Table | 数据表 |
| Verify Company Entry | 数据表 |
| Filter by Company Revenue | 过滤器 |

## 触发方式
- Trigger Search Form 触发

## 统计
- 节点总数：12
- 触发节点：1
- 处理节点：9
- 输出节点：2
- 分类：workflow-automation
