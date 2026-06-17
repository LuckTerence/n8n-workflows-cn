# Ebook to Audiobook converter using MiniMax and FFmpeg

https://n8nworkflows.xyz/workflows/9944

## 节点清单

| 节点 | 类型 |
|------|------|
| Save Audio Chucks | 读写文件 |
| Generate `concat_list.txt` | Code |
| Save concat_list | 读写文件 |
| Join audio chucks and delete all files | 执行命令 |
| read final_merged | 读写文件 |
| FORM | 表单触发器 |
| EXTRACT TEXT | 从文件提取 |
| SPLITS THE TEXT ACCORGING TO RULES | Code |
| Loop Over Text chunks (5) at a time | 分批处理 |
| WAITS FOR 5 SECONDS | 等待 |
| CONVERTS URL TO AUDIO FILES | HTTP Request |
| GIVES INDEXES TO AUDIO FILES | Code |
| Uploads Ebook | Google Drive |
| MINIMAX TTS | HTTP Request |

## 触发方式
- FORM 触发

## 统计
- 节点总数：14
- 触发节点：1
- 处理节点：11
- 输出节点：2
- 分类：multimodal-ai
