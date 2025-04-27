import pandas as pd
import folium
from folium.plugins import HeatMap

url = "https://deprem.afad.gov.tr/last-earthquakes.html"
df = pd.read_html(url)[0]

marmara_df = df[df["Yer"].str.contains("Marmara Denizi", case=False, na=False)]

marmara_map = folium.Map(location=[40.7, 28.5], zoom_start=7)

heat_data = [[row['Enlem'], row['Boylam']] for index, row in marmara_df.iterrows()]


HeatMap(heat_data, radius=15).add_to(marmara_map)


marmara_map.save("marmara_deprem_heatmap.html")
print("Heatmap oluşturuldu: marmara_deprem_heatmap.html")