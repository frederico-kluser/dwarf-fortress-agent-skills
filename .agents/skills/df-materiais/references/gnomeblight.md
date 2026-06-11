# Gnomeblight

> Fonte: [Gnomeblight](https://dwarffortresswiki.org/index.php/Gnomeblight) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Gnomeblight** is a poisonous extract made from kobold bulbs, prepared by an herbalist at a still using the "Extract from plant" job. As a poison, gnomeblight causes moderate necrosis to both mountain and dark gnomes, though currently there exists no easy way to apply it. It is extracted into a vial. 1 kobold bulb will yield 5 units of gnomeblight, worth 100☼ each, for a total of 500☼ per bulb.

There is a work around to apply it (from the forums):

1.  Build your gnome cage in a sealable room, then link it to a lever.
2.  Using a garbage dump activity zone, place one or more barrels of gnomeblight on top of the cage.
3.  Forbid all of the gnomeblight, but not the barrel(s) themselves.
4.  Wait until a caravan arrives.
5.  Order the gnomeblight barrel(s) to be taken to the trade depot. Since the gnomeblight itself is forbidden, it will be dumped onto the floor.
6.  Seal the room and pull the lever.
7.  Watch the gnomes walk around in the pool of gnomeblight and slowly dissolve.

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
