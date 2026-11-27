---
title: Anthropic přepsal Messages API z Pythonu do Rustu pomocí agentů Claude – o 70 % méně CPU, ověřování přes produkční provoz
url: https://www.anthropic.com/research/migrating-api-to-rust
source: Anthropic
published: 2026-11-25
added: 2026-11-27
category: ai
tags:
  - agenti
  - workflow
  - multiagent
related_urls:
  - https://www.techrepublic.com/article/news-anthropic-claude-messages-api-rust-migration/
---

Anthropic popsal, jak agenty Claude převedl své Messages API (přes ně jde provoz Claude Code i zákazníků) z Pythonu do Rustu, aniž by službu vypnul nebo zmrazil vývoj. Claude napsal první verzi hlavní cesty požadavku zhruba za týden. Těžší bylo ověřit, že se nová verze chová stejně jako produkční. Řešení: produkční API se samo stalo verifikátorem. Rustová verze dostávala kopii živého provozu, rozdíly se automaticky vyhodnocovaly a agenti dostávali úkoly je opravit. Lidé schvalovali opravy a postupně se přesunuli od řízení agentů k psaní pravidel a kontrol. Výsledek: asi o 70 % méně CPU na požadavek a o 20 % kratší medián času do prvního tokenu, veřejný provoz běží na Rustu od září 2026.

## Proč je to důležité

Je to podrobný popis práce s agenty na velkém živém systému od firmy, která je vyrábí. Hlavní poučení: generovat kód je snadné, úzkým hrdlem je ověřování. Kdo chce nechat agenty přepsat nebo migrovat cokoli živého (WMS integraci, interní nástroj, web), potřebuje nejdřív spolehlivý způsob, jak porovnat „staré vs. nové“ na reálných datech. Teprve pak má smysl pouštět agenty ve smyčce. Vzor „jednoduché smyčky kolem silných verifikátorů“ se dá přenést i do menších projektů.
