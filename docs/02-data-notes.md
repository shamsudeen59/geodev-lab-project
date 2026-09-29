# Data notes

**Week 2 deliverable.** GeoDev Lab Africa, Cohort One.  
**Author:** Shamsudeen Muhammad

What I downloaded, where it came from, what is in it, and what is wrong with it.

---

## Summary

| # | Dataset | Type | Retrieved | Status |
|---|---|---|---|---|
| 1 | Nigeria Operational Wards (`GARATU_ward`) | Vector | 2026-09-10 | OK |
| 2 | Health Facilities Layer | Vector | 2026-09-10 | OK |
| 3 | Bosso LGA Operational Boundary | Vector | 2026-09-10 | OK |
| 4 | Major Highways and Local Access Roads | Vector | 2026-09-13 | OK |

---

## 1. Nigeria Operational Wards (`GARATU_ward`)

* **Source:** https://data.grid3.org (Data Producer: CIESIN)
* **Retrieved:** 2026-09-10
* **File:** `data/raw/GARATU_ward.gpkg`
* **Format:** GeoPackage
* **Geometry type:** Polygon (Vector)
* **Feature count:** 1 feature
* **CRS as downloaded:** EPSG:4326 (WGS 84)

### Key columns

| Column | What it holds | Nulls |
|---|---|---|
| `country` | Country name (`Nigeria`) | 0 |
| `iso3` | Country ISO3 code (`NGA`) | 0 |
| `state` | State name (`Niger`) | 0 |
| `statecode` | State code (`NI`) | 0 |
| `lga` | Local Government Area (`Bosso`) | 0 |
| `lga_alt_na` | Alternate LGA name | Recorded NULLs |
| `ward` | Ward name (`Garatu`) | 0 |
| `ward_alt_n` | Alternate ward name | Recorded NULLs |
| `ward_v1_gr` | Ward version group | Recorded NULLs |
| `ward_in_gr` | Ward index code (`1.00000000000`) | 0 |
| `multipart_` | Multipart geometry indicator (`1.00000000000`) | 0 |
| `source` | Data provenance (`CIESIN`) | 0 |
| `date` | Layer record date (`2026-06-30`) | 0 |
| `area_sqkm` | Total ward surface area (`321.000000000000`) | 0 |

### What I noticed

The dataset contains one polygon that fully delineates the administrative boundary of Garatu Ward. The important administrative fields correctly identify the area as Garatu Ward, Bosso LGA, Niger State, Nigeria.

`NULL`values were recorded in (`lga_alt_na`, `ward_alt_n`, and `ward_v1_gr`). These are alternate or supporting fields and do not prevent the ward from being identified using the main administrative fields.

The recorded ward area is 321.00 km².

---

## 2. Health Facilities Layer

* **Source:** https://data.grid3.org
* **Retrieved:** 2026-09-10
* **File:** `data/raw/health_facilities.gpkg`
* **Format:** GeoPackage
* **Geometry type:** Point (Vector)
* **Feature count:** 16 features in the attribute table 
* **CRS as downloaded:** EPSG:4326 (WGS 84)

### Key columns

| Column | What it holds | Nulls |
|---|---|---|
| `facility_n` | Name of the health facility | 0 |
| `latitude` | Latitude coordinate | 0 |
| `longitude` | Longitude coordinate | 0 |
| `facility_l` | Facility level | 4 |
| `facility_t` | Facility type | 4 |
| `facility_o` | Facility ownership | 4 |
| `functional` | Facility functional status | 4 |
| `alt_name` | Alternative facility name | 6 |
| `settlement` | Settlement type/location | 0 |
| `date_creat` | Facility record creation date | 6 |
| `issues` | Recorded data-quality issues | 12 |
### What I noticed

The attribute table contains 16 health-facility records, while 14 locations are visible on the map. Some records are flagged as clustered with another point within 50 m and 100 m, which may explain the difference and requires further quality checking.

