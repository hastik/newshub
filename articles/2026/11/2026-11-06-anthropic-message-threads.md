---
title: Anthropic Message Threads – rychlejší dlouhé agenty na Messages API
url: https://claude.com/resources/articles/message-threads
source: Anthropic / Claude
published: 2026-11-02
added: 2026-11-06
category: ai
tags:
  - agenti
  - api
  - workflow
  - ovladani-pocitace
  - vydani
related_urls:
  - https://platform.claude.com/docs/en/build-with-claude/message-threads
---

Veřejná beta Message Threads na Messages API: agent pošle historii jednou a pak jen nové turny plus ID předchozí odpovědi. Vlákno drží server v šifrované paměti (expiruje 5 minut po posledním requestu). U Claude Code sessions s 500k–1M tokeny medián TTFT klesá asi o 35 %; tokeny a rate limity se nemění. Dostupné na Claude Platform i přes AWS, Foundry a Anthropic-managed Google Cloud.

## Proč je to důležité

Praktická latence u coding a computer-use agentů – méně opětovného nahrávání screenshotů a tool traces bez změny modelu. Přímo ovlivňuje, jak rychle běží dlouhé agentní workflow, které Ondřej používá.
