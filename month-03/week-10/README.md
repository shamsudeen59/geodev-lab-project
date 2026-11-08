# Week 10: GeoPandas, layers as tables

## What this folder contains

- explore_pandas.py: explores the ward population table.
- filter_sort.py: filters and sorts population data.
- explore_layer.py: inspects the ward GeoDataFrame.
- geom_props.py: examines geometry properties.
- csv_to_points.py: converts facility coordinates into points.
- join_population.py: joins population data to ward polygons.
- make_map.py: creates a map of health facilities.
- save_outputs.py: saves GeoPackage and CSV outputs.

## How to run it

From the repository root:

uv run month-03/week-10/make_map.py

## What I found

Using pandas and GeoPandas, I successfully loaded and analyzed tabular population data alongside spatial ward polygons. The data exploration revealed a total population of 385,800 across 12 wards, with Agbowo, Bodija, and Samonda identified as the top three most populated areas. Furthermore, converting the health facility CSV coordinates into a GeoDataFrame allowed me to successfully join attributes, visualize the spatial distribution on a map, and export clean processed outputs.

## What went wrong and how I fixed it

Initially, the tabular join between the population CSV and the ward GeoDataFrame failed to match three wards due to subtle text inconsistencies like capitalisation and hyphens. I resolved this by writing a custom python cleaning function to strip whitespaces, convert names to uppercase, and standardize formatting, which successfully achieved a 12 of 12 ward match.