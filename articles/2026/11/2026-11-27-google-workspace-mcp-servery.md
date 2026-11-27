---
title: Google Workspace MCP servery a CLI jsou GA – od 1. 2. 2027 musí AI agenti do Gmailu, Disku a Kalendáře přes ně
url: https://workspaceupdates.googleblog.com/2026/11/mcp-servers-cli-standardized-usage-tiers-now-available.html
source: Google Workspace Updates
published: 2026-11-24
added: 2026-11-27
category: ai
tags:
  - agenti
  - api
  - nastroje
  - automatizace-kancelare
related_urls:
  - https://developers.google.com/workspace/guides/configure-mcp-servers
  - https://developers.google.com/workspace/guides/quota-usage-tiers
  - https://www.techrepublic.com/article/news-google-workspace-ai-agent-access/
---

Google zpřístupnil obecně (GA) hostované Workspace MCP servery pro Gmail, Disk, Dokumenty, Tabulky, Prezentace, Kalendář, Chat a Tasks (Keep brzy) a oficiální Workspace CLI pro agenty běžící v terminálu. Zároveň mění pravidla. AI agenti a podobné nástroje budou smět k datům Workspace jen přes MCP servery nebo CLI, ne přímo přes REST API. Technické vynucení začne 1. února 2027. API dostávají dva tarify: Standard zdarma s publikovanými limity a Scaled s placením nad denní free limit od 1. dubna 2027. OAuth klienty pro agenty je potřeba označit jako „AI-powered agent“ (is_agentic). Admini získají audit log akcí agentů, pravidla pro potvrzení citlivých akcí člověkem a DLP. Nový dodatek AI Tools Addendum zakazuje mj. dlouhodobé ukládání dat z API a scraping přes agenty.

## Proč je to důležité

Pokud používáš nebo stavíš agenty, kteří čtou poštu, kalendář nebo Disk přes Google API (vlastní skripty, n8n, různé asistenty), do února je musíš přepnout na MCP/CLI, jinak přestanou fungovat. Prakticky to znamená zkontrolovat, přes co se tvoje automatizace k Workspace připojují, a nastavit OAuth klienty pro agenty zvlášť. Pro firmu je to zase cesta, jak mít agenty pod správou admina s audit logem. Google uvádí, že přes 99 % vývojářů se vejde do bezplatného tarifu.
