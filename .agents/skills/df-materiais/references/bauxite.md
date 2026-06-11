# Bauxite

> Fonte: [Bauxite](https://dwarffortresswiki.org/index.php/Bauxite) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Uses**
- **Masonry Stone crafting Construction**
- **Location**
- **Found in sedimentary layers as large clusters**
- **Properties**
- **Material value 1☼ Fire-safe Magma-safe Melting point 13600 °U ( m ) Boiling point 15000 °U ( m ) Ignition point none ( m ) Solid density 3100 kg/m³ Specific heat 800 J/kg·K Color vermilion**
- **Fire-safe:** Magma-safe
- **Contains**
- **Variscite (small clusters) Ruby (small clusters) Sapphire (small clusters)**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Bauxite** is a non-economic and low-value dark-red sedimentary stone that only appears as large clusters in sedimentary layers. Once highly prized as the only practical source of magma-safe mechanisms to create magma-proof devices, its importance has declined with the addition of many new heat-resistant forms of stone, as well as the ability to make metal mechanisms from iron and steel. Nevertheless, it is still used by some long-time players for nostalgia, and its rare, bloody appearance makes it an interesting aesthetic choice.

Bauxite may contain both sapphire and ruby.

## In real life

In real life, bauxite is an ore of aluminum. It is often called "hardpan" and the result of progressed chemical leaching of the soil via water. It's commonly found near the surface in well-aged and weathered soil, and is the world's primary source of gallium and aluminum. The technology required to extract these, however, is beyond the level possessed by any of *Dwarf Fortress'* civilizations.

Bauxite is composed primarily of the minerals gibbsite (aluminum hydroxide: Al(OH)3), boehmite (aluminum oxide-hydroxide: γ-AlO(OH)), and diaspore (aluminum oxide-hydroxide: α-AlO(OH)) (none of which are individually present in *Dwarf Fortress*). Bauxite forms by the weathering and mineralization of various aluminum-rich soils or clays. Despite the correspondence in-game, corundum, the mineral that makes up ruby and sapphire (aluminum oxide: Al2O3), does **not** form in bauxite.

Extracting aluminum from bauxite, even in the most primitive way, requires the use of the Hall–Héroult process: the electrolysis of bauxite which has been dissolved into molten cryolite. The development of this process transformed aluminum from an exceptionally rare metal to a cheap, utilitarian material. Dwarves have not yet discovered electricity, therefore they cannot make use of electrolysis to get aluminum from bauxite.

Bauxite.

    an ore of aluminum, but through a too-advanced process, in-game as the source of the corundum gemstones (ruby and sapphire)
    bauxite melts around 2000C, so it's not practical to smelt it for aluminum (magma only goes up to 1300-1400)
    [INORGANIC:BAUXITE]
    [USE_MATERIAL_TEMPLATE:STONE_TEMPLATE]
    [STATE_NAME_ADJ:ALL_SOLID:bauxite][DISPLAY_COLOR:4:7:0][TILE:'+']
    [ENVIRONMENT:SEDIMENTARY:CLUSTER:100]
    [MELTING_POINT:13600]
    [BOILING_POINT:15000]
    [IS_STONE]
    [SOLID_DENSITY:3100]
    [STATE_COLOR:ALL_SOLID:VERMILION]
