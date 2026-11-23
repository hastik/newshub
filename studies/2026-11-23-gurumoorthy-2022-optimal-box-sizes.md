---
title: "A decision-tree framework to select optimal box-sizes for product shipments"
url: https://arxiv.org/abs/2202.04277
authors: "K. S. Gurumoorthy, A. Hinge"
year: 2022
venue: "arXiv:2202.04277 [cs.LG] (Amazon), preprint"
added: 2026-11-23
category: studie
tags: [studie, baleni, e-commerce, automatizace-skladu, benchmark]
queue_n: 10
---

# Studie týdne: A decision-tree framework to select optimal box-sizes for product shipments
**K. S. Gurumoorthy, A. Hinge (Amazon, Bangalore), 2022, preprint arXiv:2202.04277 [cs.LG]** (položka #10 z fronty)

Tentokrát jsem přeskočil #2, #4, #6, #7, #8 a #9. U všech jsem dohledal jen abstrakt, volný plný text ne. #2 a #4 jsou dlouhodobě za paywallem. #6 (Petersen 1997) a #9 (Gu a kol. 2007) jsou za paywallem. U #7 (de Koster a kol. 1999) a #8 (Grosse a kol. 2017) mají repozitáře EUR a TU Darmstadt jen záznam bez PDF, takže značka OA ve frontě u #7 neplatí. Všechny zůstávají jako `todo`. #10 je volně na arXivu a celý jsem ho přečetl.

## Co studie zkoumá a v jakém prostředí
Kolik různých velikostí krabic mít a jaké mají mít rozměry, aby se zboží posílalo s co nejmenším prázdným místem („air-in-box“). Studie řeší jen **single-count zásilky** (1 produkt = 1 krabice), které jsou u e-commerce gigantů většinou. Data jsou z Amazonu: učení na **~2 mil. jednopoložkových zásilkách z června 2019** (**~75 000 produktů**, u každého délka, šířka, výška a počet zásilek), validace na červenci 2019 a test na **~2 mil. zásilkách ze srpna 2019**. Výchozí stav je **14 krabic**, jejichž rozměry Amazon ručně ladil na datech z několika měsíců.

## Metoda (dá se zopakovat v Pythonu nad daty z WMS)
1. **Převod na shlukování.** Každý shluk produktů = jedna velikost krabice. Krabice má rozměry max(délka), max(šířka), max(výška) produktů ve shluku. Minimalizuje se celkový odeslaný objem: Σ přes krabice (objem krabice × počet zásilek ve shluku). Počet zásilek („sales velocity“) váhuje, takže rychloobrátkové produkty dostanou těsné krabice.
2. **Forward pass (dělení, jako rozhodovací strom).** Začne se s jednou krabicí pro všechno. V každém kroku se zkusí každý shluk rozdělit podle každého rozměru (L/Š/V) v nejlepším bodě řezu. Rozdělí se ten shluk, jehož rozdělení nejvíc sníží objem. Pokračuje se až na K̃ ≥ K krabic (víc, než je cílový počet).
3. **Product reassignment.** Po každé změně se každý produkt přeřadí do krabice, do které se vejde (každý rozměr krabice ≥ rozměr produktu) a která má nejmenší objem.
4. **Iterative refinement.** Opakovaně se přesune jeden „rozměrově určující“ produkt (nejdelší, nejširší nebo nejvyšší ve shluku) do jiného shluku, pokud to sníží celkový objem. Končí se, když už žádný přesun nepomáhá.
5. **Backward pass (slučování).** Z K̃ krabic se postupně slučuje vždy ta dvojice, jejíž sloučení nejméně zvýší objem, až se dojde na K. Po každém kroku následuje reassignment a refinement.
6. **Volba parametrů.** K̃ se ladí na validačním měsíci (vyšlo K̃ = 44). Finální K se volí jako **elbow point**, tedy tam, kde přidání další krabice už skoro nesnižuje objem. Výkon se měří metrikou ξ = 100 × (1 − objem produktů / objem krabic) na nezávislém testovacím měsíci.
- Složitost je O(KN log N + NK²), takže to škáluje i na stovky tisíc SKU. Přidat nebo ubrat jednu velikost znamená zastavit backward pass o krok dřív nebo pozdě, a není potřeba počítat znovu od nuly.

## Klíčová čísla
- Současných 14 ručně laděných krabic: **ξ = 60,5 %** vzduchu v krabici (test, srpen 2019).
- Nových 14 rozměrů (stejný počet krabic): **ξ = 58,3 %** a celkový objem zásilek **−4,4 %**, vzduch −2,2. Autoři to přepočítávají na „úspory desítek milionů dolarů i na rozvíjejících se trzích“.
- Už se **13 krabicemi** (o jednu méně než dnes) vychází ξ = 59,9 %, tedy lépe než současný stav.
- Elbow point je **K = 18**: objem **−10,3 %**, vzduch **−6,1** oproti dnešním 14 krabicím.
- Z rozložení použití 18 krabic plyne, že **88,1 % zásilek jde do menších krabic (č. ≤ 8)** a jen 11,9 % do velkých.
- Největší podíl na výsledku má krok **product reassignment**: bez něj ξ vzroste o víc než 1 bod.
- Srovnání s alternativami: 1D shlukování jen podle objemu produktu (dynamické programování) dává **ξ = 90,8 % i při K = 20**. Genetický algoritmus (Jia 2014; 5 startů, populace 200) je lepší než 1D, ale konzistentně horší než navržená metoda.
- Stabilita: při učení na 3 různých měsících vycházejí téměř stejné rozměry krabic i ξ, takže výsledek nezávisí na volbě období.

## Co je přenositelné do Notina a jak to otestovat
- **Kosmetika = hodně malých jednopoložkových zásilek s velkými rozdíly v rozměrech** (parfém, rtěnka, krém), což je přesně profil studie. Stačí data z WMS: L/Š/V u každého SKU a počty jednopoložkových zásilek za měsíc.
- **Pilot nanečisto (offline):** vzít 1 měsíc jednopoložkových zásilek na učení, 1 na validaci a 1 na test. Spočítat ξ a objem pro současnou sadu krabic, pro optimalizovanou sadu se stejným počtem krabic a pro křivku K = současný počet ± 4. Algoritmus je popsaný dost podrobně na reimplementaci (zhruba stovky řádků v Pythonu, žádné speciální solvery).
- **Napojení na automatizaci:** při výběru linky (auto-bagger, krabicovací stroj, cartonization ve WMS) dává křivka „počet formátů vs. objem/vzduch“ podklad k tomu, kolik formátů má mít linka nebo zásobník u balicího stolu. Menší objem se navíc promítá do přepravného (u dopravců počítajících objemovou hmotnost) a do spotřeby výplně.
- **Rychlá výhra bez investice:** i beze změny počtu krabic přinesla úprava rozměrů 4,4 % objemu. Pro Notino je to první otázka do pilotu.

## Omezení a výhrady
- **Jen jednopoložkové zásilky.** Vícepoložkové objednávky (u Notina pravděpodobně významný podíl) autoři výslovně nechávají na další výzkum, protože záleží na kombinacích, orientaci a pořadí balení.
- Produkt „se vejde“, pokud je každý jeho rozměr ≤ rozměru krabice. Rotace se v textu neřeší a chybí i rezerva na výplň nebo ochranné balení. Pro křehké zboží (sklo parfémů) je potřeba přidat přídavky.
- Vstupem je jen objem. Cena krabic, náklady na skladování dalších formátů, rychlost balení ani tarify dopravců v modelu nejsou, a počet krabic se volí jen heuristicky (elbow).
- Absolutní objemy Amazon nezveřejnil (ze stejného důvodu se reportuje jen ξ). Výsledky jsou simulace na historických datech, ne měření z provozu.
- Jde o **preprint na arXivu** (9 stránek), recenzované vydání jsem nenašel.

**Odkaz:** https://arxiv.org/abs/2202.04277 (PDF: https://arxiv.org/pdf/2202.04277)
