---
title: ProcessWire Weekly #652 – stabilnější sessions a hooky, modul Native Command
url: https://weekly.pw/issue/652/
source: ProcessWire Weekly
published: 2026-11-07
added: 2026-11-13
category: processwire
tags:
  - weekly
  - dev
  - modul
related_urls:
  - https://processwire.com/talk/topic/32112-native-command-%E2%80%94-a-alt%E2%8C%A5k-command-palette-for-processwire-admin-and-front-end/
---

Dev větev bez nové verze, ale s opravami: méně nečekaných odhlášení (challenge cookie), hooky se stejnou prioritou běží v pořadí přidání, uncache stránky už nezahodí neuložené změny a textformattery se u jazykových polí neaplikují dvakrát. Hlavní novinkou je modul Native Command od Roych: paleta příkazů na Alt+K v adminu i na front-endu pro editaci polí, hromadné akce přes selektory s undo a rychlou navigaci.

## Proč je to důležité

Opravy sessions a pořadí hooků řeší reálné potíže na produkčních webech. Native Command je praktický nástroj pro rychlejší správu obsahu (něco jako Raycast pro ProcessWire), s kontrolou oprávnění a možností přidat vlastní příkazy přes hooky.
