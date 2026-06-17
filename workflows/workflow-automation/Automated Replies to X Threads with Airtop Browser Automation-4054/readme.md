## 简介
**Automated Replies to X Threads with Airtop Browser Automation**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/4054

---

# Automated Replies to X Threads with Airtop Browser Automation


## 节点清单

| 节点 | 类型 |
|------|------|
| When Executed by Another Workflow | 执行工作流触发器 |
| Session | Airtop |
| Window | Airtop |
| Type response | Airtop |
| Wait 8 secs | 等待 |
| On form submission | 表单触发器 |
| Parameters | 数据设置 |
| Click Reply button | Airtop |
| Terminate session | Airtop |
| Post-action screenshot | Airtop |



## 功能说明

AI 招聘助手，简历筛选或面试流程自动化（Replies)表单提交触发，通过 n8n 内置节点实现自动化。

，通过 工作流编排 实现自动化。

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
- 触发方式：表单提交触发

## 触发方式
- When Executed by Another Workflow 触发
- On form submission 触发

## 统计
- 节点总数：10
- 触发节点：2
- 处理节点：8
- 输出节点：0
- 分类：workflow-automation
