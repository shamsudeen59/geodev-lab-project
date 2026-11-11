
import pandas as pd
import geopandas as gpd
from pathlib import Path

# 1. Read health facility CSV
table = pd.read_csv(
    "data/raw/garatu_health_facilities.csv"
)

print("Original records:", len(table))

# 2. Check coordinate columns
print("\nCoordinate information:")
print(table[["latitude", "longitude"]].head())

# 3. Remove records with missing coordinates
table = table.dropna(
    subset=["latitude", "longitude"]
).copy()

# 4. Convert coordinates into spatial points
facilities = gpd.GeoDataFrame(
    table,
    geometry=gpd.points_from_xy(
        table["longitude"],
        table["latitude"]
    ),
    crs="EPSG:4326"
)

print("\n===== BEFORE REPROJECTION =====")
print("Number of facilities:", len(facilities))
print("CRS:", facilities.crs)
print(facilities.head())

# 5. Load Garatu ward boundary
ward = gpd.read_file(
    "data/processed/garatu_ward.gpkg",
    layer="garatu_ward"
)

# 6. Reproject facilities to match ward CRS
facilities = facilities.to_crs(ward.crs)

print("\n===== AFTER REPROJECTION =====")
print("Facilities CRS:", facilities.crs)
print("Ward CRS:", ward.crs)

# 7. Save processed health facilities
output = Path("data/processed/garatu_facilities.gpkg")
output.parent.mkdir(parents=True, exist_ok=True)

facilities.to_file(
    output,
    layer="garatu_facilities",
    driver="GPKG"
)

print("\nSuccessfully saved:", output)
print("Total facilities saved:", len(facilities))
