# n8n-workflows-cn

基于 [nusquama/n8nworkflows.xyz](https://github.com/nusquama/n8nworkflows.xyz) 的 n8n 工作流模板进行中文本地化适配。

将原始模板中用到的海外服务（OpenAI、Slack、Google Workspace 等）替换为国内可用的替代方案，并对每个工作流添加中文说明。

---

## 适配内容

- **AI 模型**：OpenAI → DeepSeek，Claude → DeepSeek，Gemini → 通义千问（直接修改了 workflow.json 中节点的 Base URL 和 Model 参数）
- **消息服务**：Slack → 飞书群机器人，Gmail → Email(SMTP)，Google Sheets → 飞书多维表格
- **文档标注**：每个 JSON 文件包含 `_cn_meta` 字段，记录中文标题、分类、适配等级及具体修改项

---

## 分类

| 分类 | 数量 |
|------|:--:|
| [workflow-automation](workflows/workflow-automation/) | 1110 |
| [devops](workflows/devops/) | 153 |
| [ai-agent](workflows/ai-agent/) | 93 |
| [multimodal-ai](workflows/multimodal-ai/) | 52 |
| [knowledge-rag](workflows/knowledge-rag/) | 47 |
| [finance-analysis](workflows/finance-analysis/) | 25 |

[查看完整索引（1480 个工作流）](INDEX.md)

---

## 服务替换对照

n8n 的专用节点本质上是 HTTP Request 的封装。大部分替换方案通过将专用节点改为 HTTP Request 节点并配置对应国内服务的 API 实现。

| 原始服务 | 替换方案 | 修改方式 |
|------|------|------|
| OpenAI (GPT-4/GPT-4o) | DeepSeek | 修改 OpenAI Chat Model 节点的 Base URL 为 `https://api.deepseek.com`，Model 为 `deepseek-chat` |
| Anthropic (Claude) | DeepSeek | 将 Anthropic Chat Model 节点替换为 OpenAI Chat Model，同上配置 |
| Google Gemini | 通义千问 | 替换为 OpenAI Chat Model 节点，Base URL 为 `https://dashscope.aliyuncs.com/compatible-mode/v1` |
| Slack | 飞书群机器人 | 修改 Webhook URL 为飞书机器人地址，调整消息体格式 |
| Gmail | QQ邮箱 / 网易企业邮箱 | 替换为 Email (IMAP/SMTP) 节点 |
| Google Sheets | 飞书多维表格 | 替换为 HTTP Request 节点，调用飞书 Bitable API |
| Google Drive | 阿里云 OSS / 腾讯云 COS | 替换为 HTTP Request 节点 |
| Google Calendar | 飞书日历 | 替换为 HTTP Request 节点 |
| Notion | 飞书文档 / 语雀 | 替换为 HTTP Request 节点 |
| Twilio | 腾讯云短信 / 阿里云短信 | 替换为 HTTP Request 节点 |
| Stripe / PayPal | 微信支付 / 支付宝 | 替换为 HTTP Request 节点 |
| GitHub | Gitee | HTTP Request 节点调用 Gitee API |
| Supabase | 腾讯云 CloudBase | HTTP Request 节点 |
| Zoom | 腾讯会议 | HTTP Request 节点 |

---

## 使用方式

在 n8n 编辑器中通过 Import from File 导入 `workflow.json` 即可。

n8n 安装（Docker）：

```bash
docker run -d --name n8n -p 5678:5678 -v n8n_data:/home/node/.n8n n8nio/n8n
```

---

## 目录结构

```
workflows/
  {分类}/
    {工作流名称}-{ID}/
      workflow.json    # 工作流定义
      readme.md        # 节点说明与适配记录
```

---

## 许可

模板来源：[nusquama/n8nworkflows.xyz](https://github.com/nusquama/n8nworkflows.xyz)，MIT 许可。
