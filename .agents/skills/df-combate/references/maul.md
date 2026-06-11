# Maul

> Fonte: [Maul](https://dwarffortresswiki.org/index.php/Maul) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*For a comparison of different weapons, see Weapon.*

A **maul** is a blunt weapon that is essentially a very large war hammer (similar to a modern-day sledgehammer). Mauls are more than three times larger than standard war hammers, with a similar "bash" attack. Mauls also have a 10× larger contact area and greatly increased penetration, but cannot be swung with nearly as much velocity. Their great size grants them a large amount of momentum however, and they easily bend and mangle joints when striking limbs and other extremities.

Mauls use and train the hammerdwarf skill. Being foreign weapons, dwarves cannot forge mauls, limiting supply to whatever specimens can be traded from human caravans (which can never be steel ones, but can be of masterwork quality if you're lucky) or scavenged from invaders; although, it is possible that a dwarf in a strange mood craft a maul as a legendary artifact.

Due to the size of mauls, most dwarves are unable to equip them. With height and broadness modifiers, some dwarves *should* be able to use a maul, and a select few might manage to do so one-handed. Unfortunately, due to a bug, mauls cannot currently be equipped by any dwarves, but they work really well inside a weapon trap. Alternatively, you can grant residency to human visitors and have them wield them for you.

## Bugs

In fortress mode, one-handed vs. two-handed checks are performed correctly, but can wield vs. can't wield ignores height and broadness modifiers, so dwarves cannot equip mauls.Bug:0005812 See this forum post for details.

    [ITEM_WEAPON:ITEM_WEAPON_MAUL]
    [NAME:maul:mauls]
    [SIZE:1300]
    [SKILL:HAMMER]
    [TWO_HANDED:77500]
    [MINIMUM_SIZE:62500]
    [MATERIAL_SIZE:5]
    [ATTACK:BLUNT:100:6000:bash:bashes:NO_SUB:2000]
        [ATTACK_PREPARE_AND_RECOVER:3:3]
