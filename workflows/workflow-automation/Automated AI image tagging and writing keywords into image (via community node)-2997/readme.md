# Automated AI image tagging and writing keywords into image (via community node)

https://n8nworkflows.xyz/workflows/2997

## 节点清单

| 节点 | 类型 |
|------|------|
| Trigger: New file added to Google Drive Folder | Google Drive 触发器 |
| Download Image File | Google Drive |
| Analyze Image Content | OpenAI |
| Merge Metadata and Image File | 数据合并 |
| Write Metadata into Image | exifData |
| Update Image File | Google Drive |

## 触发方式
- Trigger: New file added to Google Drive Folder 触发

## 统计
- 节点总数：6
- 触发节点：1
- 处理节点：5
- 输出节点：0
- 分类：workflow-automation
