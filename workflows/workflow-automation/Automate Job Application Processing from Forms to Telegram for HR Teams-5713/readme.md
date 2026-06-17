## 简介
**Automate Job Application Processing from Forms to Telegram for HR Teams**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/5713

---

# Automate Job Application Processing from Forms to Telegram for HR Teams


## 节点清单

| 节点 | 类型 |
|------|------|
| On form submission | 表单触发器 |
| If Have Resume | IF 判断 |
| Edit Fields | 数据设置 |
| Date & Time | 日期时间 |
| Merge | 数据合并 |
| Send a Resume | Telegram |
| Send a Info | Telegram |
| No Operation, do nothing | 空操作 |
| Code | Code |



## 功能说明

Telegram 机器人，消息驱动自动化流程（Job)表单提交触发，通过 Telegram 实现自动化。

，通过 Telegram 通知 实现自动化。

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

- 节点总数：9
- 触发方式：表单提交触发

## 触发方式
- On form submission 触发

## 统计
- 节点总数：9
- 触发节点：1
- 处理节点：6
- 输出节点：2
- 分类：workflow-automation
