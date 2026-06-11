# Biome token

> Fonte: [Biome token](https://dwarffortresswiki.org/index.php/Biome_token) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

\

**Biome tokens** are used to indicate biomes for creatures, plants and entities.

All objects that use biome tokens can take multiple entries, so they can be found in many different locations.

## Individual Biomes

|  |  |  |
|----|----|----|
| ID | Token | Description |
| 0 |  MOUNTAIN or  MOUNTAINS | Mountain |
| 1 |  GLACIER | Glacier |
| 2 |  TUNDRA | Tundra |
| 3 |  SWAMP_TEMPERATE_FRESHWATER | Temperate Freshwater Swamp |
| 4 |  SWAMP_TEMPERATE_SALTWATER | Temperate Saltwater Swamp |
| 5 |  MARSH_TEMPERATE_FRESHWATER | Temperate Freshwater Marsh |
| 6 |  MARSH_TEMPERATE_SALTWATER | Temperate Saltwater Marsh |
| 7 |  SWAMP_TROPICAL_FRESHWATER | Tropical Freshwater Swamp |
| 8 |  SWAMP_TROPICAL_SALTWATER | Tropical Saltwater Swamp |
| 9 |  SWAMP_MANGROVE | Mangrove Swamp |
| 10 |  MARSH_TROPICAL_FRESHWATER | Tropical Freshwater Marsh |
| 11 |  MARSH_TROPICAL_SALTWATER | Tropical Saltwater Marsh |
| 12 |  FOREST_TAIGA or  TAIGA | Taiga |
| 13 |  FOREST_TEMPERATE_CONIFER | Temperate Coniferous Forest |
| 14 |  FOREST_TEMPERATE_BROADLEAF | Temperate Broadleaf Forest |
| 15 |  FOREST_TROPICAL_CONIFER | Tropical Coniferous Forest |
| 16 |  FOREST_TROPICAL_DRY_BROADLEAF | Tropical Dry Broadleaf Forest |
| 17 |  FOREST_TROPICAL_MOIST_BROADLEAF | Tropical Moist Broadleaf Forest |
| 18 |  GRASSLAND_TEMPERATE | Temperate Grassland |
| 19 |  SAVANNA_TEMPERATE | Temperate Savanna |
| 20 |  SHRUBLAND_TEMPERATE | Temperate Shrubland |
| 21 |  GRASSLAND_TROPICAL | Tropical Grassland |
| 22 |  SAVANNA_TROPICAL | Tropical Savanna |
| 23 |  SHRUBLAND_TROPICAL | Tropical Shrubland |
| 24 |  DESERT_BADLAND | Badlands |
| 25 |  DESERT_ROCK | Rocky Wasteland |
| 26 |  DESERT_SAND | Sand Desert |
| 27 |  OCEAN_TROPICAL | Tropical Ocean |
| 28 |  OCEAN_TEMPERATE | Temperate Ocean |
| 29 |  OCEAN_ARCTIC | Arctic Ocean |
| 30 |  POOL_TEMPERATE_FRESHWATER | Temperate Freshwater Pool |
| 31 |  POOL_TEMPERATE_BRACKISHWATER | Temperate Brackish Pool |
| 32 |  POOL_TEMPERATE_SALTWATER | Temperate Saltwater Pool |
| 33 |  POOL_TROPICAL_FRESHWATER | Tropical Freshwater Pool |
| 34 |  POOL_TROPICAL_BRACKISHWATER | Tropical Brackish Pool |
| 35 |  POOL_TROPICAL_SALTWATER | Tropical Saltwater Pool |
| 36 |  LAKE_TEMPERATE_FRESHWATER | Temperate Freshwater Lake |
| 37 |  LAKE_TEMPERATE_BRACKISHWATER | Temperate Brackish Lake |
| 38 |  LAKE_TEMPERATE_SALTWATER | Temperate Saltwater Lake |
| 39 |  LAKE_TROPICAL_FRESHWATER | Tropical Freshwater Lake |
| 40 |  LAKE_TROPICAL_BRACKISHWATER | Tropical Brackish Lake |
| 41 |  LAKE_TROPICAL_SALTWATER | Tropical Saltwater Lake |
| 42 |  RIVER_TEMPERATE_FRESHWATER | Temperate Freshwater River |
| 43 |  RIVER_TEMPERATE_BRACKISHWATER | Temperate Brackish River |
| 44 |  RIVER_TEMPERATE_SALTWATER | Temperate Saltwater River |
| 45 |  RIVER_TROPICAL_FRESHWATER | Tropical Freshwater River |
| 46 |  RIVER_TROPICAL_BRACKISHWATER | Tropical Brackish River |
| 47 |  RIVER_TROPICAL_SALTWATER | Tropical Saltwater River |
| 48 |  SUBTERRANEAN_WATER | Underground caverns (in water) |
| 49 |  SUBTERRANEAN_CHASM | Underground caverns (out of water) |
| 50 |  SUBTERRANEAN_LAVA | Magma sea |

\

## Biome Sets

|  |  |  |
|----|----|----|
| Token | Biomes | Description |
|  ALL_MAIN | 0-29, 36-41 | All biomes excluding pools, rivers, and underground features |
|  ANY_LAND | 0-26 | All main biomes excluding oceans and lakes |
|  ANY_OCEAN | 27-29 | All ocean biomes |
|  ANY_LAKE | 36-41 | All lake biomes |
|  ANY_TEMPERATE_LAKE | 36-38 | All temperate lake biomes |
|  ANY_TROPICAL_LAKE | 39-41 | All tropical lake biomes |
|  ANY_RIVER | 42-47 | All river biomes |
|  ANY_TEMPERATE_RIVER | 42-44 | All temperate river biomes |
|  ANY_TROPICAL_RIVER | 45-47 | All tropical river biomes |
|  ANY_POOL | 30-35 | All pool biomes |
|  NOT_FREEZING | 3-26 | All land biomes excluding Mountain, Glacier, and Tundra |
|  ANY_TEMPERATE | 3-6, 13-14, 18-20 | All Temperate land biomes - marshes, swamps, forests, grassland, savanna, and shrubland |
|  ANY_TROPICAL | 7-11, 15-17, 21-23 | All Tropical land biomes - marshes, swamps (including Mangrove), forests, grassland, savanna, and shrubland |
|  ANY_FOREST | 13-17 | All Forest biomes (excluding Taiga) |
|  ANY_SHRUBLAND | 20, 23 | Temperate and Tropical Shrubland |
|  ANY_GRASSLAND | 18, 21 | Temperate and Tropical Grassland |
|  ANY_SAVANNA | 19, 22 | Temperate and Tropical Savanna |
|  ANY_TEMPERATE_FOREST | 13-14 | Temperate Coniferous and Broadleaf Forests |
|  ANY_TROPICAL_FOREST | 15-17 | Tropical Coniferous and Dry/Moist Broadleaf Forests |
|  ANY_TEMPERATE_BROADLEAF | 3-6, 14, 18-20 | Temperate Broadleaf Forest, Grassland/Savanna/Shrubland, Swamps, and Marshes |
|  ANY_TROPICAL_BROADLEAF | 7-11, 16-17, 21-23 | Tropical Dry/Moist Broadleaf Forest, Grassland/Savanna/Shrubland, Swamps (including Mangrove), and Marshes |
|  ANY_WETLAND | 3-11 | All swamps and marshes |
|  ANY_TEMPERATE_WETLAND | 3-6 | All temperate swamps and marshes |
|  ANY_TROPICAL_WETLAND | 7-11 | All tropical swamps and marshes |
|  ANY_TROPICAL_MARSH | 10-11 | All tropical marshes |
|  ANY_TEMPERATE_MARSH | 5-6 | All temperate marshes |
|  ANY_TROPICAL_SWAMP | 7-9 | All tropical swamps (including Mangrove) |
|  ANY_TEMPERATE_SWAMP | 3-4 | All temperate swamps |
|  ANY_DESERT | 24-26 | Badlands, Rocky Wasteland, and Sand Desert |
