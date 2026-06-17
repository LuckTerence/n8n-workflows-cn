## 简介
**Hostinger Daily VPS Snapshot and server metrics**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3807

---

# Hostinger Daily VPS Snapshot and server metrics


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Test workflow’ | 手动触发 |
| Split Out | 数据拆分 |
| Loop Over Items | 分批处理 |
| Wait 2 seg | 等待 |
| Every day 4:00am | 定时触发器 |
| Hostinger API list VPS | hostingerApi |
| Avaliables VPS | 过滤器 |
| Get VPS Metrics | hostingerApi |
| WhatsApp Message (success) | evolutionApi |
| Create Snapshot | hostingerApi |
| Next VPS | 空操作 |
| WhatsApp Message (error) | evolutionApi |
| Calculate metrics | 数据设置 |



## 功能说明

Hostinger Daily VPS Snapshot and server metrics。

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

- 节点总数：13
- 触发方式：手动触发, 定时触发

## 触发方式
- When clicking ‘Test workflow’ 触发
- Every day 4:00am 触发

## 统计
- 节点总数：13
- 触发节点：2
- 处理节点：11
- 输出节点：0
- 分类：devops
