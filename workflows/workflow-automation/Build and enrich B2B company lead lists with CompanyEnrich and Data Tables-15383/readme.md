## 简介
**Build and enrich B2B company lead lists with CompanyEnrich and Data Tables**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
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



## 功能说明

客户关系管理工具，自动管理销售线索和客户数据（And)表单提交触发，通过 HTTP API 实现自动化。

，通过 HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- 搜索 API Key（如 SerpAPI / Brave Search）

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：12
- 触发方式：表单提交触发

## 触发方式
- Trigger Search Form 触发

## 统计
- 节点总数：12
- 触发节点：1
- 处理节点：9
- 输出节点：2
- 分类：workflow-automation
