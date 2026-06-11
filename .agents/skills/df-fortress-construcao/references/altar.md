# Altar

> Fonte: [Altar](https://dwarffortresswiki.org/index.php/Altar) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Construction**
- **Rooms**
- **None**
- **Base value:** Size
- **10☼:** 500 cm³

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Altars**, also known as **Offering Places**, are a furniture item optionally used in temples. They can be placed with bfp, though they currently serve no purpose other than increasing a room's value and decoration, as temples don't require them to function.

In fortress mode, altars can be made from most materials like wood, stone, glass, and metal at their respective workshops. Altars can be stored in furniture stockpiles, and fall in the "other large tools" item type category.

Altars are extremely lightweight compared to other "furniture" (1/20 to 1/60 the weight) with the same base value, and so make excellent trade items to produce. Dwarves have been known to place skulls on altars.

In adventure mode, you can often find dice that can be rolled on altars.

#### Curses

A dwarf that knocks over an altar within a dedicated temple, during a tantrum or otherwise, will be cursed by that temple's deity with a random were-curse (as long as they are a believer of that deity). There is no cure. The player will receive a pop-up notification stating that the god has cursed their dwarf, and that dwarf will transform into a hostile beast during the next full moon.

    [ITEM_TOOL:ITEM_TOOL_ALTAR]
    [NAME:altar:altars]
    [VALUE:10]
    [HARD_MAT]
    [TOOL_USE:PLACE_OFFERING]
    [FURNITURE]
    [TILE:144]
    [SIZE:500]
    [MATERIAL_SIZE:6]
