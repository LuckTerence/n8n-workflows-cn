## 简介
**Automate CV Screening & Candidate Validation with AI & Email Parsing**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/6216

---

# Automate CV Screening & Candidate Validation with AI & Email Parsing


## 节点清单

| 节点 | 类型 |
|------|------|
| Trigger on New CV Email	 | Email 读取 |
| Extract Text from PDF CV	 | 从文件提取 |
| Ensure All CV Data Loaded	 | 等待 |
| Parse & Structure CV Information	 | Code |
| Check CV for Required Fields	 | IF 判断 |
| Save Valid CV to Folder	 | 执行命令 |
| Notify HR of Invalid CV	 | Email 发送 |

## 触发方式
- 手动触发

## 统计
- 节点总数：7
- 触发节点：0
- 处理节点：5
- 输出节点：2
- 分类：workflow-automation
