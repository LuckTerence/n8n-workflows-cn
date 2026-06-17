## 简介
**Anonymize Faces and License Plates in Media with BlurIt**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/8535

---

# Anonymize Faces and License Plates in Media with BlurIt


## 节点清单

| 节点 | 类型 |
|------|------|
| Set Auth Config | 数据设置 |
| Auth Get Token | HTTP Request |
| Upload Input File | 表单触发器 |
| Create Blurit Task | HTTP Request |
| Merge | 数据合并 |
| Wait | 等待 |
| Get Task Status | HTTP Request |
| Switch | Switch 路由 |
| Get Result File | HTTP Request |

## 触发方式
- Upload Input File 触发

## 统计
- 节点总数：9
- 触发节点：1
- 处理节点：4
- 输出节点：4
- 分类：workflow-automation
