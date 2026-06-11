# Dagger

> Fonte: [Dagger](https://dwarffortresswiki.org/index.php/Dagger) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*For a comparison of different weapons, see Weapon.*

A **large dagger** is an edged weapon that is essentially larger than a knife but smaller than a short sword. Compared to the standard short sword, large daggers have no "flat" attack and a significantly less lethal "slash" attack, but gain a much more vicious "stab" attack with 1/10 the contact area of a sword point. This makes large daggers particularly effective against armored opponents: an iron dagger has a fair chance to pierce even steel armor, and the resulting internal injuries can be debilitating and deadly.

Large daggers use and train the knife user skill, and are common weapons for kobold and goblin thieves. As foreign weapons, dwarves cannot forge large daggers, limiting supply to whatever low-quality specimens can be scavenged from ambushers. Even the smallest dwarves are able to equip large daggers one-handed.

|  |
|----|
| "Dagger" in other / Languages / Dwarven / : / urist / Elven / : / acita / Goblin / : / ulspa / Human / : / olith |

    [ITEM_WEAPON:ITEM_WEAPON_DAGGER_LARGE]
    [NAME:dagger:daggers]
    [ADJECTIVE:large]
    [SIZE:200]
    [SKILL:DAGGER]
    [TWO_HANDED:27500]
    [MINIMUM_SIZE:5000]
    [MATERIAL_SIZE:1]
    [ATTACK:EDGE:1000:800:slash:slashes:NO_SUB:1250]
        [ATTACK_PREPARE_AND_RECOVER:3:3]
    [ATTACK:EDGE:5:1000:stab:stabs:NO_SUB:1000]
        [ATTACK_PREPARE_AND_RECOVER:3:3]
    [ATTACK:BLUNT:20:600:strike:strikes:pommel:1000]
        [ATTACK_PREPARE_AND_RECOVER:3:3]
