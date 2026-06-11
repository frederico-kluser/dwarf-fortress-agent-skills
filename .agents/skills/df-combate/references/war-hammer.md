# War hammer

> Fonte: [War hammer](https://dwarffortresswiki.org/index.php/War_hammer) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*For a comparison of different weapons, see Weapon.*

A **war hammer** is a blunt weapon that is essentially a hammer with a long handle. A war hammer is half the size of a mace with half the contact area as well, and less than 1/3 the size of a maul. Because blunt damage focused in a small contact area is mostly unaffected by armor, war hammers are considered one of the best weapons for fighting humanoid opponents.

War hammers use and train the hammerdwarf skill. Dwarves can forge effective war hammers out of any weapons-grade metal, though those with higher densities (like silver) or higher impact fracture/yields (like steel) tend to cause more damage. All dwarves can equip war hammers, though a tiny fraction must use two hands.

## Forging and melting

- Metal war hammers cost **one** metal bar to forge, or **three** adamantine wafers.
- When a non-adamantine metal war hammer is melted down, it will return **0.9** metal bars, for an **efficiency of 90%**.
- When an adamantine war hammer is melted down, it will produce **0.9** wafers, for an **efficiency of 30%**

|  |
|----|
| "War hammer" in other / Languages / Dwarven / : / alnis nil / Elven / : / athama ÿeri / Goblin / : / aslez ospum / Human / : / ashro ongu |

    [ITEM_WEAPON:ITEM_WEAPON_HAMMER_WAR]
    [NAME:war hammer:war hammers]
    [SIZE:400]
    [SKILL:HAMMER]
    [TWO_HANDED:37500]
    [MINIMUM_SIZE:32500]
    [MATERIAL_SIZE:3]
    [ATTACK:BLUNT:10:200:bash:bashes:NO_SUB:2000]
        [ATTACK_PREPARE_AND_RECOVER:3:3]
