# Readable Workflow Export & Deployment Pipeline for Multi-Environment CI-CD

https://n8nworkflows.xyz/workflows/3994

## 节点清单

| 节点 | 类型 |
|------|------|
| Remove root node | 数据设置 |
| TAG? Auto deploy to dev | IF 判断 |
| TAG? Auto deploy to PROD | IF 判断 |
| Start export workflows | 手动触发 |
| Create folders and run n8n cli | 执行命令 |
| load exported workflows | 读写文件 |
| parse workflow | 从文件提取 |
| Create JSON  file with readable name | 转换为文件 |
| Store named workflow | 读写文件 |
| Create JSON  file with readable name (dev) | 转换为文件 |
| Create JSON  file with readable name (prod) | 转换为文件 |
| Store named workflow (dev) | 读写文件 |
| Store named workflow (prod) | 读写文件 |

## 触发方式
- Start export workflows 触发

## 统计
- 节点总数：13
- 触发节点：1
- 处理节点：12
- 输出节点：0
- 分类：workflow-automation
