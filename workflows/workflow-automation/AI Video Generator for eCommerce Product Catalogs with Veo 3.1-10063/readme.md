## 简介
**AI Video Generator for eCommerce Product Catalogs with Veo 3.1**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：B（需替换Google Drive)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/10063

---

# AI Video Generator for eCommerce Product Catalogs with Veo 3.1


## 节点清单

| 节点 | 类型 |
|------|------|
| form_trigger | 表单触发器 |
| scrape_catalog_collection | Firecrawl |
| split_products | 数据拆分 |
| limit_products | 数据限制 |
| iterate_products | 分批处理 |
| fetch_image | HTTP Request |
| generate_video | HTTP Request |
| set_prompt | 数据设置 |
| fetch_status | HTTP Request |
| wait | 等待 |
| check_response | IF 判断 |
| download_video | HTTP Request |
| convert_to_base64 | 从文件提取 |
| upload_source_image | Google Drive |
| upload_output_video | Google Drive |
| convert_to_binary | 转换为文件 |

## 触发方式
- form_trigger 触发

## 统计
- 节点总数：16
- 触发节点：1
- 处理节点：11
- 输出节点：4
- 分类：workflow-automation