The dataset also contains additional information on facility level, type, ownership, functional status, settlement, and other metadata. Some secondary attributes contain null values, while the facility names and latitude/longitude fields are populated for all 16 records.

**Confirmed Facilities List:**
1. Alura Primary Health Center
2. Bangifu Baby Friendly Hospital
3. Garatu Health Center / Tsohon Daga Primary Health Centre
4. Gbata Primary Health Centre
5. Gidan Kwano Primary Health Centre
6. Gidan Mongoro Primary Health Centre
7. Kodoko Health Post
8. Lunko Primary Health Centre
9. Mai Unguwar Bosso Health Post
10. Pompo Health Post
11. Sabon Daga Primary Health Centre
12. Sabon Lunko Primary Health Center
13. Zamani Maternity Home Clinic

---

## 3. Bosso LGA Operational Boundary

* **Source:** https://data.grid3.org
* **Retrieved:** 2026-09-10
* **File:** `data/raw/bosso_lga_boundary.gpkg`
* **Format:** GeoPackage
* **Geometry type:** Polygon (Vector)
* **Feature count:** 1 feature
* **CRS as downloaded:** EPSG:4326 (WGS 84)

### Key columns

| Column | What it holds | Nulls |
|---|---|---|
| `country` | Country name (`Nigeria`) | 0 |
| `state` | State name (`Niger`) | 0 |
| `lga` | LGA name (`Bosso`) | 0 |
| `source` | Data source attribution | 0 |

### What I noticed

The dataset contains one polygon representing Bosso Local Government Area, Niger State. It provides the wider administrative context for the Garatu Ward study area.

No null values were recorded in the important fields.

The LGA boundary is not the main analysis boundary, but it helps confirm the location of Garatu Ward within Bosso LGA.

---

## 4. Major Highways and Local Access Roads

* **Source:** OpenStreetMap (via QGIS QuickOSM plugin)
* **Retrieved:** 2026-09-13
* **File:** `data/raw/roads_osm.gpkg`
* **Format:** GeoPackage
* **Geometry type:** Line / Polyline (Vector)
* **Feature count:** Multiple line features
* **CRS as downloaded:** EPSG:4326 (WGS 84)

### Key columns

| Column | What it holds | Nulls |
|---|---|---|
| `highway` | Road classification (primary, secondary, residential) | 0 |
| `name` | Road/street name | Present on major highways; NULL on local tracks |
| `ref` | Official route number/reference code | Present on primary arterial routes |

### What I noticed

The road network contains major highways, primary arterial roads, secondary routes, and local access paths connecting areas across Garatu Ward and the surrounding parts of Bosso LGA.

Some local access tracks do not have name attributes. This does not prevent the roads from being used as spatial data, but it means that some roads cannot be identified by name.

The road data was obtained through the `QuickOSM` plugin and clipped to the study area.
---

## Cross-cutting problems

* **Unprojected Geographic Coordinate System:** All raw datasets arrived in EPSG:4326 (WGS 84). Performing distance or buffer analysis directly in geographic degrees introduces significant distortion. All layers was clipped and reprojected to EPSG:32632 (WGS 84 / UTM Zone 32N) prior to proximity modeling.
* **Extent Mismatch:** Raw layers cover wider administrative regions (national/state/LGA levels). Clipping to the Garatu Ward study area boundary is required to isolate local features and streamline processing.

---

## CRS and Preparation

* **Source CRS:** All source layers arrived in EPSG:4326 (WGS 84).
* **Study Area:** Garatu Ward, Bosso LGA, Niger State, Nigeria (~321.00 sq. km).
* **Geoprocessing:** Clipped health facilities and OSM road networks to the Garatu Ward boundary, then reprojected all clipped layers to **EPSG:32632 (WGS 84 / UTM Zone 32N)**.
* **Storage:** Working files are stored in `data/processed/`; raw files remain untouched in `data/raw/`.

---

**Status:** Week 2 complete. Reprojection and quality checks in Week 3, see [data-preparation.md](03-data-preparation.md).
