
from pathlib import Path
import geopandas as gpd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[2]

ward_path = ROOT / "data/processed/garatu_ward.gpkg"
facilities_path = ROOT / "data/processed/garatu_facilities.gpkg"

output_path = ROOT / "data/processed/garatu_coverage_analysis.gpkg"
map_path = ROOT / "month-03/week-11/garatu_coverage_map.png"

TARGET_CRS = "EPSG:32632"
BUFFER_DISTANCE = 5000  # 5 kilometres in metres

# Load the datasets
ward = gpd.read_file(
    ward_path,
    layer="garatu_ward"
).to_crs(TARGET_CRS)

facilities = gpd.read_file(
    facilities_path,
    layer="garatu_facilities"
).to_crs(TARGET_CRS)

# Check that the ward geometry is available
if ward.empty or ward.geometry.is_empty.any():
    raise ValueError("The Garatu Ward geometry is empty.")

# Step 1: Create 5 km buffers around health facilities
facility_buffers = gpd.GeoDataFrame(
    geometry=facilities.geometry.buffer(BUFFER_DISTANCE),
    crs=facilities.crs
)

# Step 2: Dissolve all buffers into one coverage area
dissolved_buffers = facility_buffers.dissolve()

# Step 3: Clip coverage to the Garatu Ward boundary
covered = gpd.clip(dissolved_buffers, ward)

# Step 4: Identify areas outside all facility buffers
uncovered = gpd.overlay(
    ward[["geometry"]],
    covered[["geometry"]],
    how="difference"
)

# Step 5: Calculate area measurements
ward_area_km2 = ward.geometry.area.sum() / 1_000_000

covered_area_km2 = covered.geometry.area.sum() / 1_000_000

uncovered_area_km2 = uncovered.geometry.area.sum() / 1_000_000

uncovered_percentage = (
    uncovered_area_km2 / ward_area_km2
) * 100 if ward_area_km2 else 0

covered_percentage = (
    covered_area_km2 / ward_area_km2
) * 100 if ward_area_km2 else 0

print("=" * 60)
print("GARATU WARD: 5 KM HEALTH FACILITY COVERAGE ANALYSIS")
print("=" * 60)

print(f"Ward area: {ward_area_km2:.2f} km²")
print(f"Covered area: {covered_area_km2:.2f} km²")
print(f"Uncovered area: {uncovered_area_km2:.2f} km²")
print(f"Covered percentage: {covered_percentage:.2f}%")
print(f"Uncovered percentage: {uncovered_percentage:.2f}%")

# Step 6: Save the result layers
if output_path.exists():
    output_path.unlink()

covered.to_file(
    output_path,
    layer="covered_areas",
    driver="GPKG"
)

if not uncovered.empty:
    uncovered.to_file(
        output_path,
        layer="uncovered_areas",
        driver="GPKG",
        mode="a"
    )
    print("\nUncovered areas saved successfully.")
else:
    print("\nNo uncovered area was identified.")

# Step 7: Create the map
fig, ax = plt.subplots(figsize=(10, 10))

ward.plot(
    ax=ax,
    facecolor="none",
    edgecolor="black",
    linewidth=1.5,
    label="Garatu Ward"
)

covered.plot(
    ax=ax,
    color="lightblue",
    edgecolor="blue",
    alpha=0.6,
    label="Covered area"
)

if not uncovered.empty:
    uncovered.plot(
        ax=ax,
        color="red",
        edgecolor="darkred",
        alpha=0.85,
        label="Uncovered area"
    )

facilities.plot(
    ax=ax,
    color="darkgreen",
    markersize=25,
    marker="o",
    label="Health facilities"
)

ax.set_title(
    "Health Facility Coverage and Uncovered Areas\n"
    "Garatu Ward, Bosso LGA, Niger State",
    fontsize=13
)

ax.set_xlabel("Easting (metres)")
ax.set_ylabel("Northing (metres)")
ax.legend(loc="best")
ax.set_aspect("equal")

plt.tight_layout()
plt.savefig(map_path, dpi=300, bbox_inches="tight")
plt.close()

print("\nCoverage map saved:", map_path)
print("Coverage analysis completed.")
