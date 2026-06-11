# Size

> Fonte: [Size](https://dwarffortresswiki.org/index.php/Size) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

!!UNKNOWN!!  · xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*You may be looking for size of clothing, armor, the dimensions of a tile, or the list of creatures by size.*

**Size** is a measure of how big a creature or item is, as volume in cubic centimeters[1], and called [`[BODY_SIZE]`](/index.php/Creature_token#BODY_SIZE "Creature token") or [`[SIZE]`](/index.php/Item_definition_token "Item definition token") in the raw files.

Size has many important effects on the game, many through its direct effect on item weight, one of the many material properties in Dwarf Fortress. Size directly affects such things as which weapons your dwarves can equip, butchering returns, storage limits, and combat effectiveness for both creatures and weapons.

As far as in-game location and movement, size does *not* matter; one item or creature always is located in just one tile, regardless of size. If a path is open to a dwarf, it's open to every other creature in the game, no matter how large. A thousand full grown dragons can occupy a single square (so long as 999 of them are lying down), and a common rabbit blocks a door or fills a cage as completely as a gigantic bronze colossus.

## Game mechanics

Size is used to calculate an item's weight, along with the density of the underlying material(s):

Weight (in Γ) = Density (in kg/m3) \* Size (in cm3) / 1,000,000 (cm3 in a m3). Through weight, the size of an item has further ramifications in the game, such as hauling speed, pressure plate activation, impact momentum, weight restrictions, and so forth.

Internally, all custom size numbers are rounded down to the nearest multiple of 10 - thus, if you define an item with `[SIZE:15]`, it will actually behave as if you had specified `[SIZE:10]`.[2]

The weight of creatures is calculated from the densities and sizes of the layers of their body parts, which currently results in corpse weights that are about 1/3 heavier than expected.

## Buildings

The [`[DIM]`](/index.php/Building_token#DIM "Building token") building token defines the size of a workshop or building in tiles. This differs from creatures and items in that a building doesn't have a weight, and it's not in cm³, of course.

## Creatures

When it comes to creatures, size is a rough stand-in for weight since standard flesh weighs about one gram per cubic centimeter. However, in the typical complexity of *Dwarf Fortress*, there are a number of *other* materials animals can include (ivory, hair, horn, shell, etc.) which have their own densities, shifting a creature's actual weight relative to its size, sometimes significantly (elephant tusks weigh a *lot*). Creature size is determined by [`[BODY_SIZE]`](/index.php/Creature_token#BODY_SIZE "Creature token") tokens, often with multiple tokens to set their base size at certain ages.

Bodysize determines several things:

- Average butchering yields.
- How much damage they can absorb (along with morphology).
- How much damage they can inflict in melee (along with morphology and attack definition tokens).
- For creatures that can wear equipment ([`[EQUIPS]`](/index.php/Creature_token#EQUIPS "Creature token")).

- What size of equipment a creature can wear; clothing and armor are sized for a specific species and only creatures with a species base size near that size can wear them, an individual creature's actual size does not matter for this.
- Weapons have a minimum size that a creature must be to wield them ([`[MINIMUM_SIZE]`](/index.php/Weapon_token#MINIMUM_SIZE "Weapon token") and [`[TWO_HANDED]`](/index.php/Weapon_token#TWO_HANDED "Weapon token")), tissue layer thickness not included, see below.

The actual size of an individual creature is the result of different effects:

- The base BODY_SIZE for the species of creature.
- The age of the creature; most creatures are born at minimum size and grow to a maximum.

- Some, like dragons and most species of snake, grow throughout their entire lifetime and may not live long enough to reach the maximum.

- Inheritance; many creatures have [`[BODY_APPEARANCE_MODIFIER]`](/index.php/Creature_token#BODY_APPEARANCE_MODIFIER "Creature token")) tokens that allow them to vary in height, width, or length, which they can maybe pass on to children.

The following add to size, but are not included when determining how weapons are wielded.

- Muscle mass, determined by its strength attribute (a thin dwarf with ~44210 size will be ~64210 once they become unbelievably strong), due to muscle having [`[THICKENS_ON_STRENGTH]`](/index.php/Tissue_definition_token#THICKENS_ON_STRENGTH "Tissue definition token").
- Fat mass, due to [`[THICKENS_ON_ENERGY_STORAGE]`](/index.php/Tissue_definition_token#THICKENS_ON_ENERGY_STORAGE "Tissue definition token").\[Verify\]

Creature sizes range from 1 (small insect vermin) to 200,000,000 (giant sperm whales, the largest creature in the game). See List of creatures by adult size for details.

### Sample list of creature sizes in cm3

|  |  |  |  |
|:--:|:--:|:--:|:---|
| Name | Size at birth | Size at maturity | Notes |
| Adder | 15 | 150 | Smallest (non-vermin) creature |
| Rabbit | 50 | 500 | Smallest domestic animal |
| Cat | 500 | 5,000 |  |
| Kobold | 1,000 | 20,000 |  |
| Dog | 1000 | 30,000 |  |
| Dwarf | 3,000 | 60,000 |  |
| Giant tiercel peregrine | 8,308 | 113,292 | Smallest giant animal |
| Water buffalo | 100,000 | 1,000,000 | Largest domestic creature |
| Elephant | 500,000 | 5,000,000 | Largest natural land-based creature |
| Cave dragon | 6,000 | 15,000,000 | Largest cavernous creature |
| Sperm whale | 500,000 | 25,000,000 | Largest natural creature |
| Dragon | 6,000 | 25,000,000 | Largest megabeast |
| Giant elephant | 4,000,000 | 40,000,000 | Largest land-based creature |
| Giant sperm whale | 4,000,000 | 150,000,000 | Largest creature, period |

## Items

Most items defined in the raws require a `[SIZE]` token, each class of item has its own: for instance, [`[SIZE]`](/index.php/Ammo_token#SIZE "Ammo token") for ammo, [`[SIZE]`](/index.php/Weapon_token#SIZE "Weapon token") for weapons, [`[SIZE]`](/index.php/Tool_token#SIZE "Tool token") for tools, and so on.

Item types not defined in the raws also have a size which can be determined from their weight and material density, using DFHack, or code debugging. Some assorted item type sizes, and their storage capacity when applicable:

|  |  |  |  |
|:--:|:--:|:--:|:---|
| Item Type | Volume | Capacity | Notes |
| Bars | 6000 |  |  |
| Cut gems | 200 |  |  |
| Blocks | 6000 |  |  |
| Rough gems | 2500 |  |  |
| Mined stone | 100000 |  |  |
| Wood logs | 50000 |  |  |
| Door | 30000 |  |  |
| Floodgate | 30000 |  |  |
| Bed | 30000 |  |  |
| Chair | 30000 |  |  |
| Chain | 5000 |  |  |
| Flask | 1000 | 1800 |  |
| Goblet | 1000 | 1800 |  |
| Instrument | 4000 |  |  |
| Toy | 1000 |  |  |
| Window | 20000 |  |  |
| Cage | 30000 | 60000 |  |
| Barrel | 20000 | 60000 |  |
| Bucket | 3000 | 6000 |  |
| Animal trap | 3000 | 30000 |  |
| Table | 30000 |  |  |
| Coffin | 30000 | 60000 |  |
| Statue | 60000 |  |  |
| Corpse | Special |  | Based on the size of the corpse and what it's made of. |
| Weapon | SIZE1 |  |  |
| Armor | Special |  | Depends on armor type and the race it was crafted for. See here for some examples. |
| Shields | Special |  | Based on UPSTEP and the race that crafted it. |
| Box | 20000 | 60000 |  |
| Bag | 1000 | 60000 |  |
| Bin | 15000 | 60000 |  |
| Armor stand | 10000 | 60000 |  |
| Weapon rack | 10000 | 60000 |  |
| Cabinet | 30000 | 60000 |  |
| Figurine | 1000 |  |  |
| Amulet | 500 |  |  |
| Scepter | 3000 |  |  |
| Ammo | SIZE1 |  |  |
| Crown | 1000 |  |  |
| Ring | 50 |  |  |
| Earring | 30 |  |  |
| Bracelet | 200 |  |  |
| Large gem | 50 |  |  |
| Anvil | 10000 |  |  |
| Body part | Special |  | Based on the size of the body part and what it's made of. |
| Remains | 2000 |  |  |
| Meat | 2000 |  |  |
| Fish | 2000 |  |  |
| Unprepared fish | 2000 |  |  |
| Live vermin | Special |  | Based on creature's adult size. |
| Tame vermin | Special |  | Based on creature's adult size. |
| Seeds | 100 |  |  |
| Plant | 1000 |  |  |
| Leather | 5000 |  |  |
| Plant growths | 50 |  |  |
| Thread | ceil(Dimension/50)1 |  | Freshly gathered/produced thread has a dimension of 15000 and thus has a volume of 300 |
| Cloth | ceil(Dimension/50)1 |  | Freshly woven cloth has a dimension of 10000 and thus has a volume of 200 |
| Totem | 5000 |  |  |
| Backpack | 5000 | 30000 |  |
| Quiver | 3000 | 12000 |  |
| Catapult parts | 20000 |  |  |
| Ballista parts | 20000 |  |  |
| Siege ammo | 30000 |  |  |
| Ballista arrow head | 10000 |  |  |
| Mechanisms | 20000 |  |  |
| Trap component | SIZE1 |  |  |
| Drink | 600 |  |  |
| Powder | 600 |  |  |
| Cheese | 1000 |  |  |
| Prepared meal | 1000 |  |  |
| Misc. liquid | 600 |  |  |
| Coin | 10/161 |  | The size of a stack is 0.625 per coin, then subject to the rounding; so a single coin is 10 cm³ but a stack of 500 is 310 cm³. |
| Glob | 600 |  |  |
| Small rock | 2000 |  | As thrown by adventurers. |
| Pipe section | 30000 |  |  |
| Hatch cover | 10000 |  |  |
| Grate | 10000 |  |  |
| Quern | 30000 |  |  |
| Millstone | 30000 |  |  |
| Splint | 2000 |  |  |
| Crutch | 2000 |  |  |
| Traction bench | 30000 |  |  |
| Orthopedic cast | 2000 |  |  |
| Tool | SIZE1 | CAPACITY1 | Includes items such as nest boxes, jugs, large pots, hives, minecarts, wheelbarrows, stepladders, pedestals, and display cases |
| Slab | 60000 |  |  |
| Egg | Special |  | Presumably the caste's EGG_SIZE. |
| Book | 1000 |  |  |
| Sheet | ceil(Dimension/50)1 |  | A fresh sheet has a dimension of 10000 and thus has a volume of 200 |
| Branch | 5000 |  | An adventurer mode item |

1 - As noted above, all values are rounded *down* to the nearest multiple of 10, with a minimum value of 10.

## See also

- Density
- Weight
