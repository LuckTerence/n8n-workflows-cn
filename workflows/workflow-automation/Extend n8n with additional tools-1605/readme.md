## 简介
**Extend n8n with additional tools**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/1605

---

# Extend n8n with additional tools


## 节点清单

| 节点 | 类型 |
|------|------|
| Switch | Switch 路由 |
| msg_greet | Telegram |
| msg_wrongcommand | Telegram |
| Telegram Trigger | Telegram 触发器 |
| msg_getweather | Telegram |
| City List | Function |
| Convert API response | Function |
| Get weather data | HTTP Request |
| Spreadsheet File | 电子表格文件 |
| Write csv | 写入二进制文件 |
| Filename | 数据设置 |
| msg_errorAPI | Telegram |
| Any errors API? | IF 判断 |
| msg_errorR | Telegram |
| Read Binary File | 读取二进制文件 |
| R successful? | IF 判断 |
| Merge | 数据合并 |
| Merge1 | 数据合并 |
| msg_pleasewait | Telegram |
| Merge2 | 数据合并 |
| Run R script | 执行命令 |



## 功能说明

Extend n8n with additional tools。

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

- 节点总数：21
- 触发方式：Telegram 消息触发

## 触发方式
- Telegram Trigger 触发

## 统计
- 节点总数：21
- 触发节点：1
- 处理节点：13
- 输出节点：7
- 分类：workflow-automation
