## 简介
**Automated AI image tagging and writing the keywords into the image file**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A-adapted（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2995

---

# Automated AI image tagging and writing the keywords into the image file


## 节点清单

| 节点 | 类型 |
|------|------|
| Extract from File | 从文件提取 |
| Convert to File | 转换为文件 |
| Analyze Image Content | OpenAI |
| Download Image File | Google Drive |
| Trigger: New file added to Google Drive Folder | Google Drive 触发器 |
| Write Metadata to Base64 Code | Code |
| Update Image File | Google Drive |
| Merge Metadata and Base64 Code | 数据合并 |

## 触发方式
- Trigger: New file added to Google Drive Folder 触发

## 统计
- 节点总数：8
- 触发节点：1
- 处理节点：7
- 输出节点：0
- 分类：workflow-automation
