---
title: Matematika idle her – cenové křivky, „buy max“ bez smyčky, velká čísla, offline příjem a prestige
url: https://playkovo.com/developers/blog/idle-game-math-cost-curves-offline-progress-prestige
source: PlayKovo
published: 2026-11-19
added: 2026-11-20
category: gamedev
tags:
  - idle
  - vzorce
  - prestige
  - design
  - tutorial
---

Stručný návod s hotovými JavaScript vzorci pro idle/clicker hry. Cena generátoru je `baseCost * growth^n` s růstem typicky 1,07 až 1,15. „Buy 10 / buy max“ se počítá v konstantním čase přes součet geometrické řady. Generátory jdou řetězit do tierů, kde vyšší tier vyrábí nižší. Formátování velkých čísel řeší s ohledem na limity JS floatů (přesná celá čísla do ~9×10^15, přetečení kolem 1,8×10^308). Offline příjem doporučuje omezit stropem a sazbou 50 až 100 % a počítat ho z uplynulého času, ne z ticků. Prestige body počítá přes odmocninu z celoživotního výdělku.

## Proč je to důležité

Je to přímo použitelné v HTML + Alpine.js prototypu: funkce `costForMany` a `maxAffordable`, formátovač čísel a výpočet offline příjmu se dají vzít skoro beze změny. Doplňuje minulotýdenní návod na balancování botem. Pozor na rozdílné cíle tempa: PlayKovo míří na první prestige zhruba za hodinu, Arelvox na 20 až 40 minut. Nejlepší je ověřit si to vlastní simulací.
