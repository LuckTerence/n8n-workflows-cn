## 简介
**Automate follower resource distribution on BlueSky with keyword-triggered DMs**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/12159

---

# Automate follower resource distribution on BlueSky with keyword-triggered DMs


## 节点清单

| 节点 | 类型 |
|------|------|
| Schedule Trigger | 定时触发器 |
| BlueSky Auth | HTTP Request |
| Get Notifications | HTTP Request |
| Split Out | 数据拆分 |
| Loop Over Items | 分批处理 |
| Does Follow? | IF 判断 |
| Get Convo ID | HTTP Request |
| Check Follow Status | HTTP Request |
| Send DM | HTTP Request |
| Filter New Only | Code |
| Filter Reply contains | 过滤器 |
| Like the reply | HTTP Request |
| Configuration | 数据设置 |
| Extract Post ID | 数据设置 |



## 功能说明

Automate follower resource distribution on BlueSky。

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

- 节点总数：14
- 触发方式：定时触发

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：14
- 触发节点：1
- 处理节点：7
- 输出节点：6
- 分类：workflow-automation
