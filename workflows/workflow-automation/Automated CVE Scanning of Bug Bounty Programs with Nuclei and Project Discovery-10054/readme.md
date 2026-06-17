## 简介
**Automated CVE Scanning of Bug Bounty Programs with Nuclei and Project Discovery**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/10054

---

# Automated CVE Scanning of Bug Bounty Programs with Nuclei and Project Discovery


## 节点清单

| 节点 | 类型 |
|------|------|
| Schedule Trigger | 定时触发器 |
| Get All Bug Bounty Domains | HTTP Request |
| Create domains.txt | 转换为文件 |
| Upload domains.txt | SSH |
| Loop Over CVEs | 分批处理 |
| Split CVEs | 数据拆分 |
| GET Last CVEs (PROJECT DISCOVERY) | HTTP Request |
| Template Exists Filter | 过滤器 |
| Date Filter | IF 判断 |
| Set Variables | 数据设置 |
| Set Null Variable | 数据设置 |
| Loop Over Templates | 分批处理 |
| Create Template | 转换为文件 |
| Upload Template | SSH |
| Convert Template to .yaml | SSH |
| Execute Nuclei | SSH |
| Remove Templates | SSH |
| Set Results Variable | 数据设置 |
| Check Results | IF 判断 |
| Send a message | Email 发送 |
| Remove Items | 文本摘要 |



## 功能说明

AI 代码助手，代码生成或审查，定时执行。

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

- 节点总数：21
- 触发方式：定时触发

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：21
- 触发节点：1
- 处理节点：17
- 输出节点：3
- 分类：workflow-automation
