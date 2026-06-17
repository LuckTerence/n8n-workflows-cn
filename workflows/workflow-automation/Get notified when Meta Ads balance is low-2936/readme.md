## 简介
**Get notified when Meta Ads balance is low**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2936

---

# Get notified when Meta Ads balance is low


## 节点清单

| 节点 | 类型 |
|------|------|
| Every 12h | 定时触发器 |
| No Operation, do nothing | 空操作 |
| Edit Fields1 | 数据设置 |
| Edit Fields | 数据设置 |
| Lower than 400 ? | IF 判断 |
| Send message | Telegram |
| Method 2 | facebookGraphApi |
| Method 1 | facebookGraphApi |



## 功能说明

通知推送系统，多渠道消息分发，定时执行。

定时触发，通过 Telegram 通知 实现自动化。

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

- 节点总数：8
- 触发方式：定时触发

## 触发方式
- Every 12h 触发

## 统计
- 节点总数：8
- 触发节点：1
- 处理节点：6
- 输出节点：1
- 分类：workflow-automation
