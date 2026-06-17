## 简介
**Bitrix24 Task Form Widget Application Workflow with Webhook Integration**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2974

---

# Bitrix24 Task Form Widget Application Workflow with Webhook Integration


## 节点清单

| 节点 | 类型 |
|------|------|
| Bitrix24 Handler | Webhook |
| Extract Credentials | 数据设置 |
| Check Event Type | Code |
| Is Installation? | IF 判断 |
| Register Placement | HTTP Request |
| Process Settings | Function |
| Installation Response | 响应 Webhook |
| Has Valid Settings? | IF 判断 |
| Get Task Data | HTTP Request |
| Format Task Data | Function |
| Task View Response | 响应 Webhook |
| Error Response | 响应 Webhook |
| Save Installation Settings | 读写文件 |
| Set Settings Data | 数据设置 |
| Create Settings File | 转换为文件 |
| Read Installation Settings | 读写文件 |
| If Installation finished | IF 判断 |
| Installation finished Response | 响应 Webhook |
| Merge Installation info | 数据合并 |
| Extract Installation Settings | 从文件提取 |
| Merge request data with installation settings | 数据合并 |



## 功能说明

表单问卷工具，自动收集和处理用户反馈，Webhook 触发。

Webhook触发，通过 HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

无需额外 API Key，导入即可运行。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：21
- 触发方式：Webhook 触发

## 触发方式
- Bitrix24 Handler 触发

## 统计
- 节点总数：21
- 触发节点：1
- 处理节点：14
- 输出节点：6
- 分类：workflow-automation
