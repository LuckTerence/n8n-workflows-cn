## 简介
**Control Your n8n Instance Remotely with Telegram Bot Commands**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/4928

---

# Control Your n8n Instance Remotely with Telegram Bot Commands


## 节点清单

| 节点 | 类型 |
|------|------|
| Telegram Trigger | Telegram 触发器 |
| Cmd Parse | 数据设置 |
| Cmd Switch | Switch 路由 |
| Execute Arg | IF 判断 |
| Activate Workflow | n8n |
| Deactivate Workflow | n8n |
| Activate Arg | IF 判断 |
| Deactivate Arg | IF 判断 |
| Arg Error | Telegram |
| Cmd Error | Telegram |
| Executed | Telegram |
| Activated | Telegram |
| Deactivated | Telegram |
| Workflow Name Error | Telegram |
| List Workflows 1 | n8n |
| List Workflows 2 | n8n |
| List Workflows 3 | n8n |
| If Inactive | IF 判断 |
| If Active | IF 判断 |
| Workflow Active Error | Telegram |
| Workflow Inactive Error | Telegram |
| List Workflows | n8n |
| Help | Telegram |
| Workflow List | 数据设置 |
| Workflows | Telegram |
| Workflow Found 1 | IF 判断 |
| Workflow Found 2 | IF 判断 |
| Workflow Found 3 | IF 判断 |
| Not Archived | 过滤器 |
| Find Workflow 1 | 过滤器 |
| Find Workflow 2 | 过滤器 |
| Find Workflow 3 | 过滤器 |
| Executions Arg | IF 判断 |
| List Workflows 4 | n8n |
| Find Workflow 4 | 过滤器 |
| Workflow Found 4 | IF 判断 |
| List Workflow Executions | n8n |
| Executions Fields | 数据设置 |
| Executions | Telegram |
| Executions Message | Code |
| Workflows Message | Code |
| Execute Workflow | 执行工作流 |
| Execution Error | Telegram |
| Activation Error | Telegram |
| Deactivation Error | Telegram |
| List Archived | n8n |
| Only Archived | 过滤器 |
| Archived Message | Code |
| Cleanup | Telegram |
| Archived List | 数据设置 |
| Delete Archived | n8n |
| Backup Workflows | 执行命令 |
| Backup Credentials | 执行命令 |
| Backup Tarball | 执行命令 |
| Backup | Telegram |
| Cleanup Files | 执行命令 |
| Read File | 读写文件 |
| Backup Error | Telegram |
| Telegram Nodes | Telegram |
| n8n Nodes | n8n |
| Error Trigger | 错误触发器 |
| If not manual exec | IF 判断 |
| n8n Started Trigger | n8nTrigger |
| Workflow Error Msg | Telegram |
| n8n Started Msg | Telegram |



## 功能说明

Telegram 机器人，消息驱动自动化流程。

Telegram 消息触发，通过 Telegram 通知 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- Telegram Bot Token → @BotFather 创建

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：65
- 触发方式：Telegram 消息触发

## 触发方式
- Telegram Trigger 触发
- Error Trigger 触发
- n8n Started Trigger 触发

## 统计
- 节点总数：65
- 触发节点：3
- 处理节点：42
- 输出节点：20
- 分类：workflow-automation
