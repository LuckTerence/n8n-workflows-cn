# 适配升级指南

> 以下 21 个工作流当前为 Tier B（核心链路通了，边角节点需手动调），列出了每个需要替换的外服节点和推荐方案。

---

## 升级操作清单

### 通用步骤（所有工作流）

1. **OpenAI → DeepSeek**：修改 OpenAI Chat Model 节点参数：
   - `Base URL` → `https://api.deepseek.com`
   - `Model` → `deepseek-chat`
2. **OpenAI Embeddings** → 替换为兼容的嵌入模型（如 `text-embedding-v3` 走 DeepSeek 或换通义千问嵌入 API）
3. 改完后在 n8n 里导入测试，确认核心链路能跑通

### 各工作流具体替换

---

### ai-agent (2 个)

#### AI 日历助手
| 外服节点 | 推荐替换 |
|----------|----------|
| OpenAI Chat Model | DeepSeek（已在 readme 注明） |
| Google Calendar | 飞书日历 HTTP Request |
| OpenAI Embeddings | 通义千问 Embedding API |
| Supabase | 腾讯云 CloudBase |

#### AI个人助理WhatsApp
| 外服节点 | 推荐替换 |
|----------|----------|
| OpenAI (多处) | DeepSeek |
| Supabase | 腾讯云 CloudBase |
| Google Calendar | 飞书日历 |

---

### knowledge-rag (1 个)

#### 自适应RAG策略
| 外服节点 | 推荐替换 |
|----------|----------|
| Google Gemini (5处) | DeepSeek 或通义千问 |
| Google Gemini Embeddings | 通义千问 Embedding API |

---

### multimodal-ai (3 个)

#### 3D手办生成
| 外服节点 | 推荐替换 |
|----------|----------|
| Stripe | 微信支付 / 支付宝 HTTP Request |

#### AI邮件附件分析
| 外服节点 | 推荐替换 |
|----------|----------|
| OpenAI | DeepSeek OK（已部分替换） |
| Google Gemini | 通义千问 |
| Google Drive | 阿里云 OSS |

#### 电商3D视频生成
| 外服节点 | 推荐替换 |
|----------|----------|
| Gmail | QQ邮箱 SMTP/IMAP |

---

### workflow-automation (14 个)

#### AI文章抓取到Notion
| 外服节点 | 推荐替换 |
|----------|----------|
| OpenAI | DeepSeek |
| Anthropic Claude | DeepSeek |
| Google Gemini | 通义千问 |
| Notion | 飞书文档 / 语雀 HTTP Request |

#### AI文章摘要生成
| 外服节点 | 推荐替换 |
|----------|----------|
| OpenAI | DeepSeek |
| Google Sheets | 飞书多维表格 |
| Slack | 飞书群机器人 |

#### AI新闻简报构建
| 外服节点 | 推荐替换 |
|----------|----------|
| OpenAI | DeepSeek |
| Gmail | QQ邮箱 |

#### AI新闻研究团队
| 外服节点 | 推荐替换 |
|----------|----------|
| OpenAI | DeepSeek |
| Gmail | QQ邮箱 |

#### AI数字产品销售
| 外服节点 | 推荐替换 |
|----------|----------|
| OpenAI | DeepSeek |
| Gmail | QQ邮箱 |

#### AI网页抓取
| 外服节点 | 推荐替换 |
|----------|----------|
| OpenAI | DeepSeek |
| Google Sheets | 飞书多维表格 |

#### AI邮件处理+审批
| 外服节点 | 推荐替换 |
|----------|----------|
| OpenAI | DeepSeek OK（已部分替换） |
| Gmail | QQ邮箱 |

#### AI邮件自动回复RAG
| 外服节点 | 推荐替换 |
|----------|----------|
| OpenAI | DeepSeek |
| Gmail | QQ邮箱 |
| Google Drive | 阿里云 OSS |
| Google Docs | 飞书文档 |
| Notion | 飞书文档 / 语雀 |
| Pinecone | 腾讯云向量数据库 / Milvus |

#### Gmail垃圾邮件清理
| 外服节点 | 推荐替换 |
|----------|----------|
| OpenAI | DeepSeek |
| Gmail | QQ邮箱 |

#### Gmail客服自动回复
| 外服节点 | 推荐替换 |
|----------|----------|
| Gmail | QQ邮箱 |
| Pinecone | 腾讯云向量数据库 / Milvus |

#### Gmail智能分类归档
| 外服节点 | 推荐替换 |
|----------|----------|
| OpenAI | DeepSeek |
| Gmail | QQ邮箱 |

#### Shopify弃购挽回
| 外服节点 | 推荐替换 |
|----------|----------|
| Gmail | QQ邮箱 |
| Twilio | 腾讯云短信 |

#### 人工审核邮件回复
| 外服节点 | 推荐替换 |
|----------|----------|
| OpenAI | DeepSeek OK（已部分替换） |
| Gmail | QQ邮箱 |

#### 弃购挽回分析
| 外服节点 | 推荐替换 |
|----------|----------|
| Gmail | QQ邮箱 |

---

### finance-analysis (1 个)

#### AAVE投资组合Agent
| 外服节点 | 推荐替换 |
|----------|----------|
| OpenAI | DeepSeek |
| Gmail | QQ邮箱 |
| Google Sheets | 飞书多维表格 |
| Notion | 飞书文档 |

---

## 升级后操作

每完成一个工作流的替换后：

1. 在 n8n 中导入并测试核心链路
2. 更新 `workflow.json` 中的 `_cn_meta.tier` 为 `"A"`
3. 在 `readme.md` 的「适配修改」章节补充替换说明
4. 修改 `workflow.json` 中 `_cn_meta.tier` 从 `"B"` 改为 `"A"`
5. 提交 PR

## 优先级建议

| 优先级 | 工作流 | 理由 |
|:---:|--------|------|
| 🔴 高 | AI 日历助手 | 仅5节点，改动量最小 |
| 🔴 高 | 人工审核邮件回复 | DeepSeek 已替换 |
| 🔴 高 | AI邮件处理+审批 | DeepSeek 已替换 |
| 🔴 高 | AI邮件附件分析 | DeepSeek 已替换 |
| 🟡 中 | Gmail系列（3个） | 改动模式一致，可批量处理 |
| 🟡 中 | AI新闻/AI文章系列（4个） | 核心链路简单 |
| 🟢 低 | AI邮件自动回复RAG | 外服节点多（6个），改动量大 |
| 🟢 低 | AI个人助理WhatsApp | 64节点，改动量大 |
| 🟢 低 | AI文章抓取到Notion | 涉及5种外服，改动量大 |

---

> 如果你完成了某些工作流的升级，欢迎提 PR。只要核心链路在替换后能跑通，就可以标记为 Tier A。
