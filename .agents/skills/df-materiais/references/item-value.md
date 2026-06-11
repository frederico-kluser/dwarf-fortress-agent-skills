# Item value

> Fonte: [Item value](https://dwarffortresswiki.org/index.php/Item_value) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*For value optimization, see Maximizing value.*

*For cultural values, see Personality value.*

*For room values, see Zones: Quality and value.*

**Item value** is determined by a number of factors: the form of the item, the material it is made out of, the quality of its creation, and any decorations on it.

The **final value** of an item is the **base value** of the form of the item (e.g. block *or* statue) multiplied by the **material multiplier** (e.g. granite *or* gold), multiplied by the **quality modifier** (e.g. fine *or* masterful) if any, then summed with the final value of all **decorations**.

# Base values of items

The **base value** of an item is determined by the form of the item, not what it is made out of. For example, a wood block uses the **base value** for a block; a native gold block uses the *same* **base value**, since it too is in the form of a "block". In both cases, the **final value** is then determined by adjusting the base value with the appropriate modifiers.

## Items without quality levels

|  |  |
|----|----|
| Base Value | Items |
| 0 | Body part, Corpse, Remains, small rock |
| 1 | glob, seed, alcohol, powder, extract, tree branches |
| 2 | Fish, unprepared fish, Meat, Egg, Plant, Leaves |
| 3 | Log, Stone |
| 5 | Bar, Block, Leather |
| 6 | Thread, Gem (rough) |
| 10 | Ballista arrowhead, cheese, Honeycomb |
| 20 | Gem (cut) |
| Varies | live vermin, tame vermin |

## Items with quality level

### Misc. items

|  |  |
|----|----|
| Base Value | Items |
| 1/50 | Coin1 |
| 1 | Die, Orthopedic cast, Prepared meal4 |
| 5 | Paper & Papyrus sheets |
| 7 | Cloth2 |
| 10 | Animal trap / , / Altar / , / Amulet / , / Anvil / , / Armor stand / , / Backpack / , / Barrel / , / Bed / , / Bin / , / Book / , / Bookcase / , / Bowl / , / Box / , / Bag / , / Bracelet / , / Bucket / , / Cabinet / , / Cage / , / Chain / , / Chair / , / Cleaver / , / Coffin / , / Crown / , / Crutch / , / Decoration / 3 / , / Display Case / , / Door / , / Earring / , / Figurine / , / Flask / , / Floodgate / , / Fork / , / Goblet / mug / cup / , / Grate / , / Hatch cover / , / Helve / , / Hive / , / Instrument / (non-main components) / , / Jug / , / Knives / , / Ladle / , / Large gem / , / Large pot / , / Millstone / , / Mortar / , / Nest box / , / Pedestal / , / Pestle / , / Pipe section / , / Pouch / , / Quiver / , / Quern / , / Ring / , / Scepter / , / Scroll Roller / , / Slab / , / Stone axe / , / Splint / , / Table / , / Totem / , / Toy / , / Weapon rack / , / Trap component |
| 20 | Quire/Scroll, Siege ammo, Traction bench |
| 25 | Window, Statue |
| 30 | Ballista part, Catapult part, Mechanism |
| 50 | Cauldron, Instrument *(main part)*, Minecart, Parchment sheet, Stepladder, Wheelbarrow |
| 200 | Parchment Quire/Scroll |
| *variable*5 | Weapon, Armor, Shoe, Shield, Helm, Glove, Ammo, Pants |

*Notes*:

- 1\) Coins minted at a forge are always of base quality
- 2\) Goods made out of cloth get the following built in as decorations: the cloth (with quality mod) and the thread (without quality). Dyes are added separately (with quality), as a powder, not a decoration.
- 3\) "Decorations" include "It is decorated with ", "It is encircled with bands of ", "It is adorned with hanging rings of ", "This object menaces with spikes of ", "On this object is an image of in ", "It is studded with ". Decorations of bolts have a 1/3 base value instead.
- 4\) Prepared meals always have a base value of 1, with a quality modifier, but the ingredients also affect the final value.
- 5\) These items have their value based on their properties - see categories below:

### Prepared meal

This table shows how the quality modifiers compare to other items:

