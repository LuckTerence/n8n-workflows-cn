## 简介
**Generate 360° Virtual Try-on Videos for Clothing with Kling API (unofficial)**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：12 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/3411

---

# Generate 360° Virtual Try-on Videos for Clothing with Kling API (unofficial)


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Test workflow’ | 手动触发 |
| Kling Virtual Try-On Task | HTTP Request |
| Switch | Switch 路由 |
| Get Kling Video Task | HTTP Request |
| Generate kling video | HTTP Request |
| Preset Parameters | 数据设置 |
| Get Kling Virtual Try-On Task | HTTP Request |
| Check Data Status | IF 判断 |
| Wait for Image Generation | 等待 |
| Wait for Video Generation | 等待 |
| Check Video Data Status | Switch 路由 |
| Get Video Data Status | IF 判断 |
| Get Final Video URL | 数据设置 |

## 触发方式
- When clicking ‘Test workflow’ 触发

## 统计
- 节点总数：13
- 触发节点：1
- 处理节点：8
- 输出节点：4
- 分类：devops
