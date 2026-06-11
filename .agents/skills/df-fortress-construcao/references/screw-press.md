# Screw press

> Fonte: [Screw press](https://dwarffortresswiki.org/index.php/Screw_press) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Shortcut : b - o - R**
- **Icon**
- **Job Requirement**
- **Presser , Papermaker**
- **Construction**
- **Materials:** Labors
- **2 Mechanisms:** Mechanic
- **Materials Used**
- **Rock nut paste Cottonseed paste Linseed paste Hempseed paste Kenafseed paste Olive Honeycomb Empty jugs Slurry**
- **Goods Created**
- **Oil Press cake Honey bee honey Honey bee wax cake Sheet**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

A **screw press** is a special workshop used to press liquids out of various substances and to press slurry into sheets of paper.

Food-related jobs at the screw press consist of pressing seed pastes or fruit (olives) to yield oil (which can then be made into soap or cooked), pressing cake (which can be cooked), and pressing honeycombs to yield honey (which can then be brewed into mead) and wax cake (which can be made into wax crafts). These jobs require the pressing skill.

Pressing seed paste or fruit into oil and honeycombs into honey require an empty jug to hold the resulting liquid.

Slurry may be pressed into sheets of paper at the screw press by a dwarf with the papermaking skill. Sheets of paper have quality levels, while other products at the screw press do not.

Constructing a screw press requires two mechanisms and is done through the Build menu boR.

## Bugs

- Screw presses sometimes do not allow the "press honeycomb" job to be added directly; adding the job via the manager interface should get the work started.

    [BUILDING_WORKSHOP:SCREW_PRESS]
        [NAME:Screw Press]
        [NAME_COLOR:7:0:1]
        [DIM:1:1]
        [WORK_LOCATION:1:1]
        [BUILD_LABOR:MECHANIC]
        [BUILD_KEY:CUSTOM_SHIFT_R]
        [BLOCK:1:0]
        [TILE:0:1:207]
        [COLOR:0:1:0:7:0]
        [TILE:1:1:207]
        [COLOR:1:1:MAT]
        [BUILD_ITEM:2:TRAPPARTS:NONE:NONE:NONE][CAN_USE_ARTIFACT]
        [TOOLTIP:A useful workshop for pressing liquids from various sources. Some plants might need to be milled first before they can be used.  Empty jugs are required to store the liquid products.]
