#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 15:59:58 2020

@author: ragarner
"""

import json
import urllib.request
from pprint import pprint

def get_local_weather():
    
    weather_base_url = 'http://forecaset.weather.gov/MapClick.php?FcstType=json&'
    
    places = {
        'Austin': ['30.3074624', '-98.0335911'],
        'Portland': ['45.542094', '-122.9346037'],
        'Dallas': ['32.77822000000003', '-96.79511999999994']
    }
    
    for place in places:
        latitude, longitude = places[place][0], places[place][1]
        weather_url = weather_base_url + "lat=" + latitude + "&lon" + longitude
        # Show the URL we use to ger the weater data. (Paste this URL into browser)
        
        # print("Getting the current weather for", place, "at", weather_url, ":")
        
        page_response = urllib.urlopen(weather_url).read()