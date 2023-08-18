import pandas as pd
import matplotlib.pyplot as plt

def graf_metov():
    sezone = pd.read_csv(r"C:\FAKS\UVP\AnalizaNBA-projektna\AnalizaNBA\obdelani_podatki\sezone.csv", index_col="Sezona")
    x = sezone.index
    y1 = sezone["Število metov"]
    y2 = sezone["Število zadetih metov"]
    y3 = sezone["Število točk na tekmo"]
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, y1, label = "Število metov")
    plt.plot(x, y2, label = "Število zadetih metov")
    plt.plot(x, y3, label = "Število točk")
    plt.xlabel("Sezona")
    plt.ylabel("Število metov")
    plt.title("Število metov skozi sezone")
    plt.xticks([x[0]] + list(x[:-1:10]) + [x[-1]], rotation=45)
    plt.gca().invert_xaxis()
    plt.legend()
    plt.show()

#graf_metov()

def spreminjanje_odstokov_metov():
    sezone = pd.read_csv(r"C:\FAKS\UVP\AnalizaNBA-projektna\AnalizaNBA\obdelani_podatki\sezone.csv", index_col="Sezona")
    x = sezone.index
    y1 = sezone["Odstotek meta"]
    y2 = sezone["Odstotek prostih metov"]
    y3 = sezone["Odstotek meta za tri točke"]

    plt.figure(figsize=(10, 6))
    plt.plot(x, y1, label = "Odstotek meta")
    plt.plot(x, y2, label = "Odstotek prostih metov")
    plt.plot(x, y3, label = "Odstotek meta za tri točke")
    plt.xticks([x[0]] + list(x[:-1:10]) + [x[-1]], rotation=45)
    plt.gca().invert_xaxis()
    plt.legend()
    plt.show()

#spreminjanje_odstokov_metov()    

def starost_MVP():
    sezone_MVP = pd.read_csv(r"C:\FAKS\UVP\AnalizaNBA-projektna\AnalizaNBA\obdelani_podatki_MVP\sezone_MVP.csv", index_col="Sezona")
    
    age_counts = sezone_MVP["Starost"].value_counts().sort_index()
    
    plt.figure(figsize=(10, 6))
    age_counts.plot(kind="bar")
    plt.xlabel("Starost")
    plt.ylabel("Število MVP-jev")
    plt.title("Število MVP-jev glede na starost")
    plt.xticks(rotation=0)
    plt.show()

#starost_MVP()

def koliko_tekem_MVP():
    sezone_MVP = pd.read_csv(r"C:\FAKS\UVP\AnalizaNBA-projektna\AnalizaNBA\obdelani_podatki_MVP\sezone_MVP.csv", index_col="Sezona")
    
    x = sezone_MVP.index
    y = sezone_MVP["Odigrane tekme"]

    plt.figure(figsize=(10, 6))
    plt.plot(x, y)
    plt.xlabel("Sezona")
    plt.ylabel("Število odigranih tekem")
    plt.title("Število odigranih tekem MVP-jev")
    plt.xticks([x[0]] + list(x[:-1:10]) + [x[-1]], rotation=45)
    plt.gca().invert_xaxis()
    plt.show()

#koliko_tekem_MVP()

def sestevek_vseh_statistik():
    sezone_MVP = pd.read_csv(r"C:\FAKS\UVP\AnalizaNBA-projektna\AnalizaNBA\obdelani_podatki_MVP\sezone_MVP.csv")
    
    izbrana_statistika = ["Točke na tekmo", "Asistence na tekmo", "Število odvzetih žog", "Skoki na tekmo", "Blokade"]
    sezone_MVP["Skupne statistike"] = sezone_MVP[izbrana_statistika].sum(axis=1)
    
    grouped_stats = sezone_MVP.groupby("Sezona")["Skupne statistike"].sum()

    plt.figure(figsize=(10, 6))
    grouped_stats.plot(kind="bar")
    plt.xlabel("Sezona")
    plt.ylabel("Skupna vsota statistik")
    plt.title("Skupne vsote statistik za vsako sezono")
    plt.xticks(rotation=90)
    plt.show()

#sum_stats_for_each_season()
