## 简介
**Automate PostgreSQL & MySQL Database Management on Linux Servers**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/6134

---

# Automate PostgreSQL & MySQL Database Management on Linux Servers


## 节点清单

| 节点 | 类型 |
|------|------|
| Start | 手动触发 |
| Set Parameters | 数据设置 |
| Database Type Check | IF 判断 |
| PostgreSQL Action Check | IF 判断 |
| MySQL Action Check | IF 判断 |
| Install PostgreSQL | SSH |
| Install MySQL | SSH |
| PostgreSQL Create Check | IF 判断 |
| MySQL Create Check | IF 判断 |
| Create PostgreSQL DB | SSH |
| Create MySQL DB | SSH |
| Delete PostgreSQL DB | SSH |
| Delete MySQL DB | SSH |
| Format Output | 数据设置 |



## 功能说明

内容管理工具，自动生成或发布内容。

手动触发，通过 数据库 实现自动化。

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
- 触发方式：手动触发

## 触发方式
- Start 触发

## 统计
- 节点总数：14
- 触发节点：1
- 处理节点：13
- 输出节点：0
- 分类：devops
