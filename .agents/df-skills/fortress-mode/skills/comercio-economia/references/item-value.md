# Item value

> Fonte: [Item value](https://dwarffortresswiki.org/index.php/Item_value) — Dwarf Fortress Wiki (GFDL/MIT)

**Item value** is determined by a number of factors: the form of the item, the material it is made out of, the quality of its creation, and any decorations on it.

The **final value** of an item is the **base value** of the form of the item (e.g. block *or* statue) multiplied by the **material multiplier** (e.g. granite *or* gold), multiplied by the **quality modifier** (e.g. fine *or* masterful) if any, then summed with the final value of all **decorations**.

# Base values of items

The **base value** of an item is determined by the form of the item, not what it is made out of. For example, a wood block uses the **base value** for a block; a native gold block uses the *same* **base value**, since it too is in the form of a "block". In both cases, the **final value** is then determined by adjusting the base value with the appropriate modifiers.

## Items without quality levels

| Base Value | Items |
|----|----|
| 0 | Body part, Corpse, Remains, small rock |
| 1 | glob, seed, alcohol, powder, extract |
| 2 | Fish, unprepared fish, Meat, Egg, Plant, Leaves |
| 3 | Gem (rough), Log, Stone |
| 5 | Bar, Block, Gem (cut), Leather |
| 6 | Thread |
| 10 | Ballista arrowhead, cheese, Honeycomb |
| Varies | live vermin, tame vermin |

## Items with quality levels

### Misc. items

| Base Value | Items |
|----|----|
| 1/50 | Coin¹ |
| 1 | Die, Orthopedic cast |
| 5 | Paper & Papyrus sheets |
| 7 | Cloth² |
| 10 | Animal trap, Altar, Amulet, Anvil, Armor stand, Backpack, Barrel, Bed, Bin, Book, Bookcase, Bowl, Box, Bracelet, Bucket, Cabinet, Cage, Chain, Chair, Cleaver, Coffin, Crown, Crutch, Decoration³, Display Case, Door, Earring, Figurine, Flask, Floodgate, Fork, Goblet/mug/cup, Grate, Hatch cover, Helve, Hive, Instrument *(non-main components)*, Jug, Knives, Ladle, Large gem, Large pot, Millstone, Mortar, Nest box, Pedestal, Pestle, Pipe section, Pouch, Prepared meal⁴, Quiver, Quern, Ring, Scepter, Scroll Roller, Slab, Stone axe, Splint, Table, Totem, Toy, Weapon rack |
| 20 | Quire/Scroll, Siege ammo, Traction bench |
| 25 | Window, Statue |
| 30 | Ballista part, Catapult part, Mechanism |
| 50 | Cauldron, Instrument *(main part)*, Minecart, Parchment sheet, Stepladder, Wheelbarrow |
| 200 | Parchment Quire/Scroll |
| *variable*⁵ | Weapon, Armor, Shoe, Shield, Helm, Glove, Ammo, Pants, Trap component *(see below)* |

*Notes*:

- 1\) Coins minted at a forge are always of base quality
- 2\) Goods made out of cloth get the following built in as decorations: the cloth (with quality mod) and the thread (without quality). Dyes are added separately (with quality), as a powder, not a decoration.
- 3\) "Decorations" include "It is decorated with \", "It is encircled with bands of \", "It is adorned with hanging rings of \", "This object menaces with spikes of \", "On this object is an image of \ in \", "It is studded with \". Decorations of bolts have a 1/3 base value instead.
- 4\) Prepared meals always have a base value of 10, with a quality modifier. Each ingredient is calculated separately, with its own base value and "minced" quality modifier. The total value of a meal stack is the sum of the above values multiplied by the total quantity, regardless of the proportion of ingredients. A more thorough explanation and example exists at the Cook page.
- 5\) These items have their value based on their properties - see categories below:

### Weapons

The base value of a melee weapon is (SIZE / 50) + 1; if the weapon has any EDGE attacks, its value is doubled. Ranged weapons simply have a value of 10.

