---
title: "Design and control of warehouse order picking: A literature review"
url: https://doi.org/10.1016/j.ejor.2006.07.009
authors: "R. de Koster, T. Le-Duc, K.J. Roodbergen"
year: 2007
venue: "European Journal of Operational Research 182(2), 481–501"
added: 2026-11-02
category: studie
tags: [studie, picking, slotting, produktivita, e-commerce]
queue_n: 1
---

# Design and control of warehouse order picking (de Koster, Le-Duc, Roodbergen, 2007)

Plný text (verze vydavatele) je volně v repozitáři Erasmus University: https://pure.eur.nl/ws/portalfiles/portal/46713708/DesignandControl_2007.pdf

## Co studie zkoumá a v jakém prostředí

Jde o přehledový článek (invited review), ne o experiment s vlastními daty. Autoři prošli zhruba 140 prací a strukturují rozhodovací problémy při návrhu a řízení **ručního pickingu typu picker-to-parts na nízké úrovni** (picker chodí s vozíkem mezi regály a bere zboží z polic). Podle zkušenosti autorů tvoří takové systémy přes 80 % všech pickingových systémů v západní Evropě. Literaturu dělí do pěti oblastí: vnitřní layout, přiřazení zboží k lokacím (storage assignment), zónování, batching a routing pickerů, plus akumulace a třídění po pickingu.

Výchozí čísla, která článek uvádí: picking může tvořit až 55 % celkových provozních nákladů skladu. Typické rozložení času pickera (podle Tompkins et al., 2003) je zhruba 50 % chůze, 20 % hledání, 15 % samotné vychystání, 10 % příprava (setup) a 5 % ostatní. Chůze je proto první kandidát na zlepšení („travel time is waste“).

## Metody a postupy, které stojí za to znát

**Layout.** Rozhoduje se počet bloků, počet a délka uliček, počet a poloha příčných uliček a poloha depa. Optimální layout závisí na zvolené storage a routing politice.

**Forward–reserve.** Oddělení malé pickovací zóny (forward) od zásobní (reserve). Čím menší forward, tím kratší chůze, ale tím víc doplňování. Příbuzný koncept je „dynamic storage“: pickovací plocha je velmi malá a SKU se do ní přivážejí automatem (jeřáb, karusel, VLM) těsně před pickem. Autoři o něm v roce 2007 píšou, že akademicky jde o „virgin ground“.

**Storage assignment (pět politik).**
- Random: vysoké využití prostoru, delší chůze, nutné řízení WMS.
- Closest open location: picker uloží na první volné místo.
- Dedicated: pevné místo pro SKU; nejhorší využití prostoru, ale pickeři si místa pamatují.
- Full-turnover / COI: nejrychlejší SKU nejblíž depu. COI (cube-per-order index) = požadovaný prostor SKU / počet výjezdů potřebných na jeho poptávku; nejnižší COI jde nejblíž depu. Nevýhoda: časté přeskládávání, když se mění poptávka a sortiment.
- Class-based (ABC): klasicky třída A obsahuje asi 15 % SKU a dělá asi 85 % obratu; uvnitř třídy je umístění náhodné. Simulace (Petersen et al., 2004) ukazují, že full-turnover je co do chůze lepší, ale pro praxi doporučují 2 až 4 třídy, protože se snáz udržují. Umístění tříd buď „within-aisle“ (každá ulička jedna třída), nebo „across-aisle“ (A u depa napříč uličkami); across-aisle je podle Le-Duc a De Koster blízko optima pro return routing.

**Family grouping.** SKU objednávané spolu skladovat u sebe. Dvě varianty: complementary-based (shluknout SKU podle síly společné poptávky, pak shluk umístit co nejblíž u sebe) a contact-based (podle toho, jak často picker bere SKU i bezprostředně po SKU j na optimální trase). Předpoklad: korelace mezi SKU je známá nebo předvídatelná.

**Zónování.** Pick-and-pass (progresivní, objednávka putuje zónami) vs. synchronizované (paralelní pickování a následné sloučení). Klíčové je vyvážení zátěže mezi zónami. Alternativa „bucket brigades“: pickeři seřazení podle rychlosti si předávají rozpracovanou objednávku podél linky; systém se sám vyvažuje a v nasazení v DC zvýšil propustnost a snížil nároky na řízení (Bartholdi et al., 2001; konkrétní čísla článek neuvádí).

**Batching.** Seskupení více objednávek do jedné pochůzky, výhodné hlavně u malých objednávek. Problém je NP-těžký, proto heuristiky:
- Seed: vyber „semínko“ (např. objednávku s nejvíce pozicemi, nejdelší trasou nebo nejvzdálenější od depa) a přidávej objednávky, které přidají nejméně dalších uliček nebo mají nejbližší těžiště.
- Savings (Clarke–Wright): spojuj malé trasy do větších, pokud to šetří vzdálenost.
- Time-window batching: seskupí objednávky došlé v časovém okně; pak buď sort-while-pick (třídění na vozíku), nebo pick-and-sort (třídění až po pickingu).
Závěr srovnání (De Koster et al., 1999b): i jednoduchý batching výrazně překoná FCFS; seed metody fungují nejlépe se S-shape routingem a velkou kapacitou vozíku, time-savings s largest-gap routingem a malou kapacitou.

