# Native silver

> Fonte: [Native silver](https://dwarffortresswiki.org/index.php/Native_silver) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Uses**
- **Ore of silver (100%) Masonry Stone crafting Construction**
- **Location**
- **Found within granite as veins Found within gneiss as veins**
- **Properties**
- **Material value 10☼ Fire-safe Not magma-safe Melting point 11731 °U ( x ) Boiling point 13892 °U ( m ) Ignition point none ( m ) Solid density 10490 kg/m³ Specific heat 230 J/kg·K Color silver**
- **Fire-safe:** Not magma-safe
- **Contains**
- **Horn silver (small clusters)**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Native silver** is an ore of silver, a mid-value metal. Native silver may also be smelted with other ores to create electrum and billon. Native silver can be found as veins in gneiss and granite. When mined, hunks of native silver are called **silver nuggets**.

Horn silver is mostly identical to native silver, other than its name and physical properties. Tetrahedrite and galena are related ores which, once smelted, **may** produce a bar of silver.

## In Real Life

Native silver is not technically an ore; it's just chunks of mostly pure metallic silver, naturally formed. As silver is not very reactive, as metals go, this is not an extremely uncommon form to find silver in.

Size: 5.7 x 4.3 x 1.7 cm.

    [INORGANIC:NATIVE_SILVER]
    [ENVIRONMENT_SPEC:GRANITE:VEIN:100]
    [ENVIRONMENT_SPEC:GNEISS:VEIN:100]
    [ITEM_SYMBOL:'*']
    [METAL_ORE:SILVER:100]
    [STONE_NAME:silver nuggets]
    [STATE_NAME_ADJ:ALL_SOLID:native silver]
    [STATE_NAME_ADJ:LIQUID:molten native silver]
    [STATE_NAME_ADJ:GAS:boiling native silver]
    [DISPLAY_COLOR:7:7:1]
    [TILE:156]
    [MATERIAL_VALUE:10]
    [SPEC_HEAT:230]
    [MELTING_POINT:11731]
    [BOILING_POINT:13892]
    [SOLID_DENSITY:10490]
    [LIQUID_DENSITY:9320]
    [MOLAR_MASS:107868]
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
    [STATE_COLOR:ALL_SOLID:SILVER]
