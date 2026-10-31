---
title: "Shallot po 0.10.2: lepší import glTF modelů, tangenty přes MikkTSpace a port Box3D fyziky"
url: https://github.com/dylanebert/shallot/compare/v0.10.2...main
source: GitHub – dylanebert/shallot
published: 2026-10-31
added: 2026-10-31
category: gemdevspec
tags:
  - shallot
  - dylan-ebert
  - devlog
  - funkcionalita
  - fyzika
related_urls:
  - https://github.com/dylanebert/shallot/commit/1291a9c1
  - https://github.com/dylanebert/shallot/commit/6f91bce7
---

Hned po vydání 0.10.2 přibylo v hlavní větvi přes 25 commitů, hlavně do importu glTF modelů (sparse accessory, vertex streamy, textury standardního materiálu podle role, výběr modelů v příkladu), generování tangent přes WASM MikkTSpace a aktualizovaný port fyziky Box3D včetně opravy issue #157. Zatím to není ve vydané verzi, zřejmě to míří do příštího releasu.

## Proč je to důležité

Spolehlivý import glTF znamená, že do hry půjde vložit hotové 3D modely z Blenderu nebo asset storů bez ručních úprav, což je pro shooter (zbraně, postavy, prostředí) zásadní. Správné tangenty jsou potřeba, aby normal mapy na modelech vypadaly dobře.
