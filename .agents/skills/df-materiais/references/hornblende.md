# Hornblende

> Fonte: [Hornblende](https://dwarffortresswiki.org/index.php/Hornblende) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Uses**
- **Masonry Stone crafting Construction**
- **Location**
- **Found in igneous layers as small clusters Found in metamorphic layers as small clusters**
- **Properties**
- **Material value 1☼ Fire-safe Not magma-safe Melting point 11890 °U ( x ) Boiling point 14000 °U ( m ) Ignition point none ( m ) Solid density 3235 kg/m³ Specific heat 800 J/kg·K Color gray**
- **Fire-safe:** Not magma-safe

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Hornblende** is an unremarkable dark gray stone, which can be found in both metamorphic and igneous stone layers.

## In Real Life

Hornblende is typically a component of igneous rocks such as granite, basalt, or gabbro. It often contains titanium, which the dwarves do not have the technology to refine (no electricity). Hornblende can be processed into white asbestos. Unfortunately, dwarven strand extractors can't do that.

Not for eating.

    [INORGANIC:HORNBLENDE]
    [USE_MATERIAL_TEMPLATE:STONE_TEMPLATE]
    [STATE_NAME_ADJ:ALL_SOLID:hornblende][DISPLAY_COLOR:0:7:1][TILE:'"']
    [ENVIRONMENT:IGNEOUS_ALL:CLUSTER_SMALL:100]
    [ENVIRONMENT:METAMORPHIC:CLUSTER_SMALL:100]
    [IS_STONE]
    [MELTING_POINT:11890]
    [SOLID_DENSITY:3235]
    [STATE_COLOR:ALL_SOLID:GRAY]
