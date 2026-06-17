## 简介
**Product Visualization in Spaces with AI: Generate & Publish Videos to Social Media**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Zoom/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/7963

---

# Product Visualization in Spaces with AI: Generate & Publish Videos to Social Media


## 节点清单

| 节点 | 类型 |
|------|------|
| Download Final Video | HTTP Request |
| Photo Upload Form | 表单触发器 |
| Set APIs Vars | 数据设置 |
| Upload Original Image to imgbb | HTTP Request |
| HTTP Request | HTTP Request |
| Set Prompts | 数据设置 |
| Gemini 2.5 Flash - Generate Image | HTTP Request |
| Separate Image Outputs | 数据拆分 |
| Rename to photo | Code |
| Upload Image to imgbb | HTTP Request |
| FAL WAN i2v (Queue) | HTTP Request |
| Wait i2v | 等待 |
| FAL WAN i2v (status) | HTTP Request |
| Animation Completed? | IF 判断 |
| FAL WAN i2v (Result) | HTTP Request |
| Merge | 数据合并 |
| Merge1 | 数据合并 |
| Upload Original Image to imgbb1 | HTTP Request |
| Upload Post | uploadPost |

## 触发方式
- Photo Upload Form 触发

## 统计
- 节点总数：19
- 触发节点：1
- 处理节点：9
- 输出节点：9
- 分类：workflow-automation
