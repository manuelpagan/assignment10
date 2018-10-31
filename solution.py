# Manny Pagan
# Sept 24th Python Course
# Assignment 10
# Due: Oct 31st

import requests
import geocoder

API_BASE_URL = "https://api.darksky.net/forecast/60bb82076d33e48d2cb2480bd4a8f897/"

destinations = ["The Space Needle",
                "Crater Lake",
                "The Golden Gate Bridge",
                "Yosemite National Park",
                "Las Vegas, NV",
                "Grand Canyon National Park",
                "Aspen, CO",
                "Mount Rushmore",
                "Yellowstone National Park",
                "Sandpoint, ID",
                "Banff National Park",
                "Capilano Suspension Bridge"]

for x in destinations:
    y = geocoder.arcgis(x)
    t = y.latlng[0]
    u = y.latlng[1]
    full_api_url = "{0}{1},{2}".format(API_BASE_URL, t, u)
    result = requests.request('GET', full_api_url).json()
    v = result["currently"]["summary"]
    w = result["currently"]["temperature"]
    print("{0} is located at ({1:.4f}, {2: .4f})".format(x, t, u))
    print("At {0} right now, it's {1} with a temperature of {2}\n".format(x, v, w))