|  |  |  |  |  |
|----|----|----|----|----|
| Quality | Ingredient | Meal | Value Modifier | Meal Bonus |
| (normal) | minced | (none) | 1.0× | +0 |
| -Well-Crafted- | well-minced | well-prepared | 1.1× | +3 |
| +Finely-crafted+ | finely minced | finely-prepared | 1.2× | +6 |
| \*Superior quality\* | superiorly minced | superiorly prepared | 4/3× | +10 |
| ≡Exceptional≡ | exceptionally minced | exceptional prepared | 1.5× | +15 |
| ☼Masterful☼ | masterfully minced | masterfully prepared | 2.0× | +30 |

The value of a stack of prepared meals is equal to the material multiplier of the main ingredient (multiplied by the meal's base value of 1) times the meal's quality modifier (finely-prepared, etc.), plus the *average* of the products of each ingredient's base value and quality modifier (well-minced, etc.), all multiplied by the stack size. So, for example: a well-prepared meal consisting of 5 finely-minced cow cheese, 3 finely-minced llama tripe, 1 finely-minced llama sweetbread, and 2 superiorly minced mussels would yield a stack of 11 mussel roasts with a total value of 88☼ (for 62☼ of ingredients). (Exact calculation: `([1 * 1 * 11/10 + 3] + ([10 * 1 * 6/5] + [2 * 1 * 6/5] + [2 * 1 * 6/5] + [2 * 1 * 4/3])/4) * (5 + 3 + 1 + 2)`)

This example can be understood as:

    (base value of prepared meal = 1☼) × (mussel material multiplier = 1) × (well-prepared = 11/10) + (meal bonus = 3) = 4.1, rounded down to 4
    +
    (
     (value of cheese = 10☼) × (cow material multiplier = 1) × (finely-minced = 5/4) = 12
     +
     (value of tripe = 2☼) × (llama material multiplier = 1) × (finely minced = 5/4) = 2.4, rounded down to 2
     +
     (value of sweetbread = 2☼) × (llama material multiplier = 1) × (finely minced = 5/4) = 2.4, rounded down to 2
     +
     (value of fish = 2☼) × (mussel material multiplier = 1) × (superiorly minced = 4/3) = 2.66, rounded down to 2
    ) ÷ 4 = 4.5, rounded down to 4

    all multiplied by the total number of meals (11)
    =
    88☼

Because all math is performed with integers (with the results always rounded down), ingredient quality modifiers typically will not have any visible effect for low-value ingredients.

The individual stack sizes of the ingredients may affect your profits, but have no effect on the final meal's value. One "masterfully minced plump helmet" cooked with ten "well-minced dog meat" will have exactly the same value and description as ten "masterfully minced plump helmet" and one "well-minced dog meat".

The quality symbols shown in the name of a meal reflect the highest quality involved in its making, looking at the overall preparation as well as the mincing of each ingredient. With up to five skill rolls involved, monetary values of apparently same-quality meals can vary a lot, and a lower-quality meal can be more valuable than a higher-quality meal cooked from the same ingredients.

### Weapon

The base value of a melee weapon is (SIZE / 50) + 1; if the weapon has any EDGE attacks, its value is doubled. Ranged weapons simply have a value of 10.

Weapon values

Base Value
Weapon

3
Whip

7
Training sword

9
Training spear, War hammer

10
Crossbow, Blowgun, Bow, Large dagger

11
Flail

14
Scourge, Scimitar, Short sword

17
Training axe, Mace

18
Spear

22
Pick, Morningstar

27
Maul

30
Long sword

34
Battle axe, Pike

38
Two-handed sword

50
Halberd

54
Great axe

#### Ammo

The base value of a single unit of ammo is (SIZE / 200) + 1.

Ammo values

Base Value
Ammo

1
Blowdart, Bolt, Arrow

Value listed is for a single bolt, not stacks of bolts. Multiply the single value by the stack size for total value of a stack. (e.g. 1 bar of metal = stack of 25 bolts, etc.)

### Shield

The base value of a shield is (UPSTEP \* 3) + BLOCKCHANCE + 1.

- UPSTEP cannot be greater than 3
- BLOCKCHANCE cannot be greater than 100

Shield values

Base Value
Shields

14
Buckler

27
Shield

### Headwear

The base value of a helm is (LAYER_SIZE / 5) + (COVERAGE / 20) + 1.

- LAYER_SIZE and COVERAGE cannot be greater than 100

Helm values

Base Value
Helm

5
Cap, Head Veil, Face Veil, Headscarf

7
Mask, Turban

8
Hood

12
Helm

### Armor / torso

*(Note - When DF speaks of clothing, "armor" refers to anything worn on the torso, i.e. shirts, vests, togas, robes, etc., which all do provide some small protection, as well as breastplates and chain shirts. Combat-quality "armor" pieces are listed here by their location.)*

The base value of a piece of armor is ((UBSTEP + LBSTEP) \* 3) + (LAYER_SIZE / 5) + (COVERAGE / 10) + 1.

- UBSTEP and LBSTEP cannot be greater than 3
- LAYER_SIZE and COVERAGE cannot be greater than 100

Armor values

Base Value
Armor

8
Cape, Vest

15
Breastplate

16
Tunic

20
Mail shirt

21
Leather armor

22
Shirt

23
Toga

26
Cloak

27
Coat

31
Dress

33
Robe

### Legwear

The base value of a pair of pants is (LBSTEP \* 3) + (LAYER_SIZE / 5) + (COVERAGE / 10) + 1

- LBSTEP cannot be greater than 3
- LAYER_SIZE and COVERAGE cannot be greater than 100

Pants values

Base Value
Pants

5
Thong

8
Loincloth

13
Short skirt

16
Skirt, Braies

22
Long skirt

23
Trouser, Leggings, Greaves

### Hand- & footwear

The base value of a shoe or glove is (UPSTEP \* 3) + (LAYER_SIZE / 5) + (COVERAGE / 30) + 1.

- UPSTEP cannot be greater than 3
- LAYER_SIZE and COVERAGE cannot be greater than 100

Glove values

Base Value
Gloves

6
Gloves

7
Mittens

11/ (22*)
Gauntlets*

Shoe values

Base Value
Shoes

6
Socks

8
Shoes

9/ (18*)
Sandals, low boots*

12/ (24*)
High boots*

15
Chausses

\* Gauntlets and boots are made 2 at a time from a single bar, effectively doubling the total value of the final items.

## Material multipliers

The material multiplier for an item is found from the \[MATERIAL_VALUE:#\] tag in the raws for the material it is made out of, and can be further augmented using \[MULTIPLY_VALUE:#\]. A wood block uses the same material multiplier as a wood log or a wooden chest - that is the material value for wood, which is 1.

Common

Multiplier
Material

×2
Green glass

×3
Earthenware

×4
Stoneware

×5
Clear glass

×10
Crystal glass, Porcelain

Stones

Multiplier
Stone

×1
common stone, Bismuthinite, Bituminous coal, Lignite

×2
Cassiterite, Garnierite, Malachite, Native copper, Sphalerite, Calcite, Chalk, Dolomite, Limestone, Marble

×3
Tetrahedrite, Obsidian

×5
Galena

×8
Hematite, Limonite, Magnetite

×10
Horn silver, Native silver

×30
Native gold

×40
Native aluminum, Native platinum

×250
Raw adamantine

Gems

Multiplier
Gem

×2
Banded agate, Bloodstone, Blue jade, Brown jasper, Carnelian, Chrysocolla, Chrysoprase, Citrine, Dendritic agate, Fire agate, Fortification agate, Gray chalcedony, Lace agate, Lapis lazuli, Lavender jade, Milk quartz, Moonstone, Morion, Moss agate, Onyx, Pink jade, Plume agate, Prase, Pyrite, Rock crystal, Sardonyx, Sard, Schorl, Smoky quartz, Sunstone, Tiger iron, Tigereye, Tube agate, Turquoise, Variscite, White chalcedony, White jade, Yellow jasper

×3
Aventurine, Picture jasper, Rose quartz

×10
Amber opal, Bone opal, Cherry opal, Clear tourmaline, Gold opal, Jasper opal, Milk opal, Moss opal, Onyx opal, Pineapple opal, Pipe opal, Prase opal, Resin opal, Shell opal, Wax opal, Wood opal

×15
Fire opal, Jelly opal, Melanite, Pink tourmaline, Red tourmaline

×20
Alexandrite, Almandine, Amethyst, Aquamarine, Bandfire opal, Black pyrope, Black zircon, Brown zircon, Cat's eye, Chrysoberyl, Cinnamon grossular, Claro opal, Clear garnet, Crystal opal, Golden beryl, Goshenite, Green jade, Green tourmaline, Green zircon, Harlequin opal, Heliodor, Honey yellow beryl, Kunzite, Levin opal, Morganite, Peridot, Pinfire opal, Pink garnet, Precious fire opal, Purple spinel, Red beryl, Red flash opal, Red grossular, Red pyrope, Red spinel, Red zircon, Rhodolite, Rubicelle, Tanzanite, Topaz, Topazolite, Violet spessartine, White opal, Yellow grossular, Yellow spessartine, Yellow zircon

×25
Clear zircon, Indigo tourmaline

×30
Demantoid, Light yellow diamond, Blue garnet, Black opal, Tsavorite

×40
Faint yellow diamond, Emerald, Ruby, Sapphire

×60
Black diamond, Blue diamond, Clear diamond, Green diamond, Red diamond, Yellow diamond, Star ruby, Star sapphire

Metals

Multiplier
Metal

×2
Bismuth, Copper, Lead, Nickel, Tin, Zinc

×3
Lay pewter, Nickel silver

×4
Trifle pewter

×5
Bronze, Fine pewter

×6
Billon, Bismuth bronze

×7
Brass

×8
Sterling silver

×10
Iron, Pig iron, Silver

×11
Black bronze

×20
Electrum

×23
Rose gold

×30
Gold, Steel

×40
Aluminum, Platinum

×300
Adamantine

Creatures

Multiplier
Creature

×1
all creatures not listed below

×2
adder, beak dog, black bear, black mamba, bobcat, bushmaster, capybara, copperhead snake, cougar, coyote, dingo, elk, giant cave swallow, giant dingo, giant earthworm, giant mole, giant rat, helmet snake, hyena, ice wolf, jackal, king cobra, magma crab, molemarian, monitor lizard, muskox, ocelot, panda, python, rattlesnake, sloth bear, strangler, wolf, all giant variants of the creatures in this category

×3
alligator, anaconda, blind cave bear, cheetah, draltha, elk bird, fire imp, gila monster, green devourer, grizzly bear, jaguar, leopard, lion, lynx, polar bear, rutherer, saltwater crocodile, sasquatch, tiger, yeti, all giant variants of the creatures in this category

×4
cave crocodile, cave dragon, giant bat, giant cave spider, giant olm, giant cave toad, jabberer, unicorn, voracious cave crawler

×5
elephant, sea monster, sea serpent, giraffe, rhinoceros, all giant variants of the creatures in this category

×10
hydra

×15
dragon, roc

Plants

Multiplier
Plant

×1
hide root / , / kobold bulb / , / muck root / , / prickle berry / , / rat weed / , / sliver barb / , / whip vine / all / trees / and plant / seeds

×2
blade weed / , / bloated tuber / , / cave wheat / , / chicory / , / dimple cup / , / fisher berry / , / longland grass / , / pig tail / , / plump helmet / , / quarry bush / , / rope reed / , / sweet pod / , / strawberry / tuber beer ( / bloated tuber / drink)

×3
sun berry / whip wine ( / whip vine / drink)

×5
valley herb / quarry bush / leaf, rock nut oil ( / quarry bush / oil), rock nut soap ( / quarry bush / soap), sunshine ( / sun berry / drink)

×10
redroot dye (hide root powder)

×20
cave wheat flour (cave wheat powder), dimple dye (dimple cup powder), dwarven sugar (sweet pod powder), dwarven syrup (sweet pod extract), emerald dye (blade weed powder), longland flour (longland grass powder), sliver dye (sliver barb powder)

×25
whip vine flour (whip vine powder)

×100
gnomeblight (kobold bulb extract), golden salve (valley herb extract)

Note
Plants are made of various materials - the predominant material (usually STRUCTURAL) is listed for each individual plant, and other materials are listed separately when they differ.

Miscellaneous

Multiplier
Material

×1
Ash

×2
Amber, Coral, Coal, Lye

×3
Potash

×4
Pearlash

×10
Salt

## Quality

Item value is further increased by applying the quality multiplier and bonus.

|  |  |  |  |  |
|----|:---|:--:|----|----|
| **Designation** | **Description** | Value / Multiplier | Value / Bonus |  |
|  Item Name | —     | ×1  | +0 |  |
| -Item Name- | Well-crafted | ×1.1  | +3 |  |
| +Item Name+ | Finely-crafted | ×1.2  | +6 |  |
| \*Item Name\* | Superior quality | ×1.33  | +10 |  |
| ≡Item Name≡ | Exceptional | ×1.5  | +15 |  |
| ☼Item Name☼ | Masterful | ×2  | +30 |  |
| Unique Name | Artifact | ×20  | +300 |  |
