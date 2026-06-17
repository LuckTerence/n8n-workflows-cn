## 简介
**Process Telegram Image Albums with Data Tables Cache and NanoBanana AI**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/9288

---

# Process Telegram Image Albums with Data Tables Cache and NanoBanana AI


## 节点清单

| 节点 | 类型 |
|------|------|
| Telegram Trigger | Telegram 触发器 |
| Upsert row(s) | 数据表 |
| Schedule Trigger | 定时触发器 |
| When clicking ‘Execute workflow’ | 手动触发 |
| Filter | 过滤器 |
| Merge | 数据合并 |
| Get a file | Telegram |
| Is media group with images? | IF 判断 |
| Summarize | 文本摘要 |
| Convert to File | 转换为文件 |
| Merge1 | 数据合并 |
| Merge2 | 数据合并 |
| NOOP | 空操作 |
| Latest message in media_group | 文本摘要 |
| Sort | 数据排序 |
| Call NanoBanana via OpenRouter | HTTP Request |
| Extract Base64 | 数据设置 |
| Send processing message | Telegram |
| Send result message | Telegram |
| status:processing | 数据表 |
| status:done | 数据表 |
| Get new requests | 数据表 |
| prepare user messages | 数据设置 |
| parse TG messages | 数据设置 |
| If any new records | 数据表 |
| Send initial notification | Telegram |
| Filter1 | 过滤器 |
| Process other messages as usual | 空操作 |



## 功能说明

Telegram 机器人，消息驱动自动化流程，定时执行。

定时触发、Telegram 消息触发、手动触发，通过 Telegram 通知 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- Telegram Bot Token → @BotFather 创建
- 通义万相 API Key → https://dashscope.aliyun.com

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：28
- 触发方式：Telegram 消息触发, 定时触发, 手动触发

## 触发方式
- Telegram Trigger 触发
- Schedule Trigger 触发
- When clicking ‘Execute workflow’ 触发

## 统计
- 节点总数：28
- 触发节点：3
- 处理节点：20
- 输出节点：5
- 分类：workflow-automation
