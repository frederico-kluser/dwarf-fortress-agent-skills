# Bow

> Fonte: [Bow](https://dwarffortresswiki.org/index.php/Bow) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*Not to be confused with a dwarven crossbow; For a comparison of different weapons, see Weapon.*

A **bow** is a ranged weapon that uses arrows as ammunition. Compared to crossbows, bows are less accurate but can be loaded faster. Stronger and more skilled bowmen fire arrows at higher velocities.

As ranged weapons, bows use and train the bowman (bowdwarf) skill; as melee weapons, bows use and train the swordsman (swordsdwarf) skill, instead (although a blunt, wooden "sword" is rarely much of a threat). Dwarves cannot forge bows nor make arrows, limiting supply to rare artifacts and whatever low-quality specimens can be traded from elven or human caravans and scavenged from invaders. Trading for ammunition with humans is preferred because they can have metal arrows. Bows are not always made out of wood; like most other weapons, they can also be found made of metal.

All dwarves can equip bows. However, in all but rare cases, your dwarves would be better served with crossbows and bolts instead, as they are native weapons. Bows can be used in weapon traps, using arrows as ammunition.

## Bugs

- If a squad is assigned multiple ammo types, dwarves with "individual choice ranged" may carry the wrong ammoBug:1374.

|  |
|----|
| "Bow" in other / Languages / Dwarven / : / egdoth / Elven / : / ramí / Goblin / : / uneg / Human / : / ethro |

    [ITEM_WEAPON:ITEM_WEAPON_BOW]
    [NAME:bow:bows]
    [SIZE:300]
    [SKILL:SWORD]
    [RANGED:BOW:ARROW]
    [AIM_DIFFICULTY:5]
    [NOCKED:20:7]
    [INITIATE_SHOT_TIME:1]
    [SHOT_RECOVERY_TIME:0]
    [SHOOT_FORCE:1000]
    [SHOT_FORCE_REQUIRES:STRENGTH:1500]
    [SHOT_FORCE_REQUIRES:BOW:15]
    [SHOOT_MAXVEL:200]
    [TWO_HANDED:0]
    [MINIMUM_SIZE:15000]
    [MATERIAL_SIZE:3]
    [ATTACK:BLUNT:10000:4000:bash:bashes:NO_SUB:1250]
        [ATTACK_PREPARE_AND_RECOVER:3:3]
