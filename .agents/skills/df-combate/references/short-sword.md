# Short sword

> Fonte: [Short sword](https://dwarffortresswiki.org/index.php/Short_sword) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*For a comparison of different weapons, see Weapon.*

A **short sword** is an edged weapon larger than a knife, with a blade long enough to make slashing effective, but shorter than other swords. Short swords have the same basic attacks as other swords, but suffer slightly because of their reduced size. As with all edged weapons, metals with good edge properties are most effective.

## Properties

Short swords use and train the swordsman skill (called "Swordsdwarf" in dwarf mode). They have stabbing and slashing attacks, along with a blunt pommel strike. Swords can be useful for dealing with all kinds of foes, although they're not as good at any of these attacks as more specialized weapons.

## Fortress mode

Dwarves can forge short swords out of any weapon-grade metal, but those with superior edge properties are more effective. All dwarves can equip short swords, but a tiny fraction must use two hands.

"Rock short swords" are a special type of short sword that are constructed out of obsidian (with wooden handles) by a stonecrafter at a craftsdwarf's workshop. Rock short swords are graphically depicted as the Aztec macuahuitl, a club with rows of sharp stone edges affixed to the sides.

### Production

- Metal short swords cost **one** metal bar to forge, or **three** adamantine wafers.
- Rock short swords cost **one** stone and **one** log.
- When a non-adamantine metal short sword is melted down, it will return **0.9** metal bars, for an **efficiency of 90%**.
- When an adamantine short sword is melted down, it will produce **0.9** wafers, for an **efficiency of 30%**

## Adventurer mode

As an adventurer, it is possible to play as a swordsman. If you're an elf or a dwarf, a short sword is a good all-round weapon. which can be used successfully on a wide variety of foes, but is most effective against lightly armoured creatures. Generally, it's best to *slash* when fighting relatively small unarmoured foes (goblins, kobolds, and humans for example), and to *stab* larger unarmoured foes, such as megabeasts. Short swords are a fine choice against heavily-armoured foes, too; stabbing is strictly better than pommel striking due to the low contact area, so it should be ignored.

-

  A drawing of an obsidian shortsword.

|  |
|----|
| "Short sword" in other / Languages / Dwarven / : / idrom dastot / Elven / : / coci ocade / Goblin / : / ôbang oxox / Human / : / pasub thil |

    [ITEM_WEAPON:ITEM_WEAPON_SWORD_SHORT]
    [NAME:short sword:short swords]
    [SIZE:300]
    [SKILL:SWORD]
    [TWO_HANDED:37500]
    [MINIMUM_SIZE:32500]
    [CAN_STONE]
    [MATERIAL_SIZE:3]
    [ATTACK:EDGE:20000:4000:slash:slashes:NO_SUB:1250]
        [ATTACK_PREPARE_AND_RECOVER:3:3]
    [ATTACK:EDGE:50:2000:stab:stabs:NO_SUB:1000]
        [ATTACK_PREPARE_AND_RECOVER:3:3]
    [ATTACK:BLUNT:20000:4000:slap:slaps:flat:1250]
        [ATTACK_PREPARE_AND_RECOVER:3:3]
    [ATTACK:BLUNT:100:1000:strike:strikes:pommel:1000]
        [ATTACK_PREPARE_AND_RECOVER:3:3]
