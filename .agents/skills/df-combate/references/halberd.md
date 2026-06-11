# Halberd

> Fonte: [Halberd](https://dwarffortresswiki.org/index.php/Halberd) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*For a comparison of different weapons, see Weapon.*

A **halberd** is an edged weapon that is essentially a combination of long-hafted axe and short spear. Halberds are 50% greater in size than dwarven battle axes and gain a piercing stab attack, but lose the axe's blunt pommel strike. Additionally, the halberd's blade has half the contact area and 33% greater penetration, meaning this slashing weapon is *much* more effective vs. armor than its smaller cousins. Attack range is not currently modeled, so halberds are neither granted distance attack bonuses nor rendered useless as enemies advance to close combat range.

Halberds use and train the Axeman / Axedwarf skill. As foreign weapons, dwarves cannot forge halberds, limiting supply to whatever low-quality specimens can be traded from human caravans or scavenged from invaders.

Due to the size of halberds, most dwarves are unable to equip them. With height and broadness modifiers, some dwarves *should* be able to use a halberd, and a select few might manage to do so one-handed. Unfortunately, due to a bug, halberds cannot currently be equipped by any dwarves in fortress mode.

## Bugs

In fortress mode, one-handed vs. two-handed checks are performed correctly, but can wield vs. can't wield ignores height and broadness modifiers, so dwarves cannot equip halberds.Bug:0005812 See this forum post for details.

    [ITEM_WEAPON:ITEM_WEAPON_HALBERD]
    [NAME:halberd:halberds]
    [SIZE:1200]
    [SKILL:AXE]
    [TWO_HANDED:77500]
    [MINIMUM_SIZE:62500]
    [MATERIAL_SIZE:5]
    [ATTACK:EDGE:20000:8000:slash:slashes:NO_SUB:1250]
        [ATTACK_PREPARE_AND_RECOVER:3:3]
    [ATTACK:EDGE:50:2000:stab:stabs:NO_SUB:1000]
        [ATTACK_PREPARE_AND_RECOVER:3:3]
    [ATTACK:BLUNT:20000:6000:bash:bashes:shaft:1250]
        [ATTACK_PREPARE_AND_RECOVER:3:3]
