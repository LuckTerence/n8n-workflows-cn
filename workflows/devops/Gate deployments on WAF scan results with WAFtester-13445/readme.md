# Gate deployments on WAF scan results with WAFtester

https://n8nworkflows.xyz/workflows/13445

## 节点清单

| 节点 | 类型 |
|------|------|
| Deploy Webhook | Webhook |
| Detect WAF | HTTP Request |
| Start Scan | HTTP Request |
| Wait for Scan | 等待 |
| Poll Task Status | HTTP Request |
| Parse Results | Code |
| Pass or Fail? | IF 判断 |
| Respond Pass | 响应 Webhook |
| Respond Fail | 响应 Webhook |

## 触发方式
- Deploy Webhook 触发

## 统计
- 节点总数：9
- 触发节点：1
- 处理节点：3
- 输出节点：5
- 分类：devops
