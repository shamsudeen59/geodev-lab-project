
from pathlib import Path
import geopandas as gpd

ROOT = Path(__file__).resolve().parents[2]

ward_path = ROOT / "data/processed/garatu_ward.gpkg"
facilities_path = ROOT / "data/processed/garatu_facilities.gpkg"

output_path = ROOT / "data/processed/garatu_facility_counts.gpkg"

ward = gpd.read_file(
    ward_path,
    layer="garatu_ward"
)

facilities = gpd.read_file(
    facilities_path,
    layer="garatu_facilities"
)

# Ensure both layers use the same projected CRS
ward = ward.to_crs("EPSG:32632")
facilities = facilities.to_crs(ward.crs)

# Give each polygon a unique identifier
ward = ward.reset_index(drop=True)
ward["ward_id"] = ward.index

# Spatial join: find facilities within the ward polygon
joined = gpd.sjoin(
    facilities,
    ward[["ward_id", "geometry"]],
    how="left",
    predicate="within"
)

# Count facilities assigned to each polygon
counts = (
    joined.dropna(subset=["ward_id"])
    .groupby("ward_id")
    .size()
    .reset_index(name="facility_count")
)

# Merge counts back to all polygons
ward_counts = ward.merge(
    counts,
    on="ward_id",
    how="left"
)

# Polygons without facilities receive zero
ward_counts["facility_count"] = (
    ward_counts["facility_count"]
    .fillna(0)
    .astype(int)
)

total_facilities = len(facilities)
total_counted = int(ward_counts["facility_count"].sum())

print("=" * 50)
print("GARATU HEALTH FACILITY COUNT")
print("=" * 50)

print(ward_counts[["ward", "facility_count"]].to_string(index=False))

print("\nTotal facilities in source layer:", total_facilities)
print("Total facilities counted within ward:", total_counted)

if total_counted == total_facilities:
    print("CHECK PASSED: All facilities were counted.")
else:
    print(
        "CHECK: Some facilities were not counted within the ward. "
        "Check their locations and boundary relationship."
    )

# Save the result
if output_path.exists():
    output_path.unlink()

ward_counts.to_file(
    output_path,
    layer="facility_counts",
    driver="GPKG"
)

print("\nSaved:", output_path)