## 简介
**Convert n8n tags into folders and move workflows**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3445

---

# Convert n8n tags into folders and move workflows


## 节点清单

| 节点 | 类型 |
|------|------|
| set credentials | 数据设置 |
| login n8n | HTTP Request |
| get tags | HTTP Request |
| my-projects | HTTP Request |
| Split Out | 数据拆分 |
| filter owned projects | 过滤器 |
| Get folders | HTTP Request |
| Split Out2 | 数据拆分 |
| Remove Duplicates | 去重 |
| Loop Over Items | 分批处理 |
| get workflows | n8n |
| Move workflow to folder | HTTP Request |
| Normalize names | 数据设置 |
| Limit1 | 数据限制 |
| Create folders | HTTP Request |
| set folder name + id | 数据设置 |
| set folder name + id1 | 数据设置 |
| set global | 数据设置 |
| Filter | 过滤器 |
| Edit Fields | 数据设置 |
| On form submission | 表单触发器 |
| Code | Code |
| If no folder | IF 判断 |
| If folder exists | IF 判断 |
| set name | 数据设置 |
| end import | 表单 |
| pass all items | 数据设置 |
| select tags to move | 表单 |
| extract name from form | 数据设置 |
| Split Out the tags | 数据拆分 |
| tags to string | 数据设置 |



## 功能说明

n8n 工作流管理工具，编排控制工作流的启停（Tags)表单提交触发，通过 HTTP API 实现自动化。

，通过 HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

无需额外 API Key，导入即可运行。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：31
- 触发方式：表单提交触发

## 触发方式
- On form submission 触发

## 统计
- 节点总数：31
- 触发节点：1
- 处理节点：24
- 输出节点：6
- 分类：workflow-automation
