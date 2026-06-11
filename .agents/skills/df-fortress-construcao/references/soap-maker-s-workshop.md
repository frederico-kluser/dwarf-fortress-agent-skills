# Soap maker's workshop

> Fonte: [Soap maker's workshop](https://dwarffortresswiki.org/index.php/Soap_maker's_workshop) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Shortcut : b - o - P**
- **Icon**
- **Job Requirement**
- **Soap making**
- **Construction**
- **Materials:** Labors
- **Bucket (empty) Building material (non- economic ):** Soap making
- **Materials Used**
- **Lye Animal tallow or Oil**
- **Goods Created**
- **Soap**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

This building is used by a soap maker to produce soap. Soap can be made using lye and either oil or tallow.

    [BUILDING_WORKSHOP:SOAP_MAKER]
        [NAME:Soap Maker's Workshop]
        [NAME_COLOR:7:0:1]
        [DIM:3:3]
        [WORK_LOCATION:2:2]
        [BUILD_LABOR:SOAP_MAKER]
        [BUILD_KEY:CUSTOM_SHIFT_P]
        [BLOCK:1:0:0:0] workbenches no longer block
        [BLOCK:2:0:0:0]
        [BLOCK:3:0:0:0]
        [TILE:0:1:' ':' ':150]
        [TILE:0:2:' ':' ':'/']
        [TILE:0:3:'-':' ':' ']
        [COLOR:0:1:0:0:0:0:0:0:6:0:0]
        [COLOR:0:2:0:0:0:0:0:0:6:0:0]
        [COLOR:0:3:6:0:0:0:0:0:0:0:0]
        [TILE:1:1:' ':' ':'=']
        [TILE:1:2:'-':' ':8]
        [TILE:1:3:' ':' ':150]
        [COLOR:1:1:0:0:0:0:0:0:6:0:0]
        [COLOR:1:2:6:0:0:0:0:0:6:0:0]
        [COLOR:1:3:0:0:0:0:0:0:6:0:0]
        [TILE:2:1:'-':' ':8]
        [TILE:2:2:' ':' ':8]
        [TILE:2:3:' ':150:' ']
        [COLOR:2:1:6:0:0:0:0:0:6:0:0]
        [COLOR:2:2:0:0:0:0:0:0:6:0:0]
        [COLOR:2:3:0:0:0:6:0:0:0:0:0]
        [TILE:3:1:150:' ':8]
        [TILE:3:2:' ':' ':8]
        [TILE:3:3:' ':240:' ']
        [COLOR:3:1:6:0:0:0:0:0:6:7:0]
        [COLOR:3:2:0:0:0:0:0:0:6:7:0]
        [COLOR:3:3:0:0:0:7:0:1:0:0:0]
        [BUILD_ITEM:1:BUCKET:NONE:NONE:NONE][EMPTY][CAN_USE_ARTIFACT]
        [BUILD_ITEM:1:NONE:NONE:NONE:NONE][BUILDMAT][WORTHLESS_STONE_ONLY][CAN_USE_ARTIFACT]
        [TOOLTIP:Use tallow (rendered fat) or oil here with lye to make soap.]
