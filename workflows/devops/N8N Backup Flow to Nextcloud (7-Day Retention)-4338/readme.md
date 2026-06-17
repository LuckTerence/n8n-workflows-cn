## 简介
**N8N Backup Flow to Nextcloud (7-Day Retention)**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/4338

---

# N8N Backup Flow to Nextcloud (7-Day Retention)


## 节点清单

| 节点 | 类型 |
|------|------|
| On clicking 'execute' | 手动触发 |
| n8n | n8n |
| Loop Over Items | 分批处理 |
| Convert to File | 转换为文件 |
| Backups | 数据排序 |
| Schedule Trigger | 定时触发器 |
| Backup Path | 数据设置 |
| Nextcloud Directory | NextCloud |
| Nextcloud Upload | NextCloud |
| Nextcloud List Dir | NextCloud |
| Limits Backups | Code |
| Nextcloud - Delete old backups | NextCloud |



## 功能说明

自动备份系统，定时备份数据或配置，定时执行。

定时触发、手动触发，通过 工作流编排 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

无需额外 API Key，导入即可运行。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：12
- 触发方式：手动触发, 定时触发

## 触发方式
- On clicking 'execute' 触发
- Schedule Trigger 触发

## 统计
- 节点总数：12
- 触发节点：2
- 处理节点：10
- 输出节点：0
- 分类：devops
