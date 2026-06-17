## 简介
**Automate NPM Package Installation and Updates for Self-Hosted Environments**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3293

---

# Automate NPM Package Installation and Updates for Self-Hosted Environments


## 节点清单

| 节点 | 类型 |
|------|------|
| libraries_set | 数据设置 |
| trigger_manual | 手动触发 |
| libraries_array | 数据设置 |
| libraries_split | 数据拆分 |
| library_install | 执行命令 |
| trigger_schedule | 定时触发器 |
| trigger_instance | n8nTrigger |



## 功能说明

Automate NPM Package Installation and Updates for。

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

- 节点总数：7
- 触发方式：手动触发, 定时触发

## 触发方式
- trigger_manual 触发
- trigger_schedule 触发
- trigger_instance 触发

## 统计
- 节点总数：7
- 触发节点：3
- 处理节点：4
- 输出节点：0
- 分类：workflow-automation
