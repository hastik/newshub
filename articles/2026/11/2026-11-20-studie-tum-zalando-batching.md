---
title: Studie TUM – nové heuristiky pro výběr objednávek, batching a routing na modelu ze Zalanda, s kontrolou stáří objednávek
url: https://arxiv.org/abs/2611.24529
source: arXiv (Technical University of Munich)
published: 2026-11-18
added: 2026-11-20
category: logistika
tags:
  - studie
  - picking
  - produktivita
  - e-commerce
  - vzorce
---

Alexander Grosz a Leander Schnaars z TU Mnichov navazují na model, který představili výzkumníci ze Zalanda. Model naráz řeší výběr objednávek, alokaci zásob (scattered storage), tvorbu batchů a trasy pickerů pro desetitisíce čekajících objednávek ve skladu s více zónami. Autoři zrychlili referenční greedy algoritmus a rozšířili model na víc navazujících fází, což víc odpovídá reálnému provozu. Ukázali, že naivní optimalizace jen na vzdálenost nechává část objednávek viset donekonečna (v testu až 100 fází). Nové varianty to řeší za podobnou nebo nižší cenu: například FDGA-Soft(0.9) snížil celkovou cenu tras o 5,2 % a maximální stáří objednávky stlačil ze 100 na zhruba 13 fází. Tvrdý limit 10 fází (Cutoff) vyšel zhruba o 19 % dráž.

## Proč je to důležité

Ukazuje konkrétní, měřitelný kompromis mezi efektivitou tras a SLA. Čistá optimalizace vzdálenosti systematicky odsouvá „nevýhodné“ objednávky, což je přesně problém next-day a same-day e-commerce. Užitečné jako argument a vzor pro nastavení vlnového a batchovacího algoritmu ve WMS: penalizovat stáří objednávky postupně (měkce) místo tvrdého cutoffu. Omezení: zjednodušené (náhodné) doskladňování a zatím žádný test na reálných datech.
