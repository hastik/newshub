---
title: MCP slaví dva roky – Skills over MCP v betě, Tasks a Elicitation GA v Claude
url: https://claude.com/resources/articles/skills-over-mcp-tasks-and-more
source: Anthropic (Claude)
published: 2026-11-24
added: 2026-11-27
category: ai
tags:
  - agenti
  - api
  - nastroje
  - workflow
related_urls:
  - https://blog.modelcontextprotocol.io/posts/mcp-turns-two/
  - https://modelcontextprotocol.io/extensions/skills/overview
---

K druhému výročí Model Context Protocolu Anthropic oznámil, že MCP servery mohou spolu s nástroji publikovat i skills (návody a workflow ve formátu SKILL.md), které si Claude načte, až když je potřebuje. Skills over MCP jsou ve veřejné betě v Claude a Claude Code a používají je např. Shopify, HubSpot a Atlassian. GA jsou rozšíření Tasks (server může běžet dlouho nebo spustit celou agentní smyčku na pozadí, zatímco Claude pracuje dál) a Elicitation (server se uprostřed volání zeptá uživatele na potvrzení nebo vstup, třeba před placenou nebo destruktivní akcí). Brzy přibude File Uploads pro předávání PDF, tabulek a obrázků serveru mimo kontextové okno. MCP má podle Anthropicu přes 700 milionů stažení SDK měsíčně a přes 10 000 konektorů pro Claude.

## Proč je to důležité

MCP se mění z „volání nástrojů“ na protokol pro spolupráci s jinými agenty: server dodá i know-how, jak se nástroje používají, umí dlouhé úlohy a bezpečné potvrzení člověkem. Kdo staví vlastní MCP server (třeba nad interními daty nebo ProcessWire webem), může teď přibalit i postup práce a schvalovací krok. Jde o otevřený standard, takže to nefunguje jen v Claude. Spolu se zprávou o Google Workspace MCP to potvrzuje, že MCP je dnes výchozí cesta, jak agenty napojovat na systémy.
