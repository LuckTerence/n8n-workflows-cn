## 简介
**Convert PDF to PNG with PDF.co API (Multi-Page Support)**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3847

---

# Convert PDF to PNG with PDF.co API (Multi-Page Support)


## 节点清单

| 节点 | 类型 |
|------|------|
| Pass through binary | 数据设置 |
| Get Presigned Upload URL (PDF.co) | HTTP Request |
| Combine binary and json data | 数据合并 |
| Upload PDF to Presigned URL | HTTP Request |
| Strip binary data | 数据设置 |
| Combine data | 数据合并 |
| Convert PDF to PNG (PDF.co) | HTTP Request |
| Download PNG from PDF.co | HTTP Request |
| When clicking ‘Test workflow’ | 手动触发 |
| Split multipage PDF files | HTTP Request |
| Compress into zip file | compression |
| Combine binaries | 数据聚合 |
| GET example PDF files | HTTP Request |
| Extract PDF links | HTML |
| Split links into items | 数据拆分 |
| Use two relevant PDF examples | 数据限制 |
| Download example PDF Files | HTTP Request |
| Split out urls | 数据拆分 |
| Loop over pdf files | 分批处理 |

## 触发方式
- When clicking ‘Test workflow’ 触发

## 统计
- 节点总数：19
- 触发节点：1
- 处理节点：11
- 输出节点：7
- 分类：workflow-automation
