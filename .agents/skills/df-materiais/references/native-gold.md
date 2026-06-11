# Native gold

> Fonte: [Native gold](https://dwarffortresswiki.org/index.php/Native_gold) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Uses**
- **Ore of gold (100%) Masonry Stone crafting Construction**
- **Location**
- **Found in igneous layers as veins Found in alluvial layers as small clusters**
- **Properties**
- **Material value 30☼ Fire-safe Not magma-safe Melting point 11915 °U ( x ) Boiling point 15141 °U ( m ) Ignition point none ( m ) Solid density 19320 kg/m³ Specific heat 129 J/kg·K Color gold**
- **Fire-safe:** Not magma-safe

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Native gold** is the only ore of gold, a precious metal. Native gold is very common in igneous layers, a bit less in sedimentary layers.

When mined, hunks of native gold are called *gold nuggets*. Gold nuggets can be smelted to produce 4 gold bars. Gold nuggets can also be smelted with a silver-bearing ore to create the alloy electrum. Using low-value silver ores (galena and tetrahedrite) in this reaction will result in a net value increase for your fortress (electrum bars are each less valuable than gold bars, but you will have twice as many total bars).

Native gold is just as valuable as metallic gold, so if you have a decently skilled stonecrafter and did not start your metal industry yet, native gold mugs are very good to quickly boost the value of your starting fortress and/or buy stuff from an early caravan. However, melting the gold will make far more bars and generally more wealth.

### In real life

Native gold is not technically an "ore"; it's merely chunks of mostly-pure metallic gold, naturally formed. As gold is an extremely unreactive metal, this is by far the most common form in which gold is found in nature.

Native gold.

    [INORGANIC:NATIVE_GOLD]
    [ENVIRONMENT:IGNEOUS_ALL:VEIN:100]
    [ENVIRONMENT:ALLUVIAL:CLUSTER_SMALL:100]
    [ITEM_SYMBOL:'*']
    [METAL_ORE:GOLD:100]
    [STONE_NAME:gold nuggets]
    [STATE_NAME:SOLID:native gold]
    [STATE_NAME:SOLID_POWDER:native gold dust]
    [STATE_ADJ:ALL_SOLID:native gold]
    [STATE_NAME_ADJ:LIQUID:molten native gold]
    [STATE_NAME_ADJ:GAS:boiling native gold]
    [DISPLAY_COLOR:6:7:1]
    [TILE:156]
    [MATERIAL_VALUE:30]
    [SPEC_HEAT:129]
    [MELTING_POINT:11915]
    [BOILING_POINT:15141]
    [SOLID_DENSITY:19320]
    [LIQUID_DENSITY:17310]
    [MOLAR_MASS:196967]
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
    [STATE_COLOR:ALL_SOLID:GOLD]
