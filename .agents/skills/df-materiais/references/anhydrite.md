# Anhydrite

> Fonte: [Anhydrite](https://dwarffortresswiki.org/index.php/Anhydrite) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Uses**
- **Masonry Stone crafting Construction**
- **Location**
- **Found within gypsum as small clusters Found within satinspar as individual tiles Found within alabaster as individual tiles Found within selenite as individual tiles**
- **Properties**
- **Material value 1☼ Fire-safe Magma-safe Melting point 12610 °U ( m ) Boiling point 14000 °U ( m ) Ignition point none ( m ) Solid density 2960 kg/m³ Specific heat 800 J/kg·K Color periwinkle**
- **Fire-safe:** Magma-safe

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Anhydrite** is a magma-safe stone of base value that is only found within various types of gypsum. In real life, anhydrite is essentially dehydrated gypsum, and on contact with water will immediately hydrate and soften; however in *Dwarf Fortress*, anhydrite floodgates are just as effective as floodgates made from granite. Oddly, unlike the gypsum in which it occurs, anhydrite **cannot** be used to make gypsum plaster.

Anhydrite.

    gypsum without any water (plaster still has some)
    [INORGANIC:ANHYDRITE]
    [USE_MATERIAL_TEMPLATE:STONE_TEMPLATE]
    [STATE_NAME_ADJ:ALL_SOLID:anhydrite][DISPLAY_COLOR:7:7:1][TILE:'v']
    [BASIC_COLOR:7:0]
    [ENVIRONMENT_SPEC:GYPSUM:CLUSTER_SMALL:100]
    [ENVIRONMENT_SPEC:SATINSPAR:CLUSTER_ONE:100]
    [ENVIRONMENT_SPEC:ALABASTER:CLUSTER_ONE:100]
    [ENVIRONMENT_SPEC:SELENITE:CLUSTER_ONE:100]
    [SOLID_DENSITY:2960]  Significantly denser than the other gypsum-related minerals.
    [IS_STONE]
    [MELTING_POINT:12610]
    [STATE_COLOR:ALL_SOLID:PERIWINKLE]
