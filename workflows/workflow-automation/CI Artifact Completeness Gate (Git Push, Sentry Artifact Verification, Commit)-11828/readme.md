# CI Artifact Completeness Gate (Git Push, Sentry Artifact Verification, Commit)

https://n8nworkflows.xyz/workflows/11828

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
