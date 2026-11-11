
import geopandas as gpd

# 1. Load Garatu ward boundary
ward = gpd.read_file(
    "data/processed/garatu_ward.gpkg",
    layer="garatu_ward"
)

# 2. Load processed health facilities
facilities = gpd.read_file(
    "data/processed/garatu_facilities.gpkg",
    layer="garatu_facilities"
)

print("Health facilities:", len(facilities))
print("Ward features:", len(ward))

# 3. Make sure both datasets use the same CRS
facilities = facilities.to_crs(ward.crs)

# 4. Select useful ward attributes
ward_attributes = ward[
    ["ward", "lga", "state", "area_sqkm", "geometry"]
].copy()

# 5. Perform spatial join
joined = gpd.sjoin(
    facilities,
    ward_attributes,
    how="left",
    predicate="within"
)

# 6. Inspect the results
print("\n===== SPATIAL JOIN RESULTS =====")
print("Joined records:", len(joined))

print("\nFacilities matched to a ward:")
print(joined["ward"].value_counts(dropna=False))

print("\nUnmatched facilities:")
print(joined["ward"].isna().sum())

# 7. Save joined dataset
joined.to_file(
    "data/processed/garatu_facilities_with_ward.gpkg",
    layer="facilities_with_ward",
    driver="GPKG"
)

print("\nSpatial join completed successfully.")
