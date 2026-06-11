# Die

> Fonte: [Die](https://dwarffortresswiki.org/index.php/Die) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Construction**
- **Used for**
- **Divination (see Die#Adventurer Mode ) Tavern games (unimplemented)**
- **Base value:** Size
- **10☼:** 5 cm³
- **Browse other items**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Dice** (singular *die*) are an item randomly found in religious (not for megabeasts "Shrine (megabeast)")) shrines located throughout the world, with several able to spawn at monasteries. They can be picked up and rolled to divine the will of the gods relevant to the dice, granting a variety of possible effects both positive or *fun*. Divination can be disallowed in advanced world generation.

Dice come in several known varieties, depending on the number of sides:

- D20 (twenty-sided, known as "icosahedral")
- D12 ("twelve-sided" or "dodecahedral")
- D8 ("eight-sided" or "octahedral")
- D6 ("six-sided" or "cubic")
- D4 ("four-sided" or "tetrahedral" \*) (\* *this is, in fact, To Be Confirmed; due to technical issues with it, according to Toady*)

## Fortress Mode

In fortress mode, dice can be created in a craftsdwarf's workshop from wood, stone, or glass. It is not currently possible to specify the number of sides to make on dice, nor do descriptions on dice mention the number of sides that they have. Divination currently does not occur in fortress mode, making dice only usable as trading goods.

## Adventurer Mode

In adventurer mode, dice can be found and used for divination by the player. Each die will have a series of words, images or numbers, the former two influenced by the deity's spheres. Effects are tied to the specific number or image on the die, but are unique to each specific divination practice (which several dice may share, however). Therefore, rolling the same number or image on the same die after the time since the last divination has expired will result in the same effect. A die with a large number of faces can have several numbers or images that produce the same effect (such as bad or good luck curses). Multiple dice may be held and rolled at a time, though this only appears to count as rolling the die selected in the inventory, dropping all other dice while mentioning their number or image (but not their effect). Only dice found in shrines have any effect - dice taken as equipment at character creation can be rolled, but won't have any special effect, giving only "You roll." text, without any additional text, as they lack any numbers or images to show after the roll.

List of known dice effects:

|  |
|:--:|
|   This article or section contains **minor spoilers**. You may want to avoid reading it. |

- Cosmetic: various messages that have no effect, giving ominous, foreboding, or fateful advice or statements.
- Minor blessing: grants the user a week of good luck (50% chance of 150% skill rate multiplier).
- Minor curse: grants the user a week of bad luck (20% chance to fail any skill roll).
- Medium blessing, only appears on D12 (which will each have exactly one effect of the four below) and D20 (which may have up to two):
  - Creates a random artifact-quality "holy" piece of equipment at the tile where the die was rolled, made of divine metal, divine fabric or (rarely) adamantine. Any given die will only ever produce equipment of one specific category (weapon, bodywear, legwear, headwear, handwear, footwear, or shield), but the successive gifts vary and may be anything in the chosen category, from training weapons or thongs, to procedural divine equipment.
  - Upgrades the quality level of each worn or held item, including containers and things strapped to the upper body (like backpacks and shields). One- and two-level upgrades have been observed so far. Testing shows that this does not upgrade masterwork or artifact items in any way, which is to be expected.
  - Heals most wounds and scars over a period of several turns. May even regrow limbs, but this is buggy.Bug:11396
  - Grants the user a random friendly pet spawned nearby (must have \[NATURAL\] or \[LARGE_PREDATOR\] tokens; vermin, aquatic, sentient or supernatural creatures are excluded).
- Medium curse: transforms the user into a random creature for one week (same selection as above, except \[LARGE_PREDATOR\] is forbidden). Removes the need to eat or drink for the duration of the curse.

The possible effects of a die mostly depend on its number of sides, although medium blessings and cosmetic messages are chosen randomly (per divination practice). The distribution is as follows:

|          |          |                 |              |                  |               |
|----------|----------|-----------------|--------------|------------------|---------------|
| Die type | Cosmetic | Minor blessings | Minor curses | Medium blessings | Medium curses |
| D4       | 2        | 1               | 1            | 0                | 0             |
| D6       | 4        | 1               | 1            | 0                | 0             |
| D8       | 4        | 2               | 2            | 0                | 0             |
| D12      | 4        | 3               | 3            | 1                | 1             |
| D20      | 6        | 5               | 5            | 2                | 2             |

The type of divine material from which the gifted holy item is made seems to be random,\[Verify\] irrespective of the deity's spheres.

Dice do not have to be rolled at the shrine, so the player can freely take them with them on adventures to roll later. If the player has an entirely player-made party of adventurers, each character can roll the dice individually to perform their own divinations.

Warning: each die is tied to a specific *deity*, *not* a religion, and using *any* dice tied to the *same deity* more than twice in 24 hours–1 week, even if the dice came from different religions, will anger the gods, cursing the ill-fated thrower in a similar way to toppling over a statue of one's patron. Because of this, it is dangerous to roll an unknown die if you recently performed a divination, as it may belong to the same deity. If the player does roll the dice of the same god a second time, they will get one (and only one) warning; the next roll for the same god will result in the character getting cursed. However, the god(s) may choose to "ignore your hubris", resulting in no punishment. Any creature cursed by the gods in such a way will be unable to benefit from *any* deity's dice ever again. Below is a table with the known ignoring hubris messages

|              |                                     |
|--------------|-------------------------------------|
| Deity Sphere | Message                             |
| Any          | \[SPHERE\] is allowed even in this. |
| Any          | Infinite \[SPHERE\]!                |
| Any          | Such is the spirit of \[SPHERE\]    |
| Any          | \[SPHERE\] without bound.           |
| Any          | Oh sweet \[SPHERE\]!                |
| Freedom      | You are free to do as you choose.   |

### Rolling a die in Adventurer Mode

An adventurer rolls a four-sided divination die. The ominous message "It is too soon to forgive" has no effect.

You must hold the die in your hand, so either:

- r remove it from any containers you're carrying it in, or,
- with a hand empty, g get it from the ground or a pedestal;

then I interact with the die, selecting the "roll" option.

Your character will then "Divine the will of according to the practice of ".

## Bugs

- The luck modifiers and the "beast transformation" curse seem to be treated as normal syndromes, and, thus, can be instantly ended by simply unloading the cell (fast travelling, sleeping).
- The transformation curse also heals all wounds, much like a werebeast curse.
- Holy armor is always human-sized, even when gifted to a dwarf. It also sometimes has inappropriate materials (e.g. a divine fabric helm).
- Dice may, under unknown circumstances, respawn even after being taken from their home shrine, after a cell reload.\[Verify\]

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Some dwarves love to roll dice and play games about dungeons and dragons. They might also play games about masquerading vampires or war hammers.

    [ITEM_TOOL:ITEM_TOOL_DIE]
    [NAME:die:dice]
    [VALUE:1]
    [HARD_MAT]
    [TOOL_USE:DIVINATION]
    [TOOL_USE:GAMES_OF_CHANCE]
    [SHAPE_CATEGORY:DICE]
    [USES_FACE_IMAGE_SET]
    [TILE:8]
    [SIZE:5]
    [MATERIAL_SIZE:1]