**Routing.** Picker routing je Steinerův problém obchodního cestujícího; pro obdélníkový sklad s jedním blokem existuje optimální algoritmus v lineárním čase (Ratliff a Rosenthal, 1983). V praxi se používají heuristiky:
- S-shape: každou uličku s pickem projde celou.
- Return: do uličky vstoupí a vrátí se stejnou stranou.
- Midpoint: přední půlka z přední příčné uličky, zadní ze zadní.
- Largest gap: jako midpoint, ale hranice je největší mezera mezi picky; vždy lepší než midpoint.
- Combined/composite: pro každou uličku dynamickým programováním rozhodne, zda projít, nebo se vrátit.
Optimální trasy se v praxi nepoužívají, protože nejsou pro každý layout, pickerům připadají nelogické a nepočítají s kongescí.

**Akumulace a třídění.** Po batchingu nebo zónování je potřeba třídit podle objednávek (sorter, recirkulace, přiřazení objednávek k výstupům). Dynamické přiřazení objednávek k výstupům těsně před příjezdem je lepší než jakékoli pevné pravidlo (Bozer et al., 1988; Johnson, 1998).

## Klíčová čísla (vše citované v článku)

- Picking: až 55 % provozních nákladů skladu.
- Čas pickera: ~50 % chůze, 20 % hledání, 15 % pick, 10 % setup, 5 % ostatní.
- Put systémy (order distribution): kolem 500 picků na pickera a hodinu u malých položek, nové systémy až 1000 put operací za hodinu; průmysl obecně až 1000 picků na osobu a hodinu.
- Wave picking: velikost vlny typicky odpovídá 30 minutám až 2 hodinám práce.
- Nejlepší routing heuristika je v průměru asi 5 % nad optimem (Petersen, 1997).
- S-shape je o 7 až 33 % delší než optimum; largest gap je lepší než S-shape při méně než zhruba 4 picích na uličku (Hall, 1993).
- Combined+ heuristika vyhrála v 74 z 80 instancí skladů s více příčnými uličkami (7 až 15 uliček, 2 až 11 příčných uliček, 10 až 30 položek na pick listu).
- L-shaped třídy v AS/RS jsou obecně max. 3 % nad optimem (Graves et al., 1977).
- Pro AS/RS vyšlo 6 tříd jako nejlepší (Yang, 1988; Van den Berg a Gademann, 2000); pro ruční picking doporučení 2 až 4 třídy.
- Méně než 30 % ze zhruba 140 prací se týká picker-to-parts systémů, přestože dominují praxi.

## Co je přenositelné do Notina a jak to otestovat

1. **Změřit rozpad času pickera.** Pokud chůze dělá kolem poloviny času, je to hlavní páka. Test: časová studie nebo data ze skenerů (časy mezi scany vs. vzdálenost) na vzorku směn.
2. **ABC s 2 až 4 třídami a across-aisle umístěním A u depa.** U mnoha malých SKU kosmetiky je to levná první vlna slottingu. Test: přeslotovat jednu zónu, porovnat metry na pick a picky za hodinu před a po (A/B na zónách nebo směnách).
3. **Family grouping podle společných objednávek.** E-commerce data z objednávek přímo dávají matici „kupováno spolu“ (např. sady, řady jedné značky). Test: offline simulace vzdálenosti nad historickými objednávkami pro současný slotting vs. shlukový slotting.
4. **Batching malých objednávek.** U e-commerce s 1 až 3 položkami na objednávku je batching s tříděním (sort-while-pick do přihrádek vozíku, nebo pick-and-sort na put wallu) silná páka. Pravidlo z článku: seed batching + S-shape při velkém vozíku, savings + largest gap při malém. Test: přehrát historické vlny přes WMS logiku nebo jednoduchý simulátor a porovnat s FCFS.
5. **Routing v WMS.** Ověřit, jakou heuristiku WMS používá. Pokud S-shape a hustota je pod ~4 picky na uličku, largest gap nebo combined může zkrátit trasu. Test: přepočítat trasy historických pick listů různými heuristikami.
6. **Automatizace.** Článek zmiňuje dynamic storage a put systémy jako směr s nejvyšší produktivitou; pro projekt automatizace je užitečné hodnotit, jak se změní batching, doplňování forward zóny a třídění, ne jen samotný stroj. Konkrétní čísla k AutoStore a RMFS článek nemá (vyšel 2007); na to jsou ve frontě další studie (např. č. 5).
7. **Stochastická poptávka.** Autoři upozorňují, že většina modelů bere poptávku jako známou předem, což neplatí pro online prodejce s krátkými okny. Pro Notino to znamená preferovat dynamické (průběžné) batchování a vlny před statickým plánem.

## Omezení

- Je to přehled, nikoli vlastní experiment: všechna čísla pocházejí z citovaných studií s jejich vlastními předpoklady (často náhodné umístění, jednoblokový sklad, uniformní rozložení picků).
- Rok 2007: chybí moderní e-commerce systémy (AMR, RMFS/Kiva, AutoStore, mixed-shelves), datově řízený slotting a dynamický batching v reálném čase.
- Zaměřuje se na ruční picker-to-parts systémy; automatizované systémy pokrývá jen okrajově.
- Rozložení času pickera je „typické“ podle učebnice (Tompkins), ne naměřené pro konkrétní sklad; u Notina se může výrazně lišit.
- Autoři sami uvádějí, že kombinace rozhodnutí (layout + slotting + batching + routing) jsou málo prozkoumané a metody z jedné situace nejsou snadno přenositelné na jinou.

## Odkaz

- DOI: https://doi.org/10.1016/j.ejor.2006.07.009
- Volné PDF (verze vydavatele): https://pure.eur.nl/ws/portalfiles/portal/46713708/DesignandControl_2007.pdf
