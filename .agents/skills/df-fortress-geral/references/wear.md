# Wear

> Fonte: [Wear](https://dwarffortresswiki.org/index.php/Wear) — Dwarf Fortress Wiki (GFDL/MIT)

**Wear** is the degradation of certain items' materials over time. Clothing will slowly wear out when being used, subject to damage, or through natural decay. Using equipment, such as weapons and armor, can wear them down. Wear alters the value of an item, and it eventually will be destroyed. Additionally, animal-based products can rot, which is different from wear (see miasma), while crops and harvested plants can **wither** if not stored in a stockpile, making them useless but generating no miasma (see farming).

## Overview

Wear will alter the value of an item, and is denoted by the symbols x, X and XX. For example, over time a dwarf's "Pig tail shirt" will degrade into a "xPig tail shirtx", a "XPig tail shirtX" and eventually a "XXPig tail shirtXX" before disappearing entirely. Every 806400 "points" of wear will increase the item's damage level one step (i.e. "item" -\> "xitemx" -\> "XitemX" -\> "XXitemXX" -\> destroyed). If you sell worn clothes to caravans early enough, they are still worth good money:

|            |      |                |                |                  |
|------------|------|----------------|----------------|------------------|
| Wear Level | Item | **x**Item**x** | **X**Item**X** | **XX**Item**XX** |
| Value      | 100% | 75%            | 50%            | 25%              |

Armor and weapons can also suffer wear as a result of combat . For weapons, the chances of suffering wear depend on the material properties of the body tissues or armor encountered during an attack, while armor suffers wear depending on the material properties of the body part/weapon hitting it. The chance depends on their relative fracture, yield, and possibly strain-at-yield, impact or shear depending on the type of attack. For example, a leather helm will rapidly deteriorate if you let its wearer suffer a few dog bites, while bone or shell helms will degrade much slower (being equivalent to tooth in shear values).

## Notes

- All improvable items made from creature or plant materials (e.g. cloth, silk, leather, yarn, or wood) will gradually wear out over a very long period of time, even if just sitting in stockpiles, gaining one level of wear every 100 years.
- All clothing *and armor* in a refuse stockpile will wear out. This is intended as a means of destroying old used clothing that would otherwise make dwarves grumpy. Note that a stockpile with any type of refuse enabled (such as bone) counts as a refuse stockpile for wear application.

- Clothing that is being worn will wear out over time, due to normal usage. This happens regardless of material.
- Clothing worn by invaders is also subject to wear.
- Armor does not wear out over time, unless put in a refuse stockpile. Combat damage can inflict wear.
- Soft materials like leather and bone make for inadequate armor. While bone will hold up well enough against wildlife, neither can stand up to metal weapons for long.

- Items (including clothing, leather, and wood) suffer accelerated wear while on fire (10 points of "wear" every game tick; a burning item will be totally consumed after exactly 322560 game ticks (which, at 1200 ticks per day, takes 9 months and 16.8 days)).
- Items suffer accelerated wear when their temperature exceeds their base material's HEATDAM_POINT (common with burning organics).
- Items suffer accelerated wear when their temperature falls below their base material's COLDDAM_POINT (such as wood and cloth items stored aboveground in a trade depot or starting wagon "starting wagon") in a glacier biome). Walls do not halt this effect.
- Artifacts never burn away, because their artifact status locks their "wear" level at zero. However, they would still melt or boil when their temperature exceed their melting/boiling point. An artifact book will be destroyed when tossed into magma.

- Building destroyers cause wear on certain types of furniture (such as doors and hatch covers) until they are completely destroyed.
- Cages do not prevent wear.
- Being unavailable to potential invaders, steel and other fun materials will likely outlast the dwarves equipped with them. Most dwarves will only ever witness armor made from steel degrading if subjected to public transportation mishaps.

## Bugs

- Cloth and leather items suffer gradual wear at 1/5 the intended rate. DFHack's "tweak craft-age-wear" (enabled by default) modifies these items to wear at the intended rate (one wear level every 20 years).
- Worn clothing issued by a military uniform is not replaced.

## See also

- Quality

## The Human Market

Even if a piece of clothing has been worn down to the point that any self-respecting dwarf would disdain to wear it, it still has value and can be sold back to humans. This seems especially true for xtrousersx that have holes around the knee section, or have been exposed to acids. These particularly worn trousers are highly prized by short-sighted human adolescents and are resold in human markets as ☼Masterwork☼ trousers at exorbitant prices. Additionally, xglovesx whose fingers have worn off are similarly prized. Humans call them "Fingerless Gloves", though it is unknown how a human without fingers would wear such a glove.
