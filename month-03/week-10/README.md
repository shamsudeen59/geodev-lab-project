# Month 3 – Week 10: GeoPandas and Spatial Data Processing

## Overview

This folder contains my Month 3, Week 10 GeoDev Lab exercises, focusing on working with geospatial data in Python using GeoPandas, Pandas and Matplotlib.

The week's activities involved exploring spatial datasets, inspecting geometries, processing tabular data, converting coordinate data into spatial points, performing data joins, creating maps and saving processed outputs.

### Python Libraries

The project uses the following Python libraries:

- **Pandas:** For reading and processing tabular data.
- **GeoPandas:** For loading, processing and analysing geospatial datasets.
- **Matplotlib:** For creating and visualising maps.

The work is divided into two main parts:

1. **Guided Practice:** Completing the Week 10 exercises using the provided teaching datasets.
2. **Independent Project:** Applying the knowledge gained to my existing Garatu health facility and road network project using my Month 1 datasets.

---

# 1. Guided Practice

The guided exercises introduced the use of Python for exploring, processing and visualising geospatial data.

The activities involved working with tabular population data, spatial ward polygons and health facility coordinates.

### Scripts and Activities

| Script | Description |
|---|---|
| `explore_pandas.py` | Explores the ward population table using Pandas. |
| `filter_sort.py` | Filters and sorts population records and creates additional columns. |
| `explore_layer.py` | Inspects the ward GeoDataFrame, including its attributes, geometry types and CRS. |
| `geom_props.py` | Examines geometry properties and checks geometry validity. |
| `csv_to_points.py` | Converts health facility CSV coordinates into spatial point geometries. |
| `join_population.py` | Joins population data to ward polygons and handles inconsistent ward names. |
| `make_map.py` | Creates a map showing health facilities and ward boundaries. |
| `save_outputs.py` | Exports processed GeoPackage data and CSV outputs. |

### How to Run the Guided Scripts

All scripts are executed from the root directory of the GeoDev Lab project.

```bash
uv run month-03/week-10/explore_pandas.py
uv run month-03/week-10/filter_sort.py
uv run month-03/week-10/explore_layer.py
uv run month-03/week-10/geom_props.py
uv run month-03/week-10/csv_to_points.py
uv run month-03/week-10/join_population.py
uv run month-03/week-10/make_map.py
uv run month-03/week-10/save_outputs.py
```

### What I Found

Using Pandas and GeoPandas, I successfully loaded and analysed tabular population data alongside spatial ward polygons.

The data exploration revealed:

- A total population of **385,800** across 12 wards.
- Agbowo, Bodija and Samonda were identified as the three most populated areas.
- Filtering and sorting operations helped identify wards based on their population values.
- Converting health facility CSV coordinates into a GeoDataFrame allowed the facility locations to be represented as spatial points.
- Population attributes were successfully joined to ward polygons.
- The resulting spatial data was visualised on a map and exported into processed output files.

### Challenges Encountered and How I Fixed Them

Initially, the tabular join between the population CSV and the ward GeoDataFrame failed to match three wards because of inconsistencies in the ward names, including differences in capitalisation, trailing spaces and hyphens.

To resolve this issue, I created a custom Python function to clean and standardise the ward names by:

- Removing unnecessary whitespace.
- Converting names to uppercase.
- Replacing hyphens with spaces.

After applying the cleaning function, the join successfully matched all **12 out of 12 wards**.

This exercise helped me understand the importance of data cleaning and standardisation when joining tabular and spatial datasets.

---

# 2. Independent Project: Garatu Health Facility and Road Network Analysis

For the independent exercise, I adapted the Week 10 workflows to my existing Month 1 GIS project.

Instead of using the course's Ibadan population datasets, I used my own geographical datasets for Garatu, Bosso Local Government Area, Niger State, Nigeria.

### Project Focus

The project focuses on the spatial distribution of health facilities, ward boundaries and road networks within the study area.

### Datasets Used

The following datasets were used:

| Dataset | File |
|---|---|
| Health facilities | `garatu_health_facilities.csv` |
| Ward information | `garatu_ward.csv` |
| Ward boundary | `garatu_ward.gpkg` |
| Road network | `garatu_roads.gpkg` |

### Data Sources

