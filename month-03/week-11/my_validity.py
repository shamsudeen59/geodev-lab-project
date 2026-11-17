
from pathlib import Path
import geopandas as gpd

ROOT = Path(__file__).resolve().parents[2]

ward_path = ROOT / "data/processed/garatu_ward.gpkg"
output_path = ROOT / "data/processed/garatu_ward_validated.gpkg"

ward = gpd.read_file(
    ward_path,
    layer="garatu_ward"
)

print("=" * 50)
print("GARATU WARD GEOMETRY VALIDITY CHECK")
print("=" * 50)

# Count invalid geometries before repair
invalid_before = (~ward.geometry.is_valid).sum()

print("Invalid geometries before repair:", invalid_before)

# Repair invalid geometries
ward["geometry"] = ward.geometry.make_valid()

# Count invalid geometries after repair
invalid_after = (~ward.geometry.is_valid).sum()

print("Invalid geometries after repair:", invalid_after)

if invalid_after == 0:
    print("CHECK PASSED: All geometries are valid.")
else:
    print("WARNING: Some geometries remain invalid.")

# Save the validated layer
if output_path.exists():
    output_path.unlink()

ward.to_file(
    output_path,
    layer="garatu_ward_validated",
    driver="GPKG"
)

print("\nValidated ward layer saved:", output_path)
