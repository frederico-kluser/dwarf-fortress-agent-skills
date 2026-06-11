# Long sword

> Fonte: [Long sword](https://dwarffortresswiki.org/index.php/Long_sword) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*For a comparison of different weapons, see Weapon.*

A **long sword** is an edged weapon that is more than twice the size of a short sword, but still 30% smaller than a two-handed sword. While not as powerful as a two-handed sword, it has the potential to be used in one hand, making it a better defensive option, as the other hand retains the ability to use a shield. Long swords have the same basic attacks as other swords, but benefit from increased damage potential over short swords.

Long swords use and train the swordsdwarf skill. As foreign weapons, dwarves cannot forge long swords, limiting supply to whatever low-quality specimens can be traded from human caravans or scavenged from invaders.

Although longer than standard short swords, most dwarves are still able to equip long swords. With height and broadness modifiers, some dwarves *should* be unable to use a long sword, and a few others might only manage to do so two-handed. Currently, due to a bug, long swords can be equipped by all dwarves, no matter their size.

## Bugs

In fortress mode, one-handed vs. two-handed checks are performed correctly, but can wield vs. can't wield ignores height and broadness modifiers, so all dwarves can equip long swords.Bug:0005812 See this forum post for details.

|  |
|----|
| "Long sword" in other / Languages / Dwarven / : / romek dastot / Elven / : / beresi ocade / Goblin / : / xom oxox / Human / : / inid thil |

    [ITEM_WEAPON:ITEM_WEAPON_SWORD_LONG]
    [NAME:long sword:long swords]
    [SIZE:700]
    [SKILL:SWORD]
    [TWO_HANDED:57500]
    [MINIMUM_SIZE:52500]
    [MATERIAL_SIZE:4]
    [ATTACK:EDGE:60000:6000:slash:slashes:NO_SUB:1250]
        [ATTACK_PREPARE_AND_RECOVER:3:3]
    [ATTACK:EDGE:50:3000:stab:stabs:NO_SUB:1000]
        [ATTACK_PREPARE_AND_RECOVER:3:3]
    [ATTACK:BLUNT:60000:6000:slap:slaps:flat:1250]
        [ATTACK_PREPARE_AND_RECOVER:3:3]
    [ATTACK:BLUNT:100:1000:strike:strikes:pommel:1000]
        [ATTACK_PREPARE_AND_RECOVER:3:3]
