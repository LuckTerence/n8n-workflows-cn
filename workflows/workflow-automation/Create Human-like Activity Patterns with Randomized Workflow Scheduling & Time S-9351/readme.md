## 简介
**Create Human-like Activity Patterns with Randomized Workflow Scheduling & Time Slots**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/9351

---

# Create Human-like Activity Patterns with Randomized Workflow Scheduling & Time Slots


## 节点清单

| 节点 | 类型 |
|------|------|
| Execute sub-process | 执行工作流 |
| Get Sub-workflow Name | n8n |
| Append Planning File | 读写文件 |
| Read Planning File | 读写文件 |
| ERROR: Execute Sub-worflow | 停止并报错 |
| Monitoring | Code |
| ERROR: Monitoring | 停止并报错 |
| Schedule Trigger | 定时触发器 |
| Go/no go | Switch 路由 |
| Daily Scheduler | Code |
| Init | Code |
| NOTHING Planned Email | Email 发送 |
| Write Planning File | 读写文件 |
| Send planning | Email 发送 |
| Write Log File | 读写文件 |
| Split Out | 数据拆分 |
| ERROR: Daily Scheduler | 停止并报错 |
| FINAL SUCCESS Email | Email 发送 |
| Read Final Planning File | 读写文件 |
| Loop Over Items | 分批处理 |
| LOOP SUCCESS email | Email 发送 |
| Aggregate | 数据聚合 |
| Return Monitoring Data | Code |
| Merge | 数据合并 |
| Extract from File | 从文件提取 |
| Read Log File | 读写文件 |



## 功能说明

n8n 工作流管理工具，编排控制工作流的启停，定时执行。

定时触发，通过 邮箱 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- 邮箱 SMTP/IMAP 账号密码

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：26
- 触发方式：定时触发

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：26
- 触发节点：1
- 处理节点：21
- 输出节点：4
- 分类：workflow-automation
