# Month 03 – Week 11: Coordinate Reference Systems and Spatial Analysis

## Overview

This practical focuses on applying coordinate reference systems, spatial operations, geometry validation, and distance based accessibility analysis using Python and GeoPandas.

The independent challenge uses my own health facility accessibility project in Garatu Ward, Bosso Local Government Area, Niger State, Nigeria.

## Study Area and Research Question

**Study Area:** Garatu Ward, Bosso LGA, Niger State, Nigeria.

**Research Question:**

Which parts of Garatu Ward are covered by at least one 5 km health facility buffer, and which parts are outside all buffers?

The analysis investigates the geographical coverage of health facilities using a 5 km straight line distance threshold.

## Datasets

The following processed datasets were used:

| Dataset | File | Geometry |
|---|---|---|
| Garatu Ward boundary | `garatu_ward.gpkg` | MultiPolygon |
| Health facilities | `garatu_facilities.gpkg` | Point |
| Roads and other line features | `garatu_roads.gpkg` | MultiLineString |

The ward boundary contains one feature, the health facility dataset contains 16 point features, and the line dataset contains 495 features.

## Coordinate Reference System

All three spatial datasets use:

**EPSG:32632 – WGS 84 / UTM Zone 32N**

The estimated UTM CRS for the datasets also returned EPSG:32632.

This CRS was selected because Garatu Ward is located in Niger State, Nigeria, within UTM Zone 32N. Its projected coordinates are measured in metres, making it suitable for spatial distance and area calculations.

The scripts also check the original CRS and estimated UTM CRS before performing measurements.

## Practical Exercises

### 1. CRS Verification and Measurement – `my_crs.py`

This script:

- Checks the original CRS of the ward, facilities, and roads datasets.
- Estimates the appropriate UTM CRS.
- Reprojects the datasets to EPSG:32632.
- Calculates the Garatu Ward area in square kilometres.
- Calculates the total length of the line features in kilometres.

### 2. Health Facility Point Count – `my_count.py`

This exercise uses GeoPandas spatial joins to count health facilities within the Garatu Ward polygon.

The analysis uses:

- `gpd.sjoin()`
- `groupby()`
- `merge()`

The resulting facility count is merged back to the ward polygon. This ensures that polygons without facilities can still receive a count of zero.

A total-count check is included to compare the number of facilities in the original dataset with the number assigned to the ward.

### 3. Health Facility Coverage Analysis – `my_reach.py`

This exercise investigates areas within and outside the 5 km health facility coverage zones.

The analysis follows these operations:

1. Creates a 5,000-metre buffer around each health facility.
2. Dissolves the individual buffers into a combined coverage area.
3. Clips the coverage area to the Garatu Ward boundary.
4. Uses spatial difference analysis to identify uncovered areas.
5. Calculates covered and uncovered areas in square kilometres.
6. Calculates the percentage of the ward covered and uncovered.
7. Saves the output spatial layers and produces a map.

### 4. Geometry Validity – `my_validity.py`

This script checks the validity of the Garatu Ward polygon geometry.

It:

- Counts invalid geometries before repair.
- Uses `make_valid()` to repair invalid geometries where necessary.
- Checks the geometry validity again.
- Saves the validated ward dataset.

## Outputs

The practical produces the following outputs:

| Output | Description |
|---|---|
| `garatu_facility_counts.gpkg` | Ward polygon with health facility count |
| `garatu_ward_validated.gpkg` | Validated Garatu Ward geometry |
| `garatu_coverage_analysis.gpkg` | Covered and uncovered spatial areas |
| `garatu_coverage_map.png` | Map showing health facility coverage and uncovered areas |

The coverage map uses different colours to distinguish covered areas, uncovered areas, the ward boundary, and health facility locations.

## Project Structure

The Week 11 project uses the following folder structure:

```text
month-03/
└── week-10/
└── week-11/
    ├── area_wrong_and_right.py
    ├── set_vs_to.py
    ├── one_point.py
    ├── spatial_ops.py
    ├── coverage_gap.py
    ├── nearest.py
    ├── clip_dissolve.py
    ├── my_crs.py
    ├── my_count.py
    ├── my_validity.py
    ├── my_reach.py
    ├──garatu_coverage_map.png
    ├── README.md
    └── fix_geometry.py
```

---

## Methodological Limitation

The 5 km buffer analysis measures straight-line geographical distance from health facilities. It does not account for actual road-network travel distances, travel time, terrain, transport availability, facility capacity, or service quality. Therefore, an area outside the 5 km buffer is identified as geographically uncovered under the selected distance threshold, but this does not establish that residents cannot access healthcare. A more detailed accessibility assessment would require network-based analysis and additional information about the health facilities and transportation conditions.

## Conclusion

This practical applies coordinate reference system verification, spatial joins, buffer analysis, overlay operations, geometry validation, and cartographic visualisation to a real world health facility accessibility project.

It demonstrates how Python and GeoPandas can support spatial analysis and help identify geographical gaps in health facility coverage.