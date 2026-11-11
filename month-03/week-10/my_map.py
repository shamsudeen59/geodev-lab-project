
import geopandas as gpd
import matplotlib.pyplot as plt
from pathlib import Path
from matplotlib.lines import Line2D

# 1. Load ward boundary
ward = gpd.read_file(
    "data/processed/garatu_ward.gpkg",
    layer="garatu_ward"
)

# 2. Load roads
roads = gpd.read_file(
    "data/processed/garatu_roads.gpkg",
    layer="garatu_highways32"
)

# 3. Load joined health facilities
facilities = gpd.read_file(
    "data/processed/garatu_facilities_with_ward.gpkg",
    layer="facilities_with_ward"
)

# 4. Select highway features
highways = roads[
    roads["highway"].notna()
].copy()

# 5. Select administrative boundary features
admin_boundaries = roads[
    roads["boundary"] == "administrative"
].copy()

# 6. Create map
fig, ax = plt.subplots(figsize=(11, 9))

# Plot ward boundary
ward.plot(
    ax=ax,
    facecolor="#F1F4F8",
    edgecolor="#17365D",
    linewidth=2,
    zorder=1
)

# Plot all classified roads
highways.plot(
    ax=ax,
    color="#A7A7A7",
    linewidth=0.7,
    zorder=2
)

# Highlight primary highways
primary = highways[
    highways["highway"] == "primary"
]

primary.plot(
    ax=ax,
    color="#D97706",
    linewidth=2,
    zorder=3
)

# Plot administrative boundary features
if not admin_boundaries.empty:
    admin_boundaries.plot(
        ax=ax,
        color="#7B3294",
        linewidth=1.5,
        linestyle="--",
        zorder=4
    )

# Plot health facilities
facilities.plot(
    ax=ax,
    color="#D62728",
    edgecolor="white",
    markersize=45,
    marker="o",
    zorder=5
)

# 7. Add title
ax.set_title(
    "Health Facilities and Road Network in Garatu Ward",
    fontsize=15,
    fontweight="bold",
    pad=18
)

# 8. Add legend
legend_items = [
    Line2D(
        [0], [0],
        color="#17365D",
        linewidth=2,
        label="Garatu Ward Boundary"
    ),
    Line2D(
        [0], [0],
        color="#A7A7A7",
        linewidth=1.5,
        label="Road Network"
    ),
    Line2D(
        [0], [0],
        color="#D97706",
        linewidth=2,
        label="Primary Highway"
    ),
    Line2D(
        [0], [0],
        color="#7B3294",
        linewidth=1.5,
        linestyle="--",
        label="Administrative Boundary"
    ),
    Line2D(
        [0], [0],
        marker="o",
        color="w",
        markerfacecolor="#D62728",
        markeredgecolor="white",
        markersize=9,
        label="Health Facilities"
    )
]

ax.legend(
    handles=legend_items,
    loc="lower left",
    fontsize=9
)

# 9. Remove coordinate axes
ax.set_axis_off()

# 10. Add source information
fig.text(
    0.5,
    0.025,
    "Data: Health facility dataset, CIESIN ward boundary "
    "and OpenStreetMap road data",
    ha="center",
    fontsize=8
)

# 11. Save map
output = Path("month-03/week-10/my_map.png")
output.parent.mkdir(parents=True, exist_ok=True)

plt.savefig(
    output,
    dpi=300,
    bbox_inches="tight"
)

print("Map saved successfully:", output)

plt.show()
