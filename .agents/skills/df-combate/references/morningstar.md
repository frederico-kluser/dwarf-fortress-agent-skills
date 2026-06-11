# Morningstar

> Fonte: [Morningstar](https://dwarffortresswiki.org/index.php/Morningstar) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*For a comparison of different weapons, see Weapon.*

A **morningstar** is an edged weapon that consists of a spiked ball mounted on the end of a handle. Despite similarities to a mace in appearance, a morningstar's size and contact area are closer to those of a war hammer. Specifically, a morningstar is 25% larger than a war hammer with the same contact area, and uses piercing damage to inflict internal injuries.

Morningstars use and train the macedwarf skill. As foreign weapons, dwarves cannot forge morningstars, limiting supply to whatever low-quality specimens can be traded from human caravans and scavenged from invaders. All dwarves can equip morningstars, though a tiny fraction must use two hands.

|  |
|----|
| "Morningstar" in other / Languages / Dwarven / : / sanád-vîr / Elven / : / rifa-ila / Goblin / : / smungras-ex / Human / : / sabu-ama |

    [ITEM_WEAPON:ITEM_WEAPON_MORNINGSTAR]
    [NAME:morningstar:morningstars]
    [SIZE:500]
    [SKILL:MACE]
    [TWO_HANDED:37500]
    [MINIMUM_SIZE:32500]
    [MATERIAL_SIZE:3]
    [ATTACK:EDGE:10:500:bash:bashes:NO_SUB:2000]
        [ATTACK_PREPARE_AND_RECOVER:3:3]
    [ATTACK:BLUNT:50:1000:strike:strikes:pommel:1000]
        [ATTACK_PREPARE_AND_RECOVER:3:3]
