## 简介
**Automated AI image tagging and writing keywords into image (via community node)**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Drive)（基本改完，配置 API Key 应该就能跑）
> 节点数：6 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/2997

---

# Automated AI image tagging and writing keywords into image (via community node)


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
