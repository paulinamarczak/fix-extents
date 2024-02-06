# from arcgis.gis import GIS
# import getpass

# # Connect to your ArcGIS Online organization
# PORTAL_URL = "https://governmentofbc.maps.arcgis.com"
# agol_username = "Px.BCGS.Creator"
# agol_password = getpass.getpass(prompt='Enter AGO password:')

# gis = GIS(PORTAL_URL, agol_username, agol_password)

# items = gis.content.search(query=f'owner:{gis.users.me.username} AND type:Web Map', max_items=100000)
# # Iterate over each web map item and update its extent and viewpoint
# for item in items:
#     if item.title.startswith("British Columbia Geological Survey Critical Mineral Explorer") and not "App" in item.title:
#         web_map = item.get_data()
        
#         # Update the extent and viewpoint as desired
#         # For example, you can set a new extent using the following format:
#         web_map["initialState"]["viewpoint"] =  {
#             "targetGeometry": {
#                 "spatialReference": {
#                     "latestWkid": 3857,
#                     "wkid": 102100
#                 },
#                 "xmin": -15475769.261834534,
#                 "ymin": 6592893.77373104,
#                 "xmax": -13037122.31142492,
#                 "ymax": 8104512.445098283
#             }
#         }
#       # Or set a new center and scale using the following format:
#       # Update the web map item with the modified data
#         item.update(data=web_map)

#         print(f"Updated extent and viewpoint for: {item.title}")
#     print("Finished all updates")


# +-------------------------------------------------------------------------------------------------
# Author: Paulina Marczak
# Ministry, Division, Branch: EMLI, RMCD, BCGS
# Created Date: Feb 5, 2024
# Updated Date:  Feb 6, 2024
# Description: Do you own many web maps that all need to have their default view/scale changed?
# Look no further than this script.
# This script is easily called from opening a Notebook in ArcGIS Pro. No additional setup or installation required.
# +-------------------------------------------------------------------------------------------------


# Define class 
# +-------------------------------------------------------------------------------------------------

from arcgis.gis import GIS
import getpass

class WebMapUpdater:
    def __init__(self, portal_url, username, password):

        self.gis = GIS(portal_url, username, password)

    def update_webmaps(self, query_prefix, new_viewpoint):

        items = self.gis.content.search(query=f'owner:{self.gis.users.me.username} AND type:Web Map', max_items=10000)
        for item in items:
            if item.title.startswith(query_prefix) and not "App" in item.title:
                web_map = item.get_data()
                web_map["initialState"]["viewpoint"] = new_viewpoint
                item.update(data=web_map)
                print(f"Updated extent and viewpoint for: {item.title}")

        print("Finished all updates")


# +-------------------------------------------------------------------------------------------------

# Plug in your variables  
# +-------------------------------------------------------------------------------------------------

# Connect to your account

portal_url = "https://governmentofbc.maps.arcgis.com"
agol_username = "Px.BCGS.Creator"
agol_password = getpass.getpass(prompt='Enter AGO password:')

# Initialize the WebMapUpdater class
updater = WebMapUpdater(portal_url, agol_username, agol_password)

# Define the new viewpoint
# This is best done by manually saving one of your maps to the scale and extent you want.
# Then extract the ranges in AGO Assistant in the Data tab of your map and paste them below.

xmin = -15475769.261834534
ymin = 6592893.77373104
xmax = -13037122.31142492
ymax = 8104512.445098283

new_viewpoint = {
    "targetGeometry": {
        "spatialReference": {
            "latestWkid": 3857,
            "wkid": 102100
        },
        "xmin": xmin,
        "ymin": ymin,
        "xmax": xmax,
        "ymax": ymax
    }
}

# Your maps should be named with the same prefix so they can be grouped.

query_prefix = "British Columbia Geological Survey Critical Mineral Explorer"

# +-------------------------------------------------------------------------------------------------

# Run.

# +-------------------------------------------------------------------------------------------------

# Update web maps in the specified folder with the new viewpoint
updater.update_webmaps(query_prefix= query_prefix, 
                       new_viewpoint=new_viewpoint)
