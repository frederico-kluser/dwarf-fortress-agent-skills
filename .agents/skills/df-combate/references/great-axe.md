# Great axe

> Fonte: [Great axe](https://dwarffortresswiki.org/index.php/Great_axe) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*For a comparison of different weapons, see Weapon.*

A **great axe** is an edged weapon that is essentially a larger battle axe. Great axes are more than 50% larger than standard battle axes, and its blade has a 50% larger contact area and 33% greater penetration, for even more limb-severing fun.

Great axes use and train the Axedwarf skill. As foreign weapons, dwarves cannot forge great axes, limiting supply to whatever low-quality specimens can be traded from human caravans, or scavenged from invaders.

Due to the size of great axes, most dwarves are unable to equip them. With height and broadness modifiers, some dwarves *should* be able to use a great axe, and a select few might manage to do so one-handed. Unfortunately, due to a bug, great axes cannot currently be equipped by any dwarves.

## Analysis

A multi-grasp, edged weapon. Due to increased size, penetration, and contact, great axes are technically superior to battle axes...provided that, like any multi-grasp weapon, the user is of the right size to use them in a one-grasp manner without getting a penalty to hit, which will unfortunately almost never be the case in Fortress Mode. If a creature can only equip them two-handed without triggering the penalty, they will suffer from the lack of a shield and losing either \[GRASP\] means they'll be forced to one-hand a weapon they shouldn't, triggering said hefty accuracy penalty. Thus, in the majority cases they will lose out to battle axes since the majority of creatures cannot single-grasp great axes without triggering said penalty, meanwhile battle axes can be wielded with one hand and combined with a shield by anyone. Otherwise, if able to be single-grasped properly by its wielder, the great axe makes for an excellent weapon well-suited for limb severing and decapitation and is particularly an ideal weapon for the majority of Adventure Mode threats, though like other edged, slashing weapons may have issues with armored enemies and those of very large size.

## Bugs

In fortress mode, one-handed vs. two-handed checks are performed correctly, but can wield vs. can't wield ignores height and broadness modifiers, so dwarves cannot equip great axes.Bug:5812 See this forum post for details.

|  |
|----|
| "Great axe" in other / Languages / Dwarven / : / saràm libash / Elven / : / apaca cuthefi / Goblin / : / snuz agun / Human / : / umon osp |

    [ITEM_WEAPON:ITEM_WEAPON_AXE_GREAT]
    [NAME:great axe:great axes]
    [SIZE:1300]
    [SKILL:AXE]
    [TWO_HANDED:77500]
    [MINIMUM_SIZE:62500]
    [MATERIAL_SIZE:5]
    [ATTACK:EDGE:60000:8000:hack:hacks:NO_SUB:1250]
        [ATTACK_PREPARE_AND_RECOVER:3:3]
    [ATTACK:BLUNT:60000:8000:slap:slaps:flat:1250]
        [ATTACK_PREPARE_AND_RECOVER:3:3]
    [ATTACK:BLUNT:100:1000:strike:strikes:pommel:1000]
        [ATTACK_PREPARE_AND_RECOVER:3:3]
