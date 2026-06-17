# Automated GA4 Analytics Data Backfill to BigQuery with Telegram Alerts

https://n8nworkflows.xyz/workflows/11010

## 节点清单

| 节点 | 类型 |
|------|------|
| GA4 - Session Channel Group | Google Analytics |
| BQ - ga4_data_session_channel_group | Google BigQuery |
| GA4 - Session Source/Campaign/Medium | Google Analytics |
| BQ - ga4_data_session_source_campaign_medium | Google BigQuery |
| GA4 - Country/Language/City | Google Analytics |
| BQ - ga4_data_country_language_city | Google BigQuery |
| GA4 - Item Name | Google Analytics |
| BQ - ga4_data_item_name | Google BigQuery |
| GA4 - Browser/OS/Device | Google Analytics |
| BQ - ga4_data_browser_os_device | Google BigQuery |
| GA4 - First User Source/Medium | Google Analytics |
| BQ - ga4_data_first_user_source_medium | Google BigQuery |
| GA4 - First User Channel Group | Google Analytics |
| BQ - ga4_data_first_user_channel_group | Google BigQuery |
| GA4 - Ads Data | Google Analytics |
| BQ - ga4_ads_data | Google BigQuery |
| GA4 - All Metrics | Google Analytics |
| BQ - ga4_all_metrics_data | Google BigQuery |
| GA4 - Event Metrics | Google Analytics |
| BQ - ga4_event_metrics_data | Google BigQuery |
| GA4 - Page Location | Google Analytics |
| BQ - ga4_page_location_data | Google BigQuery |
| GA4 - Landing Page | Google Analytics |
| GA4 - Transaction Items | Google Analytics |
| BQ - ga4_transaction_items | Google BigQuery |
| Backfill Config | 数据设置 |
| Schedule Trigger | 定时触发器 |
| BQ - ga4_landing_page_data | Google BigQuery |
| Merge | 数据合并 |
| Merge1 | 数据合并 |
| Code | Code |
| Send a text message | Telegram |

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：32
- 触发节点：1
- 处理节点：30
- 输出节点：1
- 分类：workflow-automation
