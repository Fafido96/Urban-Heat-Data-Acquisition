import geopandas as gpd
from owslib.wfs import WebFeatureService
import os


#Check the correct layer name

#url = "https://servicios.ine.es/arcgis/services/WFS_INE_SECCIONES_G01/MapServer/WFSServer"

#wfs = WebFeatureService(url=url, version='2.0.0')

#print(list(wfs.contents))


#WFS request URL
url = (
    "https://servicios.ine.es/arcgis/services/"
    "WFS_INE_SECCIONES_G01/MapServer/WFSServer?"
    "service=WFS"
    "&version=2.0.0"
    "&request=GetFeature"
    "&typeNames=WFS_INE_SECCIONES_G01:Secciones2021"
    "&outputFormat=GEOJSON"
    "&cql_filter=CLAU2='12040'"  # Hopefully this additional filter will let me get the finer grained census sections.
)

# Load census sections from WFS
gdf_castello = gpd.read_file(url)

#check filtered gdf
print (gdf_castello.head(10).T)

# Convert CRS to WGS84 for web maps / GeoJSON
gdf_castello = gdf_castello.to_crs(4326)

# Save locally as GeoJSON
output_folder = "/mnt/c/Users/HP/Documents/Academics/Munster/Courses/Spatial Justice and Support Decision Systems/Practicals/Final Project/Data Acquisition/outputs"
output_file = os.path.join(output_folder, "castellon_sections.geojson")
gdf_castello.to_file(output_file, driver="GeoJSON")
print(f"Successfully saved to: {output_file}")