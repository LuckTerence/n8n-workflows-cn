## 简介
**AI个人助理WhatsApp**

GPT-4o RAG语音助手WhatsApp

> 分类：AI Agent | 适配等级：A（AI模型已替换为DeepSeek，部分边角节点可能仍需手动调整）
> 原始来源：https://n8nworkflows.xyz/workflows/3947

---

# AI个人助理WhatsApp


## 节点清单

| 节点 | 类型 |
|------|------|
| OpenAI Chat Model | OpenAI Chat Model |
| Convert to File | 转换为文件 |
| edit1 | 数据设置 |
| edit2 | 数据设置 |
| auth | IF 判断 |
| Message Delay | 等待 |
| Puxar as Mensagens | Redis |
| If1 | IF 判断 |
| Database | Redis |
| Lista Mensagens1 | Redis |
| Edit Fields2 | 数据设置 |
| OpenAI | OpenAI |
| setar_supabase_tabelas_vectoriais | PostgreSQL |
| Default Data Loader | 文档加载器 |
| Embeddings OpenAI1 | OpenAI Embeddings |
| Recursive Character Text Splitter | 文本分割器 |
| arquivo_id | 数据设置 |
| deletar_arquivos_antigos | Supabase |
| extrair_pdf | 从文件提取 |
| exportar_texto | 数据设置 |
| Embeddings OpenAI | OpenAI Embeddings |
| OpenAI Chat Model2 | OpenAI Chat Model |
| supabase_vectorstore | Supabase 向量存储 |
| agendamentos | 工作流工具 |
| criar_cerebro | PostgreSQL |
| puxar_prompt | PostgreSQL |
| Postgres Chat Memory | PostgreSQL 聊天记忆 |
| Deletar_todas_as_mensagens1 | PostgreSQL |
| convert_to_file | 转换为文件 |
| base64 | 数据设置 |
| tipo_arquivo | Switch 路由 |
| OpenAI Chat Model1 | OpenAI Chat Model |
| Merge Database Data1 | 数据聚合 |
| resumo | LLM Chain |
| criar_rag_controle | PostgreSQL |
| atualizar_lista_de_arquivos | PostgreSQL |
| rag_resumos | PostgreSQL |
| Merge Database Data2 | 数据聚合 |
| Supabase Vector Store | Supabase 向量存储 |
| excluir_rag_arquivo | 工作流工具 |
| emails | 工作流工具 |
| adicionar_conhecimento | 工作流工具 |
| buscar_conhecimento | 工作流工具 |
| Convert to File1 | 转换为文件 |
| base | 数据设置 |
| Edit Fields | 数据设置 |
| mensagem_tipo | Switch 路由 |
| OpenAI1 | OpenAI |
| Merge | 数据合并 |
| Switch | Switch 路由 |
| atualizar_prompt | 执行工作流 |
| tratamento | 数据设置 |
| Webhook | Webhook |
| recepcionista | AI Agent |
| classificador_de_intencao | AI Agent |
| Merge Database Data3 | 数据聚合 |
| excluir_conhecimento | 工作流工具 |
| config | 数据设置 |
| mensagem_cliente | 数据设置 |
| mensagem_cliente_inicial | 数据设置 |
| deletar_arquivo | PostgreSQL |
| Postgres Chat Memory1 | PostgreSQL 聊天记忆 |
| deletar_conhecimento | PostgreSQL |
| RAG | 向量存储工具 |

## 触发方式
- Webhook 触发

## 统计
- 节点总数：64
- 触发节点：1
- 处理节点：63
- 输出节点：0
- 分类：ai-agent
