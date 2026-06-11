# Bolt

> Fonte: [Bolt](https://dwarffortresswiki.org/index.php/Bolt) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Bolts** are a type of ammunition used by crossbows and bolt throwers. They can be made from either wood, bone, or weapons-grade metals. As with all non-siege ammo, hunting and military dwarves must be equipped with quivers to be able to carry bolts around for shooting. On embark, hunters reserve 25 bolts.

Wooden and bone bolts are produced in a craftsdwarf's workshop by a wood crafter or a bone carver, respectively. Each job will produce a stack of 25 wooden bolts from a single log, or a stack of 5 bone bolts taking a single bone from a stack. Metal bolts are a weapon, not a craft, so require Weapon*smithing* (not Metal*crafting*) and a Metalsmith's forge or Magma forge, creating a stack of 25 bolts from a single metal bar.

When fired, bolts have a chance of shattering on impact or bouncing off onto the ground as free-laying items. However, depending on standing orders, they may be immediately forbidden after being fired (to prevent ~~suicidal~~ hauling dwarves from running into active battlefields), and have to be reclaimed by the player, either directly or from the stocks screen.

Like most edged weapons, fired bolts follow the superior metal rule [1], often struggling to penetrate armor of equal or better material. Adamantine bolts are only superior to steel against steel-clad enemies, although they're also much less encumberingBug:3677. Wooden and bone bolts are only useful for hunting and training.

## Masterwork bolts

As with other items, high-skill dwarves can make masterwork-quality bolts. While they don't care if the bolts are fired and shatter on impact, they do get upset if a bolt gets carried off the map - say, by a retreating enemy with the bolt stuck in them.

The simplest remedy for this is to simply **make more bolts** - a dwarf who has produced hundreds of masterwork bolts will be more annoyed by flies than the loss of a masterwork. This is because the stress penalty for the loss of a masterwork is divided by the number of remaining masterwork items made by that dwarf (see thoughts for more information).

## Weapon traps

Bone bolts are not advisable for weapon traps as only a stack of 5 will be stored per crossbow, making frequent restocking necessary.

## Bugs

- If bolts claimed by a squad are forbidden, then the squad may not claim new bolts. Instead, they become stuck waiting for those bolts, indicated by a yellow bolt icon in the 'equip' menu. In this case, assigning a uniform again (even the same exact uniform that's currently assigned) will force them to find new, available bolts.
- If bolts claimed by a squad are forbidden *and then made unreachable*, the squad will be unable to select new bolts. In this case, the bolt icon remains red in the 'equip' menu. The player will need to either allow them to acquire the bolts they have claimed or create a new squad.
- Masterwork bolts cause unhappy thoughts when they get carried off the map or melted downBug:3169. The solution to this is to make more bolts, since the unhappy thought caused by "art defacement" becomes less significant the more masterpieces a dwarf has produced.
- Bolts are not stored in a barracks, despite the tooltip for the 'store squad equipment' icon. Bolts will get dropped wherever the dwarf drops their quiver and promptly hauled to any stockpile where they are allowed.

|  |
|----|
| "Bolt" in other / Languages / Dwarven / : / alåth / Elven / : / ene / Goblin / : / okom / Human / : / thora |

    [ITEM_AMMO:ITEM_AMMO_BOLTS]
    [NAME:bolt:bolts]
    [CLASS:BOLT]
    [SIZE:150]
    [ATTACK:EDGE:5:1000:stab:stabs:NO_SUB:1000]
        [ATTACK_PREPARE_AND_RECOVER:3:3]
