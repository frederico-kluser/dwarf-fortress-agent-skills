# Kaolinite

> Fonte: [Kaolinite](https://dwarffortresswiki.org/index.php/Kaolinite) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Uses**
- **Masonry Stone crafting Construction**
- **Location**
- **Found in sedimentary layers as large clusters**
- **Properties**
- **Material value 1☼ Fire-safe Magma-safe Melting point 13150 °U ( m ) Boiling point 14000 °U ( m ) Ignition point none ( m ) Solid density 2600 kg/m³ Specific heat 800 J/kg·K Color pearl**
- **Fire-safe:** Magma-safe
- **Contains**
- **Marcasite (small clusters) Alunite (large clusters) Turquoise (small clusters)**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Kaolinite** is a magma-safe pink-red stone, much like bauxite, found as large clusters in sedimentary layers. Kaolinite has a material value of 1 like most stone, but can be made into medium value porcelain goods at a kiln or magma kiln.

Potters ordered to make clay or ceramic goods will use the closest source of clay, fire clay, or kaolinite by default. If you want to force your potters to use clay instead of more limited kaolinite, you could do one of two things: forbid all kaolinite through the Stocks menu, or set up a stockpile that either accepts only clay or that already has clay, and link the stockpile to the kiln.

## In real life

In the real world, Kaolinite is one of the most common minerals. Being a clay mineral, Kaolinite clay occurs in abundance in soils that have formed from the chemical weathering of rocks in hot, moist climates—for example in tropical rainforest areas. While it is largely used in the production of paper, cosmetics and soaps, it can also be used in farming in the form of a spray, so as to deter insect damage. Before the 21st century, it was widely used as an anti-diarrhea medication due to its absorbent properties.

Kaolinite.

    [INORGANIC:KAOLINITE]
    [USE_MATERIAL_TEMPLATE:STONE_TEMPLATE]
    [STATE_NAME_ADJ:ALL_SOLID:kaolinite][DISPLAY_COLOR:4:7:0][TILE:'=']
    [ENVIRONMENT:SEDIMENTARY:CLUSTER:100]
    [IS_STONE]
    [MELTING_POINT:13150]
    [SOLID_DENSITY:2600]
    [MATERIAL_REACTION_PRODUCT:FIRED_MAT:INORGANIC:CERAMIC_PORCELAIN]
    [STATE_COLOR:ALL_SOLID:PEARL]
