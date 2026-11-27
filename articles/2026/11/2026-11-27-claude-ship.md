---
title: Claude Ship – agenti, kteří pull request zrevidují, opraví a podle pravidel týmu schválí
url: https://claude.com/resources/articles/introducing-claude-ship
source: Anthropic (Claude)
published: 2026-11-23
added: 2026-11-27
category: ai
tags:
  - agenti
  - nastroje
  - workflow
  - vydani
related_urls:
  - https://code.claude.com/docs/en/ship-command
  - https://code.claude.com/docs/en/claude-ship
---

Anthropic spustil v betě Claude Ship, sadu pro celou cestu pull requestu po napsání kódu. Code Review (už GA) dělá hloubkovou revizi v úrovních Quick, Standard a Deep. Nový PR Steward opravuje padající CI, merge konflikty a připomínky z review, po každém pushi napíše, co změnil a jak to vrátit, ale sám neschvaluje ani nemerguje. Claude Approvals pak podle politiky uložené jako soubor v repu rutinní změny schválí sám a citlivější pošle člověku. Doporučuje se začít v režimu jen pozorování. Vývojář si to může vyzkoušet příkazem `/ship` v Claude Code: Claude změnu pushne, otevře PR, zreviduje ho a dotahuje opravy. Dostupné je to pro plány Team a Enterprise na GitHubu a účtuje se podle tokenů.

## Proč je to důležité

Když agent napíše většinu kódu, úzkým hrdlem je review a schvalování. Claude Ship je první větší produkt, který tuhle část automatizuje s pravidly, která tým sám definuje. Pro tebe je zajímavý hlavně `/ship` v Claude Code u vlastních projektů a pro tým model „politika schvalování jako soubor v repu“. Anthropic sám uvádí příklad, kdy produktový manažer nechal agenta otevřít PR na opravu dokumentace a ten se ještě týž večer mergoval.
