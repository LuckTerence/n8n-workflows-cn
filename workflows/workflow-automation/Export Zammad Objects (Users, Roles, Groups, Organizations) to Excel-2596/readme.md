## 简介
**Export Zammad Objects (Users, Roles, Groups, Organizations) to Excel**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2596

---

# Export Zammad Objects (Users, Roles, Groups, Organizations) to Excel


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Test workflow’ | 手动触发 |
| Zammad Univeral User Object | 数据设置 |
| Zammad Univeral Organization Object | 数据设置 |
| Zammad Univeral Role Object | 数据设置 |
| Get all Organizations | zammad |
| Get all Roles | HTTP Request |
| Convert to Excel Organizations | 转换为文件 |
| Convert to Excel Roles | 转换为文件 |
| Convert to Excel Users | 转换为文件 |
| Get all Users | zammad |
| Zammad Univeral Group Object | 数据设置 |
| Get all Groups | HTTP Request |
| If | IF 判断 |
| Basic Variables | 数据设置 |
| Convert to Excel Groups | 转换为文件 |
| Filter Groups if needed | IF 判断 |
| Filter Roles if needed | IF 判断 |
| Filter Organizations if needed | IF 判断 |



## 功能说明

Export Zammad Objects (Users、Roles、Groups、Organ。

手动触发，通过 HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

无需额外 API Key，导入即可运行。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：18
- 触发方式：手动触发

## 触发方式
- When clicking ‘Test workflow’ 触发

## 统计
- 节点总数：18
- 触发节点：1
- 处理节点：15
- 输出节点：2
- 分类：workflow-automation
