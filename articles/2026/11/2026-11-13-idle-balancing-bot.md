---
title: Balancování idle hry botem – reálná čísla pro růst cen, příjem a prestige
url: https://arelvox.com/how-to-balance-idle-games/
source: Arelvox
published: 2026-11-06
added: 2026-11-13
category: gamedev
tags:
  - idle
  - design
  - vzorce
  - prestige
  - tutorial
---

Autor browserových idle her ukazuje 30řádkového greedy bota v JavaScriptu, který za sekundu odehraje 6 hodin a zaloguje časy milníků. Zdvojnásobení příjmu posunulo druhou budovu z 6 na 3 minuty a první prestige z 56 na 28 minut; růst ceny 1,10 / 1,15 / 1,20 změnil čas do poslední budovy na 3,3 / 4,6 / 5,4 h.

## Proč je to důležité

Konkrétní, okamžitě použitelná metoda pro vlastní clicker: simulovat pacing místo ručního hraní. Praktická pravidla navíc: druhá budova do 2–3 minut, levný ×2 upgrade po každé nové budově, první prestige za 20–40 minut s bonusem aspoň +10–20 %. Kód jde snadno přenést do HTML + Alpine.js prototypu.
