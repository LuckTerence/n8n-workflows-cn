## 简介
**Smart IoT Device Health Monitor with ScrapeGraphAI and Telegram**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/6930

---

# Smart IoT Device Health Monitor with ScrapeGraphAI and Telegram


## 节点清单

| 节点 | 类型 |
|------|------|
| ⏰ Timer | 定时触发器 |
| 🤖 Get Data | ScrapeGraph AI |
| 📊 Analyze | Code |
| 🚨 Need Alert? | IF 判断 |
| 📱 Send Alert | Telegram |
| 📝 Log Data | Code |

## 触发方式
- ⏰ Timer 触发

## 统计
- 节点总数：6
- 触发节点：1
- 处理节点：4
- 输出节点：1
- 分类：workflow-automation
