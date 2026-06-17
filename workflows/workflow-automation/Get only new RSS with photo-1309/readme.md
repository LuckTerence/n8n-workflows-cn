## 简介
**Get only new RSS with photo**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/1309

---

# Get only new RSS with photo


## 节点清单

| 节点 | 类型 |
|------|------|
| Cron | 定时触发器 |
| RSS Feed Read | RSS Feed |
| Extract Image1 | htmlExtract |
| Filter RSS Data | 数据设置 |
| Only get new RSS1 | Function |



## 功能说明

AI 图像生成工作流，文生图或图生图。

手动触发，通过 工作流编排 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- 通义万相 API Key → https://dashscope.aliyun.com

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：5
- 触发方式：手动或子流程调用

## 触发方式
- Cron 触发
- RSS Feed Read 触发

## 统计
- 节点总数：5
- 触发节点：2
- 处理节点：3
- 输出节点：0
- 分类：workflow-automation
