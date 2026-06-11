# Scimitar

> Fonte: [Scimitar](https://dwarffortresswiki.org/index.php/Scimitar) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*For a comparison of different weapons, see Weapon.*

A **scimitar** is an edged weapon with a curved blade that is very similar to a short sword. In fact, the only differentiating factor appears to be the contact area of the pommel, which is half the size of those on a short sword.

Scimitars use and train the swordsdwarf skill. As foreign weapons, dwarves cannot forge scimitars, limiting supply to whatever low-quality specimens can be traded from human caravans or scavenged from invaders. All dwarves can equip scimitars, though, like short swords, a tiny fraction must use two hands. Given their marked similarity to short swords, your dwarves are almost certainly better served by equipping high-quality short swords.

    [ITEM_WEAPON:ITEM_WEAPON_SCIMITAR]
    [NAME:scimitar:scimitars]
    [SIZE:300]
    [SKILL:SWORD]
    [TWO_HANDED:37500]
    [MINIMUM_SIZE:32500]
    [MATERIAL_SIZE:3]
    [ATTACK:EDGE:20000:4000:slash:slashes:NO_SUB:1250]
        [ATTACK_PREPARE_AND_RECOVER:3:3]
    [ATTACK:EDGE:50:2000:stab:stabs:NO_SUB:1000]
        [ATTACK_PREPARE_AND_RECOVER:3:3]
    [ATTACK:BLUNT:20000:4000:slap:slaps:flat:1250]
        [ATTACK_PREPARE_AND_RECOVER:3:3]
    [ATTACK:BLUNT:50:1000:strike:strikes:pommel:1000]
        [ATTACK_PREPARE_AND_RECOVER:3:3]
