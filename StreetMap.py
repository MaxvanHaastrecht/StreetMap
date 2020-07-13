import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Import roads.shp file; the corresponding .shx file should also be contained in the directory.
map_df = gpd.read_file('roads.shp')

# Define latitude-longitude pairs for different cities.
x_diff = 0.0350
y_diff = 0.0495
latlon = {}
latlon['Doetinchem'] = [6.2700, 6.2700 + x_diff, 51.9355, 51.9355 + y_diff]
latlon['Groningen'] = [6.5480, 6.5480 + x_diff, 53.1960, 53.1960 + y_diff]
latlon['Utrecht'] = [5.1050, 5.1050  + x_diff, 52.0620, 52.0620 + y_diff]
latlon['Zwolle'] = [6.0730, 6.0730  + x_diff, 52.4900, 52.4900 + y_diff]

# Store color palettes for cities.
colors = {}
colors['Doetinchem'] = 'summer'
colors['Groningen'] = 'autumn'
colors['Utrecht'] = 'Wistia'
colors['Zwolle'] = 'winter'

# Plot roads in particular city of NL.
city = 'Zwolle'

fig, ax = plt.subplots(1, figsize=(10,14))
map_df.plot(cmap=colors[city], ax=ax)
ax.axis('off')
ax.set_xlim(latlon[city][0], latlon[city][1])
ax.set_ylim(latlon[city][2], latlon[city][3])
ax.set_aspect('equal')

plt.show()
