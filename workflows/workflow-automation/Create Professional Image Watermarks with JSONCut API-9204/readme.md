## 简介
**Create Professional Image Watermarks with JSONCut API**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：11 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/9204

---

# Create Professional Image Watermarks with JSONCut API


## 节点清单

| 节点 | 类型 |
|------|------|
| Form Trigger | 表单触发器 |
| Upload Main Image | HTTP Request |
| Upload Watermark | HTTP Request |
| Merge Uploads | 数据合并 |
| Wait | 等待 |
| If Success | IF 判断 |
| If Error | IF 判断 |
| Download Image | HTTP Request |
| Error Stop | 停止并报错 |
| Aggregate | 数据聚合 |
| Create JsonCut Job | HTTP Request |
| Check JsonCut job Status | HTTP Request |

## 触发方式
- Form Trigger 触发

## 统计
- 节点总数：12
- 触发节点：1
- 处理节点：6
- 输出节点：5
- 分类：workflow-automation
