## 简介
**Automatically Add Watermarks to Images with Telegram Bot and ImageKit.io**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/11229

---

# Automatically Add Watermarks to Images with Telegram Bot and ImageKit.io


## 节点清单

| 节点 | 类型 |
|------|------|
| Upload to ImageKit | HTTP Request |
| Telegram Trigger1 | Telegram 触发器 |
| Check if Photo1 | IF 判断 |
| Send Error Message1 | Telegram |
| Get File Path | HTTP Request |
| Download Image | HTTP Request |
| Send Watermarked Photo | Telegram |
| Add Logo1 | HTTP Request |

## 触发方式
- Telegram Trigger1 触发

## 统计
- 节点总数：8
- 触发节点：1
- 处理节点：1
- 输出节点：6
- 分类：workflow-automation
