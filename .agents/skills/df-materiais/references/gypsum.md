# Gypsum

> Fonte: [Gypsum](https://dwarffortresswiki.org/index.php/Gypsum) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Uses**
- **Masonry Stone crafting Construction Make plaster**
- **Location**
- **Found in sedimentary layers as large clusters**
- **Properties**
- **Material value 1☼ Not fire-safe Not magma-safe Melting point 10261 °U ( x ) Boiling point 14000 °U ( m ) Ignition point none ( m ) Solid density 2320 kg/m³ Specific heat 800 J/kg·K Color buff**
- **Not fire-safe:** Not magma-safe
- **Contains**
- **Brimstone (small clusters) Borax (small clusters) Alabaster (small clusters) Selenite (small clusters) Satinspar (small clusters) Anhydrite (small clusters)**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Gypsum** is an ordinary stone with a niche use for dwarven healthcare - once mined, it can be processed at a kiln to make gypsum plaster powder, which is in turn used to make plaster casts. A fort with no gypsum can use splints as an alternative.

Gypsum can also contain small clusters of selenite, satinspar, and alabaster, which can also be made into plaster powder, as well as anhydrite, which cannot.

-

  A gypsum quarry

-

  Piece of gypsum

-

  Gypsum crystals (dirty yellow) on another mineral

-

  Another gypsum crystal

-

  Though most are not this clear, gypsum can be found as a transparent crystal

    this is common gypsum, 3 vars below, any gypsum can be heated to and then mixed with water to make plaster
    [INORGANIC:GYPSUM]
    [USE_MATERIAL_TEMPLATE:STONE_TEMPLATE]
    [STATE_NAME_ADJ:ALL_SOLID:gypsum][DISPLAY_COLOR:6:7:1][TILE:'#']
    [ENVIRONMENT:SEDIMENTARY:CLUSTER:100]
    [SOLID_DENSITY:2320]  Gypsum density was rather high.  My sources all give ~2300.
    [IS_STONE]
    [REACTION_CLASS:GYPSUM]
    [MELTING_POINT:10261]
    [STATE_COLOR:ALL_SOLID:BUFF]
