## 简介
**Extend n8n with additional tools**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/1605

---

# Extend n8n with additional tools


## 节点清单

| 节点 | 类型 |
|------|------|
| Switch | Switch 路由 |
| msg_greet | Telegram |
| msg_wrongcommand | Telegram |
| Telegram Trigger | Telegram 触发器 |
| msg_getweather | Telegram |
| City List | Function |
| Convert API response | Function |
| Get weather data | HTTP Request |
| Spreadsheet File | 电子表格文件 |
| Write csv | 写入二进制文件 |
| Filename | 数据设置 |
| msg_errorAPI | Telegram |
| Any errors API? | IF 判断 |
| msg_errorR | Telegram |
| Read Binary File | 读取二进制文件 |
| R successful? | IF 判断 |
| Merge | 数据合并 |
| Merge1 | 数据合并 |
| msg_pleasewait | Telegram |
| Merge2 | 数据合并 |
| Run R script | 执行命令 |

## 触发方式
- Telegram Trigger 触发

## 统计
- 节点总数：21
- 触发节点：1
- 处理节点：13
- 输出节点：7
- 分类：workflow-automation
