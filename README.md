# Garatu Ward Health Facility Accessibility

This project uses GIS and spatial analysis to identify which parts of Garatu Ward, Bosso Local Government Area, Niger State, are within 5 km of health facilities and which parts are outside the 5 km coverage.

**GeoDev Lab Africa, Cohort One.** Shamsudeen Mohammed

---

## The question

> which part of Garatu Ward, Bosso LGA, Niger State, falls within 5 km of a health facility, and which areas fall outside this 5 km accessibility zone?

## What's in here

```text
Garatu-Ward-Health-Facility-Accessibility/

geodev-lab-project/
│
├── data/
│   ├── raw/
│   │   ├── ward_population.csv
│   │   ├── health_facilities.csv
│   │   ├── garatu_health_facilities.csv
│   │   └── garatu_ward.csv
│   │
│   └── processed/
│       ├── wards.gpkg
│       ├── roads.gpkg
│       ├── facilities.gpkg
│       ├── week10_outputs.gpkg
│       ├── garatu_roads.gpkg
│       ├── garatu_ward.gpkg
│       ├── garatu_facilities.gpkg
│       └── garatu_facilities_with_ward.gpkg
│
├── docs/
│   ├── 01-project-brief.md       Week 1
│   ├── 02-data-notes.md          Week 2
│   ├── 03-data-preparation.md    Week 3
│   └── 04-month-1-summary.md     Week 4
├──month-03/
    └── week-10/
        ├── README.md
        ├── explore_pandas.py
        ├── filter_sort.py
        ├── explore_layer.py
        ├── geom_props.py
        ├── csv_to_points.py
        ├── join_population.py
        ├── make_map.py
        ├── save_outputs.py
        ├── facilities_map.png
        ├── my_explore.py
        ├── my_points.py
        ├── my_join.py
        ├── my_map.py
        └── my_map.png
├── screenshots/
│   ├── week5.png
│   ├── week6.png
│   ├── week7_01.png
│   ├── week7_02.png
│   ├── week7_03.png
│   ├── week7_04.png
│   ├── week8.png
│   └── week9.png
├── src/
│   └── geodev_lab_project/
│       └── __init__.py
├── .gitignore
├── analyse.py
├── check.py
├── garatu_health_facilities.csv
├── hello.py
├── inspect_data.py
├── pyproject.toml
├── README.md
├── summary.py
├── uv.lock
└── wards.csv

├── scripts/

└── requirements.txt
```

## Progress

- [x] Week 1, project brief with a source link for every dataset
- [x] Week 2, data downloaded, opened and described
- [x] Week 3, reprojected, clipped and quality checked
- [x] Week 4, first spatial analysis, checked four ways

---

## Month 1 Summary

This month, I gained practical experience in using QGIS to analyze health facility accessibility in Garatu Ward, Bosso LGA. I learned how to prepare spatial datasets, work with coordinate reference systems, and perform 5 km buffer analysis. One important lesson was understanding how overlapping buffers can be dissolved to show overall coverage more clearly. This project strengthened my understanding of GIS workflows and how spatial analysis can help investigate real world problems.

## Month 1 completed

---

## Month 2: development environment and early Python

- [x] Week 5, set up Python, VS Code and the terminal; hello.py runs
- [x] Week 6, environments and project setup configured with uv
- [x] Week 7, core Python fundamentals and the six ideas implemented
- [X] Week 8, data files loaded, parsed, and inspected with Python
- [X] Week 9, code consolidation, refactoring, and capstone summary report

---

## Month 2 reflection

This month, I learned how to use Python to read, inspect, and analyse data from CSV files. The idea that finally became clearer to me was how functions help organise code into smaller sections, making it easier to understand and reuse. I am still working on becoming more confident with dictionaries, loops, and handling missing or incorrect data. My capstone helped me understand my Month 1 GIS dataset better by summarising its latitude and longitude values and showing the range and number of records in each column.

## Month 2 completed

---

## Month 03 - Geospatial Python And Automation

- [x] Week 10: GeoPandas, layers as tables
- [ ] Week 11: Coordinate reference systems and spatial operations
- [ ] Week 12: Rasters with Rasterio
- [ ] Week 13: Batch processing and automation
- [ ] Week 14: Build week, your analysis pipeline 

---

For complete project details, see **[Project Brief](docs/01-project-brief.md)**
