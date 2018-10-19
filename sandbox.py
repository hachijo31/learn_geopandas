#!/usr/bin/python3
#import pandas as pd
import geopandas as gpd
#from shapely.geometry import Point
#import matplotlib.pyplot as plt

CENSUS_SHAPE_PATH = 'census_tracts_shape/gz_2010_36_140_00_500k.shp'
#df = gpd.read_file('naturalearth_cities')
#ax = df.plot(figsize=(10, 10), alpha=0.5, edgecolor='k')
#df = gpd.read_file('naturalearth_lowres')
df = gpd.read_file(CENSUS_SHAPE_PATH)
#ax = df.plot(figsize=(10, 10), alpha=0.5, edgecolor='k')