- Health facility data: Existing Month 1 project dataset.
- Ward boundary data: Existing Month 1 project dataset.
- Road network data: OpenStreetMap-derived project dataset.

### Project Objectives

1. Explore and inspect the available geographical datasets.
2. Examine the structure, attributes and coordinate reference systems of the datasets.
3. Convert health facility coordinates into spatial point geometries.
4. Reproject spatial data into a common coordinate reference system.
5. Perform a spatial join to associate health facilities with the ward boundary.
6. Visualise health facilities, ward boundaries and road networks.
7. Export the processed spatial datasets and final map.

---

## 3. Independent Project Scripts

The following Python scripts are used for the independent exercise.

| Script | Description |
|---|---|
| `my_explore.py` | Loads and explores the health facility, ward and road datasets. |
| `my_points.py` | Converts health facility CSV coordinates into spatial points and saves them as a GeoPackage. |
| `my_join.py` | Performs a spatial join between health facilities and the Garatu ward boundary. |
| `my_map.py` | Creates a map showing health facilities, ward boundaries and road network features. |

---

## 4. Project Folder Structure

The Week 10 project uses the following folder structure:

```text
month-03/
└── week-10/
    │
    ├── explore_pandas.py
    ├── filter_sort.py
    ├── explore_layer.py
    ├── geom_props.py
    ├── csv_to_points.py
    ├── join_population.py
    ├── make_map.py
    ├── save_outputs.py
    │
    ├── my_explore.py
    ├── my_points.py
    ├── my_join.py
    ├── my_map.py
    │
    ├── my_map.png
    └── README.md

datas/
│
├── raw/
│   ├── garatu_health_facilities.csv
│   └── garatu_ward.csv
│
└── processed/
    ├── garatu_roads.gpkg
    ├── garatu_ward.gpkg
    ├── garatu_facilities.gpkg
    └── garatu_facilities_with_ward.gpkg
```

---

## 5. Coordinate Reference System

The health facility coordinates were originally provided in geographic coordinates (EPSG:4326).

The ward boundary and road network datasets use EPSG:32632 (WGS 84 / UTM Zone 32N).

The health facility points are reprojected to EPSG:32632 to ensure consistency when working with the spatial layers.

---

## 6. Independent Project Outputs

The independent exercise produces the following outputs:

| Output | Description |
|---|---|
| `garatu_facilities.gpkg` | Processed health facility point dataset. |
| `garatu_facilities_with_ward.gpkg` | Health facility dataset with associated ward attributes. |
| `my_map.png` | Visualisation of Garatu ward boundary, health facilities and road network. |

---

## 7. How to Run the Independent Scripts

The scripts are executed from the root directory of the GeoDev Lab project.

Run the following commands in the VS Code terminal:

```bash
uv run month-03/week-10/my_explore.py
```

```bash
uv run month-03/week-10/my_points.py
```

```bash
uv run month-03/week-10/my_join.py
```

```bash
uv run month-03/week-10/my_map.py
```

Ensure the required datasets are available in their specified folders before running the scripts.

---

## 8. Learning Outcomes

Through the Week 10 exercises, I gained practical experience in:

- Working with Pandas and GeoPandas.
- Understanding the relationship between tabular and spatial data.
- Exploring spatial datasets and their attributes.
- Understanding coordinate reference systems and reprojection.
- Converting coordinate tables into spatial point datasets.
- Filtering, sorting and cleaning tabular data.
- Performing attribute joins and spatial joins.
- Checking geometry properties and validity.
- Visualising geographical features using Python.
- Saving processed geospatial data in GeoPackage format.

---

## 9. Conclusion

Month 3, Week 10 provided an opportunity to develop practical skills in Python-based geospatial data processing.

The guided exercises introduced the fundamental concepts of working with tabular and spatial data using Pandas and GeoPandas.

Building on these skills, I adapted the independent exercise to my existing Month 1 Garatu GIS project, applying the techniques to my own health facility, ward boundary and road network datasets.

This helped me connect the concepts learned during the guided practice with an existing geographical project while developing my understanding of GIS automation, spatial data processing and geospatial analysis using Python.

**Project:** Garatu Health Facility and Road Network Analysis  
**Programme:** GeoDev Lab Africa – Cohort One  
**Module:** Month 3 – Week 10  
**Software:** Python, GeoPandas, Pandas and Matplotlib