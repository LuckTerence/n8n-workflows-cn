## 简介
**Automated Rsync Backup with Password Auth & Alert System**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/9873

---

# Automated Rsync Backup with Password Auth & Alert System


## 节点清单

| 节点 | 类型 |
|------|------|
| Manual Trigger | 手动触发 |
| Server Parameters | 数据设置 |
| Check Sshpass Local | 执行命令 |
| Is Installed Local? | IF 判断 |
| Install Sshpass Local | 执行命令 |
| Check Sshpass on Source | 执行命令 |
| Is Installed on Source? | IF 判断 |
| Install Sshpass on Source | 执行命令 |
| Execute Rsync Backup | 执行命令 |
| Success? | IF 判断 |
| Backup Successful | 数据设置 |
| Backup Failed | 数据设置 |
| Process Finish Report --- Telegam & SMS | 执行命令 |
| Schedule Trigger | 定时触发器 |



## 功能说明

监控告警系统，异常检测并发送通知，定时执行。

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

- 节点总数：14
- 触发方式：手动触发, 定时触发

## 触发方式
- Manual Trigger 触发
- Schedule Trigger 触发

## 统计
- 节点总数：14
- 触发节点：2
- 处理节点：12
- 输出节点：0
- 分类：devops
