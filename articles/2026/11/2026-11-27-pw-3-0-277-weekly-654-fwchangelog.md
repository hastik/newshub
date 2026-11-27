---
title: ProcessWire 3.0.277 a Weekly #654 – ~50 commitů hlavně k bezpečnosti, findRaw s jazyky a modul FwChangelog
url: https://weekly.pw/issue/654/
source: ProcessWire Weekly
published: 2026-11-21
added: 2026-11-27
category: processwire
tags:
  - dev
  - weekly
  - modul
  - webserver
related_urls:
  - https://processwire.com/talk/topic/32152-processwire-30277-%E2%80%93-core-updates/
  - https://processwire.com/talk/topic/32135-fwchangelog-per-page-changelog-with-beforeafter-values/
  - https://github.com/joaochoupinaa/FwChangelog
---

Dev verze ProcessWire 3.0.277 přinesla zhruba 50 commitů zaměřených hlavně na bezpečnost (admin, sessions, uploady, sanitizace, kontroly přístupu). Z novinek: `url` a `path` ve `findRaw()` respektují jazyk uživatele a nové vlastnosti `urls`/`paths` vrací hodnoty pro všechny jazyky. `findRaw()` vynechává nepublikované page reference (lze zapnout volbou `page_reference_status`) a Fieldtype moduly mohou implementovat `getRawValue()`. `$languages->find()` vynechává skryté jazyky a přibyla CSS proměnná `--pw-main-contrast-color` a `$log->disableQueryString()`. Opravy: login throttle už neodmítá platná 2FA přihlášení, nahrazení hodnoty repeateru nepřidává k existujícím položkám, plus kompatibilita s PHP 8.5/8.6. Weekly #654 představuje i nový modul FwChangelog od João Moty: u každé stránky loguje změny polí s hodnotou před a po, kdo a kdy změnu udělal, včetně vícejazyčných polí, souborů a repeaterů, se slučováním rychlých uložení a automatickou retencí.

## Proč je to důležité

Při upgradu pozor: 3.0.277 vyžaduje nastavený `$config->httpHosts` pro reset hesla a obsahuje aktualizované soubory .htaccess a pravidla pro nginx a Caddy, které je dobré na klientských webech porovnat. Změny ve `findRaw()` mohou změnit výsledky existujícího kódu u vícejazyčných webů a page referencí. FwChangelog řeší častý požadavek klientů („kdo to změnil a co tam bylo předtím?“) a hodí se na weby, kde obsah spravuje víc lidí.
