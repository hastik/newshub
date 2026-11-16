---
title: "Robotized and Automated Warehouse Systems: Review and Recent Developments"
url: https://doi.org/10.1287/trsc.2018.0873
authors: "K. Azadeh, R. de Koster, D. Roy"
year: 2019
venue: "Transportation Science 53(4), 917–945"
added: 2026-11-16
category: studie
tags: [studie, automatizace-skladu, as-rs, rmfs, goods-to-person, amr, e-commerce, picking]
queue_n: 5
---

# Studie týdne: Robotized and Automated Warehouse Systems: Review and Recent Developments
**K. Azadeh, R. de Koster, D. Roy, 2019, Transportation Science 53(4), 917–945** (položka #5 z fronty)

Položky #2 (Petersen & Aase 2004) a #4 (Mantel a kol. 2007) jsem tentokrát přeskočil: obě jsou za paywallem a volný plný text jsem nenašel (#4 je jen na ResearchGate/Academia, kde je potřeba přihlášení). Ve frontě zůstávají jako `todo`. Plný text #5 (verze vydavatele) je volně v repozitáři EUR.

## Co studie zkoumá a v jakém prostředí
Přehledový článek, ne experiment s vlastními daty. Autoři roztřídili automatizované pickingové systémy a podrobně prošli 55 prací o „nových“ robotických systémech: shuttle systémy v uličkách (AVS/RS), mřížkové/puzzle systémy (GridStore, GridPick, live-cube, GridFlow) a robotic mobile fulfillment (RMFS, Kiva/Amazon Robotics). Klasické AS/RS, karusely, VLM a A-frame shrnují jen stručně. Každý systém popisují ve třech rovinách: **analýza systému** (jaký výkon má daná konfigurace), **optimalizace návrhu** (hardware: tvar, počet uliček/pater/robotů/liftů, umístění stanic) a **plánování a řízení provozu** (software: přidělování vozidel, dwell point, prevence blokování, storage policy, sekvencování). Kontext: v západní Evropě je podle autorů asi 40 plně automatizovaných skladů a jen v Nizozemsku vzniklo v letech 2012–2016 63 velkých skladů s robotikou.

## Metoda: jak se takové systémy modelují (dá se použít na hodnocení nabídek dodavatelů)
- **LP/MIP modely**: deterministická optimalizace (tvar systému, storage policy, sekvencování, batching). Velké instance se řeší metaheuristikami (genetické algoritmy, tabu search, simulované žíhání, ALNS) nebo matheuristikami.
- **Modely doby jízdy (travel time)**: vzorce pro očekávaný cyklus v uzavřeném tvaru. Rychle zúží prostor návrhů, ale nezachytí čekání a interakce mezi roboty. Klasický příklad: u jeřábového AS/RS je ideální ulička „čtvercová v čase“. Když jeřáb jede zhruba 4× rychleji, než zvedá, má být ulička 4× delší než vyšší.
- **Sítě front (queueing networks)**: otevřená síť (OQN) odhadne průběžnou dobu objednávky, ale počítá s neomezeným počtem robotů. Uzavřená síť (CQN) dá maximální propustnost, ale podceňuje čekání. **Polootevřená síť (SOQN)** páruje příchozí objednávky s omezeným počtem robotů, takže zachytí i externí čekání. U robotických systémů je to dnes standard.
- Doporučený postup: v rané fázi analytické modely pro výběr několika slibných konfigurací, pak detailní simulace jen pro ně. Dlouhodobé rozhodnutí = maximalizovat propustnost a kapacitu, krátkodobé = minimalizovat lead time, čekání a nečinnost zdrojů.

## Klíčová čísla (všechna citovaná v přehledu z původních prací)
- RMFS: přivezení zboží k pickerovi může **zdvojnásobit produktivitu pickera** (Wurman a kol. 2008).
- RMFS: storage zóny podle obrátkovosti podů zvýší maximální propustnost **téměř o 50 %** (Lamballais a kol. 2017a). Dvou- nebo tříúrovňové velocity-based skladování zkrátí jízdu o **8 % / 10 %** oproti náhodnému (Yuan a kol. 2018).
- RMFS: zásobu SKU rozložit na co nejvíc podů. Optimální poměr pick stanic k doplňovacím je **2 : 1** a optimální úroveň doplnění podu je **zhruba 50 %** (Lamballais a kol. 2017b).
- RMFS: optimální sekvencování objednávek na stanici zvládne tutéž práci s **polovinou flotily robotů** oproti FCFS (Boysen a kol. 2017). Sdílené (rozptýlené) skladování SKU v několika podech flotilu ještě zmenší.
- Shuttle (AVS/RS): blokování vozidel tvoří **až 20 %** cyklu transakce (Roy a kol. 2014). Vozidla vázaná na vertikální zóny místo pater zkrátí cyklus **až o 12 %** (Kumar a kol. 2014). Paralelní pohyb liftu a shuttle zlepší odezvu **nejméně o 5,5 %** u systémů pod 10 patry (Zou a kol. 2019).
- Kompaktní sklady: sekvencovací heuristika PPR-SL je o **20 % a víc** lepší než ostatní (Yu & de Koster 2012). Dvoutřídní skladování v live-cube zlepší odezvu **až o 55 %** proti náhodnému (Zaerpour a kol. 2017b). Simultánní pohyby v puzzle systému ušetří **až 70 %** tahů (Yu a kol. 2017).
- Karusel: dávkové vydávání zkrátí cyklus o **20 %** oproti sekvenčnímu (Pazour & Meller 2013).
- ABC skladování: optimum je **3–5 tříd** (cyklus na přesném počtu moc nezáleží) a potřeba lokací nad průměrnou zásobou rychle naroste o **dalších 40 %** (Yu a kol. 2015).
- AutoStore/RCSR (Zou a kol. 2016): dedikované skladování dá kratší průběžnou dobu, sdílené ušetří prostor. Optimální poměr šířky k délce gridu je **asi 2/3**.
- Pozor na přesnost: analytické modely validované simulací mají chyby **až 40 %** a s reálnými daty je skoro nikdo neporovnal.

## Co je přenositelné do Notina a jak to otestovat
- **Kontrolní seznam pro výběr a ladění automatizace**: rozdělení na návrh (hardware), řízení (software) a srovnání systémů je přesně struktura, podle které se dají klást otázky dodavatelům (AutoStore, shuttle, RMFS, AMR typu Locus). U každé nabídky chtít: model propustnosti (ideálně SOQN nebo simulaci) pro **náš** profil objednávek, citlivost na počet robotů a stanic, politiky dwell point a blokování a validaci na reálném provozu (kvůli chybám až 40 %).
- **Sekvencování a rozprostření zásoby jsou levné páky**: výsledky Boysen 2017 a Lamballais 2017b naznačují, že software (pořadí objednávek na stanici, rozložení SKU přes více nosičů) může ušetřit tolik jako hardware. Test: v simulaci nebo digitálním dvojčeti přehrát reálné objednávky Notina s FCFS a s optimalizovaným pořadím a měřit „picks per presentation“ (kusy na jedno přistavení binu/podu) a potřebný počet robotů.
- **Afinita produktů**: autoři doporučují storage policy podle toho, co se objednává spolu (market basket analysis). Pro kosmetiku s mnoha malými SKU jde o rychlý datový test: spočítat asociační pravidla z historie objednávek a nasimulovat, kolik binů/podů na objednávku ušetří afinitní plnění oproti ABC.
- **Nestacionární poptávka**: e-commerce špičky (Black Friday, Vánoce) běžné modely nepokrývají. U každého návrhu chtít scénáře pro špičku, ne jen průměrný den.
- **Člověk + robot**: autoři čekají, že piece picking na stanicích zůstane ještě zhruba dekádu převážně lidský. Ergonomie stanice a motivace pickerů jsou proto součástí výkonu systému.

## Limity
- Přehled z roku 2019 (rukopis 2018). Novější technologie a provozní data (Exotec, AutoStore v e-commerce měřítku, AMR goods-to-person) chybí nebo jsou jen zmíněné.
- Čísla pocházejí z citovaných prací s vlastními předpoklady (často jednořádkové objednávky, stacionární poptávka, validace jen simulací). Je to orientace, ne garantovaný efekt.
- Žádné porovnání nákladů a ROI mezi systémy. Autoři sami uvádějí, že komplexní srovnání technologií v literatuře téměř chybí.

**Odkaz:** https://doi.org/10.1287/trsc.2018.0873 · volný plný text: https://pure.eur.nl/ws/portalfiles/portal/47923950/Repub_119543.pdf