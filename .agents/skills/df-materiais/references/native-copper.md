# Native copper

> Fonte: [Native copper](https://dwarffortresswiki.org/index.php/Native_copper) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Uses**
- **Ore of copper (100%) Masonry Stone crafting Construction**
- **Location**
- **Found in igneous extrusive layers as veins Found within sandstone as veins**
- **Properties**
- **Material value 2☼ Fire-safe Not magma-safe Melting point 11952 °U ( x ) Boiling point 14611 °U ( m ) Ignition point none ( m ) Solid density 8930 kg/m³ Specific heat 385 J/kg·K Color copper**
- **Fire-safe:** Not magma-safe

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Native copper** is one of the several ores of copper, the most versatile metal in *Dwarf Fortress*, primarily useful in creating alloys. Native copper is found in the form of veins. Mined-out hunks of native copper are called *copper nuggets*. Other copper-bearing ores include malachite and tetrahedrite.

## In Real Life

Native copper is not strictly an ore, but chunks of copper in its naturally formed (native) metallic state. As copper is fairly unreactive as metals go, this is much more common than native aluminum. It was an important source of copper for many prehistoric cultures.

-

  Nugget, 44 grams and about 3 cm large

-

  Another similar sized copper nugget

    [INORGANIC:NATIVE_COPPER]
    [STONE_NAME:copper nuggets]
    [ENVIRONMENT:IGNEOUS_EXTRUSIVE:VEIN:100]
    [ENVIRONMENT_SPEC:SANDSTONE:VEIN:100]
    [ITEM_SYMBOL:'*']
    [METAL_ORE:COPPER:100]
    [STATE_NAME_ADJ:ALL_SOLID:native copper]
    [STATE_NAME_ADJ:LIQUID:molten native copper]
    [STATE_NAME_ADJ:GAS:boiling native copper]
    [DISPLAY_COLOR:6:7:0]
    [TILE:156]
    [MATERIAL_VALUE:2]
    [SPEC_HEAT:385]
    [MELTING_POINT:11952]
    [BOILING_POINT:14611]
    [SOLID_DENSITY:8930]
    [LIQUID_DENSITY:8020]
    [MOLAR_MASS:63546]
    used stone template values for mining speed until there's more information about how native metal is mined
        [IMPACT_YIELD:120000]
        [IMPACT_FRACTURE:120000]
        [IMPACT_STRAIN_AT_YIELD:100]
        [COMPRESSIVE_YIELD:120000]
        [COMPRESSIVE_FRACTURE:120000]
        [COMPRESSIVE_STRAIN_AT_YIELD:100]
        [TENSILE_YIELD:15000]
        [TENSILE_FRACTURE:15000]
        [TENSILE_STRAIN_AT_YIELD:100]
        [TORSION_YIELD:15000]
        [TORSION_FRACTURE:15000]
        [TORSION_STRAIN_AT_YIELD:100]
        [SHEAR_YIELD:15000] used marble
        [SHEAR_FRACTURE:15000]
        [SHEAR_STRAIN_AT_YIELD:100]
        [BENDING_YIELD:15000]
        [BENDING_FRACTURE:15000]
        [BENDING_STRAIN_AT_YIELD:100]
    [MAX_EDGE:1000] no swords until you can pick mats
    [ITEMS_HARD]
    [IS_STONE]
    [STATE_COLOR:ALL_SOLID:COPPER]
