# Spear

> Fonte: [Spear](https://dwarffortresswiki.org/index.php/Spear) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*For a comparison of different weapons, see Weapon.*

A **spear** is a piercing weapon that is essentially a sharply pointed blade mounted on the end of a long handle. Spears are half the size of pikes "Pike (weapon)"), but only suffer a 17% decrease in penetration.

Spears use and train the speardwarf skill. Dwarves can forge spears out of any weapon-grade metal but those with superior edge properties are more effective. For the purposes of building a realistic danger room, less lethal wooden spears may be used if purchased from elves first. All dwarves can equip spears, but some must use two hands.

Spears may also be installed in upright spear traps, allowing them to be mechanically operated; this is particularly useful for constructing danger rooms.

## Forging and melting

- Metal spears cost **one** metal bar to forge, or **three** adamantine wafers.
- When a non-adamantine metal spear is melted down, it will return **0.9** metal bars, for an **efficiency of 90%**.
- When an adamantine spear is melted down, it will produce **0.9** wafers, for an **efficiency of 30%**

|  |
|----|
| "Spear" in other / Languages / Dwarven / : / lokum / Elven / : / iti / Goblin / : / bukza / Human / : / asi |

    [ITEM_WEAPON:ITEM_WEAPON_SPEAR]
    [NAME:spear:spears]
    [SIZE:400]
    [SKILL:SPEAR]
    [TWO_HANDED:47500]
    [MINIMUM_SIZE:5000] amphibian men, etc., need variants
    [MATERIAL_SIZE:3]
    [ATTACK:EDGE:20:10000:stab:stabs:NO_SUB:1000]
        [ATTACK_PREPARE_AND_RECOVER:3:3]
    [ATTACK:BLUNT:10000:6000:bash:bashes:shaft:1250]
        [ATTACK_PREPARE_AND_RECOVER:3:3]
