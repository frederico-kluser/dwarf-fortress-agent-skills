# Native aluminum

> Fonte: [Native aluminum](https://dwarffortresswiki.org/index.php/Native_aluminum) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Uses**
- **Ore of aluminum (100%) Masonry Stone crafting Construction**
- **Location**
- **Found in igneous extrusive layers as small clusters**
- **Properties**
- **Material value 40☼ Fire-safe Not magma-safe Melting point 11188 °U ( x ) Boiling point 14534 °U ( m ) Ignition point none ( m ) Solid density 2700 kg/m³ Specific heat 900 J/kg·K Color ivory**
- **Fire-safe:** Not magma-safe

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Native aluminum** is the only ore of aluminum, a metal with the same value as platinum. It occurs in small clusters and is relatively rare.

### In real life

Native aluminum is not strictly an "ore", but rather chunks of aluminum found in a naturally formed (native) metallic state. As aluminum is a very reactive metal, it's rarely found in such deposits, and the few natural deposits that do exist are found in strongly reducing environments. Most aluminum today is extracted from bauxite via a procedure called the Hall–Héroult process. Before the Hall-Héroult process, aluminum used to be rarer and more valuable than gold, despite being the most common metallic element in the earth's crust. Rumor has it Napoleon III had a treasured set of aluminum utensils for his most valuable guests, and the rest had to settle with plain gold.

Will make a great can one day.

    aluminum can occasionally be found in its free form in environments that like oxygen, volcanic muds were mentioned
    [INORGANIC:NATIVE_ALUMINUM]
    [ENVIRONMENT:IGNEOUS_EXTRUSIVE:CLUSTER_SMALL:100]
    [ITEM_SYMBOL:'*']
    [METAL_ORE:ALUMINUM:100]
    [STATE_NAME_ADJ:ALL_SOLID:native aluminum]
    [STATE_NAME_ADJ:LIQUID:molten native aluminum]
    [STATE_NAME_ADJ:GAS:boiling native aluminum]
    [DISPLAY_COLOR:7:7:1]
    [TILE:'^']
    [MATERIAL_VALUE:40]
    [SPEC_HEAT:900]
    [MELTING_POINT:11188]
    [BOILING_POINT:14534]
    [SOLID_DENSITY:2700]
    [LIQUID_DENSITY:2375]
    [MOLAR_MASS:26981]
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
    [STATE_COLOR:ALL_SOLID:IVORY]
