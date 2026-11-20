---
title: Tool Retrieval v Gemini API – agent si načítá schémata nástrojů až když je potřebuje
url: https://blog.google/innovation-and-ai/technology/developers-tools/gemini-api-tool-retrieval/
source: Google
published: 2026-11-19
added: 2026-11-20
category: ai
tags:
  - agenti
  - api
  - nastroje
  - workflow
---

Google přidal do Interactions API v Gemini (preview) funkci Tool Retrieval. Do requestu se přidá nástroj `tool_search` a u ostatních nástrojů se nastaví `defer_loading: true`. Model pak vidí jen jejich názvy a popisy a plné schéma parametrů si načte až ve chvíli, kdy nástroj potřebuje, a to v rámci stejného requestu. Funguje to i se vzdálenými MCP servery (odloží se celý server najednou), nic se za to zvlášť neplatí a podporuje to Gemini 3.6 a novější. Je i varianta, kde vyhledávání ve vlastním registru nástrojů běží na straně klienta.

## Proč je to důležité

U agentů napojených na desítky nástrojů a MCP serverů roste cena i chybovost výběru nástroje s každým dalším schématem v promptu. Odložené načítání tohle řeší bez vlastního vyhledávacího indexu a nerozbíjí prefix cache. Stejný vzor už mají i další platformy, takže jde o dobrou praxi pro návrh vlastních agentů nad firemními systémy (WMS, ERP, helpdesk).
