## 简介
**Complete LAMP Stack (Linux, Apache, MySQL, PHP) Automated Server Setup**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/6136

---

# Complete LAMP Stack (Linux, Apache, MySQL, PHP) Automated Server Setup


## 节点清单

| 节点 | 类型 |
|------|------|
| Start | 手动触发 |
| Set Parameters | 数据设置 |
| System Preparation | SSH |
| Install Apache | SSH |
| Install MySQL | SSH |
| Install PHP | SSH |
| Install Dev Tools | SSH |
| Create Dev User | SSH |
| Final Configuration | SSH |
| Setup Complete | 数据设置 |



## 功能说明

数据库操作工具，自动查询或写入数据库。

手动触发，通过 数据库 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- 数据库连接信息

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：10
- 触发方式：手动触发

## 触发方式
- Start 触发

## 统计
- 节点总数：10
- 触发节点：1
- 处理节点：9
- 输出节点：0
- 分类：devops
