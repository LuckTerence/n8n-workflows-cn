## 简介
**Create instrumental tracks from song URLs with StemSplit**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A-adapted（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/16055

---

# Create instrumental tracks from song URLs with StemSplit


## 节点清单

| 节点 | 类型 |
|------|------|
| On karaoke form submission | 表单触发器 |
| Normalize form data | 数据设置 |
| Is song URL valid? | IF 判断 |
| StemSplit: check credits | stemSplit |
| Enough StemSplit credits? | IF 判断 |
| StemSplit: create instrumental | stemSplit |
| Download instrumental MP3 | HTTP Request |
| Upload to Google Drive | Google Drive |
| Gmail: send download link | Email 发送 |
| Gmail: invalid URL notice | Email 发送 |
| Gmail: insufficient credits | Email 发送 |

## 触发方式
- On karaoke form submission 触发

## 统计
- 节点总数：11
- 触发节点：1
- 处理节点：6
- 输出节点：4
- 分类：workflow-automation
