## 简介
**Monitor S3 Bucket Changes with Automated Integrity Auditing using Mistral AI**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/7547

---

# Monitor S3 Bucket Changes with Automated Integrity Auditing using Mistral AI


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Execute workflow’ | 手动触发 |
| Schedule Trigger | 定时触发器 |
| Envoi de mail récapitulatif | Email 发送 |
| Mistral Cloud Chat Model1 | Mistral Chat Model |
| Extract .txt / .log | 从文件提取 |
| Extraction des paths | 数据拆分 |
| Remove Duplicates | 去重 |
| Switch | Switch 路由 |
| Extract text with OCR | mistralAi |
| Wait | 等待 |
| Boucle | 分批处理 |
| AnalyseIA | LLM Chain |
| Delete a folder1 | S3 |
| Create a folder1 | S3 |
| Extract from File | 从文件提取 |
| Split Out | 数据拆分 |
| Only keep PDF, TXT and Logs | 过滤器 |
| Download suspect files | S3 |
| List downloaded objects | S3 |
| Ajout à MongoDB | MongoDB |
| Error Message #1 | 数据设置 |
| Error Message #2 | 数据设置 |
| PDF Prompt Creation | 数据设置 |
| TXT/LOG Prompt Creation | 数据设置 |
| Result Message Creation | 数据设置 |
| Result Saved | SSH |
| Delete local files | SSH |
| Path Extraction | 数据拆分 |
| Objects Listing | awsS3 |
| Objects Download | awsS3 |
| Generate MD5 | 加密 |
| Create JSON from AWS S3 API Call | 数据设置 |
| Save Audit Snapshot | SSH |
| Convert to File | 转换为文件 |
| Compare Datasets | compareDatasets |
| Audit file to JSON | 从文件提取 |
| Split Objects | 数据拆分 |
| Upload objects to MinIO | S3 |
| Convert to File1 | 转换为文件 |
| Convert to File2 | 转换为文件 |
| Get previous Audit Snapshot | SSH |
| List S3 Objects | awsS3 |
| Generate MD6 | 加密 |
| Create JSON from results | 数据设置 |
| Replace previous snapshot with current one | S3 |
| Save Suspect Objects List | S3 |
| Download current Integrity Snapshot | S3 |
| Remove them from Host FS | SSH |
| Upload Snapshot on Host FS | SSH |
| Report Creation | SSH |
| Getting Report | SSH |
| Upload Report to MinIO | S3 |



## 功能说明

监控告警系统，异常检测并发送通知，定时执行。

定时触发、手动触发，通过 邮箱 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com
- 邮箱 SMTP/IMAP 账号密码

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：52
- 触发方式：手动触发, 定时触发

## 触发方式
- When clicking ‘Execute workflow’ 触发
- Schedule Trigger 触发

## 统计
- 节点总数：52
- 触发节点：2
- 处理节点：49
- 输出节点：1
- 分类：workflow-automation
