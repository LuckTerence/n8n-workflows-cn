# Solve captchas via webhook with CapSolver

https://n8nworkflows.xyz/workflows/14894

## 节点清单

| 节点 | 类型 |
|------|------|
| Webhook CAPTCHA Trigger | Webhook |
| Validate Request | Code |
| Select CAPTCHA Solver | Switch 路由 |
| Solve reCAPTCHA v2 | capSolver |
| Solve reCAPTCHA v3 | capSolver |
| Solve Turnstile CAPTCHA | capSolver |
| Solve AWS WAF CAPTCHA | capSolver |
| Solve GeeTest v3 | capSolver |
| Solve GeeTest v4 | capSolver |
| Solve MTCaptcha | capSolver |
| Image Text Extraction | capSolver |
| Vision Engine Execution | capSolver |
| Format Solution | Code |
| Handle Unsupported CAPTCHA | 响应 Webhook |
| Provide CAPTCHA Solution | 响应 Webhook |

## 触发方式
- Webhook CAPTCHA Trigger 触发

## 统计
- 节点总数：15
- 触发节点：1
- 处理节点：12
- 输出节点：2
- 分类：workflow-automation
