
from pathlib import Path
import geopandas as gpd

ROOT = Path(__file__).resolve().parents[2]

datasets = {
    "Garatu Ward": (
        ROOT / "data/processed/garatu_ward.gpkg",
        "garatu_ward",
    ),
    "Health Facilities": (
        ROOT / "data/processed/garatu_facilities.gpkg",
        "garatu_facilities",
    ),
    "Roads": (
        ROOT / "data/processed/garatu_roads.gpkg",
        "garatu_highways32",
    ),
}

TARGET_CRS = "EPSG:32632"

print("=" * 60)
print("GARATU PROJECT: CRS AND MEASUREMENT CHECK")
print("=" * 60)

projected_layers = {}

for name, (path, layer_name) in datasets.items():
    gdf = gpd.read_file(path, layer=layer_name)

    print(f"\n{name}")
    print("-" * 40)
    print("Original CRS:", gdf.crs)
    print("Estimated UTM CRS:", gdf.estimate_utm_crs())

    projected = gdf.to_crs(TARGET_CRS)
    projected_layers[name] = projected

    print("Reprojected CRS:", projected.crs)

ward = projected_layers["Garatu Ward"]
facilities = projected_layers["Health Facilities"]
roads = projected_layers["Roads"]

ward_area_km2 = ward.geometry.area.sum() / 1_000_000
line_length_km = roads.geometry.length.sum() / 1_000

print("\n" + "=" * 60)
print("MEASUREMENTS")
print("=" * 60)

print(f"Garatu Ward area: {ward_area_km2:.2f} km²")
print(f"Health facilities: {len(facilities)}")
print(f"Total length of all line features: {line_length_km:.2f} km")

print("\nCRS check completed successfully.")
