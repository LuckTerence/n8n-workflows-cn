## 简介
**Compare Flight Fares from Skyscanner, Air India & More with Email Alerts**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（需替换Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/6054

---

# Compare Flight Fares from Skyscanner, Air India & More with Email Alerts


## 节点清单

| 节点 | 类型 |
|------|------|
| Skyscanner API | HTTP Request |
| Air India API | HTTP Request |
| IndiGo API | HTTP Request |
| Akasa Air API | HTTP Request |
| Set Schedule | 定时触发器 |
| Set Input Data | 数据设置 |
| Merge API Data | 数据合并 |
| Merge Both API Data | 数据合并 |
| Merge All API Results | 数据合并 |
| Compare Data and Sorting Price | Function |
| Send Response via Email | Email 发送 |



## 功能说明

邮件自动化处理，AI 分类整理或。

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

- 节点总数：11
- 触发方式：定时触发

## 触发方式
- Set Schedule 触发

## 统计
- 节点总数：11
- 触发节点：1
- 处理节点：5
- 输出节点：5
- 分类：devops
