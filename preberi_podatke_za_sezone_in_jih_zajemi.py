import re
import orodja

with open("podatki_o_sezonah") as f:
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

#orodja.shrani_spletno_stran(url="https://www.basketball-reference.com/leagues/NBA_stats_per_game.html", ime_datoteke="podatki_o_sezonah", headers={"Accept-language": "en"})
#orodja.zapisi_json(podatki_za_sezono_list, "obdelani_podatki/sezone.json")
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

orodja.shrani_spletno_stran(url="https://www.basketball-reference.com/awards/mvp.html", ime_datoteke="MVP sezon", headers={"Accept-language": "en"})

with open("MVP sezon") as f:
    vsebina = f.read()

vzorec_MVP = re.compile(
    r'<tr ><th scope="row" class="left " data-stat="season" >.*'
)

vzorec_sezone_MVP = re.compile(
    r'data-stat="season" ><a.*?>(?P<Sezona>.*?)</a></th>'
)

vzorec_v_kateri_ligi = re.compile(
    r'data-stat="lg_id" ><a.*?>(?P<Liga>.*?)</a></td>'
)

vzorec_kdo_je_zmagal = re.compile(
    r'data-stat="player" csk=".*?" ><a.*?">(?P<Zmagovalec>.*?)</a>'
)

#data-stat="player" csk="Erving,Julius" ><a href="/players/e/ervinju01.html">Julius Erving</a>&nbsp;(Tie)</td><

vzorec_starosti = re.compile(
    r'data-stat="age" >(?P<Starost_zmagovalca>.*?)</td>'
)

vzorec_stevila_odigranih_tekem = re.compile(
    r'data-stat="g" >(?P<Stevilo_odigranih_tekem>.*?)</td>'
)

vzorec_stevila_tock_na_tekmo = re.compile(
    r'data-stat="pts_per_g" >(?P<Stevilo_tock_na_tekmo>.*?)</td>'
)

vzorec_stevila_skokov_na_tekmo = re.compile(
    r'data-stat="trb_per_g" >(?P<Stevilo_skokov_na_tekmo>.*?)</td>'
)

vzorec_stevila_asistenc_na_tekmo = re.compile(
    r'data-stat="ast_per_g" >(?P<Stevilo_asistenc_na_tekmo>.*?)</td>'
)

vzorec_stevila_odvzetih_zog_na_tekmo = re.compile(
    r'data-stat="stl_per_g" >(?P<Stevilo_odvzetih_zog_na_tekmo>.*?)</td>'
)

vzorec_stevila_blokad_na_tekmo = re.compile(
    r'data-stat="blk_per_g" >(?P<Stevilo_blokad_na_tekmo>.*?)</td>'
)


def najdi_podatke_za_sezono_MVP(blok):
    podatki_za_sezono_MVP = {}
    
    podatki_za_sezono_MVP["Sezona"] = najdi_v_html(vzorec_sezone_MVP, blok)
    podatki_za_sezono_MVP["Liga"] = najdi_v_html(vzorec_v_kateri_ligi, blok)
    podatki_za_sezono_MVP["Zmagovalec"] = najdi_v_html(vzorec_kdo_je_zmagal, blok)
    podatki_za_sezono_MVP["Starost"] = najdi_v_html(vzorec_starosti, blok)
    podatki_za_sezono_MVP["Odigrane tekme"] = int(najdi_v_html(vzorec_stevila_odigranih_tekem, blok))
    podatki_za_sezono_MVP["Točke na tekmo"] = float(najdi_v_html(vzorec_stevila_tock_na_tekmo, blok))
    podatki_za_sezono_MVP["Skoki na tekmo"] = float(najdi_v_html(vzorec_stevila_skokov_na_tekmo, blok))
    podatki_za_sezono_MVP["Asistence na tekmo"] = float(najdi_v_html(vzorec_stevila_asistenc_na_tekmo, blok))

    stevilo_odvzetih_zog = najdi_v_html(vzorec_stevila_odvzetih_zog_na_tekmo, blok)
    if stevilo_odvzetih_zog:
        podatki_za_sezono_MVP["Število odvzetih žog"] = float(stevilo_odvzetih_zog)
    else:
        podatki_za_sezono_MVP["Število odvzetih žog"] = None

    stevilo_blokad = najdi_v_html(vzorec_stevila_blokad_na_tekmo, blok)
    if stevilo_blokad:
        podatki_za_sezono_MVP["Blokade"] = float(stevilo_blokad)
    else:
        podatki_za_sezono_MVP["Blokade"] = None

    return podatki_za_sezono_MVP

podatki_za_sezono_MVP_list = []
for match in vzorec_MVP.finditer(vsebina):
    blok = match.group(0)
    podatki_za_sezono_MVP = najdi_podatke_za_sezono_MVP(blok)
    podatki_za_sezono_MVP_list.append(podatki_za_sezono_MVP)

for data in podatki_za_sezono_MVP_list:
    print(data)

#orodja.zapisi_json(podatki_za_sezono_MVP_list, "obdelani_podatki_MVP/sezone.json")
orodja.zapisi_csv(
    podatki_za_sezono_MVP_list,
    [
        "Sezona",
        "Liga",
        "Zmagovalec",
        "Starost",
        "Odigrane tekme",
        "Točke na tekmo",
        "Skoki na tekmo",
        "Asistence na tekmo",
        "Število odvzetih žog",
        "Blokade"
    ],
    "obdelani_podatki_MVP/sezone.csv",
)
