from arcgis.gis import GIS
import getpass

# Connect to your ArcGIS Online organization
PORTAL_URL = "https://governmentofbc.maps.arcgis.com"
agol_username = "Px.BCGS.Creator"
agol_password = getpass.getpass(prompt='Enter AGO password:')

gis = GIS(PORTAL_URL, agol_username, agol_password)

items = gis.content.search(query=f'owner:{gis.users.me.username} AND type:Web Map', max_items=100000)
# Iterate over each web map item and update its extent and viewpoint
for item in items:
    if item.title.startswith("British Columbia Geological Survey Critical Mineral Explorer") and not "App" in item.title:
        web_map = item.get_data()
        
        # Update the extent and viewpoint as desired
        # For example, you can set a new extent using the following format:
        web_map["initialState"]["viewpoint"] =  {
            "targetGeometry": {
                "spatialReference": {
                    "latestWkid": 3857,
                    "wkid": 102100
                },
                "xmin": -15475769.261834534,
                "ymin": 6592893.77373104,
                "xmax": -13037122.31142492,
                "ymax": 8104512.445098283
            }
        }
      # Or set a new center and scale using the following format:
      # Update the web map item with the modified data
        item.update(data=web_map)

        print(f"Updated extent and viewpoint for: {item.title}")
