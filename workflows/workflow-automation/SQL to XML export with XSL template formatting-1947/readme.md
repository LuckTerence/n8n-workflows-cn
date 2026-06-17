## 简介
**SQL to XML export with XSL template formatting**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/1947

---

# SQL to XML export with XSL template formatting


## 节点清单

| 节点 | 类型 |
|------|------|
| Webhook | Webhook |
| Show 16 random products | MySQL |
| Define file structure | 数据设置 |
| Concatenate Items | 列表操作 |
| Convert to XML | XML |
| Create HTML | HTML |
| Move Binary Data | moveBinaryData |
| Respond to Webhook | 响应 Webhook |
| Get XSLT | HTTP Request |
| Respond to Webhook1 | 响应 Webhook |
| Request xsl template | Webhook |



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

- 节点总数：11
- 触发方式：Webhook 触发

## 触发方式
- Webhook 触发
- Request xsl template 触发

## 统计
- 节点总数：11
- 触发节点：2
- 处理节点：6
- 输出节点：3
- 分类：workflow-automation
