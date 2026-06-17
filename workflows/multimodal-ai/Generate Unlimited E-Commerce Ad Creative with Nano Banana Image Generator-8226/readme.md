## 简介
**Generate Unlimited E-Commerce Ad Creative with Nano Banana Image Generator**

（待补充中文描述）

> 分类：多模态 AI | 适配等级：A（需替换Google Drive)（基本改完，配置 API Key 应该就能跑）
> 节点数：9 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/8226

---

# Generate Unlimited E-Commerce Ad Creative with Nano Banana Image Generator


## 节点清单

| 节点 | 类型 |
|------|------|
| form_trigger | 表单触发器 |
| list_influencer_images | Google Drive |
| iterate_influencer_images | 分批处理 |
| download_influencer_image | Google Drive |
| product_image_to_base64 | 从文件提取 |
| influencer_image_to_base_64 | 从文件提取 |
| generate_image | HTTP Request |
| get_image | 转换为文件 |
| upload_image | Google Drive |
| set_result | 数据设置 |

## 触发方式
- form_trigger 触发

## 统计
- 节点总数：10
- 触发节点：1
- 处理节点：8
- 输出节点：1
- 分类：multimodal-ai
