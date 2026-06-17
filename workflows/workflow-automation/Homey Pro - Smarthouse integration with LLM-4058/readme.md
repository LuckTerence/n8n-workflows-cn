## 简介
**Homey Pro - Smarthouse integration with LLM**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/4058

---

# Homey Pro - Smarthouse integration with LLM


## 节点清单

| 节点 | 类型 |
|------|------|
| OpenAI Chat Model | OpenAI Chat Model |
| output | 数据设置 |
| Workflow Input Trigger | 执行工作流触发器 |
| Smarthus Agent | AI Agent |
| Slå_På_Tv_i_stuen | 工作流工具 |
| Slå_av_Tv_i_stuen | 工作流工具 |
| steng_gardiner_i_hovedetasjen | 工作流工具 |
| apne_gardiner_i_hovedetasjen | 工作流工具 |
| Sla_pa_apple_tv_i_hovedetasjen | 工作流工具 |
| sla_på_mac_i_hovedetasjen | 工作流工具 |
| sla_pa_peis_i_hovedetasjen | 工作流工具 |
| steng_gardiner_mot_ost | 工作流工具 |
| sla_av_taklys_i_stuen | 工作流工具 |
| sla_pa_taklys_i_stuen | 工作流工具 |
| hovedetasjen_belysning_0 | 工作流工具 |
| hovedetasjen_belysning_10 | 工作流工具 |
| hovedetasjen_belysning_25 | 工作流工具 |
| hovedetasjen_belysning_50 | 工作流工具 |
| hovedetasjen_belysning_75 | 工作流工具 |
| hovedetasjen_full_belysning | 工作流工具 |
| film_i_hovedetasjen | 工作流工具 |
| vekk_siri_i_hovedetasjen | 工作流工具 |
| hent_tempratur_i_stuen | 工作流工具 |
| demp_belysning_pa_soverom | 工作流工具 |
| sla_av_begge_tv_pa_soverom | 工作流工具 |
| sla_av_lg_tv_pa_soverom | 工作流工具 |
| sla_av_samsung_tv_pa_soverom | 工作流工具 |
| sla_av_soverom | 工作流工具 |
| sla_av_taklyset_pa_soverom | 工作流工具 |
| sla_pa_apple_tv_pa_soverom | 工作流工具 |
| sla_pa_mac_pa_soverom | 工作流工具 |
| solskjerming_dag | 工作流工具 |
| solskjerming_lufting_nede | 工作流工具 |
| solskjerming_lufting_overst | 工作流工具 |
| solskjerming_natt | 工作流工具 |
| hjemmekontor | 工作流工具 |
| hjemmekontor_kveld | 工作流工具 |
| sla_pa_mac_i_soverom_med_en_skjerm | 工作流工具 |
| apne_solskjerming | 工作流工具 |
| sla_pa_taklys_pa_soverom | 工作流工具 |
| sla_av_taklys_pa_soverom | 工作流工具 |
| dimme_taklys_pa_soverom_10_prosent | 工作流工具 |
| dimme_taklys_pa_soverom_20_prosent1 | 工作流工具 |
| dimme_taklys_pa_soverom_30_prosent | 工作流工具 |
| dimme_taklys_pa_soverom_40_prosent1 | 工作流工具 |
| dimme_taklys_pa_soverom_50_prosent | 工作流工具 |
| dimme_taklys_pa_soverom_60_prosent1 | 工作流工具 |
| dimme_taklys_pa_soverom_70_prosent | 工作流工具 |
| dimme_taklys_pa_soverom_80_prosent | 工作流工具 |
| dimme_taklys_pa_soverom_90_prosent | 工作流工具 |
| dimme_taklys_pa_soverom_100_prosent | 工作流工具 |
| hent_tempratur_pa_soverom | 工作流工具 |
| sla_av_prosjektor_i_kino | 工作流工具 |
| sla_pa_prosjektor_i_kino | 工作流工具 |
| Sla_pa_apple_tv_i_kino | 工作流工具 |
| Sla_pa_mac_i_kino | 工作流工具 |
| sla_pa_musikk_i_hele_kjelleren | 工作流工具 |
| sla_pa_disco | 工作流工具 |
| sla_av_disco | 工作流工具 |
| 19_grader_i_kino | 工作流工具 |
| 21_grader_i_kino_ | 工作流工具 |
| 20_grader_i_kino | 工作流工具 |
| 22_grader_i_kino | 工作流工具 |
| 23_grader_i_kino | 工作流工具 |
| 24_grader_i_kino | 工作流工具 |
| 25_grader_i_kino | 工作流工具 |
| hent_tempratur_ute | 工作流工具 |
| kjeller_belysning_100_prosent | 工作流工具 |
| kjeller_belysning_20_prosent | 工作流工具 |
| kjeller_belysning_40_prosent | 工作流工具 |
| kjeller_belysning_60_prosent | 工作流工具 |
| kjeller_belysning_80_prosent | 工作流工具 |
| sla_av_belysning_i_hovedetasjen | 工作流工具 |
| kjeller_belysning_5_prosent | 工作流工具 |
| kino_belysning_10_prosent | 工作流工具 |
| kino_belysning_20_prosent | 工作流工具 |
| kino_belysning_30_prosent | 工作流工具 |
| kino_belysning_40_prosent | 工作流工具 |
| kino_belysning_50_prosent | 工作流工具 |
| kino_belysning_60_prosent | 工作流工具 |
| kino_belysning_70_prosent | 工作流工具 |
| kino_belysning_80_prosent | 工作流工具 |
| kino_belysning_90_prosent | 工作流工具 |
| kino_belysning_av | 工作流工具 |
| tempratur_i_badebasseng | 工作流工具 |
| avfukter_pa_vaskerom_av | 工作流工具 |
| avfukter_pa_vaskerom_pa | 工作流工具 |
| blalys_kino_pa | 工作流工具 |
| blalys_kino_av | 工作流工具 |
| Ylva_solskjerming_lukket | 工作流工具 |
| Ylva_solskjerming_apen | 工作流工具 |
| kjeller_belysning_0_prosent | 工作流工具 |
| xAI Grok Chat Model | lmChatXAiGrok |
| pause spotify | 工作流工具 |
| sjekk_garasjeport | 工作流工具 |
| apne_garasjeport | 工作流工具 |
| steng_garasjeport | 工作流工具 |
| sjekk_status_alle_enheter | 工作流工具 |



## 功能说明

Homey Pro - Smarthouse integration with LLM（AI 增强)手动或子流程调用，通过 n8n 内置节点实现自动化。

手动触发，通过 工作流编排 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：98
- 触发方式：手动或子流程调用

## 触发方式
- Workflow Input Trigger 触发

## 统计
- 节点总数：98
- 触发节点：1
- 处理节点：97
- 输出节点：0
- 分类：workflow-automation
