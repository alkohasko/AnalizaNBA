# Analiza NBA

Avtor: Aljaž Flus

Predstavil vam bom projektno nalogo, ki sem jo napisal za predmet Uvod v programiranje na Fakulteti za matematiko in fiziko na Univerzi v Ljubljani. Moj glavni cilj te naloge je bila analiza spreminjanja statističnih podatkov skozi zgodovino lige NBA na ravni poseneznikov, ki so osvajali nagrado za najboljšega igralca, kot tudi na ravni statističnih povprečij celotne lige.

Podatke sem črpal s strani:

- https://www.basketball-reference.com/

Pri tej analizi sem si predstavil tudi več hipotez:
- Igra postaja čedalje hitrejša
- Igralci postajajo čedalje boljši
- Igralci doesezejo vrhunec kariere ko so stari 27 oziroma 28 let
- Igralci igrajo čedalje manj tekem

Način črpanja in shranjevanja podatkov je upodobljeno v kodi, napisani v datoteki preberi_podatke_za_sezone_in_jih_zajemi.py. V njej sem uporabil tudi kodo iz datoteke orodja.py, ki jo je zapisal Matija Pretnar, ki shrani spletno stran ter potem naredi iz izbranih podatkov tudi potrebne csv datoteke, ki sem jih nato uporabljal. Koda ki opisuje izris grafov ter prikaz specificnih podatkov je zajeta v datoteki ureditev.py. Ta koda bi seveda lahko bila zapisana tudi direktno v datoteki analiza_podatkov.ipynb, ampak sem se odločil, da jo raje zapišem posebaj, da je .ipynb datoteka bolj pregledna.

Glavna analiza je vsebovana v datoteki analiza_podatkov.ipynb, kjer je opisano moje mišljenje glede zajetih podatkov v povezavi s predpostavljenimi hipotezami. Za prevod celotne naloge je potrebno naložiti pakete: pandas, matplotlib.pyplot, re, csv, os, requests, sys.