import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

url = "https://deprem.afad.gov.tr/last-earthquakes.html"
df = pd.read_html(url)[0]

df["Tarih"] = pd.to_datetime(df["Tarih(TS)"])

marmara_df = df[df["Yer"].str.contains("Marmara Denizi", case=False, na=False)]

marmara_df["Saat"] = marmara_df["Tarih"].dt.hour

saatlik_sayim = marmara_df.groupby("Saat").size().astype(int)

saatlik_buyukluk = marmara_df.groupby("Saat")["Büyüklük"].mean()

fig, ax1 = plt.subplots(figsize=(12, 6))

bars = ax1.bar(saatlik_sayim.index, saatlik_sayim.values, color="lightblue", label="Deprem Sayısı")
ax1.set_xlabel("Saat (0-23)", fontsize=12)
ax1.set_ylabel("Deprem Sayısı", color="blue", fontsize=12)
ax1.tick_params(axis='y', labelcolor="blue")
ax1.set_xticks(range(0, 24))
ax1.yaxis.set_major_locator(MaxNLocator(integer=True))  

for bar in bars:
    yval = int(bar.get_height())
    ax1.text(bar.get_x() + bar.get_width()/2, yval + 0.2, str(yval), ha='center', va='bottom', fontsize=9, color="blue")

ax2 = ax1.twinx()
ax2.plot(saatlik_buyukluk.index, saatlik_buyukluk.values, color="red", marker="o", label="Ortalama Büyüklük")
ax2.set_ylabel("Ortalama Büyüklük", color="red", fontsize=12)
ax2.tick_params(axis='y', labelcolor="red")

plt.title("Marmara Denizi - Saatlik Deprem Sayısı ve Ortalama Büyüklük", fontsize=14)
ax1.grid(axis='y', linestyle="--", alpha=0.7)

fig.legend(loc="upper left", bbox_to_anchor=(0.1, 0.9))

plt.tight_layout()
plt.show()