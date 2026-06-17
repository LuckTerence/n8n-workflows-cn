## 简介
**Receive and process incoming direct messages in Rocket.Chat**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/15775

---

# Receive and process incoming direct messages in Rocket.Chat


## 节点清单

| 节点 | 类型 |
|------|------|
| Schedule Trigger | 定时触发器 |
| Split Out | 数据拆分 |
| Loop Over Items | 分批处理 |
| Subscription.get | HTTP Request |
| IM.Messages | HTTP Request |
| Split Out1 | 数据拆分 |
| Get last | Code |
| Only Users Prompt | 过滤器 |
| Sort | 数据排序 |
| Unread and Direct Messages | 过滤器 |
| Mark as Read | HTTP Request |
| No Operation, do nothing | 空操作 |
| RocketChat | rocketchat |



## 功能说明

Receive and process incoming direct messages in Ro。

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
- 分类：workflow-automation
