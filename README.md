# Analiza NBA

Avtor: Aljaž Flus

V projektni nalogi, napisani za predmet Uvod v programiranje na Fakulteti za matematiko in fiziko na Univerzi v Ljubljani, sem na podlagi zajetih statističnih podatkov naredil analizo zgodovine lige NBA. Glavni cilj moje naloge je bila analiza spreminjanja statističnih podatkov skozi zgodovine lige, in sicer na ravni posameznikov, ki so dobili nagrado za najboljšega igralca sezone, kot tudi na ravni statističnih povprečij celotne lige po sezonah.

Podatke sem črpal s strani:

- https://www.basketball-reference.com/

Pri tej analizi sem si zadal tudi več hipotez:
- igra postaja čedalje hitrejša,
- igralci postajajo čedalje boljši,
- igralci dosežejo vrhunec kariere, ko so stari 27 oziroma 28 let,
- igralci igrajo čedalje manj tekem.

Način črpanja in shranjevanja podatkov je upodobljen v kodi, napisani v datoteki preberi_podatke_za_sezone_in_jih_zajemi.py. V njej sem uporabil tudi kodo iz datoteke orodja.py, ki jo je zapisal Matija Pretnar, ki shrani spletno stran ter naredi iz izbranih podatkov tudi potrebne csv datoteke, ki sem jih nato uporabljal. Koda, ki opisuje izris grafov ter prikaz specifičnih podatkov, je zajeta v datoteki ureditev.py. Ta koda bi seveda lahko bila zapisana tudi direktno v datoteki analiza_podatkov.ipynb, ampak sem se odločil, da jo raje zapišem posebaj, da je .ipynb datoteka bolj pregledna.

Glavna analiza je vsebovana v datoteki analiza_podatkov.ipynb, kjer je opisano moje mišljenje glede zajetih podatkov v povezavi s zadanimi hipotezami. Za prevod celotne naloge je potrebno naložiti pakete: pandas, matplotlib.pyplot, re, csv, os, requests, sys.