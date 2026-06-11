# Galena

> Fonte: [Galena](https://dwarffortresswiki.org/index.php/Galena) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Uses**
- **Ore of lead (100%) Ore of silver (50%) Masonry Stone crafting Construction**
- **Location**
- **Found in igneous extrusive layers as veins Found in metamorphic layers as veins Found within granite as veins Found within limestone as veins**
- **Properties**
- **Material value 5☼ Fire-safe Magma-safe Melting point 12005 °U ( m ) Boiling point 12305 °U ( m ) Ignition point none ( m ) Solid density 7500 kg/m³ Specific heat 800 J/kg·K Color silver**
- **Fire-safe:** Magma-safe

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*For the month, see Calendar.*

**Galena** is an ore of both lead and silver, found as veins in a variety of locations.

When galena ore is smelted, it will produce 4 lead bars and 0-4 silver bars (with a 50% chance of each silver bar being produced). On average, each nugget of galena will produce two bars of silver when smelted.

Galena can also be used in alloy reactions requiring silver-bearing ore. Because these reactions treat the galena nugget as the equivalent of 4 silver bars, the resulting alloy will show a roughly 30% increase in value over smelting the galena separately.

Galena is also magma-safe, but just barely. Since galena is a mid-value ore, however, you'll probably want to use something less valuable for magma management.

"Galena" is the name of the 6th month of the dwarven calendar, covering late Summer.

## In real life

Galena is a brittle, gray ore, the natural mineral form of lead(II) sulfide. It's been used as a source of lead since ancient times. Despite being magma-safe in *Dwarf Fortress*, it has a low melting point, making it easy to smelt into lead. Its more valuable use, however, is in the silver often found within galena deposits, which is also rather easy to extract; the Greeks were extracting silver from galena since the 7th century B.C. In real life, silver occurs within galena in concentrations up to 1-2% in pure form, as well as other forms such as silver sulfide.

One of galena's earliest uses was as an ingredient in kohl, an early form of eyeliner used in Africa and the Middle East, particularly Ancient Egypt. It is also a semiconductor, and was widely used in early wireless radio systems until the mid-1920's. However, galena's more important uses are from the lead and silver extracted from it, the uses of which are too vast to properly note here.

Galena.

\

    [INORGANIC:GALENA]
    [USE_MATERIAL_TEMPLATE:STONE_TEMPLATE]
    [STATE_NAME_ADJ:ALL_SOLID:galena][DISPLAY_COLOR:7:7:1][TILE:156]
    [ENVIRONMENT:IGNEOUS_EXTRUSIVE:VEIN:100]
    [ENVIRONMENT:METAMORPHIC:VEIN:100]
    [ENVIRONMENT_SPEC:GRANITE:VEIN:100]
    [ENVIRONMENT_SPEC:LIMESTONE:VEIN:100]
    [ITEM_SYMBOL:'*']
    [METAL_ORE:LEAD:100]
    [METAL_ORE:SILVER:50]
    [SOLID_DENSITY:7500]
    [MATERIAL_VALUE:5]
    [IS_STONE]
    [MELTING_POINT:12005]
    [BOILING_POINT:12305]
    [STATE_COLOR:ALL_SOLID:SILVER]
