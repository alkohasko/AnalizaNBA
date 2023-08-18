import pandas as pd
import matplotlib.pyplot as plt

def graf_metov():
    sezone = pd.read_csv("C:/FAKS/UVP/AnalizaNBA-projektna/obdelani_podatki/sezone.csv", index_col="Sezona")
    x = sezone.index
    y1 = sezone["Število metov"]
    y2 = sezone["Število zadetih metov"]
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, y1, label = "Število metov")
    plt.plot(x, y2, label = "Število zadetih metov")
    plt.xlabel("Sezona")
    plt.ylabel("Število metov")
    plt.title("Število metov skozi sezone")
    plt.xticks([x[0]] + list(x[:-1:10]) + [x[-1]], rotation=45)
    plt.gca().invert_xaxis()
    plt.legend()
    plt.show()

pokazi_tabelo()