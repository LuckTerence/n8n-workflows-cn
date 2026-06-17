## 简介
**Extract Organizations & Summarize Documents with Foxit and Diffbot**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/6286

---

# Extract Organizations & Summarize Documents with Foxit and Diffbot


## 节点清单

| 节点 | 类型 |
|------|------|
| Fire on New File in Google Drive Folder | Google Drive 触发器 |
| Download File | Google Drive |
| Upload to Foxit | HTTP Request |
| Kick off Foxit Extract | HTTP Request |
| Check Task | HTTP Request |
| Is the job done? | IF 判断 |
| Wait | 等待 |
| Download Extracted Text | HTTP Request |
| Get Diffbot Entities | HTTP Request |
| Shape Data | Code |
| Gmail | Email 发送 |
| Make Email Contents | Code |

## 触发方式
- Fire on New File in Google Drive Folder 触发

## 统计
- 节点总数：12
- 触发节点：1
- 处理节点：5
- 输出节点：6
- 分类：workflow-automation
