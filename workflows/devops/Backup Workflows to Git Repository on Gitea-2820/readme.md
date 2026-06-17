## 简介
**Backup Workflows to Git Repository on Gitea**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2820

---

# Backup Workflows to Git Repository on Gitea


## 节点清单

| 节点 | 类型 |
|------|------|
| Globals | 数据设置 |
| n8n | n8n |
| Schedule Trigger | 定时触发器 |
| SetDataUpdateNode | 数据设置 |
| SetDataCreateNode | 数据设置 |
| Base64EncodeUpdate | Code |
| Base64EncodeCreate | Code |
| Exist | IF 判断 |
| Changed | IF 判断 |
| PutGitea | HTTP Request |
| GetGitea | HTTP Request |
| PostGitea | HTTP Request |
| ForEach | 分批处理 |



## 功能说明

自动备份系统，定时备份数据或配置，定时执行。

定时触发，通过 HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

无需额外 API Key，导入即可运行。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：13
- 触发方式：定时触发

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：13
- 触发节点：1
- 处理节点：9
- 输出节点：3
- 分类：devops
