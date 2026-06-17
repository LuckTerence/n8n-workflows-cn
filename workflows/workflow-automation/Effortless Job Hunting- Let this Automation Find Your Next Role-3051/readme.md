## 简介
**Effortless Job Hunting: Let this Automation Find Your Next Role**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Google Drive)（基本改完，配置 API Key 应该就能跑）
> 节点数：7 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/3051

---

# Effortless Job Hunting: Let this Automation Find Your Next Role


## 节点清单

| 节点 | 类型 |
|------|------|
| On clicking 'execute' | 手动触发 |
| Read PDF | readPDF |
| Download Resume (PDF File) | Google Drive |
| Filter Relevant Information | 数据拆分 |
| Analyse Resume | OpenAI |
| Find Suitable Job Offers  | HTTP Request |
| Organise the Job Posts | 数据拆分 |
| Upload Job Posts Organised in a Spreadsheet | Google Sheets |

## 触发方式
- On clicking 'execute' 触发

## 统计
- 节点总数：8
- 触发节点：1
- 处理节点：6
- 输出节点：1
- 分类：workflow-automation
