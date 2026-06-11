# Sphalerite

> Fonte: [Sphalerite](https://dwarffortresswiki.org/index.php/Sphalerite) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Uses**
- **Ore of zinc (100%) Masonry Stone crafting Construction**
- **Location**
- **Found in metamorphic layers as veins**
- **Properties**
- **Material value 2☼ Fire-safe Magma-safe Melting point none ( m ) Boiling point 12133 °U ( m ) Ignition point none ( m ) Solid density 4050 kg/m³ Specific heat 800 J/kg·K Color plum**
- **Fire-safe:** Magma-safe

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Sphalerite** is the only ore of zinc, and can also be used as an ingredient in the smelting of brass. In the game, sphalerite is found as veins in metamorphic layers.

## Smelting

Sphalerite is needed to make two types of metal bars at a smelter:

- Zinc bars
- Brass bars - with native copper, malachite, or tetrahedrite

*(Brass can also be made with 1 zinc bar + 1 copper bar)*

## Other uses

Sphalerite is twice as valuable as common stone, and is magma-safe, but zinc itself is not. As such, it's worth considering enabling sphalerite to be used for masonry (in the Stone use tab in the Labor menu y), especially if your fortress lacks other magma-safe materials.

## Trivia

Interestingly, dwarves can smelt sphalerite into zinc, while in Real Life the stone itself does not melt, but *sublimates* (going from solid to gas without melting).

## Gallery

-

  Crystallized, lustrous, black sphalerite crystals with red highlights, are the host for two discrete rosettes of light tan baryte, to 3.25 cm across along with a single, glassy and gemmy, lavender colored fluorite crystal.

-

  Sphalerite

-

  A 6 mm sphalerite crystal

    [INORGANIC:SPHALERITE]
    [USE_MATERIAL_TEMPLATE:STONE_TEMPLATE]
    [STATE_NAME_ADJ:ALL_SOLID:sphalerite][DISPLAY_COLOR:0:7:1][TILE:156]
    [ENVIRONMENT:METAMORPHIC:VEIN:100]
    [ITEM_SYMBOL:'*']
    [METAL_ORE:ZINC:100]
    [MATERIAL_VALUE:2]
    [IS_STONE]
    [MELTING_POINT:NONE]
    [BOILING_POINT:12133]
    [SOLID_DENSITY:4050]
    [STATE_COLOR:ALL_SOLID:PLUM]
