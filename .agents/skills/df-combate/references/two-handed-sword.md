# Two-handed sword

> Fonte: [Two-handed sword](https://dwarffortresswiki.org/index.php/Two-handed_sword) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*For a comparison of different weapons, see Weapon.*

A **two-handed sword** is an edged weapon that is 3× the size of a short sword, with 5× the contact area. Two-handed swords have the same basic attacks as other swords, but benefit from increased damage potential, at a cost of reduced usability. Two-handed swords can span up to 6 ft. in length, and, as the name implies, were intended for use with a two-hand grip. The enormous contact area of two-handed swords allows massive wounds to be inflicted on nearly any target, no matter their size, if body parts are not simply cloven apart or removed altogether.

Two-handed swords use and train the swordsdwarf skill. As foreign weapons, dwarves cannot forge two-handed swords, limiting supply to whatever low-quality specimens can be traded from human caravans or scavenged from invaders.

Due to the size of two-handed swords, most dwarves are unable to equip them. With height and broadness modifiers, some dwarves *should* be able to use a two-handed sword, and a select few might manage to do so one-handed. Unfortunately, due to a bug, two-handed swords cannot currently be equipped by any dwarves.

## Bugs

In fortress mode, one-handed vs. two-handed checks are performed correctly, but can wield vs. can't wield ignores height and broadness modifiers, so dwarves cannot equip two-handed swords.Bug:0005812 See this forum post for details.

    [ITEM_WEAPON:ITEM_WEAPON_SWORD_2H]
    [NAME:two-handed sword:two-handed swords]
    [SIZE:900]
    [SKILL:SWORD]
    [TWO_HANDED:77500]
    [MINIMUM_SIZE:62500]
    [MATERIAL_SIZE:5]
    [ATTACK:EDGE:100000:8000:slash:slashes:NO_SUB:1250]
        [ATTACK_PREPARE_AND_RECOVER:3:3]
    [ATTACK:EDGE:50:4000:stab:stabs:NO_SUB:1000]
        [ATTACK_PREPARE_AND_RECOVER:3:3]
    [ATTACK:BLUNT:100000:8000:slap:slaps:flat:1250]
        [ATTACK_PREPARE_AND_RECOVER:3:3]
    [ATTACK:BLUNT:100:1000:strike:strikes:pommel:1000]
        [ATTACK_PREPARE_AND_RECOVER:3:3]
