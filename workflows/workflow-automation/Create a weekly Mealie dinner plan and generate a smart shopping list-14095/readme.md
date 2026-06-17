## 简介
**Create a weekly Mealie dinner plan and generate a smart shopping list**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/14095

---

# Create a weekly Mealie dinner plan and generate a smart shopping list


## 节点清单

| 节点 | 类型 |
|------|------|
| Add Ingredients To Shopping List | HTTP Request |
| Delete Random Meal Plan | HTTP Request |
| Split Removals Array | 数据拆分 |
| Generate Random Meal Plan | HTTP Request |
| Create Shopping List in Mealie | HTTP Request |
| Normalize Recipe Data | Code |
| Fetch Current Week Meal Plans | HTTP Request |
| Send Meal Plan Email | Email 发送 |
| Normalize User Response | Code |
| Check for Removals | IF 判断 |
| Generate Upcoming Week | Code |
| Weekly Schedule Trigger | 定时触发器 |
| Prepare Meal Plan Email Data | Code |
| Fetch Recipe By Slug | HTTP Request |



## 功能说明

电商自动化，订单处理或商品管理，定时执行。

定时触发，通过 邮箱 + HTTP API 实现自动化。

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

- 节点总数：14
- 触发方式：定时触发

## 触发方式
- Weekly Schedule Trigger 触发

## 统计
- 节点总数：14
- 触发节点：1
- 处理节点：6
- 输出节点：7
- 分类：workflow-automation
