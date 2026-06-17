## 简介
**Retry on fail except for known error**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2719

---

# Retry on fail except for known error


## 节点清单

| 节点 | 类型 |
|------|------|
| Retry limit reached | 停止并报错 |
| Set tries | 数据设置 |
| Update tries | 数据设置 |
| Wait | 等待 |
| Catch known error | IF 判断 |
| Replace Me | 空操作 |
| Success | 空操作 |
| Known Error | 空操作 |
| Manual Trigger | 手动触发 |
| If tries left | IF 判断 |



## 功能说明

Retry on fail except for known error。

手动触发，通过 工作流编排 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

无需额外 API Key，导入即可运行。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：10
- 触发方式：手动触发

## 触发方式
- Manual Trigger 触发

## 统计
- 节点总数：10
- 触发节点：1
- 处理节点：9
- 输出节点：0
- 分类：workflow-automation
