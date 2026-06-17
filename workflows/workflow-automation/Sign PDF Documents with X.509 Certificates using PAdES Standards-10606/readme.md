## 简介
**Sign PDF Documents with X.509 Certificates using PAdES Standards**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/10606

---

# Sign PDF Documents with X.509 Certificates using PAdES Standards


## 节点清单

| 节点 | 类型 |
|------|------|
| Check Java | 执行命令 |
| Java Missing? | IF 判断 |
| Get Install Script | HTTP Request |
| Write Install Script | 读写文件 |
| Install Dependencies | 执行命令 |
| Extract Password | 数据设置 |
| Read Signed PDF | 读取二进制文件 |
| Return Signed PDF | 响应 Webhook |
| Get Cleanup Script | HTTP Request |
| Write Cleanup Script | 读写文件 |
| Cleanup | 执行命令 |
| Add Codegic Trust | 执行命令 |
| Without Visible? | IF 判断 |
| Switch Sign Visible | Switch 路由 |
| Write Files : PDF | 读写文件 |
| Write Files : PFX | 读写文件 |
| Write Files : LOGO | 读写文件 |
| Write JAR | 读写文件 |
| Get JAR | HTTP Request |
| Get Process Script | HTTP Request |
| Write Process Script | 读写文件 |
| Get Trust Script | HTTP Request |
| Write Trust Script | 读写文件 |
| Get Cert Script | HTTP Request |
| Write Cert Script | 读写文件 |
| Run Cert Script | 执行命令 |
| Read PDF | 读写文件 |
| Write PDF | 读写文件 |
| Read PFX | 读写文件 |
| Write PFX | 读写文件 |
| Show Visible | 数据设置 |
| No Visible | 数据设置 |
| B | 数据设置 |
| T | 数据设置 |
| LT | 数据设置 |
| LTA | 数据设置 |
| Components | 数据设置 |
| Sign PDF | 执行命令 |
| Webhook | Webhook |
| Webhook - LandingPage-LangHU | Webhook |
| Respond to Webhook - LandingPage-LangHU | 响应 Webhook |
| Webhook - LandingPage-LangEN | Webhook |
| Respond to Webhook - LandingPage-LangEN | 响应 Webhook |
| Webhook - LandingPage-LangDE | Webhook |
| Respond to Webhook - LandingPage-LangDE | 响应 Webhook |
| Get LandingPage-LangEN | HTTP Request |
| Get LandingPage-LangDE | HTTP Request |
| Get LandingPage-LangHU | HTTP Request |

## 触发方式
- Webhook 触发
- Webhook - LandingPage-LangHU 触发
- Webhook - LandingPage-LangEN 触发
- Webhook - LandingPage-LangDE 触发

## 统计
- 节点总数：48
- 触发节点：4
- 处理节点：31
- 输出节点：13
- 分类：workflow-automation
