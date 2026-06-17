## 简介
**Automatic Job Listings Extraction and Publishing Template**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：B（需替换Google Drive/Supabase)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/6518

---

# Automatic Job Listings Extraction and Publishing Template


## 节点清单

| 节点 | 类型 |
|------|------|
| Search File | Google Drive |
| Get Data | Google Drive |
| Supabase Vector Store | Supabase 向量存储 |
| Embeddings OpenAI | OpenAI Embeddings |
| Default Data Loader | 文档加载器 |
| Recursive Character Text Splitter | 文本分割器 |
| Loop Over Items | 分批处理 |
| Supabase Vector Store1 | Supabase 向量存储 |
| Embeddings OpenAI1 | OpenAI Embeddings |
| Google Drive Trigger | Google Drive 触发器 |
| 📥 New Job Link via Telegram | Telegram 触发器 |
| 🔧 Prepare URL for Extraction | 数据设置 |
| 🧮 Map Job Type & Category IDs | Code |
| 📥 Download Company Logo | HTTP Request |
| ☁️ Upload Logo to WordPress | HTTP Request |
| 📦 Format Final Job Post Data | 数据设置 |
| ✅ All Fields Available? | IF 判断 |
| if not valid | Telegram |
| notify: processing job | Telegram |
| notify: extracting | Telegram |
| If | IF 判断 |
| notify: success extract | Telegram |
| 📚 Load Valid Job Types & Categories | 数据设置 |
| notify: error | Telegram |
| Wait | 等待 |
| valid url? | IF 判断 |
| notify: wrong url | Telegram |
| 🧠 Extract Job Data with GPT | OpenAI |
| Create Url | Code |
| notify: openai success | Telegram |
| Edit Fields | 数据设置 |
| 📥 Download Company Logo - Alt | HTTP Request |
| ☁️ Upload Logo to WordPress - Alt | HTTP Request |
| 📦 Format Final Job Post Data - Alt | 数据设置 |
| ✅ All Fields Available? - Alt | IF 判断 |
| 📊 Did Publish Succeed?1 | IF 判断 |
| 📨 Notify Success - Alt | Telegram |
| 📨 Notify Failed - Alt | Telegram |
| 📊 Did Publish Succeed?2 | IF 判断 |
| notify: failed extract | Telegram |
| Error | Telegram |
| changing method | Telegram |
| Wait1 | 等待 |
| Wait2 | 等待 |
| Error Trigger | 错误触发器 |
| Kirim ke Telegram | Telegram |
| Code | Code |
| Publiched! | Telegram |
| 🚀 Publish to Your web | HTTP Request |
| 🚀 Publish to Yourweb - Alt | HTTP Request |
| Extract | HTTP Request |

## 触发方式
- Google Drive Trigger 触发
- 📥 New Job Link via Telegram 触发
- Error Trigger 触发

## 统计
- 节点总数：51
- 触发节点：3
- 处理节点：27
- 输出节点：21
- 分类：workflow-automation
