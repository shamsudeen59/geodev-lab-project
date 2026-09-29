# Project Brief

**Week 1 deliverable.** GeoDev Lab Africa, Cohort One.  
Author: Shamsudeen Mohammad

---

## 1. The question

Which part of Garatu Ward, Bosso LGA, Niger State, falls within 5 km of a health facility, and which areas fall outside this 5 km accessibility zone?

## 2. Why this question

Access to healthcare is important for community wellbeing and emergency response. Identifying areas within and outside a 5 km accessibility zone can help show where health facilities are geographically accessible and where gaps in coverage may exist. I am interested in this question because it allows me to apply GIS analysis to a real world healthcare accessibility problem.

## 3. Study area

The study area is Garatu Ward in Bosso Local Government Area, Niger State, Nigeria. The boundary of Garatu Ward will be defined using the GRID3 Nigeria Operational Ward Boundaries dataset. The analysis will focus specifically on the area contained within the Garatu Ward boundary.

## 4. What I mean by the terms

* **5 km accessibility zone:** The area located within a straight line distance of 5 km from a mapped health facility.
* **Within 5 km:** Any part of Garatu Ward that falls inside the 5 km zone around a health facility.
* **Outside the 5 km accessibility zone:** Any part of Garatu Ward that is beyond 5 km from the mapped health facilities.
* **Health facility:** A health facility represented by a point in the selected health facility dataset.

## 5. Datasets


| # | Dataset | What it gives me | Source | format |
|---|---|---|---|---|
| 1 | GRID3 Nigeria Operational LGA Boundaries | Provides the Bosso LGA boundary needed to locate the study area within Niger State. | https://data.grid3.org/ |  Geopackage (5 MB) |
| 2 | GRID3 Nigeria Operational Ward Boundaries | Provides ward boundaries and allows Garatu Ward to be identified and extracted for the analysis. | https://data.grid3.org/ | Geopackage (200 MB) |
| 3 | GRID3 Nigeria Health Facilities | Provides the locations of health facilities used to create the 5 km accessibility zones. | https://data.grid3.org/ | Geopackage (17 MB) |
| 4 | Road Network | Provides road network data for the study area and can provide additional geographic context for the analysis. | QGIS QuickOSM plugin |

*If OpenStreetMap road network coverage contains spatial gaps in remote rural settlements within Bosso LGA, satellite imagery visual inspection and digitizing will serve as a fallback.*

## 6. What "done" looks like

The finished output will be a GIS map showing Garatu Ward and the 5 km accessibility zones around the mapped health facilities. It will clearly distinguish the parts of the ward that fall within the 5 km zone from the areas that fall outside it.
The analysis should be reproducible in QGIS using the documented datasets and workflow.

## 7. Known risks

**Distance measurement.** A 5 km buffer represents straight line distance and may not reflect the actual distance people travel by road. The final map will therefore be described as a geographic accessibility analysis rather than a measure of actual travel time or road distance.

**Data completeness and accuracy.** The health facility dataset may not contain every facility or may contain locations that are outdated or inaccurate. The analysis will therefore be based on the health facilities represented in the selected dataset.

---

**Status:** Week 1 complete. Data acquisition in Week 2, see
[data-notes.md](data-notes.md).
