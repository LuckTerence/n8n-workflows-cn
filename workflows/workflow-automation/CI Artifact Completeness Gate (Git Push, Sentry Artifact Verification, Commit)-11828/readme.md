## 简介
**CI Artifact Completeness Gate (Git Push, Sentry Artifact Verification, Commit)**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/11828

---

# CI Artifact Completeness Gate (Git Push, Sentry Artifact Verification, Commit)


## 节点清单

| 节点 | 类型 |
|------|------|
| Verify Artifacts | Code |
| GithubPushTrigger | githubTrigger |
| Check Sentry Artifacts Releases | HTTP Request |
| Check Sentry Artifacts files | HTTP Request |
| Update Status | HTTP Request |
| Artifacts Validation and Get Repository Data | Code |

## 触发方式
- GithubPushTrigger 触发

## 统计
- 节点总数：6
- 触发节点：1
- 处理节点：2
- 输出节点：3
- 分类：workflow-automation
