## 简介
**Consolidate Data from 5 Sources for Automated Reporting with SQL, MongoDB & Google Tools**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/8890

---

# Consolidate Data from 5 Sources for Automated Reporting with SQL, MongoDB & Google Tools


## 节点清单

| 节点 | 类型 |
|------|------|
| 📄 Google Sheets Source | Google Sheets |
| 🐘 PostgreSQL Source | PostgreSQL |
| 🍃 MongoDB Source | MongoDB |
| ⚙️ Process Merged Data | Function |
| 📊 Final Google Sheet | Google Sheets |
| Add Sheets Source ID | Function |
| Add PostgreSQL Source ID | Function |
| Add SQL Server Source ID | Function |
| Add MongoDB Source ID | Function |
| Add Analytics Source ID | Function |
| Microsoft SQL Server | microsoftSql |
| Google Analytics | Google Analytics |
| Merge | 数据合并 |
| Schedule Trigger | 定时触发器 |



## 功能说明

数据库操作工具，自动查询或写入数据库，定时执行。

定时触发，通过 在线表格 + 数据库 + HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- 数据库连接信息

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：14
- 触发方式：定时触发

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：14
- 触发节点：1
- 处理节点：13
- 输出节点：0
- 分类：workflow-automation