{\| class="collapsible collapsed" style="border-spacing: 1"

\|- style=background-color:#ccf ! colspan=2\|Weapon values \|- style=text-align:left ! style=padding-right:1em\|Base Value ! Weapon \|- style="background-color: \#EEE" \|3\|\|Whip \|- \|7\|\|Training sword \|- style="background-color: \#EEE" \|9\|\|Training spear, War hammer \|- \|10\|\|Crossbow, Blowgun, Bow, Large dagger \|- style="background-color: \#EEE" \|11\|\|Flail \|- \|14\|\|Scourge, Scimitar, Short sword \|- style="background-color: \#EEE" \|17\|\|Training axe, Mace \|- \|18\|\|Spear \|- style="background-color: \#EEE" \|22\|\|Pick, Morningstar \|- \|27\|\|Maul \|- style="background-color: \#EEE" \|30\|\|Long sword \|- \|34\|\|Battle axe, Pike \|- style="background-color: \#EEE" \|38\|\|Two-handed sword \|- \|50\|\|Halberd \|- style="background-color: \#EEE" \|54\|\|Great axe \|}

#### Ammo

The base value of a single unit of ammo is (SIZE / 200) + 1.

{\| class="collapsible collapsed" style="border-spacing: 1"

\|- style=background-color:#ccf ! colspan=2\|Ammo values \|- style=text-align:left ! style=padding-right:1em\|Base Value ! Ammo \|- style="background-color: \#EEE" \|1 \|\|Blowdart, Bolt, Arrow \|} Value listed is for a single bolt, not stacks of bolts. Multiply the single value by the stack size for total value of a stack. (e.g. 1 bar of metal = stack of 25 bolts, etc.)

### Shields

The base value of a shield is (UPSTEP \* 3) + BLOCKCHANCE + 1.

- UPSTEP cannot be greater than 3
- BLOCKCHANCE cannot be greater than 100

{\| class="collapsible collapsed" style="border-spacing: 1"

\|- style=background-color:#ccf ! colspan=2\|Shield values \|- style=text-align:left ! style=padding-right:1em\|Base Value ! Shields \|- style="background-color: \#EEE" \| 14 \|\| Buckler \|- \| 27 \|\| Shield \|}

### Headwear

The base value of a helm is (LAYER_SIZE / 5) + (COVERAGE / 20) + 1.

- LAYER_SIZE and COVERAGE cannot be greater than 100

{\| class="collapsible collapsed" style="border-spacing: 1"

\|- style=background-color:#ccf ! colspan=2\|Helm values \|- style=text-align:left ! style=padding-right:1em\|Base Value ! Helm \|- style="background-color: \#EEE" \| 5 \|\| Cap, Head Veil, Face Veil, Headscarf \|- \| 7 \|\| Mask, Turban \|- style="background-color: \#EEE" \| 8 \|\| Hood \|- \| 12 \|\| Helm \|}

### Armor / torso

*(Note - When DF speaks of clothing, "armor" refers to anything worn on the torso, i.e. shirts, vests, togas, robes, etc., which all do provide some small protection, as well as breastplates and chain shirts. Combat-quality "armor" pieces are listed here by their location.)*

The base value of a piece of armor is ((UBSTEP + LBSTEP) \* 3) + (LAYER_SIZE / 5) + (COVERAGE / 10) + 1.

- UBSTEP and LBSTEP cannot be greater than 3
- LAYER_SIZE and COVERAGE cannot be greater than 100

{\| class="collapsible collapsed" style="border-spacing: 1"

\|- style=background-color:#ccf ! colspan=2\|Armor values \|- style=text-align:left ! style=padding-right:1em\|Base Value ! Armor \|- \| 8 \|\| Cape, Vest \|- style="background-color: \#EEE" \| 15 \|\| Breastplate \|- \| 16 \|\| Tunic \|- style="background-color: \#EEE" \| 20 \|\| Mail shirt \|- \| 21 \|\| Leather armor \|- style="background-color: \#EEE" \| 22 \|\| Shirt \|- \| 23 \|\| Toga \|- style="background-color: \#EEE" \| 26 \|\| Cloak \|- \| 27 \|\| Coat \|- style="background-color: \#EEE" \| 31 \|\| Dress \|- \| 33 \|\| Robe \|}

### Legwear

The base value of a pair of pants is (LBSTEP \* 3) + (LAYER_SIZE / 5) + (COVERAGE / 10) + 1

- LBSTEP cannot be greater than 3
- LAYER_SIZE and COVERAGE cannot be greater than 100

{\| class="collapsible collapsed" style="border-spacing: 1"

\|- style=background-color:#ccf ! colspan=2\|Pants values \|- style=text-align:left ! style=padding-right:1em\|Base Value ! Pants \|- style="background-color: \#EEE" \| 5 \|\| Thong \|- \| 8 \|\| Loincloth \|- style="background-color: \#EEE" \| 13 \|\| Short skirt \|- \| 16 \|\| Skirt, Braies \|- style="background-color: \#EEE" \| 22 \|\| Long skirt \|- \| 23 \|\| Trouser, Leggings, Greaves \|}

### Hand- & footwear

The base value of a shoe or glove is (UPSTEP \* 3) + (LAYER_SIZE / 5) + (COVERAGE / 30) + 1.

- UPSTEP cannot be greater than 3
- LAYER_SIZE and COVERAGE cannot be greater than 100

{\| class="collapsible collapsed" style="border-spacing: 1"

\|- style=background-color:#ccf ! colspan=2\|Glove values \|- style=text-align:left ! style=padding-right:1em\|Base Value ! Gloves \|- style="background-color: \#EEE" \| 6 \|\| Gloves \|- \| 7 \|\| Mittens \|- style="background-color: \#EEE" \| 11\* \|\| Gauntlets \|}

{\| class="collapsible collapsed" style="border-spacing: 1"

\|- style=background-color:#ccf ! colspan=2\|Shoe values \|- style=text-align:left ! style=padding-right:1em\|Base Value ! Shoes \|- style="background-color: \#EEE" \| 6 \|\| Socks \|- \| 8 \|\| Shoes \|- style="background-color: \#EEE" \| 9 \|\| Sandals, low boots\* \|- \| 12 \|\| High boots\* \|- style="background-color: \#EEE" \| 15 \|\| Chausses \|}

\* Gauntlets and boots are made 2 at a time from a single bar, effectively doubling the total value of the final items.

### Trap component

The base value of a trap component is ((SIZE / 50) + 1) \* HITS; if it has any EDGE attacks, its value is doubled.

{\| class="collapsible collapsed" style="border-spacing: 1"

\|- style=background-color:#ccf ! colspan=2\|Trap component values \|- style=text-align:left ! style=padding-right:1em\|Base Value ! Trap Component \|- style="background-color: \#EEE" \|66\|\|Giant axe blade, Enormous corkscrew, Menacing spike \|- style="background-color: \#EEE" \|126\|\|Large, serrated disc, Spiked ball \|- style="background-color: \#EEE" \|}

## Material multipliers

The material multiplier for an item is found from the \[MATERIAL_VALUE:#\] tag in the raws for the material it is made out of, and can be further augmented using \[MULTIPLY_VALUE:#\]. A wood block uses the same material multiplier as a wood log or a wooden chest - that is the material value for wood, which is 1.

| Stones |  |
|----|----|
| Multiplier | Stone |
| ×1 | Bismuthinite, Bituminous coal, Lignite, Common stone |
| ×2 | Cassiterite, Garnierite, Malachite, Native copper, Sphalerite, Calcite, Chalk, Dolomite, Limestone, Marble |
| ×3 | Tetrahedrite, Obsidian |
| ×5 | Galena |
| ×8 | Hematite, Limonite, Magnetite |
| ×10 | Horn silver, Native silver |
| ×30 | Native gold |
| ×40 | Native aluminum, Native platinum |
| ×250 | Raw adamantine |

| Gems |  |
|----|----|
| Multiplier | Gem |
| ×2 | Banded agate, Bloodstone, Blue jade, Brown jasper, Carnelian, Chrysocolla, Chrysoprase, Citrine, Dendritic agate, Fire agate, Fortification agate, Gray chalcedony, Lace agate, Lapis lazuli, Lavender jade, Milk quartz, Moonstone, Morion, Moss agate, Onyx, Pink jade, Plume agate, Prase, Pyrite, Rock crystal, Sard, Sardonyx, Schorl, Smoky quartz, Sunstone, Tiger iron, Tigereye, Tube agate, Turquoise, Variscite, White chalcedony, White jade, Yellow jasper |
| ×3 | Aventurine, Picture jasper, Rose quartz |
| ×10 | Amber opal, Bone opal, Cherry opal, Gold opal, Jasper opal, Milk opal, Moss opal, Onyx opal, Pineapple opal, Pipe opal, Prase opal, Resin opal, Shell opal, Wax opal, Wood opal, Clear tourmaline |
| ×15 | Fire opal, Jelly opal, Melanite, Pink tourmaline, Red tourmaline |
| ×20 | Alexandrite, Almandine, Amethyst, Aquamarine, Bandfire opal, Black pyrope, Black zircon, Brown zircon, Cat's eye, Chrysoberyl, Cinnamon grossular, Claro opal, Clear garnet, Crystal opal, Golden beryl, Goshenite, Green jade, Green tourmaline, Green zircon, Harlequin opal, Heliodor, Honey yellow beryl, Kunzite, Levin opal, Morganite, Peridot, Pinfire opal, Pink garnet, Precious fire opal, Purple spinel, Red beryl, Red flash opal, Red grossular, Red pyrope, Red spinel, Red zircon, Rhodolite, Rubicelle, Tanzanite, Topaz, Topazolite, Violet spessartine, White opal, Yellow grossular, Yellow spessartine, Yellow zircon |
| ×25 | Clear zircon, Indigo tourmaline |
| ×30 | Demantoid, Light yellow diamond, Blue garnet, Black opal, Tsavorite |
| ×40 | Faint yellow diamond, Emerald, Ruby, Sapphire |
| ×60 | Black diamond, Blue diamond, Clear diamond, Green diamond, Red diamond, Yellow diamond, Star ruby, Star sapphire |

| Metals |  |
|----|----|
| Multiplier | Metal |
| ×2 | Bismuth, Copper, Lead, Nickel, Tin, Zinc |
| ×3 | Lay pewter, Nickel silver |
| ×4 | Trifle pewter |
| ×5 | Bronze, Fine pewter |
| ×6 | Billon, Bismuth bronze |
| ×7 | Brass |
| ×8 | Sterling silver |
| ×10 | Iron, Pig iron, Silver |
| ×11 | Black bronze |
| ×20 | Electrum |
| ×23 | Rose gold |
| ×30 | Gold, Steel |
| ×40 | Aluminum, Platinum |
| ×300 | Adamantine |

| Animals |  |
|----|----|
| Multiplier | Animal |
| ×1 | all animals not listed below |
| ×2 | adder, beak dog, black bear, black mamba, bobcat, bushmaster, capybara, copperhead snake, cougar, coyote, dingo, elk, giant cave swallow, giant dingo, giant earthworm, giant mole, giant rat, helmet snake, hyena, ice wolf, jackal, king cobra, magma crab, molemarian, monitor lizard, muskox, ocelot, panda, python, rattlesnake, sloth bear, strangler, wolf, all giant variants of the creatures in this category |
| ×3 | alligator, anaconda, blind cave bear, cheetah, draltha, elk bird, fire imp, gila monster, green devourer, grizzly bear, jaguar, leopard, lion, lynx, polar bear, rutherer, saltwater crocodile, sasquatch, tiger, yeti, all giant variants of the creatures in this category |
| ×4 | cave crocodile, cave dragon, giant bat, giant cave spider, giant olm, giant cave toad, jabberer, unicorn, voracious cave crawler |
| ×5 | elephant, sea monster, sea serpent, giraffe, rhinoceros, all giant variants of the creatures in this category |
| ×10 | hydra |
| ×15 | dragon, roc |

[TABLE]

| Miscellaneous |  |
|----|----|
| Multiplier | Material |
| ×1 | Ash |
| ×2 | Amber, Coral, Coal, Green glass, Lye |
| ×3 | Potash, Earthenware |
| ×4 | Pearlash, Stoneware |
| ×5 | Clear glass |
| ×10 | Crystal glass, Porcelain, Salt |

## Quality

Item value is further increased by applying the quality multiplier.

[TABLE]
