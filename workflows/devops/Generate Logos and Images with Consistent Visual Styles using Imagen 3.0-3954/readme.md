## 简介
**Generate Logos and Images with Consistent Visual Styles using Imagen 3.0**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3954

---

# Generate Logos and Images with Consistent Visual Styles using Imagen 3.0


## 节点清单

| 节点 | 类型 |
|------|------|
| Split Out | 数据拆分 |
| Imagen 3.0 | HTTP Request |
| Variables | 数据设置 |
| Download Image | HTTP Request |
| On form submission | 表单触发器 |
| Form Validation | IF 判断 |
| Retry Form | 表单 |
| Upload to Cloudinary | HTTP Request |
| Convert to File1 | 转换为文件 |
| Generate HTML | HTML |
| Convert to File | 转换为文件 |
| Form Ending | 表单 |
| Has Email? | IF 判断 |
| Send Results to Email | Email 发送 |
| Image to Base64 | 从文件提取 |
| Gemini 2.0 | HTTP Request |

## 触发方式
- On form submission 触发

## 统计
- 节点总数：16
- 触发节点：1
- 处理节点：10
- 输出节点：5
- 分类：devops
