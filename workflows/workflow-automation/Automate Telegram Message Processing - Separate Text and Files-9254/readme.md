## 简介
**Automate Telegram Message Processing - Separate Text and Files**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Google Drive)（基本改完，配置 API Key 应该就能跑）
> 节点数：10 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/9254

---

# Automate Telegram Message Processing - Separate Text and Files


## 节点清单

| 节点 | 类型 |
|------|------|
| Waiting For Message | Telegram 触发器 |
| Get Chat Message Only | 数据设置 |
| Switch | Switch 路由 |
| Split Out | 数据拆分 |
| Get Attachment Only | 数据设置 |
| Get & Download Attachment | Telegram |
| Get Attachment | 数据设置 |
| Next Step ! | 空操作 |
| Next Step !   | 空操作 |
| Next Step !  | 空操作 |
| Get Chat Message Content | 数据设置 |

## 触发方式
- Waiting For Message 触发

## 统计
- 节点总数：11
- 触发节点：1
- 处理节点：9
- 输出节点：1
- 分类：workflow-automation
