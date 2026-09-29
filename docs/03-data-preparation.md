# Data preparation

**Week 3 deliverable.** GeoDev Lab Africa, Cohort One.
Author: <your name>

What I reprojected, what I clipped, what I checked, and what I fixed.

---

## 1. Coordinate system decisions

**Working CRS:** <EPSG:XXXX>

**Why this one:** <One or two sentences. If you are measuring distance or
area, say that your chosen CRS is in metres and name the zone.>

| Dataset | CRS as downloaded | CRS after | Operation |
|---|---|---|---|
| <name> | EPSG:4326 | EPSG:32631 | Reprojected |
| <name> | EPSG:32631 | EPSG:32631 | No change needed |

> Reprojecting recalculates every coordinate. Assigning a CRS only
> relabels the data. Say which one you did.

## 2. Clipping to the study area

- **Boundary used:** <source and file>
- **Features before clipping:** <number>
- **Features after clipping:** <number>

<One sentence on anything unexpected, for example features that fell just
outside the boundary and whether you kept them.>

## 3. The five quality checks

| Check | Result | Action taken |
|---|---|---|
| Is the CRS what I think it is? | <yes / no> | <what you did> |
| Are there nulls in the fields I need? | <count> | <what you did> |
| Are there duplicate features? | <count> | <what you did> |
| Is the geometry valid? | <count invalid> | <what you did> |
| Does coverage span the whole study area? | <yes / no> | <what you did> |

## 4. Problems found, and what I did

**<Problem.>** <What it was, and whether you fixed it or flagged it.
Flagging honestly is acceptable. Hiding it is not.>

## 5. The analysis-ready output

- **File:** `data/processed/<filename>.gpkg`
- **Format:** GeoPackage
- **CRS:** <EPSG:XXXX>
- **Features:** <number>
- **Produced by:** <script name, or "manually in QGIS">

---

**Status:** Week 3 complete. First spatial analysis in Week 4.
