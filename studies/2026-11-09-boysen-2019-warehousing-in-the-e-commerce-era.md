---
title: "Warehousing in the e-commerce era: A survey"
url: https://doi.org/10.1016/j.ejor.2018.08.023
authors: "N. Boysen, R. de Koster, F. Weidinger"
year: 2019
venue: "European Journal of Operational Research 277(2), 396–411"
added: 2026-11-09
category: studie
tags: [studie, e-commerce, picking, slotting, rmfs, amr, goods-to-person, automatizace-skladu]
queue_n: 3
---

# Warehousing in the e-commerce era (Boysen, de Koster, Weidinger, 2019)

Plný text (verze vydavatele) je volně v repozitáři Erasmus University: https://pure.eur.nl/ws/portalfiles/portal/47940084/RePub-110234.pdf

## Co studie zkoumá a v jakém prostředí

Jde o přehledový článek (invited review), ne o experiment s vlastními daty. Autoři se zaměřují na B2C e-shopy a vycházejí ze čtyř požadavků: (i) malé objednávky (u německého Amazonu v průměru jen 1,6 kusu na objednávku), (ii) velký sortiment (dlouhý ocas), (iii) těsné dodací lhůty a (iv) kolísavé zatížení. Z návštěv skladů, rozhovorů s manažery a webů výrobců sestavili seznam skladových systémů a každý binárně ohodnotili podle toho, zda splňuje čtyři požadavky. Do přehledu vzali jen systémy, které splňují aspoň tři ze čtyř. Vyřadili tradiční picker-to-parts bez úprav, kompaktní úložiště (shuttle, live-cube, puzzle), A-Frame (vhodný jen pro malý sortiment drobných zboží jako léky a kosmetika), systémy pro velké objednávky kamenných prodejen a prototypy.

Zbylo šest systémů: mixed-shelves (rozptýlené) skladování, batching + zónování + třídění, dynamické zpracování objednávek, picking s asistencí AGV, roboty přenášející regály (MRFS typu Kiva) a pokročilé pickovací stanice. Rešerše běžela v databázích Business Source Premier a Scopus, anglické recenzované články plus „snowballing“ z citací.

## Metoda: jak je přehled postavený

U každého systému autoři popisují: (a) jak funguje, (b) vhodnost pro e-commerce, (c) tři rozhodovací úlohy – návrh layoutu, přiřazení zboží k místům (storage assignment) a vlastní picking (priorita objednávek, přiřazení pickerům, routing), (d) literaturu a mezery ve výzkumu. Pro tebe je užitečný hlavně popis, jak se systémy chovají a kde jsou jejich slabiny:

- **Mixed-shelves**: kusy jednoho SKU se rozptýlí po celém skladu, takže nejbližší kus je vždy blízko. Zboží se ukládá náhodně (v praxi tam, kde je místo) a pickeři potřebují čtečku nebo voice, protože polohu si nelze pamatovat. Nevýhoda: složitější uskladnění a problém u objednávek s velkým množstvím jednoho SKU.
- **Batching + zónování + třídění**: batch = víc objednávek v jedné pochůzce, parallel zoning = každý picker bere jen svou zónu. Vyžaduje konsolidaci (put wall ručně, nebo třídicí konveyor), mezi picking a konsolidací bývá mezisklad. Zásadní kompromis je urgentnost vs. efektivita: urgentní objednávky se mají dávat do dalších dávek, ale podobné objednávky (blízké lokace) se mají spojovat.
- **Dynamické zpracování**: pick list lze měnit i po startu pochůzky. Dvě varianty – milk-run (pevné trasy zónou, nové objednávky se jen signalizují na polici) a interventionist (trasa se přepočítá při každé nové objednávce, picker dostane novou trasu).
- **AGV asistence**: AGV nese bedny a jezdí s pickerem, picker se nevrací do depa. Dvě politiky: fixed-assignment a free-floating.
- **MRFS (Kiva)**: roboti zvedají regály (nad 1 000 kg) a vozí je ke stacionárnímu pickerovi.
- **Pickovací stanice**: ergonomická stanice napojená přes konveyor na automatický sklad (karusel, miniload, lift & shuttle).

## Klíčová čísla a zjištění (vše z článku, jde o citované výsledky jiných studií)

