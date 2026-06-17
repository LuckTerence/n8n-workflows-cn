## 简介
**Automate Face Swapping for GIFs with Fal.run AI and Google Services**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Google Drive)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/4450

---

# Automate Face Swapping for GIFs with Fal.run AI and Google Services


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Test workflow’ | 手动触发 |
| Get File image | HTTP Request |
| Get Url image | HTTP Request |
| Get status | HTTP Request |
| Google Sheets | Google Sheets |
| Wait 60 sec. | 等待 |
| Schedule Trigger | 定时触发器 |
| Completed? | IF 判断 |
| Upload Image | Google Drive |
| Update result | Google Sheets |
| Set data | 数据设置 |
| Create Image | HTTP Request |



## 功能说明

Automate Face Swapping for GIFs with Fal.run AI an。

定时触发、手动触发，通过 在线表格 + HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- 通义万相 API Key → https://dashscope.aliyun.com

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：12
- 触发方式：手动触发, 定时触发

## 触发方式
- When clicking ‘Test workflow’ 触发
- Schedule Trigger 触发

## 统计
- 节点总数：12
- 触发节点：2
- 处理节点：6
- 输出节点：4
- 分类：workflow-automation
