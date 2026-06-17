# Monitor S3 Bucket Changes with Automated Integrity Auditing using Mistral AI

https://n8nworkflows.xyz/workflows/7547

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

## 触发方式
- When clicking ‘Execute workflow’ 触发
- Schedule Trigger 触发

## 统计
- 节点总数：52
- 触发节点：2
- 处理节点：49
- 输出节点：1
- 分类：workflow-automation
