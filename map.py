import folium
import pandas as pd


df = pd.read_csv("data.txt")
lat = list(df["LAT"])
lon = list(df["LON"])
name = list(df["NAME"])
stud = list(df["NUMUNIQUESTUDENTS"])

html = """<h4>School Suspensions/Expulsions Related to Alcohol, Drug Use [2021-2022]</h4>
<h5>County: %s, IN </h5>
<p>Num of Students: %s </p>
"""
 

"""to add children, create a feature group
    zip function goes through two(or more lists) at the same time
    create a separate txt file so you can add multiple markers
"""

map=folium.Map(location=[41.2801,-86.6187],zoom_start=7, tiles="Stamen Terrain")

fg=folium.FeatureGroup(name="My Map")
def color_prod(students):
    if students<100:
        return 'green'
    elif 100<students<200:
        return 'orange'
    else:
        return 'red'

for lt,ln,nm,std in zip(lat,lon,name,stud):
    iframe = folium.IFrame(html=html % (nm,std), width=200, height=200)

    fg.add_child(folium.Marker(location=[lt,ln], popup=folium.Popup(iframe),icon=folium.Icon(color=color_prod(std))))
map.add_child(fg)

map.save("Map.html")