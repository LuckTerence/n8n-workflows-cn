## 简介
**Monitor PKI Certificates & CRLs for Expiration with Telegram & SMS Alerts**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/9865

---

# Monitor PKI Certificates & CRLs for Expiration with Telegram & SMS Alerts


## 节点清单

| 节点 | 类型 |
|------|------|
| Write Binary - TempFile : crlfile.der | 写入二进制文件 |
| B64 Encode : crlfile.der | 执行命令 |
| OpenSSL Parse CRL : crlfile.der | 执行命令 |
| Parse Data OpenSSL output | Code |
| Get CRL URL | HTTP Request |
| nextUpdate - TimeFilter | Code |
| Good Or Evil | IF 判断 |
| Is this CRL ? | IF 判断 |
| Execute With Manual Start | 手动触发 |
| Execute With Scheduled Start | 定时触发器 |
| Get Url From List | 数据拆分 |
| Loop Over Items -- Process Checking | 分批处理 |
| Website Available? | IF 判断 |
| Wait B4 Retry | 等待 |
| Website Available Now? | IF 判断 |
| Send Website Down - Telegram & SMS | 执行命令 |
| Respose Extend With Requested URL | 数据设置 |
| Is this CA? | IF 判断 |
| Get Non-CRL/CA URL | HTTP Request |
| Retry to Non-CRL/CA URL | HTTP Request |
| nextUpdate - TimeFilter1 | Code |
| Get CA URL | HTTP Request |
| Write Binary - TempFile : cacertfile.crt | 写入二进制文件 |
| B64 Encode : cacertfile.crt | 执行命令 |
| OpenSSL Parse CA Cert : cacertfile.crt | 执行命令 |
| Parse Data OpenSSL CA output | Code |
| Alive? | IF 判断 |
| Set-Info for CA Alert | 数据设置 |
| Set-Info for CRL Alert | 数据设置 |
| CRL Alert --- Telegam & SMS | 执行命令 |
| Collect Checking URL list | 执行命令 |
| Get Checking URL list to URL objects | 数据设置 |
| CRL Available? | IF 判断 |
| CA Available? | IF 判断 |
| CA Alert --- Telegam & SMS | 执行命令 |



## 功能说明

Telegram 机器人，消息驱动自动化流程，定时执行。

定时触发、手动触发，通过 Telegram 通知 实现自动化。

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

- 节点总数：35
- 触发方式：手动触发, 定时触发

## 触发方式
- Execute With Manual Start 触发
- Execute With Scheduled Start 触发

## 统计
- 节点总数：35
- 触发节点：2
- 处理节点：29
- 输出节点：4
- 分类：workflow-automation
