# Bituminous coal

> Fonte: [Bituminous coal](https://dwarffortresswiki.org/index.php/Bituminous_coal) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Uses**
- **Create 9 coke at smelter Masonry Stone crafting Construction**
- **Location**
- **Found in sedimentary layers as veins**
- **Properties**
- **Material value 1☼ Fire-safe Not magma-safe Melting point none ( m ) Boiling point 16708 °U ( m ) Ignition point 11440 °U ( x ) Solid density 1346 kg/m³ Specific heat 409 J/kg·K Color charcoal**
- **Fire-safe:** Not magma-safe

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*In Dwarf Fortress, bituminous coal is not the same as "coal", an ingredient in many reactions – see that article for more information.*

**Bituminous coal** is found in veins in sedimentary layers and is one of the two mineral sources of fuel. When processed at a smelter or magma smelter, one unit of bituminous coal produces 9 units of coke. If done at a regular smelter, this processing requires one pre-existing unit of fuel (either charcoal or coke), leaving a *net* production of 8 fuel.

Bituminous coal is flammable—if exposed to fire or magma, an item made of bituminous coal will burn for the better part of a year before wearing away. Exposure to water (including rain) will extinguish it, unless it happens to be stored in a bin.

However, since its ignition point is above the cutoff for fire-safetyBug:9795, it is considered a fire-safe material and as such can be used for the construction of non-magma furnaces and forges.

Bituminous coal is **not** the same as "refined coal" or "coal", though it is immediately related.

Because bituminous coal only costs 3 embark points, and produces a large amount of fuel when processed, it may be wise to bring some bituminous coal with you on embark as an early source of fuel.

It otherwise behaves as an ordinary stone. If you don't need to produce coke, you can use it to produce goods with a mason or stonecrafter. By default, bituminous coal is considered an Economic Stone and it will be reserved for coke production unless changed in the Stone submenu.

## See also

- Lignite
- Fuel

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Of all the fallacies of the humans, probably the most laughable is "Old Eartherism". Some human "scholars" have estimated the world's age from the ludicrous 6000 to the unimaginable 4.5 billion years. As "proof", they point to the bones of giant lizards buried beneath the soil, and coal, which they claim is the byproduct of the lizards' decay. Dwarven historical records extend back to 1 year after the creation of the world, and coal is amply documented even then. Dwarves are also well aware of how those monstrous lizards' bones ended up underground, as well as *exactly* what they decay into. They don't bother to correct the humans because they think they're cute when they're wrong.

-

  A piece of bituminous coal.

    [INORGANIC:COAL_BITUMINOUS]
    [USE_MATERIAL_TEMPLATE:STONE_TEMPLATE]
    [STATE_NAME_ADJ:ALL_SOLID:bituminous coal][DISPLAY_COLOR:0:7:1][TILE:15]
    [ENVIRONMENT:SEDIMENTARY:VEIN:100]
    [ITEM_SYMBOL:15]
    [SPEC_HEAT:409]
    [IGNITE_POINT:11440]
    [MELTING_POINT:NONE]
    [BOILING_POINT:16708]
    [SOLID_DENSITY:1346]
    [IS_STONE]
    [STATE_COLOR:ALL_SOLID:CHARCOAL]
