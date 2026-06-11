# Display furniture

> Fonte: [Display furniture](https://dwarffortresswiki.org/index.php/Display_furniture) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Construction**
- **Rooms**
- **Museum**
- **Base value:** Size
- **10☼:** 500 cm³

## Dados (infobox)

- **Construction**
- **Rooms**
- **Museum**
- **Base value:** Size
- **10☼:** 1,000 cm³

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

A piece of **display furniture** can be used to display other items. There are two available types of display furniture, pedestals and display cases.

Pedestals are created from wood, stone, glass, or metal at a carpenter's workshop, stoneworker's workshop, glass furnace, or forge, respectively; while wood, stone, and glass only require 1 material to craft, metal requires 2 bars. Being tools, they are listed at a forge under "Other objects" rather than "Furniture", but still use the blacksmithing skill.

Display cases are created from a log and a window at a carpenter's workshop. The window used to create the display case does not affect it in any way; a ☼display case☼ made with a ☼crystal glass window☼ is worth as much as a ☼display case☼ made with a -green glass window-, and the window used is not mentioned in any context.

Other than the above-mentioned creation processes, their visual appearances and the fact that display cases are twice as large as pedestals (and thus, twice as heavy as a pedestal made out of the same material), pedestals and display furniture are completely identical, their behavior determined entirely by the DISPLAY_OBJECT tool use.

In the building menu, they are listed in furniture bfy. Once built, display furniture can be examined by clicking on it. Items to display can be selected with the "**Assign new display items**" option. This opens a menu similar to the Stocks menu, listing only items that can be displayed. Clicking the checkmark on the left marks an item to be placed on the display by item haulers. Once placed, the item appears in the furniture menu with the label "On display". Its description can be viewed in the building materials list below by clicking  icon. Displayed items also have  icon, indicating they are not a permanent part of the building. Meeting area designated over a display furniture will be called a "museum".

A line of pedestals with sacks of *something* on them.

Dwarves will admire both the display furniture and the item on display, giving them happy thoughts. A dwarf must stand in or pass through the actual tile containing the display furniture in order to admire it; they cannot do so from a distance. This unfortunately leaves your artifacts on display vulnerable to sticky-fingered villains. If the only objective is to increase the value of a location, however (for example, to instantly turn a meeting place into a grand guildhall), the object can be locked away, such as by vertical grates or bars.

Display furniture is stockpiled as furniture, under "Other Large Tools".

In adventurer mode, pedestals can be found in many generated sites, sometimes alongside display cases. It is possible to place an item on a pedestal by standing next to (or on) it and p putting the item onto the pedestal. Likewise, it is possible to remove an item from a pedestal by standing on the same tile as it and g getting it. These actions will be seen by NPCs as, respectively placing or taking the item from the site, though they only care if the item is an artifact.

-

  Room 232 of the Louvre, a human museum.

-

  Can hold - not one - but *three* containers of alcohol.

    [ITEM_TOOL:ITEM_TOOL_PEDESTAL]
    [NAME:pedestal:pedestals]
    [VALUE:10]
    [HARD_MAT]
    [TOOL_USE:DISPLAY_OBJECT]
    [FURNITURE]
    [TILE:139]
    [SIZE:500]
    [MATERIAL_SIZE:6]

    [ITEM_TOOL:ITEM_TOOL_DISPLAY_CASE]
    [NAME:display case:display cases]
    [VALUE:10]
    [HARD_MAT]
    [TOOL_USE:DISPLAY_OBJECT]
    [FURNITURE]
    [TILE:227]
    [INVERTED_TILE]
    [SIZE:1000]
    [NO_DEFAULT_JOB]
