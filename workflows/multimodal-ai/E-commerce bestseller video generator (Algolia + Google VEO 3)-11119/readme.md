## 简介
**E-commerce bestseller video generator (Algolia + Google VEO 3)**

（待补充中文描述）

> 分类：多模态 AI | 适配等级：B（需替换Supabase/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/11119

---

# E-commerce bestseller video generator (Algolia + Google VEO 3)


## 节点清单

| 节点 | 类型 |
|------|------|
| Every week on monday morning | 定时触发器 |
| Test Trigger while building the workflow | 手动触发 |
| Get weekly bestseller from Algolia | HTTP Request |
| If no video for that product | IF 判断 |
| Image URL is present | IF 判断 |
| Check image availability | HTTP Request |
| No Operation, do nothing | 空操作 |
| Tell admin that bestseller has no image | Email 发送 |
| Tell admin that bestseller has broken image | Email 发送 |
| Image is present and valid | IF 判断 |
| Wait for video generation | 等待 |
| Finished ? | IF 判断 |
| Wait more | 等待 |
| Generate video with Google VEO 3 | HTTP Request |
| Get video name and storage bucket | 数据设置 |
| Checking if we're done | HTTP Request |
| Downloading the MP4 file | HTTP Request |
| Drop video in Supabase Bucket | HTTP Request |
| Aggregate | 数据聚合 |
| Index in Algolia | HTTP Request |
| Convert image to base64 for VEO 3 | 从文件提取 |

## 触发方式
- Every week on monday morning 触发
- Test Trigger while building the workflow 触发

## 统计
- 节点总数：21
- 触发节点：2
- 处理节点：10
- 输出节点：9
- 分类：multimodal-ai
