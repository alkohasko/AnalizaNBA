import pandas as pd
import matplotlib.pyplot as plt

def graf_metov():
    sezone = pd.read_csv("C:/FAKS/UVP/AnalizaNBA-projektna/obdelani_podatki/sezone.csv", index_col="Sezona")
    x = sezone.index
    y = sezone["Število metov"]
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, y)
    plt.xlabel("Sezona")
    plt.ylabel("Število metov")
    plt.title("Število metov skozi sezone")
    plt.xticks([x[0], x[-1]], rotation=45)
    plt.show()

