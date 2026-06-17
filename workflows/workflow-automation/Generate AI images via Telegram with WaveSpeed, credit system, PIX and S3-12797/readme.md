## 简介
**Generate AI images via Telegram with WaveSpeed, credit system, PIX and S3**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：88 | 难度：⭐⭐⭐ 高级
> 原始来源：https://n8nworkflows.xyz/workflows/12797

---

# Generate AI images via Telegram with WaveSpeed, credit system, PIX and S3


## 节点清单

| 节点 | 类型 |
|------|------|
| WaveSpeed text-to-image submit | waveSpeedTaskSubmit |
| newOptionAfterConfig | Telegram |
| sendOptionsWelcome | Telegram |
| welcomeMessage | Telegram |
| resolutionConfig | Telegram |
| aspectRatioConfig | Telegram |
| upsertStatusReturn | 数据表 |
| upsertStatusConfig | 数据表 |
| switchReturn/Config | Switch 路由 |
| switchMaster | Switch 路由 |
| getUser | 数据表 |
| updateUserFirstAccess | 数据表 |
| welcomeGenerateImage | Telegram |
| sendForceReply | Telegram |
| editImageOnReply | waveSpeedTaskSubmit |
| editFields | 数据设置 |
| messageType | Switch 路由 |
| getFilePath | HTTP Request |
| downloadImage | HTTP Request |
| uploadS3 | S3 |
| swtichW/WOCallback | Switch 路由 |
| upsertUserStatus | 数据表 |
| messageTypeGenerateImage | Switch 路由 |
| ifImage+Caption | IF 判断 |
| ifCreditsEnough | IF 判断 |
| ifCreditsEnough1 | IF 判断 |
| ifCreditsEnough2 | IF 判断 |
| welcomeImageEdit | Telegram |
| promptConfig | Telegram |
| switchPromptAction | Switch 路由 |
| upsertStatusWaitingPrompt | 数据表 |
| upsertClearPrompt | 数据表 |
| upsertSkipPrompt | 数据表 |
| askPromptInput1 | Telegram |
| upsertSavePrompt1 | 数据表 |
| confirmPromptSaved1 | Telegram |
| menuOptions | Telegram |
| sendDepositOptions | Telegram |
| switchDeposit | Switch 路由 |
| getPaymentStatus | HTTP Request |
| paymentStatus | Webhook |
| sendOptionsAfterPayment | Telegram |
| depositCredentials | 数据设置 |
| checkIfDepositInProgress | IF 判断 |
| setDepositAmount3 | 数据设置 |
| setDepositAmount6 | 数据设置 |
| setDepositAmount10 | 数据设置 |
| insertPaymentRow | 数据表 |
| apiMercadoPago | HTTP Request |
| getPix | 数据设置 |
| pix_baseToFile | 转换为文件 |
| sendPixQRCode | Telegram |
| sendPixText | Telegram |
| raceConditionDelay | 等待 |
| switchForPaymentStatus | Switch 路由 |
| checkIfPaymentPending | IF 判断 |
| fetchPaymentRecord | 数据表 |
| upsertPaymentStatus | 数据表 |
| getUserAfterPayment | 数据表 |
| updateUserCreditsAfterPayment | 数据表 |
| paymentConfirmedText | Telegram |
| updateUserStatusAfterDecline | 数据表 |
| getUserAfterDecline | 数据表 |
| paymentDeclinedText | Telegram |
| qrCodePaymentInProgress | Telegram |
| updateCreditsSendedTask | 数据表 |
| notCreditsEnoughMessage | Telegram |
| taskSubmitedGenerate | Telegram |
| sendActionGenerate | Telegram |
| checkTaskGenerate | wavespeedTaskStatus |
| waitGenerateStatus | 等待 |
| switchTaskGenerate | Switch 路由 |
| getImage | HTTP Request |
| sendFailedGenerate | Telegram |
| resizeImage | 图片编辑 |
| updateCreditOnFail | 数据表 |
| sendGeneratedImage | Telegram |
| Send a text message1 | Telegram |
| If demo sended1 | IF 判断 |
| Welcome | Telegram |
| Send welcome media | Telegram |
| Update welcome_demo_sended | 数据表 |
| Fields Chat | 数据设置 |
| Update use_edit_demo | 数据表 |
| Edit image question | Telegram |
| If use_edit_demo1 | IF 判断 |
| Send a media group demo1 | Telegram |
| Welcome image edit message | Telegram |
| Global env | 数据设置 |
| Telegram Trigger | Telegram 触发器 |

## 触发方式
- paymentStatus 触发
- Telegram Trigger 触发

## 统计
- 节点总数：90
- 触发节点：2
- 处理节点：53
- 输出节点：35
- 分类：workflow-automation
