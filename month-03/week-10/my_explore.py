
import pandas as pd
import geopandas as gpd

# 1. Load the health facilities CSV
facilities = pd.read_csv(
    "data/raw/garatu_health_facilities.csv"
)

print("\n===== HEALTH FACILITIES =====")
print("Shape:", facilities.shape)
print("Columns:", list(facilities.columns))
print("\nFirst five records:")
print(facilities.head())

print("\nMissing values:")
print(facilities.isna().sum())


# 2. Load the ward CSV
ward_table = pd.read_csv(
    "data/raw/garatu_ward.csv"
)

print("\n===== WARD TABLE =====")
print("Shape:", ward_table.shape)
print("Columns:", list(ward_table.columns))
print(ward_table.head())


# 3. Load the ward boundary GeoPackage
ward = gpd.read_file(
    "data/processed/garatu_ward.gpkg",
    layer="garatu_ward"
)

print("\n===== WARD BOUNDARY =====")
print("Shape:", ward.shape)
print("CRS:", ward.crs)
print("Geometry types:")
print(ward.geom_type.value_counts())
print("Bounds:", ward.total_bounds)
print(ward.head())


# 4. Load the roads GeoPackage
roads = gpd.read_file(
    "data/processed/garatu_roads.gpkg",
    layer="garatu_highways32"
)

print("\n===== ROADS DATA =====")
print("Shape:", roads.shape)
print("CRS:", roads.crs)
print("Geometry types:")
print(roads.geom_type.value_counts())

print("\nHighway classifications:")
print(roads["highway"].value_counts(dropna=False))

print("\nBoundary classifications:")
print(roads["boundary"].value_counts(dropna=False))

print("\nAll datasets have been inspected.")