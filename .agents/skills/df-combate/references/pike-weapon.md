# Pike (weapon)

> Fonte: [Pike (weapon)](https://dwarffortresswiki.org/index.php/Pike_(weapon)) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*For a comparison of different weapons, see Weapon.*

*For the fish, see Pike (fish) "Pike (fish)").*

A **pike** is a piercing weapon that is essentially a very long spear. Pikes are twice the size of standard spears, with a 20% increase in penetration (which, theoretically, should prove useful when fighting large monsters). Attack range is not currently modeled, so pikes are neither granted the initial attack nor rendered useless as enemies advance to close combat range.

Pikes use and train the Pikeman / Pikedwarf skill. As foreign weapons, dwarves cannot forge pikes, limiting supply to whatever low-quality specimens can be traded from human caravans and scavenged from invaders.

Due to the size of pikes, most dwarves are unable to equip them. With height and broadness modifiers, some dwarves *should* be able to use a pike, and a select few might manage to do so one-handed. Unfortunately, due to a bug, pikes cannot currently be equipped by any dwarves.

If in Adventurer Mode, if your character passes the one-handed check for being capable of single-handing a multi-grasp weapon, the pike seems to actually be the most effective all-around weapon in the game, capable of fighting and damaging any threat from armored soldiers to megabeasts, provided the weapon's material is sufficient. The only drawbacks are that it lacks the quick, easy decapitation of an edged weapon and thus may not as reliably be able to instantly kill in a single attack as them, and like spears they are prone to getting stuck in an enemy, necessitating a turn to wrestle it out or move one space in any direction to automatically pull it out.

## Bugs

In fortress mode, one-handed vs. two-handed checks are performed correctly, but can wield vs. can't wield ignores height and broadness modifiers, so dwarves cannot equip pikes.Bug:0005812 See this forum post for details.

    [ITEM_WEAPON:ITEM_WEAPON_PIKE]
    [NAME:pike:pikes]
    [SIZE:800]
    [SKILL:PIKE]
    [TWO_HANDED:77500]
    [MINIMUM_SIZE:62500]
    [MATERIAL_SIZE:4]
    [ATTACK:EDGE:20:12000:stab:stabs:NO_SUB:1000]
        [ATTACK_PREPARE_AND_RECOVER:3:3]
    [ATTACK:BLUNT:10000:6000:bash:bashes:shaft:1250]
        [ATTACK_PREPARE_AND_RECOVER:3:3]
