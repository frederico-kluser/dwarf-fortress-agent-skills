# Cinnabar

> Fonte: [Cinnabar](https://dwarffortresswiki.org/index.php/Cinnabar) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Uses**
- **Masonry Stone crafting Construction**
- **Location**
- **Found in igneous extrusive layers as veins Found within shale as veins Found within quartzite as veins**
- **Properties**
- **Material value 1☼ Fire-safe Not magma-safe Melting point 11044 °U ( x ) Boiling point 14000 °U ( m ) Ignition point none ( m ) Solid density 8100 kg/m³ Specific heat 800 J/kg·K Color red**
- **Fire-safe:** Not magma-safe

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Cinnabar** is a brilliant red stone found as veins in numerous environments. Despite its appearance in ASCII mode (showing up as £ unmined and \* mined), it is **not** a usable ore.

Cinnabar is also the most dense non-economic stone besides slade, so it's very good for stone-fall traps and as catapult ammo. Hauling cinnabar is not realistic, or at least will take an eternity, without a wheelbarrow. Additionally, cinnabar crafts are so heavyweight that they can quickly fill up a caravan.

## In real life

Cinnabar is a mineral of mercury sulfide (HgS), and has been used throughout history both for the ease in which it can be made to release its elemental mercury, and for use as a red pigment in paint. In ancient Roman history, slaves or prisoners were consigned to cinnabar mines as a death sentence – unlike humans, dwarves are evidently immune to mercury poisoning.

Cinnabar.

    ore of mercury, powdered gives vermilion dye
    [INORGANIC:CINNABAR]
    [USE_MATERIAL_TEMPLATE:STONE_TEMPLATE]
    [STATE_NAME_ADJ:ALL_SOLID:cinnabar][DISPLAY_COLOR:4:7:1][TILE:156]
    [ENVIRONMENT:IGNEOUS_EXTRUSIVE:VEIN:100]
    [ENVIRONMENT_SPEC:SHALE:VEIN:100]
    [ENVIRONMENT_SPEC:QUARTZITE:VEIN:100]
    [ITEM_SYMBOL:'*']
    [IS_STONE]
    [MELTING_POINT:11044]
    [SOLID_DENSITY:8100]
    [STATE_COLOR:ALL_SOLID:RED]
