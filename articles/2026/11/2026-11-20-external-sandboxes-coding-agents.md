---
title: Externí sandboxy pro coding agenty – agent zůstane venku, jeho příkazy běží v izolovaném Linuxu
url: https://blog.primeradiant.com/external-sandboxes-for-coding-agents/
source: Prime Radiant (Simon Willison)
published: 2026-11-16
added: 2026-11-20
category: ai
tags:
  - agenti
  - kyberbezpecnost
  - nastroje
  - lokalni-ai
related_urls:
  - https://github.com/prime-radiant-inc/external-sandbox
---

Simon Willison s laboratoří Prime Radiant zveřejnil vzor „external sandbox“. Claude Code, Codex nebo Pi běží normálně na vašem počítači, ale každý příkaz, který spustí, se vykoná v izolovaném Alpine Linuxu. Ten vidí jen připojené složky a bez povolení nemá síť. Proxy pouští jen povolené hosty a API klíče doplňuje sama, takže je agent nevidí. K dispozici jsou tři implementace se stejným protokolem (v86 ve WebAssembly, Apple Containers, Microsoft Quicksand s QEMU) a vyzkoušet to jde dvěma příkazy přes `npx`.

## Proč je to důležité

Je to praktická odpověď na dilema „schvalovat každý krok, nebo agentovi dát celý počítač“. Hodí se hlavně při zkoušení slabších nebo lokálních modelů a při riziku prompt injection. Autoři výslovně uvádějí, že jde o experimentální prototypy bez bezpečnostního auditu a že zapisovatelná složka může být poškozena, takže ji mějte ve verzovacím systému.
