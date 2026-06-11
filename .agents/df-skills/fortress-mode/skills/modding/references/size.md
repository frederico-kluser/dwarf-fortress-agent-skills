# Size

> Fonte: [Size](https://dwarffortresswiki.org/index.php/Size) — Dwarf Fortress Wiki (GFDL/MIT)

*You may be looking for size of clothing, armor, the dimensions of a tile.* *Or more likely, the list of creatures by size.*

**Size** is a measure of how big a creature or item is, measured in cubic centimeters. It is essentially volume, but is called size in creature raw files, and is so translated to item definitions as well.1

Size, along with the underlying material's density, is used to calculate an item's weight:

Weight (in Γ) = Density (in kg/m³) \* Size (in cm³) \* 10 / 1,000,000 (cm³/m³)

Size has a large number of important ramifications on the game, many of them through its effect on overall weight, but as material properties go, its implementation in the game is somewhat underwhelming - witness the incredible compression of matter, space, and time that is the garbage dump. This is mostly because when even dragons occupy a single square, size becomes a little difficult to contextualize. It doesn't help that a thirty-five to forty foot bronze colossus fits in a basic wooden cage (although, a fire man fits in it too).

Size directly affects such things as which weapons your dwarves can equip, butchering returns, and combat effectiveness, both for creatures (elephants are very hard to kill because there's so much tissue to them, but they have a surprisingly hard time landing a hit on, say, cavys) and for weapons. Through weight, the size of an item has a large number of further ramifications in the game, such as carry time, pressure plate activation, impact momentum, weight restrictions, and so forth. Changing this value too much can lead to fun.

## Bodysize

Creature-specific size is known internally as **bodysize** (from the token). When it comes to creatures, size is a rough stand-in for weight: standard flesh weighs one gram per cubic centimeter. However, in the infinite complexity of *Dwarf Fortress*, there are a number of *other* materials animals internalize (ivory, hair, horn, shell, etc.) which have their own densities, shifting a creature's actual weight relative to its size, sometimes significantly (elephant tusks weigh a *lot*). Bodysize also determines average butchering yields, (along with morphology) how much damage they can absorb, and (along with morphology and attack definition tokens) how much damage they can inflict in melee. On creatures, size also directly determines what kind of equipment a creature can wear: large, small, normal, or none at all.

The actual size of a creature is the result of three different effects, one basic and two that are highly variable. First and most basic is the average maintained across an individual species of creature. The second is the age of the creature: most creatures are not born anywhere near their maximum size, and instead must grow into it; some, like most species of snake, grow throughout their entire lifetime, and probably will not live long enough to reach it. The third is inheritance: version 0.31.1 introduced genetics, allowing creatures to inherit part of their size from the appearance, specifically the height and girth, of their parents.

Actual creature sizes go from 1 (small insect vermin) to 200,000,000 (giant sperm whales, the largest creature in the game). See List of creatures by adult size for details. The average size set for a dwarf is 3,000, 15,000, and 60,000, the size of a baby, child and adult respectively.

## Sample list of creature sizes

| Name | Size at birth | Size at maturity | Notes |
|----|----|----|----|
| Adder | 15 | 150 | Smallest (non-vermin) creature |
| Rabbit | 50 | 500 | Smallest domestic animal |
| Cat | 500 | 5,000 |  |
| Kobold | 1,000 | 20,000 |  |
| Dwarf | 3,000 | 60,000 |  |
| Deer | 14,000 | 140,000 |  |
| Giant slug | 200,007 | 200,007 | Smallest giant creature\* |
| Polar bear | 40,000 | 400,000 |  |
| Water buffalo | 100,000 | 1,000,000 | Largest domestic creature |
| Rhinoceros | 300,000 | 3,000,000 |  |
| Elephant | 500,000 | 5,000,000 | Largest natural land-based creature |
| Cave dragon | 6,000 | 15,000,000 | Largest cavernous creature |
| Sperm whale | 500,000 | 25,000,000 | Largest natural creature |
| Dragon | 6,000 | 25,000,000 | Largest megabeast |
| Giant elephant | 4,000,000 | 40,000,000 | Largest land-based creature |
| Giant sperm whale | 4,000,000 | 150,000,000 | Largest creature, period |

\*Along with giant beetles, brown recluse spiders, damselflies, dragonflies, fireflies, flies, grasshoppers, jumping spiders, lice, mantises, monarch butterflies, mosquitoes, moths, roaches, snails, thrips, and ticks.

## Mechanics

- **Constructed items**: Item definition files for industry-crafted items are specific to various classes of items: for instance, ammo has its own ammo definition tokens, as does armor, as do tools, and so on. A token is a field required in all of these definitions.

Bars lack a defined size token in the raws. They have a size of 600 cm³, which can be deduced from the equation listed above using their weight and the densities of their corresponding materials. This is consistent with 5 bars fitting inside a 3000-capacity bin. The dimensionless unit of '150' products per bar, primarily of use for soap, suggests that each use of soap should diminish the size of the item by 4cm³ (i.e. 600cm³/150). Whether this is true is currently untested.

- **Inorganic items**: Stones, gems, and ores appear to have a default, hard-coded size that is applied to all items of that class; thus there is no direct inorganic material definition token for it.
- **Plants**: There is no size plant token.
- **Buildings**: The building token defines the by-tile size of a workshop or building.
- **Creatures**: The creature token version of is the `[BODY_SIZE:#:#:#]` token, which accepts three variables. The first number is age in years; the second additional age is in days. The third number is its size in cm³. Multiple ages and multiple tokens are used to constrain a creature's age-based growth pattern and final size. Genetics is accounted for by a token tagged for and/or . For instance, genetic variance in the anaconda is defined so: . Each interval value is genetically inherited, and each interval value has an equal chance of occurring; the numbers are the percentage of the base size a creature in the interval will be.

## See also

- Weight
