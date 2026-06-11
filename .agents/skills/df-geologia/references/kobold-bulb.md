# Kobold bulb

> Fonte: [Kobold bulb](https://dwarffortresswiki.org/index.php/Kobold_bulb) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes kobold bulbs for their shrouded history.**
- **Seasons**
- **Spring Summer Autumn Winter**
- **Biome**
- **Any Wetland**
- **Wet Dry**
- **Wet:** Dry
- **Products**
- **Extract:** Gnomeblight
- **Plant Properties**
- **Edible:** No
- **Cookable:** No

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

The **kobold bulb** is an unusual plant found in wetlands. Its only use is to make gnomeblight, a substance poisonous only to mountain gnomes and dark gnomes. Unfortunately, it requires significant workarounds to apply it and gnomes are weak in combat anyway, so it is effectively useless other than as a valuable trade good. Despite the name, they have no relation to kobolds, nor does their extract affect them.

Some dwarves like kobold bulbs for their *shrouded history*.

    [PLANT:BULB_KOBOLD]
        [NAME:kobold bulb][NAME_PLURAL:kobold bulbs][ADJ:kobold bulb]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
            [MATERIAL_VALUE:1]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [PICKED_TILE:232][PICKED_COLOR:0:0:1]
        [WET][BIOME:ANY_WETLAND]
        [VALUE:5]
        [USE_MATERIAL_TEMPLATE:EXTRACT:PLANT_EXTRACT_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:frozen gnomeblight]
            [STATE_NAME_ADJ:LIQUID:gnomeblight]
            [STATE_NAME_ADJ:GAS:boiling gnomeblight]
            [MATERIAL_VALUE:100]
            [DISPLAY_COLOR:7:0:1]
            [EXTRACT_STORAGE:FLASK]
            [ENTERS_BLOOD]
            [PREFIX:NONE]
            [SYNDROME]
                [SYN_NAME:gnomeblight]
                [SYN_AFFECTED_CREATURE:GNOME_MOUNTAIN:ALL]
                [SYN_AFFECTED_CREATURE:GNOME_DARK:ALL]
                [SYN_CONTACT]
                [SYN_INHALED]
                [SYN_INJECTED]
                [SYN_INGESTED]
                [CE_NECROSIS:SEV:100:PROB:100:BP:BY_CATEGORY:ALL:ALL:START:0:PEAK:30:END:1200]
        [EXTRACT_STILL_VIAL:LOCAL_PLANT_MAT:EXTRACT]
        [SPRING][SUMMER][AUTUMN][WINTER]
        [FREQUENCY:5]
        [CLUSTERSIZE:1]
        [PREFSTRING:shrouded history]
