# Battle axe

> Fonte: [Battle axe](https://dwarffortresswiki.org/index.php/Battle_axe) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*For a comparison of different weapons, see Weapon.*

A **battle axe** is an edge weapon that is essentially a heavy, sharp blade mounted at the end of a haft, roughly parallel to it but set somewhat forwards (in elementary mechanical terms it's just a wedge on the end of a lever). Battle axes have the same range of attacks as larger great axes, but with reduced contact area and penetration on their "hack" edged attack.

Battle axes use and train the axeman skill ("Axedwarf" in dwarf mode). Dwarves can forge battle axes out of any weapon-grade metal, though those with superior edge properties are more effective. Almost all dwarves can equip battle axes; some must use two hands.

A battle axe may also be used as a tool for chopping down trees, and the material of the axe determines how fast a tree can be felled. Any dwarf that performs wood cutting will pick up an axe (if one is available) and not put it down until they are either no longer assigned the Wood Cutting labor or required to pick up different equipment for a new job. You can make use of this to arm many of your non-military dwarves with axes, although if you do designate one or more trees for wood-cutting (l), all those dwarves will rush out to cut them down, one per tree designated. Wooden training axes are no longer able to be use to cut down trees -- they must be metal (or an artifact).

## Forging and melting

- Metal battle axes cost **one** metal bar to forge, or **four** adamantine wafers.
- When a non-adamantine metal battle axe is melted down, it will return **1.2** metal bars, for an **efficiency of 120%**.
- When an adamantine battle axe is melted down, it will produce **1.2** wafers, for an **efficiency of 30%**.

Sometimes just stands there because it looks cool.\
*Art by Jason Nguyen*

|  |
|----|
| "Battle axe" in other / Languages / Dwarven / : / nokzam libash / Elven / : / thafatha cuthefi / Goblin / : / ustrok agun / Human / : / noloc osp |

    [ITEM_WEAPON:ITEM_WEAPON_AXE_BATTLE]
    [NAME:battle axe:battle axes]
    [SIZE:800]
    [SKILL:AXE]
    [TWO_HANDED:47500]
    [MINIMUM_SIZE:42500]
    [MATERIAL_SIZE:4]

    The format is ATTACK:EDGE/BLUNT:contact area:penetration size:verb2nd:verb3rd:noun:velocity multiplier
    Penetration size currently only matters for edged attacks.

    [ATTACK:EDGE:40000:6000:hack:hacks:NO_SUB:1250]
        [ATTACK_PREPARE_AND_RECOVER:3:3]
    [ATTACK:BLUNT:40000:6000:slap:slaps:flat:1250]
        [ATTACK_PREPARE_AND_RECOVER:3:3]
    [ATTACK:BLUNT:100:1000:strike:strikes:pommel:1000]
        [ATTACK_PREPARE_AND_RECOVER:3:3]
