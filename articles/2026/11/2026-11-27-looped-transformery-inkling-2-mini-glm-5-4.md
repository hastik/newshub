---
title: Looped transformery přicházejí – Inkling 2 Mini pro notebook a GLM-5.4 jako vlajková loď Z.ai
url: https://thinkingmachines.ai/news/inkling-2-mini/
source: Thinking Machines Lab
published: 2026-11-20
added: 2026-11-27
category: ai
tags:
  - modely
  - lokalni-ai
  - vydani
related_urls:
  - https://huggingface.co/blog/inkling2mini
  - https://z.ai/blog/glm-5.4
  - https://simonwillison.net/2026/Nov/23/glm-54/
---

Thinking Machines Lab vydal Inkling 2 Mini, otevřený multimodální MoE model (~26 mld. parametrů celkem, ~3 mld. aktivních, kontext 1M tokenů), který prostředních 12 vrstev prochází třikrát na každý token. Model tak „přemýšlí hlouběji“ bez dalších parametrů a je dost malý na lokální běh. Podle firmy vede mezi otevřenými modely pod 100 mld. parametrů v DeepSWE v1.1 (48,2 %). Hugging Face hned dodal podporu v transformers, llama.cpp a MLX a ve vlastních testech ho řadí aspoň na úroveň Qwen 3.8 27B. O tři dny později Z.ai vydal GLM-5.4, první vlajkový model na stejném principu (v 750B modelu běží 28 vrstev dvakrát). Na 30B modelu stejné architektury se smyčkou spotřeboval na většině benchmarků o 10–14 % méně výstupních tokenů. GLM-5.4 je zatím jen přes GLM Coding Plan, otevřené váhy firma slibuje později.

## Proč je to důležité

Opakování vrstev je nový způsob, jak dostat víc „uvažování“ z menšího modelu. Rychle se uchytil u dvou nezávislých laboratoří během jednoho týdne. Prakticky: Inkling 2 Mini je jeden z nejsilnějších modelů na lokální běh pro agentní kódování (přes llama.cpp nebo MLX) a vyplatí se ho zkusit tam, kde nechceš posílat data do cloudu. U GLM-5.4 jde spíš o signál, že levnější čínské coding modely dál dohánějí frontier. Benchmarky jsou zatím hlavně od autorů.
