# data_notes.md

## Project Information

Project Name: Health Facility Distribution and Proximity Analysis
Study Area: Garatu Ward
LGA: Bosso Local Government Area
State: Niger State
Country: Nigeria (ISO3: NGA)
Spatial Area Measurement: 321.00 sq. km

## Datasets Used

### 1. Nigeria Operational Wards
Dataset : GARATU_ward
Data Source: GRID3 ( https://data.grid3.org )
Download : 2026-09-10
Dataset Version: v3.0
Study Area / Coverage: Garatu Ward, Bosso LGA, Niger State, Nigeria
Number of Features : 1 feature
Geometry Type: Polygon (Vector)
  Columns :
  country  (Text) — Country name (Nigeria)
  iso3 (Text) — Country ISO3 code (NGA)
  state (Text) — State name (Niger)
  statecode (Text) — State code (NI)
  lga (Text) — Local Government Area (Bosso)
  lga_alt_na (Text) — Alternate LGA name
  ward (Text) — Ward name (Garatu)
  ward_alt_n (Text) — Alternate ward name
  ward_v1_gr (Text) — Ward version group
  ward_in_gr (Text) — Ward index code (1.00000000000)
  multipart_ (Text) — Multipart geometry indicator (1.00000000000)
  source (Text) — Data provenance (CIESIN)
  date (Text) — Layer record date (2026-06-30)
  area_sqkm (Real/Double) — Total ward surface area (321.000000000000)
  Data Types of Important Fields:** Text, Real/Double
  Null :  NULL values recorded in lga_alt_na, ward_alt_n, and ward_v1_gr.
  Coverage Observations : Single polygon fully delineating the administrative boundary of Garatu Ward.

### 2. Health Facilities Layer
Dataset : Health Facilities
Data Source: GRID3 (https://data.grid3.org)
Download : 2026-09-10
Dataset Version: v3.0
Study Area / Coverage: Garatu Ward and immediate vicinity (Bosso LGA)
Number of Features : 13 point features identified in the study layout
Geometry Type: Point (Vector)
Important Columns : Facility Name, Location Coordinates
Data Types of Important Fields: Text, Point Geometry
Null : 76
Coverage Observations : Point locations cover primary health centers, maternity homes, clinics, and health posts within and immediately surrounding the Garatu Ward boundary.
Confirmed Health Facilities List:
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

### 3. LGA Operational Boundary
Dataset : Bosso LGA Boundary
Data Source: GRID3 (https://data.grid3.org)
Download :  2026-09-10
Dataset Version:  v3.0
Study Area / Coverage: Bosso Local Government Area, Niger State
Number of Features / Records: 1 feature
Geometry Type: Polygon (Vector)
Important Columns / Fields: country, state, lga, source
Data Types of Important Fields: Text, Polygon Geometry
Null : Not recorded
Coverage Observations : Provides the surrounding local government contextual boundary for Garatu Ward.

### 4. Road Network
Dataset / Layer Name: Major Highways and Local Access Roads
Data Source: OpenStreetMap (via QuickOSM tool)
Download :   2026-09-13
Dataset Version: OpenStreetMap live dataset
Study Area / Coverage: Garatu Ward and connecting transport corridors in Bosso LGA
Number of Features : Multiple line features
Geometry Type: Line / Polyline (Vector)
Important Columns : highway, name, ref
Data Types of Important Fields: Text, Line Geometry
Null : Unnamed local access tracks lack name attributes.
Coverage Observations or Gaps: Contains major highways, primary arterial roads, secondary routes, and local access paths providing transportation connectivity across the ward.


## CRS and Preparation

- All source layers were in EPSG:4326 (WGS 84).
- Study area: Garatu Ward, Bosso LGA, Niger State, Nigeria.
- All layers were clipped to the study area: Garatu health facilities and Garatu highways from QuickOSM. The clipped layers were then reprojected to EPSG:32632 (WGS 84 / UTM zone 32N).
- Area check: 321.00 km².
- Working files are stored in data/processed/; raw files remain untouched.


## Data Methodology Summary

Administrative Boundary (GARATU_ward):Defines the primary geographic boundary and spatial extent (321.00 sq. km) for Garatu Ward within Bosso LGA.
Health Facilities Layer: Supplies point geometries and names for healthcare facilities to evaluate geographic distribution and service access within the study area.
LGA Operational Boundary: Provides broader administrative context connecting Garatu Ward to the wider Bosso Local Government Area.
Road Network: Maps transportation corridors and local roads to analyze physical access routes connecting population settlement centers to health facilities.
