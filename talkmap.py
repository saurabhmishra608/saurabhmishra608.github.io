

# # Leaflet cluster map of talk locations
#
# (c) 2016-2017 R. Stuart Geiger, released under the MIT license
#
# Run this from the _talks/ directory, which contains .md files of all your talks. 
# This scrapes the location YAML field from each .md file, geolocates it with
# geopy/Nominatim, and uses the getorg library to output data, HTML,
# and Javascript for a standalone cluster map.
#
# Requires: glob, getorg, geopy

import glob
import getorg
from geopy import Nominatim
from geopy.extra.rate_limiter import RateLimiter

g = glob.glob("*.md")


# geopy's Nominatim now requires a user_agent parameter
geocoder = Nominatim(user_agent="talkmap")
# Respect Nominatim usage policy by limiting request rate
geocode = RateLimiter(geocoder.geocode, min_delay_seconds=1)
location_dict = {}
location = ""
permalink = ""
title = ""


for file in g:
    location = ""
    with open(file, 'r') as f:
        lines = f.read()
        if lines.find('location: "') > 1:
            loc_start = lines.find('location: "') + 11
            lines_trim = lines[loc_start:]
            loc_end = lines_trim.find('"')
            location = lines_trim[:loc_end]
                            
           
        if location:
            location_dict[location] = geocode(location)
            print(location, "\n", location_dict[location])


m = getorg.orgmap.create_map_obj()
getorg.orgmap.output_html_cluster_map(location_dict, folder_name="../talkmap", hashed_usernames=False)




