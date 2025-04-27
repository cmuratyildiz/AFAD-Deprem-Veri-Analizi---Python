import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

url = "https://deprem.afad.gov.tr/last-earthquakes.html"
df = pd.read_html(url)[0]

df["Tarih"] = pd.to_datetime(df["Tarih(TS)"])

marmara_df = df[df["Yer"].str.contains("Marmara Denizi", case=False, na=False)]

def saat_dilimi(saat):
    if 0 <= saat < 6:
        return "Gece"
    elif 6 <= saat < 12:
        return "Sabah"
    elif 12 <= saat < 18:
        return "Öğle"
    else:
        return "Akşam"

marmara_df["Saat Dilimi"] = marmara_df["Tarih"].dt.hour.apply(saat_dilimi)

saat_dilimleri = marmara_df["Saat Dilimi"].value_counts()

labels = saat_dilimleri.index
sizes = saat_dilimleri.values
explode = (0.1, 0, 0, 0)

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

angles = np.linspace(0, 2 * np.pi, len(sizes), endpoint=False)

heights = np.ones_like(sizes)

ax.bar3d(angles, np.zeros_like(sizes), np.zeros_like(sizes), 0.5, 0.5, sizes, shade=True)

ax.set_xticks(angles)
ax.set_xticklabels(labels)

ax.set_title("Marmara Depremleri Saat Dilimlerine Göre Dağılımı (3D Pasta Grafik)")

ax.set_ylabel('Yükseklik')
ax.set_zlabel('Deprem Sayısı')

plt.show()