# Clay

> Fonte: [Clay](https://dwarffortresswiki.org/index.php/Clay) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Properties**
- **Soil layer Clay**
- **Contains**
- **All minerals common to soil layers**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Clay** is one of the many types of soil that can be found in soil layers. Aquifers are never present in clay layers.

## Ceramics

Five different soil types are classified as clay: clay, clay loam, sandy clay, silty clay, and fire clay, each of which can be gathered for use in ceramics. If your embark site has at least one type of clay, it will be shown as *Clay* in the embark screen's biome viewer. Notably, soil of the types sandy clay loam and silty clay loam *can not* be used for ceramics despite their names.

The gathering and use of clay is done from a kiln or magma kiln and behaves similarly to most material production, but includes elements similar to glass production. In order to gather clay, a gathering zone must first be designated over a clay-bearing tile (note that clay can be collected from adjacent clay walls, even diagonally), much like with sand; however, gathering clay creates a clay "boulder" (the same as raw stone) and does not require a bag. As with sand, clay can be gathered indefinitely from a single tile – any dwarf with the item hauling labor enabled can collect clay.

Clay can be made into pots, bricks, statues, hives and crafts. Small pots, called jugs, function similarly to bags and waterskins, while large pots are treated like barrels. Creating any object from clay requires a unit of fuel, or a magma kiln.

Before an earthenware pot (large or small) can hold liquids, it must be **glazed**. Glazing is performed at a kiln and requires either a unit of ash or a unit of cassiterite (tin ore), plus a unit of fuel. Stoneware and porcelain pots do not need to be glazed.

When an underground plant (trees, shrubs, grass or moss) grows on a muddy stone floor tile (after discovering a cavern) and is either trampled, gathered, cut down or removed via building a dirt road on top of it, the floor tile turns into a soil type appropriate to the biome – for biomes which lack soil layers altogether (such as mountains and glaciers), a random soil type will be selected, which might sometimes be clay.

Grass, saplings and shrubs can grow on clay soil, which causes the underlying clay to be temporarily unavailable for collection, giving the message "Urist McClaydigger cancels Collect Clay: Clay vanished" if the job is in progress, or "Urist McClaydigger cancels Collect Clay: Need valid, active clay collection zone" if the job is new. You can easily remove the grass *and* prevent it from growing back by either building a dirt road (bnO) over the grass, or put a floor grate over the clay floor to prevent growth while allowing clay to be collected, but you must first remove the grass/sapling/shrub.

Occasionally, it is possible to "cultivate" clay by channeling down into the lowest normal layer of the caverns, revealing a "magma flow" above a floor of semi-molten rock (and a ramp on the level below, if the square had not previously been revealed). If a floor is constructed over the flow, then deconstructed, a natural floor of clay or sand may be left behind. In some cases, this may be the sole domestic source of clay for a fortress.

Gathered clay cannot be used for any purposes other than pottery - it cannot be used as a building material, carved directly into finished goods, polished for decoration, fired from catapults, or loaded into stone-fall traps.

Naturally occurring clay.

    [INORGANIC:CLAY]
    [USE_MATERIAL_TEMPLATE:SOIL_TEMPLATE]
    [STATE_NAME_ADJ:ALL_SOLID:clay][DISPLAY_COLOR:4:6:0][TILE:178]
    [SOIL]
    [SOLID_DENSITY:1210] SCS = 20/60/20
    [MATERIAL_REACTION_PRODUCT:FIRED_MAT:INORGANIC:CERAMIC_EARTHENWARE]
    [STATE_COLOR:ALL_SOLID:BRASS]
