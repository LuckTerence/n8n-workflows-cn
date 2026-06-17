## 简介
**Convert PDF Articles to Audio Podcasts with Google TTS & Cloudflare R2**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/9521

---

# Convert PDF Articles to Audio Podcasts with Google TTS & Cloudflare R2


## 节点清单

| 节点 | 类型 |
|------|------|
| ⚙️ Workflow Config | 数据设置 |
| Upload PDF for Podcast | 表单触发器 |
| Extract PDF Text | readPDF |
| Clean & Process Text | Code |
| Detect Sections & Split | Code |
| Check TTS Usage Limit | Code |
| Google TTS API | HTTP Request |
| Convert Audio to Binary | Code |
| Stitch All Mp3 Together | Code |
| Upload MP3 to R2 | cloudflareR2Storage |
| Build RSS XML | Code |
| Upload RSS to R2 | cloudflareR2Storage |
| Update Monthly Usage | Code |
| Aggregate for Email | Code |
| Send Email | Email 发送 |
| Merge | 数据合并 |

## 触发方式
- Upload PDF for Podcast 触发

## 统计
- 节点总数：16
- 触发节点：1
- 处理节点：13
- 输出节点：2
- 分类：workflow-automation
