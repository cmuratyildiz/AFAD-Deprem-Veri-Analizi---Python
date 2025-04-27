import pandas as pd
import folium

url = "https://deprem.afad.gov.tr/last-earthquakes.html"
df = pd.read_html(url)[0]

marmara_df = df[df["Yer"].str.contains("Marmara Denizi -", case=False, na=False)]

marmara_map = folium.Map(location=[40.7, 28.5], zoom_start=7)

for i, row in marmara_df.iterrows():
    folium.CircleMarker(
        location=[row["Enlem"], row["Boylam"]],
        radius=row["Büyüklük"] * 2, 
        popup=(f"Yer: {row['Yer']}<br>"
               f"Büyüklük: {row['Büyüklük']}<br>"
               f"Tarih: {row['Tarih(TS)']}"),
        color="red",
        fill=True,
        fill_color="orange",
        fill_opacity=0.7
    ).add_to(marmara_map)

marmara_map.save("marmara_deprem_haritasi.html")