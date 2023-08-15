import re
import orodja

with open(r"C:\FAKS\UVP\AnalizaNBA-projektna\AnalizaNBA\nba_source.html") as f:
    vsebina = f.read()


vzorec = re.compile(
    r'<tr ><th scope="row" class="right " data-stat="ranker".*'
)

vzorec_sezone = re.compile(
    r'data-stat="season" ><a.*?>(?P<Sezona>.*?)</a></td>'
)

vzorec_stevila_zadetih_metov_na_tekmo = re.compile(
    r'data-stat="fg_per_g" >(?P<Stevilo_zadetih_metov>.*?)</td>'
)

vzorec_stevila_metov_na_tekmo = re.compile(
    r'data-stat="fga_per_g" >(?P<Stevilo_metov_na_tekmo>.*?)</td>'
)

vzorec_stevila_tock_na_tekmo = re.compile(
    r'data-stat="pts_per_g" >(?P<stevilo_tock_na_tekmo>.*?)</td>'
)

vzorec_odstotka_meta_na_tekmo = re.compile(
    r'data-stat="fg_pct" >(?P<odstotek_meta>.*?)</td>'
)

vzorec_odstotka_meta_za_3_tocke_na_tekmo = re.compile(
    r'data-stat="fg3_pct" >(?P<odstotek_meta_za_3_tocke>.*?)</td>'
)

vzorec_odstotka_meta_prostih_metov = re.compile(
    r'data-stat="ft_pct" >(?P<odstotek_prostih_metov>.*?)</td>'
)


def najdi_v_html(vzorec, blok):
    najdeno = vzorec.search(blok)
    if najdeno:
        return najdeno.group(1)
    return None

def najdi_podatke_za_sezono(blok):
    podatki_za_sezono = {}
    
    podatki_za_sezono["Sezona"] = najdi_v_html(vzorec_sezone, blok)
    podatki_za_sezono["Število zadetih metov"] = float(najdi_v_html(vzorec_stevila_zadetih_metov_na_tekmo, blok))
    podatki_za_sezono["Število metov"] = float(najdi_v_html(vzorec_stevila_metov_na_tekmo, blok))
    podatki_za_sezono["Število točk na tekmo"] = float(najdi_v_html(vzorec_stevila_tock_na_tekmo, blok))
    podatki_za_sezono["Odstotek meta"] = float(najdi_v_html(vzorec_odstotka_meta_na_tekmo, blok))
    podatki_za_sezono["Odstotek prostih metov"] = float(najdi_v_html(vzorec_odstotka_meta_prostih_metov, blok))
    odstotek_meta_za_tri_tocke = najdi_v_html(vzorec_odstotka_meta_za_3_tocke_na_tekmo, blok)
    if odstotek_meta_za_tri_tocke:
        podatki_za_sezono["Odstotek meta za tri točke"] = float(odstotek_meta_za_tri_tocke)
    else:
        podatki_za_sezono["Odstotek meta za tri točke"] = None
    return podatki_za_sezono


podatki_za_sezono_list = []
for match in vzorec.finditer(vsebina):
    blok = match.group(0)
    podatki_za_sezono = najdi_podatke_za_sezono(blok)
    podatki_za_sezono_list.append(podatki_za_sezono)

for data in podatki_za_sezono_list:
    print(data)

orodja.shrani_spletno_stran(url="https://www.basketball-reference.com/leagues/NBA_stats_per_game.html", ime_datoteke="podatki_o_sezonah", headers={"Accept-language": "en"})
orodja.zapisi_json(podatki_za_sezono_list, "obdelani_podatki/sezone.json")
orodja.zapisi_csv(
    podatki_za_sezono_list,
    [
        "Sezona",
        "Število zadetih metov",
        "Število metov",
        "Število točk na tekmo",
        "Odstotek meta",
        "Odstotek prostih metov",
        "Odstotek meta za tri točke"
    ],
    "obdelani_podatki/sezone.csv"
)
