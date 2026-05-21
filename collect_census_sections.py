import geopandas as gpd

from owslib.wfs import WebFeatureService

#Check the correct layers

url = "https://servicios.ine.es/arcgis/services/WFS_INE_SECCIONES_G01/MapServer/WFSServer"

wfs = WebFeatureService(url=url, version='2.0.0')

print(list(wfs.contents))


#WFS request URL
#url = (
#    "https://servicios.ine.es/arcgis/services/"
#    "WFS_INE_SECCIONES_G01/MapServer/WFSServer?"
 #   "service=WFS"
  #  "&version=2.0.0"
   # "&request=GetFeature"
    #"&typeName=0"
    #"&outputFormat=application/json"
#)

# Load census sections from WFS
#gdf = gpd.read_file(url)

# Check columns
#print(gdf.columns)

# Filter Castellón province
#gdf = gdf[gdf["CPRO"] == "12"]

# Convert CRS to WGS84 for web maps / GeoJSON
#gdf = gdf.to_crs(4326)

# Save locally as GeoJSON
#gdf.to_file(
 #   "castellon_census_sections.geojson",
#    driver="GeoJSON"
#)

#print(gdf.head())