- Podle de Kostera a kol. (2007) mělo v Západní Evropě v roce 2007 přes 80 % skladů klasický picker-to-parts.
- MRFS: výkon uváděný na 600 a více řádků za hodinu a pickera (Wulfraat, 2012); pickovací stanice až 1 000 řádků za hodinu (de Koster 2008).
- Optimalizované sekvencování objednávek a regálů na jedné stanici MRFS může podle citované studie (Boysen a kol. 2018b) snížit velikost flotily robotů na méně než polovinu; čím víc jsou SKU rozptýlená po regálech, tím méně návštěv regálů je potřeba.
- MRFS konfigurace: poměr pickovacích a doplňovacích stanic 2:1 a naplnění regálů 50 % označeno za nadějné (Lamballais a kol. 2017b). Výkon je robustní vůči poměru stran skladu, ale velmi citlivý na umístění stanic (Lamballais a kol. 2017a). Sdílený (pooled) pool robotů mezi stanicemi výrazně zkracuje průběžný čas oproti dedikovaným robotům (Yuan & Gong 2017).
- Batching: společná optimalizace batchingu a routingu zkrátila celkový čas o 5–15 % oproti postupnému řešení (Hong a kol. 2012a); souběžné řešení batchingu, přiřazení pickerům a routingu zlepšilo čas dávek téměř o 10 % (Matusiak a kol. 2017); u problému s omezeními na pořadí kusů (váha, tvar) klesla ujetá vzdálenost o cca 15 % (Matusiak a kol. 2014); holistický přístup může snížit celkové zpoždění až o 84 % (Scholz a kol.).
- Spojení vratek a uskladnění do jednoho batchingu: až 44 % kratší vzdálenosti (Wruck a kol. 2013, data knihovního skladu).
- Přiřazení objednávek k výstupům sorteru podle optimalizace zkrátilo průměrný čas třídění o více než 40 % proti jednoduchému pravidlu (Meller 1997); u malé blokace výstupů ale stačí „přiřaď další objednávku do volné lajny“ (Johnson 1998).
- Waveless (dynamický) picking byl ve všech simulovaných scénářích stejně dobrý nebo lepší než vlny (Gallien & Weber 2010; Gong & de Koster 2008). Pick-and-sort se v téměř všech nastaveních ukázal lepší než sort-while-pick (van Nieuwenhuyse & de Koster 2009).
- Zónování: distribuce zboží mezi zóny – dvě nejlepší politiky podle Yuan a kol. (2018): dávat nové SKU do méně vytížených zón a ukládat polovinu zásob každého SKU do dvou náhodných zón.
- Tabulka 1 počtu zdrojů ukazuje, že batching/zónování/třídění má 48 prací, mixed-shelves jen 4, dynamické zpracování 4 a AGV asistence 1.

## Co je přenositelné na Notino a jak to otestovat

- **Zdůvodnění směru automatizace.** Profil Notina (hodně drobných SKU, malé objednávky, špičky) odpovídá přesně čtyřem požadavkům z článku. Přehled pomůže strukturovat výběr mezi G2P/MRFS, stanicemi a batchingem. Článek ale sám říká, že jeho hodnocení nestačí na reálný výběr systému (jen binární hodnocení autorů).
- **Rozptýlení SKU (scattered storage).** Test: v simulaci nebo na reálných datech objednávek porovnat průměrnou vzdálenost k nejbližšímu kusu při 1 vs. 2–3 lokacích na SKU u rychloběžných položek. Cena: složitější uskladnění a více lokací v WMS.
- **Dynamický picking místo vln.** Test: simulace nebo pilot v jedné zóně, metriky: průběžný čas objednávky a podíl objednávek stihnutých před cut-offem. Vyžaduje třídění (put wall/sorter), které už automatizační projekt pravděpodobně řeší.
- **Urgentnost vs. efektivita při batchingu.** Test: pravidlo, kde cut-off času objednávky určuje prioritu a v rámci stejné priority se objednávky spojují podle blízkosti lokací; porovnat s dnešním pravidlem na historických datech.
- **Konsolidace.** Ruční put wall škáluje přidáním lidí, sorter šetří mzdy, ale potřebuje investici a hůř škáluje; vybrat podle špiček v sezóně.
- **Vratky.** Článek zmiňuje, že vrácené zboží se často brzy objedná znovu, takže mu lze dát výhodné místo; tuto myšlenku lze otestovat na vlastních datech o vratkách.

## Limity a upozornění

- Je to přehled (survey) literatury, ne měření. Čísla jsou výsledky jiných studií, často simulací na jiných typech skladů (knihovní sklad, finský retail, holandský e-shop), nejsou přímo přenositelná na kosmetiku.
- Hodnocení vhodnosti systémů vychází z binárního subjektivního posudku autorů a rozhovorů s experty; autoři sami uvádějí, že pro výběr systému nestačí.
- Autoři vyřadili kompaktní úložiště (např. typu AutoStore) a roboty pro picking z polic jako neodpovídající tehdejším požadavkům – pro dnešní rozhodování je nutné doplnit novější zdroje (článek je z roku 2018).
- Mixed-shelves, dynamické zpracování a AGV asistence jsou podle autorů málo prozkoumané, takže zde je málo kvantitativních důkazů.
- Rozptýlené skladování zhoršuje objednávky s větším množstvím jednoho SKU a komplikuje uskladnění.

Odkaz: https://doi.org/10.1016/j.ejor.2018.08.023 (volné PDF: https://pure.eur.nl/ws/portalfiles/portal/47940084/RePub-110234.pdf)
