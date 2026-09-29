# Data preparation

**Week 3 deliverable.** GeoDev Lab Africa, Cohort One.  
Author: Shamsudeen Muhammad

What I reprojected, what I clipped, what I checked, and what I fixed.

---

## 1. Coordinate system decisions

**Working CRS:** EPSG:32632 (WGS 84 / UTM Zone 32N)

**Why this one:** The study area around Minna/Garatu Ward in Niger State falls within UTM Zone 32N. The CRS uses metres as its unit of measure, making it appropriate for measuring distances and areas in the 5 km health facility accessibility analysis.

| Dataset | CRS as downloaded | CRS after | Operation |
|---|---|---|---|
| Garatu Ward boundary | EPSG:4326 | EPSG:32632 | Reprojected |
| Bosso LGA boundary | EPSG:4326 | EPSG:32632 | Reprojected |
| Health facilities | EPSG:4326 | EPSG:32632 | Reprojected |
| Road network | EPSG:4326 | EPSG:32632 | Reprojected |

> Reprojecting recalculates every coordinate into the new coordinate reference system. Assigning a CRS only relabels the existing coordinates. I used reprojection, not CRS assignment.

## 2. Clipping to the study area

- **Boundary used:** GRID3 Nigeria Operational Ward Boundaries (`GARATU_ward` polygon)
- **Features before clipping:**
- 1 Garatu Ward polygon = 1 feature
-  16 health facilities = 14 point features  
- 946 roads/road segments = 946 line features
   
- **Features after clipping:** 
(1 Garatu Ward polygon = 1 feature)
(16 health facilities = 14 point features)
(943 roads/road segments = 943 line features)

The health facility and road network layers were clipped to the Garatu Ward study area so that the analysis would focus strictly on the defined study boundary.

## 3. The five quality checks

| Check | Result | Action taken |
|---|---|---|
| Is the CRS what I think it is? | Yes | Source layers were checked as EPSG:4326 and reprojected to EPSG:32632 for analysis. |
| Are there nulls in the fields I need? | Checked | Required fields were reviewed; key identifying fields are present. |
| Are there duplicate features? | No | No documented duplicate count was recorded in the attribute table. |
| Is the geometry valid? | Not recorded | No exact invalid geometry count was recorded. |
| Does coverage span the whole study area? | Yes | The Garatu Ward boundary was used as the study area reference and relevant layers were clipped to it. |

## 4. Problems found, and what I did

**Source data in geographic coordinates (EPSG:4326).** The source datasets were provided in geographic coordinates using degrees rather than metres, which is unsuitable for directly measuring a 5 km buffer distance.  
*Action:* The working datasets were reprojected to EPSG:32632 (WGS 84 / UTM Zone 32N) so that distance and area calculations could be performed in metres. Raw source files in `data/raw/` were kept untouched, and working layers were saved in `data/processed/`.

## 5. The analysis-ready output

- **File:** `data/processed/` prepared GIS layers
- **Format:** GeoPackage (`.gpkg`)
- **CRS:** EPSG:32632
- **Features:**
(1 Garatu Ward polygon = 1 feature) 

(16 health facilities = 14 point features) 

(943 roads/road segments = 943 line features)

- **Produced by:** Manually in QGIS

---

**Status:** Week 3 complete. First spatial analysis in Week 4.
