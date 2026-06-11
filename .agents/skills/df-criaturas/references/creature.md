# Creature

> Fonte: [Creature](https://dwarffortresswiki.org/index.php/Creature) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

In *Dwarf Fortress*, a **creature** is defined as any animate, normally-mobile (and for the sake of this article, non-vermin) being that can interact with the world and any element inside it. The creatures in the game range from being entirely realistic to completely mythical. Although most creatures are animals, dwarves, giant cave spiders, and even megabeasts are all also considered creatures. Various creatures can and will interact with a fortress or adventurer in many different ways.

Some creatures have skills that match what type of creature they are (e.g. monkeys having legendary climbing skill). Though most creatures can be found in any mode, some are exclusive to adventure mode or fortress mode. Some creatures are randomly and procedurally generated, meaning they could have many different sprites in-game. Creatures of that type may have just one to a few sprites showcased out of many in the list below. A question-mark placeholder may also be shown instead. Also note that creatures with the [`[ARENA_RESTRICTED]`](/index.php/Creature_token#ARENA_RESTRICTED "Creature token") or [`[DOES_NOT_EXIST]`](/index.php/Creature_token#DOES_NOT_EXIST "Creature token") tokens cannot be spawned in the object testing arena, similarly to vermin (e.g. flies, worms).

Nearly all creatures in the game, including very large ones, take the space of a single tile, even if their sprites imply otherwise (wagons being the only exception). There are 670 creatures in the game. In adventure mode, creatures can have different labels to differentiate similar ones from historical figures. For example, a goblin may be labeled as a "white-haired goblin bowyer" while another would be a "high-cheekbones goblin bowyer".

## Spawning

Many creatures packed into one area, but in ASCII mode.

The creatures that will spawn on any given fortress map depend on the biome(s) that the fortress is in. Additionally, there are several creature tokens in the raws that deal with creature spawning:

- `[FREQUENCY:X]`: This tag dictates *how often* a creature will spawn. It ranges from 0-100, and is a comparative number, where the higher this number is, the more likely the creature is to spawn.
- `[CLUSTER_NUMBER:X]`: This determines *how many* creatures will appear at one time on a map.
- `[POPULATION_NUMBER:X]`: This determines the *total number* of this type of creature that can *ever* visit your fortress - the exact number varies, depending on the map.

For example, deer have a `[POPULATION_NUMBER:15:30]`, meaning that if you kill between 15-30 deer, no more deer will ever visit your fortress.

## Reading the Table

|  |  |  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|----|----|
| Graphic | Tile | Name | Playable | Hostile | Food Source | Adult Body Size | Pet Value (×) | Biome | Features |

The above columns indicate, in order:

- **Graphic:** The sprite assigned to the creature. Seen only in the premium version.
- **Tile:** The tile assigned to the creature, how you will see it without a graphic set.
- **Name:** The name of the creature as it displays in-game.
- **Playable:** If "No", the creature is not playable in any modes. "Fort" indicates that the creature is playable in fortress mode ([`[SITE_CONTROLLABLE]`](/index.php/Entity_token#SITE_CONTROLLABLE "Entity token")). "Adv" indicates that the creature is playable in adventure mode. All creatures except humans must have a population in an [`[ALL_MAIN_POPS_CONTROLLABLE]`](/index.php/Entity_token#ALL_MAIN_POPS_CONTROLLABLE "Entity token") civilization in order to be playable in adventure mode; goblins (and other creatures) cannot be played from a goblin civ. Humans can be played whether or not a population exists due to [`[OUTSIDER_CONTROLLABLE]`](/index.php/Creature_token#OUTSIDER_CONTROLLABLE "Creature token"), but an `[ALL_MAIN_POPS_CONTROLLABLE]` civ still needs to have existed at some point. Creatures with [`[LOCAL_POPS_CONTROLLABLE]`](/index.php/Creature_token#LOCAL_POPS_CONTROLLABLE "Creature token") are also playable in adventure mode.
- **Hostile:** If "Yes", then the creature will attack on sight,\[Verify\] if "No" then the creature is either neutral, or friendly - mindless undead creatures are always hostile to living things.
- **Food Source:** If "Yes", then the creature can be butchered into an edible substance that your dwarves will feed on.
- **Adult Body Size:** The average size of the creature when an adult. This can be anywhere from 500 for a rabbit, to 25,000,000 for a dragon. This value represents the creature's volume in cm3, which, for creatures made of flesh, more-or-less equals the creature's weight in grams.[1] These sizes do not correspond to the sizes which trigger pressure plates. Size is modified with height and broadness (i.e. incredibly skinny and short is below the average weight, while a fat and tall one is above it).
- **Pet Value:** This is the base value that the creature and its butchering products can be bought and sold for during trading.
- **Biome:** Where the creature can be found.
- **Features:** Any special features the creature possesses, including things such as causing a syndrome, breathing fire, or spinning webs.

Note: If you wish to view alternate ways of sorting creatures, such as sorting by biomes and location, or sorting domestic creatures by features, there is a new page found here: Alternate creature sorting

## Creatures

### Civilized

#### Main races

These are intelligent creatures that form the dominant civilized races of the world. While most are part of society, many have turned to banditry.

|  |  |  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|----|----|
| Graphic | Tile | Name | Playable | Hostile | Food Source | Adult Body Size | Pet Value (×) | Biome | Features |
|  | ☺ | Dwarf | Fort, Adv | No | No | 60,000 | Not tameable | Mountain halls, dwarf fortresses, hillocks | Trading race |
|  | e | Elf | Adv | Variable1 | No | 60,000 | Not tameable | Forest retreats | Trading race |
|  | U | Human | Adv | Variable1 | No | 70,000 | Not tameable | Towns and hamlets | Trading race |
|  | g | Goblin | Adv | Usually1 | No | 60,000 | Not tameable | Dark fortresses and dark pits | Snatchers2 |
|  | k | Kobold | Adv | Usually1 | No | 20,000 | Not tameable | Caves | Skulking race |

1. Whether or not you are hostile with select civilized races depends on the history of your game world, and its length. Shorter histories mean less ongoing wars and general hostility, good for a newer player to learn the basics.

2. Snatchers try to snatch children of other civilizations. Snatched individuals become part of the Snatcher's civilization.

#### Underground Tribes

Intelligent animal people that form crude civilizations underground, but will not trade with you. They wield some weapons and can join adventurers. They can also perform ambushes once the caverns are reached, depending on which creatures are hostile.

|  |  |  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|----|----|
| Graphic | Tile | Name | Playable | Hostile | Food Source | Adult Body Size | Pet Value (×) | Biome | Features |
|  | a | Amphibian man | No | Variable1 | No | 20,000 | Not tameable | Underground | Amphibious |
|  | a | Antman | No | Variable1 | No | Variable2 | Not tameable | Underground | Four castes |
|  | b | Bat man | Adv | Variable1 | No | 35,050 | Not tameable | Underground | Can fly |
|  | f | Cave fish man | Adv | Variable1 | No | 35,500 | Not tameable | Underground | Amphibious |
|  | s | Cave swallow man | Adv | Variable1 | No | 35,050 | Not tameable | Underground | Can fly |
|  | o | Olm man | Adv | Variable1 | No | 35,100 | Not tameable | Underground | Amphibious |
|  | r | Reptile man | No | Variable1 | No | 50,000 | Not tameable | Underground | Amphibious |
|  | r | Rodent man | No | Variable1 | No | 40,000 | Not tameable | Underground |  |
|  | s | Serpent man | No | Variable1 | No | 50,000 | Not tameable | Underground | Amphibious; Causes Syndrome |

1. Animal person civilizations initially encountered in the caverns will never be hostile, even if the game states otherwise. Those encountered in ambushes, however, will be aggressive.

2. Ant-men body sizes depend on their caste.

### Livestock and Domestic Animals

Creatures that have long been domesticated, and either play a part in the meat industry, or are simply pets to keep dwarves company. Note: Except for wagons, domestic animals can be bought at embark, or requested from dwarven caravans. Animals of these types below that are caught in the wild with cage traps can be tamed after only one session with an animal trainer.

|  |  |  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|----|----|
| Graphic | Tile | Name | Playable | Hostile | Food Source | Adult Body Size | Pet Value (×) | Biome | Features |
|  | a | Alpaca | No | No | Yes | 70,000 | 200 | N/A | Domestic, milkable and can be sheared |
|  | p | Blue peafowl | No | No | Yes | 4,000 | 10 | Tropical broadleaf forest | Domestic, lay eggs |
|  | c | Cat | No | No | Yes | 5,000 | 20 | N/A | Domestic |
|  | c | Cavy | No | No | No | 800 | 3 | Tropical savanna, grassland, and shrubland | Domestic |
|  | c | Chicken | No | No | Yes | 3,000 | 10 | N/A | Domestic, lays eggs |
|  | C | Cow | No | No | Yes | 600,000 | 300 | N/A | Domestic and milkable |
|  | d | Dog | No | No | Yes | 30,000 | 30 | N/A | Domestic and trainable |
|  | d | Duck | No | No | No | 1,000 | 10 | Any lakes and any wetland | Domestic, lays eggs |
|  | D | Donkey | No | No | Yes | 300,000 | 200 | N/A | Domestic, milkable, pack animal |
|  | g | Goat | No | No | Yes | 50,000 | 50 | N/A | Domestic and milkable |
|  | g | Goose | No | No | Yes | 4,500 | 10 | Temperate lakes and temperate marshes | Domestic, lays eggs |
|  | g | Guineafowl | No | No | No | 1,500 | 10 | N/A | Domestic, lays eggs |
|  | H | Horse | No | No | Yes | 500,000 | 200 | N/A | Domestic, milkable, wagon puller, pack animal |
|  | L | Llama | No | No | Yes | 180,000 | 200 | N/A | Domestic, milkable, pack animal and can be sheared |
|  | M | Mule | No | No | Yes | 400,000 | 200 | N/A | Domestic, pack animal |
|  | C | One-humped camel | No | No | Yes | 500,000 | 500 | Any desert | Domestic, milkable, pack animal |
|  | p | Pig | No | No | Yes | 60,000 | 100 | N/A | Domestic and milkable |
|  | r | Rabbit | No | No | No | 500 | 3 | Temperate savanna, grassland, and shrubland | Domestic |
|  | R | Reindeer | No | No | Yes | 130,000 | 200 | Tundra and taiga | Domestic and milkable |
|  | s | Sheep | No | No | Yes | 50,000 | 100 | N/A | Domestic, milkable and can be sheared |
|  | t | Turkey | No | No | Yes | 5,000 | 10 | Temperate forest, swamp and shrubland | Domestic, lays eggs |
|  | C | Two-humped camel | No | No | Yes | 500,000 | 500 | Any desert | Domestic, milkable, pack animal |
|  | W | Wagon | No | No | No | 12,000 | Not tameable |  | A special "creature" - see article |
|  | W | Water buffalo | No | No | Yes | 1,000,000 | 200 | Tropical wetland | Domestic, milkable, wagon puller, pack animal |
|  | Y | Yak | No | No | Yes | 700,000 | 200 | Mountains | Domestic, milkable, wagon puller, pack animal |

### Beasts and Monsters

All kinds of monstrous creatures that roam the land and underground caverns, including: semi-megabeasts, megabeasts, and randomly generated ones that can take any form. all very powerful and can easily be game-ending.

#### Semi-Megabeasts

|  |  |  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|----|----|
| Graphic | Tile | Name | Playable | Hostile | Food Source | Adult Body Size | Pet Value (×) | Biome | Features |
|  | C | Cyclops | No | Yes | No | 8,000,000 | Not tameable | All land | One eyed |
|  | E | Ettin | No | Yes | No | 8,000,000 | Not tameable | All land | Has two heads |
|  | G | Giant | No | Yes | No | 9,000,000 | Not tameable | All land |  |
|  | M | Minotaur | No | Yes | No | 220,000 | Not tameable | All land | Starts with combat skill |

#### Megabeasts

|  |  |  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|----|----|
| Graphic | Tile | Name | Playable | Hostile | Food Source | Adult Body Size | Pet Value (×) | Biome | Features |
|  | C | Bronze colossus | No | Yes | No | 20,000,000 | Not tameable | All land | Made of bronze, fairly hard to kill, drops masterwork bronze statue on death |
|  | D | Dragon | No | Yes | Yes | 25,000,000 | 10000 | All land | Breathes fire, trainable |
|  | H | Hydra | No | Yes | Yes | 8,000,000 | 10000 | All land | Has seven heads |
|  | R | Roc | No | Yes | Yes | 20,000,000 | 10000 | All land | Can fly, trainable |

#### Procedurally generated

These creatures are procedurally generated, and different for every savefile. Their raws may be extracted from the world.dat file in uncompressed save folders. Their sprite will appear as the closest resemblance to their randomly generated appearance, including their colors and design, such as having wings, trunks, tusks, etc. The animated sprites below are just a few possible sprites without custom colors added.

|  |  |  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|----|----|
| Graphic | Tile | Name | Playable | Hostile | Food Source | Adult Body Size | Pet Value (×) | Biome | Features |
|  | Any | Forgotten beast | No | Yes | Yes | 10,000,000 | Not tameable | All underground | See article for more information |
|  | Any | Titan | No | Yes | Yes | 10,000,000 | Not tameable | All above-ground | See article for more information |

### Wild Animals

This section includes wild animals, as well as their giant and humanoid counterparts. Wild animals are mostly found roaming the wilderness. Many of them are predators, while others are benign, and will not attack unless being attacked first. Some will be drawn to your stockpiles to steal drink, food or something shiny. Some can be easily overcome, and yet others can be significant threats, like the dreaded elephant.

#### Agitation

Disruption of the environment in a savage biome, such as woodcutting or fishing, may cause the appearance of "agitated" or "irritated" animals. Agitated animals will directly seek out and attack dwarves, instead of their normal behavior. Agitation rate and threshold can be adjusted in the difficulty settings. Agitation can be removed by taming animals captured in cage traps. With DFHack, it is possible to check current agitation status by executing the command `agitation-rebalance status`[2].

#### Above Ground

|  |  |  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|----|----|
| Graphic | Tile | Name | Playable | Hostile | Food Source | Adult Body Size | Pet Value (×) | Biome | Features |
|  | a | Aardvark | No | No | Yes | 50,000 | 50 | Tropical shrubland, tropical savanna, tropical grassland | Benign |
|  | a | Aardvark man | Adv | No | No | 60,000 | 50 | Tropical shrubland, tropical savanna, tropical grassland | Animal person, Benign |
|  | a | Adder | No | No | Yes | 150 | 50 | Temperate grassland, temperate savanna, temperate shrubland, any temperate forest, any temperate wetland | Lays eggs |
|  | a | Adder man | Adv | No | No | 35,075 | 50 | Temperate grassland, temperate savanna, temperate shrubland, any temperate forest, any temperate wetland | Animal person, Lays eggs |
|  | A | Alligator | No | Yes | Yes | 400,000 | 650 | Freshwater swamps, marshes, rivers | Amphibious |
|  | A | Anaconda | No | Yes | Yes | 100,000 | 200 | Any tropical swamp |  |
|  | A | Anaconda man | Adv | Yes | No | 85,000 | 200 | Any tropical swamp | Animal person |
|  | a | Anole man | Adv | Yes | No | 35,045 | n/a | Any tropical forest | Animal person |
|  | a | Armadillo | No | No | Yes | 7,500 | 20 | Tropical savanna, tropical grassland, tropical shrubland, any tropical forest | Benign |
|  | a | Armadillo man | Adv | No | No | 38,750 | 20 | Tropical savanna, tropical grassland, tropical shrubland, any tropical forest | Animal person, Benign |
|  | a | Aye-aye | No | No | Yes | 2,500 | 50 | Tropical dry broadleaf forest, tropical moist broadleaf forest | Benign |
|  | a | Aye-aye man | Adv | No | No | 36,250 | 50 | Tropical dry broadleaf forest, tropical moist broadleaf forest | Animal person, Benign |
|  | b | Badger | No | Yes | Yes | 15,000 | 25 | Taiga, any temperate savanna, grassland, shrubland, forest |  |
|  | b | Badger man | Adv | No | No | 42,500 | 25 | Taiga, any temperate forest, temperate shrubland, temperate savanna, temperate grassland | Animal person, Benign |
|  | s | Bark scorpion man | Adv | No | No | 35,001 | Not tameable | Any desert, tropical grassland, tropical savanna, tropical shrubland, tropical conifer forest | Animal person |
|  | b | Barn owl | No | No | Yes | 500 | 25 | Any wetland, any temperate forest, tropical conifer forest, tropical dry broadleaf forest, any shrubland, any savanna, any grassland, any desert | Lays eggs, Benign |
|  | b | Barn owl man | Adv | No | No | 35,250 | 25 | Any wetland, any temperate forest, tropical conifer forest, tropical dry broadleaf forest, any shrubland, any savanna, any grassland, any desert | Animal person, Lays eggs, Benign |
|  | B | Beak dog | No | Yes | Yes | 150,000 | 50 | Evil marshes | Can be mounted by goblins |
|  | b | Beetle man | Adv | Yes | No | 35,000 | n/a | Any non-freezing biome | Animal person |
|  | g | Bilou | No | No | Yes | 6,000 | 500 | Tropical broadleaf forest |  |
|  | B | Black bear | No | Yes | Yes | 120,000 | 300 | Taiga, temperate forest | Steals booze |
|  | B | Black bear man | Adv | Yes | No | 95,000 | n/a | Forest taiga, any temperate forest | Animal person |
|  | s | Black mamba | No | No | Yes | 5,000 | 50 | Tropical savanna, tropical shrubland, any tropical forest, any tropical swamp | Lays eggs |
|  | s | Black mamba man | Adv | No | No | 37,500 | 50 | Tropical savanna, tropical shrubland, any tropical forest, any tropical swamp | Animal person, Lays eggs |
|  | g | Black-crested gibbon | No | No | Yes | 6,000 | 500 | Tropical moist broadleaf forest | Benign |
|  | g | Black-handed gibbon | No | No | Yes | 6,000 | 500 | Tropical moist broadleaf forest | Benign |
|  | M | Blizzard man | No | Yes | No | 300,000 | Not tameable | Tundra, glacier |  |
|  | p | Blue peafowl | No | No | Yes | 4,000 | 10 | Tropical broadleaf forest | Domestic, lay eggs |
|  | b | Bluejay man | Adv | Yes | No | 35,050 | n/a | Temperate grassland, temperate savanna, temperate shrubland, temperate broadleaf forest, temperate conifer forest | Animal person |
|  | b | Bobcat | No | No | Yes | 8,000 | 75 | Any forest, any desert, tropical freshwater swamp, tropical saltwater swamp, temperate freshwater swamp, temperate saltwater swamp, mangrove swamp, mountain |  |
|  | b | Bobcat man | Adv | No | No | 39,000 | 75 | Any forest, any desert, tropical freshwater swamp, tropical saltwater swamp, temperate freshwater swamp, temperate saltwater swamp, mangrove swamp, mountain | Animal person |
|  | b | Bonobo | No | No | Yes | 50,000 | 500 | Tropical broadleaf forest, shrubland |  |
|  | s | Brown recluse spider man | Adv | No | No | 35,000 | Not tameable | Temperate broadleaf forest | Animal person |
|  | s | Bushmaster | No | No | Yes | 8,500 | 50 | Tropical moist broadleaf forest | Lays eggs |
|  | s | Bushmaster man | Adv | No | No | 39,250 | 50 | Tropical moist broadleaf forest | Animal person, Lays eggs |
|  | b | Bushtit man | Adv | No | No | 35,002 | 30 | Any temperate forest | Animal person, Lays eggs, Benign |
|  | b | Buzzard | No | Yes | Yes | 1,400 | 30 | Any desert, temperate grassland, savanna, marsh | Steals food, lays eggs |
|  | b | Buzzard man | Adv | Yes | No | 35,700 | n/a | Temperate freshwater marsh, temperate saltwater marsh, temperate grassland, temperate savanna, any desert | Animal person, lays eggs |
|  | c | Capuchin | No | No | Yes | 3,500 | 50 | Any tropical forest, mangrove swamp |  |
|  | c | Capuchin man | Adv | No | Yes | 36,750 | 50 | Any tropical forest, mangrove swamp | Animal person |
|  | c | Capybara | No | No | Yes | 45,000 | 100 | Any wetland | Makes sounds in Adventure mode |
|  | c | Capybara man | Adv | No | Yes | 57,499 | 100 | Any wetland | Animal person |
|  | c | Cardinal man | Adv | Yes | No | 35,025 | n/a | temperate grassland, temperate savanna, temperate shrubland, temperate broadleaf forest, temperate conifer forest | Animal person |
|  | c | Cassowary | No | No | Yes | 50,000 | 100 | Tropical moist broadleaf forest | Lays eggs, Benign |
|  | c | Cassowary man | Adv | No | Yes | 60,000 | 100 | Tropical moist broadleaf forest | Animal person, Lays eggs, Benign |
|  | c | Cavy | No | No | No | 800 | 3 | Tropical savanna, grassland, shrubland | Domestic |
|  | c | Chameleon man | Adv | Yes | No | 35,075 | n/a | Any tropical forest, shrubland tropical, savanna tropical, any desert | Animal person |
|  | c | Cheetah | No | Yes | Yes | 50,000 | 200 | Tropical savanna, grassland, shrubland |  |
|  | c | Cheetah man | Adv | Yes | No | 60,000 | n/a | tropical savanna, tropical grassland, tropical shrubland | Animal person |
|  | c | Chimpanzee | No | No | Yes | 50,000 | 500 | Tropical broadleaf forest, shrubland |  |
|  | c | Chinchilla | No | No | Yes | 500 | 3 | Mountain | Benign |
|  | c | Chinchilla man | Adv | No | Yes | 35,250 | 3 | Mountain | Animal person, Benign |
|  | c | Chipmunk man | Adv | Yes | No | 35,150 | n/a | Any temperate forest | Animal person |
|  | c | Coati | No | No | Yes | 6,000 | 50 | Any temperate forest, any tropical forest |  |
|  | c | Coati man | Adv | No | Yes | 38,000 | 50 | Any temperate forest, any tropical forest | Animal person |
|  | c | Cockatiel man | Adv | No | No | 35,045 | 30 | Any desert, temperate grassland | Animal person, Lays eggs, Benign |
|  | s | Copperhead snake | No | No | Yes | 500 | 50 | Temperate broadleaf forest, any temperate swamp |  |
|  | s | Copperhead snake man | Adv | No | Yes | 35,250 | 50 | Temperate broadleaf forest, any temperate swamp | Animal person |
|  | c | Cougar | No | Yes | Yes | 60,000 | 100 | Any forest, any shrubland |  |
|  | c | Cougar man | Adv | Yes | No | 65,000 | n/a | Any temperate forest, any tropical forest, temperate shrubland, tropical shrubland | Animal person |
|  | c | Coyote | No | No | Yes | 15,000 | 50 | Mountain, tundra, taiga, any temperate forest, temperate savanna, temperate grassland, temperate shrubland, any temperate wetland, any desert |  |
|  | c | Coyote man | Adv | No | Yes | 42,500 | 50 | Mountain, tundra, taiga, any temperate forest, temperate savanna, temperate grassland, temperate shrubland, any temperate wetland, any desert | Animal person |
|  | c | Crow man | Adv | No | No | 35,250 | 10 | Temperate grassland, temperate savanna, temperate shrubland, taiga, any temperate forest, any temperate wetland | Animal person, Lays eggs, Benign |
|  | g | Dark gnome | No | Yes | No | 15,000 | Not tameable | Evil mountain | Steals booze |
|  | D | Deer | No | No | Yes | 140,000 | 50 | Taiga, temperate forest | Benign |
|  | d | Deer man | Adv | Yes | No | 105,000 | n/a | Forest taiga, any temperate forest | Animal person |
|  | t | Desert tortoise | No | No | Yes | 5,500 | 50 | Any desert | Lays eggs, Benign |
|  | t | Desert tortoise man | Adv | No | Yes | 37,750 | 50 | Any desert | Animal person, Lays eggs, Benign |
|  | d | Dingo | No | Yes | Yes | 20,000 | 50 | Any non-freezing biome |  |
|  | d | Dingo man | Adv | Yes | Yes | 45,000 | 50 | Any non-freezing biome | Animal person |
|  | d | Duck | No | No | No | 1,000 | 10 | Any lakes, any wetland | Domestic, lay eggs |
|  | e | Eagle | No | No | Yes | 4,000 | 25 | Any wetland, any forest, any shrubland, any savanna, any grassland, any desert, mountain, tundra | Lays eggs, Benign |
|  | e | Eagle man | Adv | No | Yes | 37,000 | 25 | Any wetland, any forest, any shrubland, any savanna, any grassland, any desert, mountain, tundra | Animal person, Lays eggs, Benign |
|  | e | Echidna | No | No | Yes | 10,000 | 50 | Any temperate forest, temperate shrubland, temperate savanna, temperate grassland, any desert | Lays eggs, Benign |
|  | e | Echidna man | Adv | No | Yes | 40,000 | 50 | Any temperate forest, temperate shrubland, temperate savanna, temperate grassland, any desert | Animal person, Lays eggs, Benign |
|  | E | Elephant | No | No | Yes | 5,000,000 | 500 | Tropical forest, shrubland | Trainable |
|  | E | Elephant man | Adv | Yes | No | 2,535,000 | n/a | Any tropical forest, shrubland tropical | Animal person |
|  | E | Elk | No | No | Yes | 300,000 | 100 | Tundra, temperate grassland |  |
|  | E | Elk man | Adv | Yes | No | 185,000 | n/a | Tundra, temperate grassland | Animal person |
|  | E | Emu | No | No | Yes | 35,000 | 100 | Temperate shrubland, any temperate forest | Lays eggs, Benign |
|  | E | Emu man | Adv | No | Yes | 52,500 | 100 | Temperate shrubland, any temperate forest | Animal person, Lays eggs, Benign |
|  | f | Firefly man | Adv | Yes | No | 35,000 | n/a | Any non-freezing biome | Animal person |
|  | f | Fly man | Adv | Yes | No | 35,000 | n/a | Any non-freezing biome, any pool |  |
|  | s | Flying squirrel man | Adv | No | No | 35,100 | 10 | Any temperate forest | Animal person, Benign |
|  | b | Foul blendec | No | Yes | No | 60,000 | 250 | Most evil forest |  |
|  | f | Fox | No | No | Yes | 6,000 | 25 | Taiga, temperate forest |  |
|  | f | Fox man | Adv | Yes | No | 38,000 | n/a | Forest taiga, any temperate forest | Animal person |
|  | g | Gazelle | No | No | Yes | 20,000 | 50 | Tropical savanna, grassland |  |
|  | g | Gazelle man | Adv | Yes | No | 45,000 | n/a | Tropical savanna, tropical grassland |  |
|  | A | Giant aardvark | No | No | Yes | 560,000 | 500 | Tropical shrubland, tropical savanna, tropical grassland | Benign |
|  | A | Giant adder | No | No | Yes | 201,049 | 500 | Temperate grassland, temperate savanna, temperate shrubland, any temperate forest, any temperate wetland | Lays eggs |
|  | A | Giant anaconda | No | Yes | Yes | 933,000 | 500 | Any tropical swamp |  |
|  | A | Giant anole | No | Yes | Yes | 200,629 | 500 | Any tropical forest |  |
|  | A | Giant armadillo | No | No | Yes | 252,750 | 1000 | Tropical savanna, tropical grassland, tropical shrubland, any tropical forest | Benign |
|  | A | Giant aye-aye | No | No | Yes | 217,525 | 500 | Tropical dry broadleaf forest, tropical moist broadleaf forest | Benign |
|  | B | Giant badger | No | No | Yes | 306,000 | 500 | Taiga, any temperate forest, temperate shrubland, temperate savanna, temperate grassland | Benign |
|  | S | Giant bark scorpion | No | No | No | 200,021 | 500 | Any desert, tropical grassland, tropical savanna, tropical shrubland, tropical conifer forest |  |
|  | B | Giant barn owl | No | No | Yes | 203,500 | 500 | Any wetland, any temperate forest, tropical conifer forest, tropical dry broadleaf forest, any shrubland, any savanna, any grassland, any desert | Lays eggs, Benign |
|  | B | Giant beetle | No | Yes | Yes | 200,007 | 500 | Any non-freezing biome |  |
|  | B | Giant black bear | No | Yes | Yes | 1,084,800 | 500 | Forest taiga, any temperate forest |  |
|  | S | Giant black mamba | No | No | Yes | 235,100 | 500 | Tropical savanna, tropical shrubland, any tropical forest, any tropical swamp | Lays eggs |
|  | B | Giant bluejay | No | Yes | Yes | 200,700 | 500 | Temperate grassland, temperate savanna, temperate shrubland, temperate broadleaf forest, temperate conifer forest |  |
|  | B | Giant bobcat | No | No | Yes | 256,320 | 500 | Any forest, any desert, tropical freshwater swamp, tropical saltwater swamp, temperate freshwater swamp, temperate saltwater swamp, mangrove swamp, mountain |  |
|  | S | Giant brown recluse spider | No | No | No | 200,007 | 500 | Temperate broadleaf forest |  |
|  | S | Giant bushmaster | No | No | Yes | 259,845 | 500 | Tropical moist broadleaf forest | Lays eggs |
|  | B | Giant bushtit | No | No | No | 200,035 | 500 | Any temperate forest | Lays eggs, Benign |
|  | B | Giant buzzard | No | Yes | Yes | 209,804 | 500 | Temperate freshwater marsh, temperate saltwater marsh, temperate grassland, temperate savanna, any desert |  |
|  | C | Giant capuchin | No | No | Yes | 224,560 | 500 | Any tropical forest, mangrove swamp |  |
|  | C | Giant capybara | No | No | Yes | 523,350 | 500 | Any wetland | Makes sounds in Adventure mode |
|  | C | Giant cardinal | No | Yes | Yes | 200,350 | 500 | Temperate grassland, temperate savanna, temperate shrubland, temperate broadleaf forest, temperate conifer forest |  |
|  | C | Giant cassowary | No | No | Yes | 560,000 | 500 | Tropical moist broadleaf forest | Lays eggs, Benign |
|  | C | Giant chameleon | No | Yes | Yes | 201,049 | 500 | Any tropical forest, shrubland tropical, savanna tropical, any desert |  |
|  | C | Giant cheetah | No | Yes | Yes | 560,000 | 500 | Tropical savanna, grassland, shrubland | Trainable |
|  | C | Giant chinchilla | No | No | Yes | 203,500 | 500 | Mountain | Benign |
|  | C | Giant chipmunk | No | Yes | Yes | 202,101 | 500 | Any temperate forest |  |
|  | C | Giant coati | No | No | Yes | 242,160 | 500 | Any temperate forest, any tropical forest |  |
|  | C | Giant cockatiel | No | No | No | 200,629 | 500 | Any desert, temperate grassland | Lays eggs, Benign |
|  | S | Giant copperhead snake | No | No | Yes | 203,500 | 500 | Temperate broadleaf forest, any temperate swamp |  |
|  | C | Giant cougar | No | Yes | Yes | 633,600 | 500 | Any temperate forest, any tropical forest, shrubland temperate, shrubland tropical |  |
|  | C | Giant coyote | No | No | Yes | 306,000 | 500 | Mountain, tundra, taiga, any temperate forest, temperate savanna, temperate grassland, temperate shrubland, any temperate wetland, any desert |  |
|  | C | Giant crow | No | No | No | 203,500 | 500 | Temperate grassland, temperate savanna, temperate shrubland, taiga, any temperate forest, any temperate wetland | Lays eggs, Benign |
|  | D | Giant deer | No | Yes | Yes | 1,237,600 | 500 | Forest taiga, any temperate forest |  |
|  | S | Giant desert scorpion | No | Yes | Yes | 200,000 | 2500 | Savage desert | No pain, no stun, no emotion; deadly Syndrome. **No longer exists past 0.42.06.** |
|  | T | Giant desert tortoise | No | No | Yes | 238,645 | 500 | Any desert | Lays eggs, Benign |
|  | D | Giant dingo | No | Yes | Yes | 341,800 | 500 | Any non-freezing biome |  |
|  | E | Giant eagle | No | Yes | Yes | 228,040 | 500 | Savage mountain | Trainable |
|  | E | Giant echidna | No | No | Yes | 270,500 | 500 | Any temperate forest, temperate shrubland, temperate savanna, temperate grassland, any desert | Lays eggs, Benign |
|  | E | Giant elephant | No | Yes | Yes | 40,000,000 | 500 | Any tropical forest, tropical shrubland |  |
|  | E | Giant elk | No | Yes | Yes | 2,478,000 | 500 | Tundra, temperate grassland |  |
|  | E | Giant emu | No | No | Yes | 450,100 | 500 | Temperate shrubland, any temperate forest | Lays eggs, Benign |
|  | F | Giant firefly | No | Yes | Yes | 200,007 | 500 | Any non-freezing biome |  |
|  | F | Giant fly | No | Yes | Yes | 200,007 | 500 | Any non-freezing biome, any pool |  |
|  | S | Giant flying squirrel | No | No | No | 201,400 | 500 | Any temperate forest | Benign |
|  | F | Giant fox | No | Yes | Yes | 242,160 | 500 | Forest taiga, any temperate forest |  |
|  | G | Giant gazelle | No | Yes | Yes | 341,800 | 500 | savanna tropical, grassland tropical |  |
|  | G | Giant gila monster | No | No | Yes | 214,020 | 500 | Any desert | Lays eggs |
|  | G | Giant giraffe | No | Yes | Yes | 8,030,000 | 500 | tropical savanna, tropical shrubland |  |
|  | G | Giant grackle | No | Yes | Yes | 200,840 | 500 | temperate grassland, temperate savanna |  |
|  | G | Giant grasshopper | No | No | No | 200,007 | 500 | Any non-freezing biome | Benign |
|  | L | Giant gray langur | No | No | Yes | 306,000 | 500 | Any desert, any grassland, any savanna, any shrubland, any forest |  |
|  | S | Giant gray squirrel | No | Yes | Yes | 202,101 | 500 | Any temperate forest |  |
|  | O | Giant great horned owl | No | No | Yes | 214,020 | 500 | Any forest, any shrubland, any savanna, any grassland, any desert, mangrove swamp, mountain, tundra | Lays eggs |
|  | F | Giant green tree frog | No | No | No | 200,700 | 500 | Temperate freshwater pool, temperate freshwater lake, temperate freshwater swamp, temperate freshwater marsh | Benign |
|  | P | Giant grey parrot | No | No | Yes | 202,800 | 500 | Tropical moist broadleaf forest | Lays eggs, Benign |
|  | B | Giant grizzly bear | No | Yes | Yes | 1,700,000 | 500 | Forest taiga, any temperate forest |  |
|  | G | Giant groundhog | No | Yes | Yes | 221,040 | 500 | Temperate shrubland, temperate savanna, temperate grassland |  |
|  | H | Giant hamster | No | No | No | 201,049 | 500 | Any non-freezing biome | Benign |
|  | H | Giant hare | No | No | Yes | 224,560 | 500 | Temperate savanna, temperate grassland | Benign |
|  | H | Giant hedgehog | No | No | No | 205,600 | 500 | Temperate shrubland, temperate savanna | Benign |
|  | H | Giant hippo | No | Yes | Yes | 12,030,000 | 500 | tropical saltwater river, tropical brackishwater river, tropical freshwater river, tropical saltwater lake, tropical brackishwater lake, tropical freshwater lake |  |
|  | M | Giant hoary marmot | No | Yes | Yes | 270,500 | 500 | Mountain |  |
|  | B | Giant honey badger | No | Yes | Yes | 298,900 | 500 | Any tropical forest, tropical shrubland, tropical savanna, tropical grassland, any tropical wetland, any desert |  |
|  | H | Giant hornbill | No | No | Yes | 217,525 | 500 | Any tropical forest | Lays eggs, Benign |
|  | H | Giant hyena | No | Yes | Yes | 633,600 | 500 | Tropical savanna, tropical grassland, tropical shrubland |  |
|  | I | Giant ibex | No | No | Yes | 560,000 | 500 | Any grassland, any desert | Benign |
|  | I | Giant iguana | No | Yes | Yes | 228,040 | 500 | Any tropical forest |  |
|  | I | Giant impala | No | No | Yes | 560,000 | 500 | Tropical savanna, tropical grassland | Benign |
|  | J | Giant jackal | No | No | Yes | 306,000 | 500 | Tropical shrubland, tropical savanna, tropical grassland |  |
|  | J | Giant jaguar | No | Yes | Yes | 745,500 | 500 | Savage tropical areas, any desert | Trainable |
|  | J | Giant jumping spider | No | No | No | 200,007 | 500 | Any non-freezing biome |  |
|  | K | Giant kakapo | No | No | Yes | 221,040 | 500 | Temperate shrubland, temperate savanna, temperate grassland, any temperate forest | Lays eggs, Benign |
|  | K | Giant kangaroo | No | No | Yes | 857,700 | 500 | Temperate grassland, temperate savanna, temperate shrubland, any desert | Benign |
|  | K | Giant kea | No | No | Yes | 207,010 | 500 | Any temperate forest, temperate shrubland, mountain | Lays eggs |
|  | K | Giant kestrel | No | No | Yes | 201,750 | 500 | Tropical freshwater marsh, tropical saltwater marsh, temperate freshwater marsh, temperate saltwater marsh, any shrubland, any savanna, any grassland | Lays eggs, Benign |
|  | K | Giant king cobra | No | No | Yes | 242,160 | 500 | Any tropical forest | Lays eggs |
|  | K | Giant kingsnake | No | No | Yes | 210,510 | 500 | Any temperate forest, temperate shrubland, mountain, any desert | Lays eggs |
|  | K | Giant kiwi | No | No | Yes | 217,525 | 1000 | Any temperate forest, temperate shrubland | Lays eggs, Benign |
|  | K | Giant koala | No | No | Yes | 270,500 | 500 | Temperate broadleaf forest | Benign |
|  | L | Giant leopard | No | Yes | Yes | 560,000 | 500 | Savage tropical areas, any desert | Trainable |
|  | G | Giant leopard gecko | No | No | No | 200,350 | 500 | Any desert |  |
|  | L | Giant lion | No | Yes | Yes | 1,700,000 | 500 | Tropical savanna, Tropical grassland, Tropical shrubland | Trainable |
|  | L | Giant lion tamarin | No | No | No | 204,302 | 500 | Tropical moist broadleaf forest | Benign |
|  | L | Giant lizard | No | Yes | Yes | 201,400 | 500 | Any non-freezing biome |  |
|  | L | Giant lorikeet | No | No | No | 201,400 | 500 | Tropical moist broadleaf forest, mangrove swamp | Lays eggs, Benign |
|  | L | Giant louse | No | No | No | 200,007 | 500 | Any non-freezing biome |  |
|  | L | Giant lynx | No | No | Yes | 377,750 | 500 | Taiga |  |
|  | M | Giant magpie | No | No | No | 201,400 | 500 | Temperate grassland, temperate savanna, temperate shrubland | Lays eggs, Benign |
|  | M | Giant mandrill | No | Yes | Yes | 341,800 | 500 | Tropical moist broadleaf forest |  |
|  | M | Giant mantis | No | No | No | 200,007 | 500 | Any non-freezing biome |  |
|  | L | Giant masked lovebird | No | No | No | 200,629 | 500 | Any tropical forest | Lays eggs |
|  | B | Giant monarch butterfly | No | Yes | Yes | 200,007 | 500 | Any non-freezing biome |  |
|  | M | Giant mongoose | No | No | Yes | 221,040 | 500 | Tropical savanna, tropical shrubland | Benign |
|  | M | Giant monitor lizard | No | No | Yes | 933,000 | 500 | Tropical grassland, tropical savanna, tropical shrubland, any tropical forest | Lays eggs |
|  | M | Giant moose | No | No | Yes | 4,257,750 | 1000 | Taiga, any temperate forest | Benign |
|  | M | Giant mosquito | No | No | No | 200,007 | 500 | Any non-freezing biome, any pool |  |
|  | M | Giant moth | No | No | No | 200,007 | 500 | Any non-freezing biome | Benign |
|  | G | Giant mountain goat | No | Yes | Yes | 560,000 | 500 | Mountain |  |
|  | M | Giant muskox | No | Yes | Yes | 2,362,650 | 500 | Tundra, temperate grassland |  |
|  | O | Giant ocelot | No | No | Yes | 377,750 | 500 | Any tropical forest, mangrove swamp, tropical savanna, tropical grassland |  |
|  | C | Giant one-humped camel | No | Yes | Yes | 4,055,000 | 500 | any desert |  |
|  | O | Giant opossum | No | No | Yes | 221,040 | 500 | Any temperate forest, temperate shrubland, temperate savanna, temperate grassland | Benign |
|  | O | Giant oriole | No | Yes | Yes | 200,280 | 500 | Temperate broadleaf forest |  |
|  | O | Giant osprey | No | No | Yes | 214,020 | 500 | Any ocean, any lake, any river, tropical freshwater marsh, tropical saltwater marsh, temperate freshwater marsh, temperate saltwater marsh | Lays eggs, Benign |
|  | O | Giant ostrich | No | No | Yes | 857,700 | 1000 | Tropical savanna, tropical grassland, any desert | Lays eggs, Benign |
|  | P | Giant pangolin | No | No | Yes | 235,100 | 500 | Tropical grassland, tropical savanna, tropical shrubland, any tropical forest | Benign |
|  | P | Giant parakeet | No | No | No | 200,840 | 500 | Tropical grassland, tropical savanna, tropical shrubland, any tropical forest | Lays eggs, Benign |
|  | L | Giant peach-faced lovebird | No | No | No | 200,419 | 500 | Temperate grassland, temperate savanna, temperate shrubland, temperate broadleaf forest | Lays eggs |
|  | P | Giant peregrine falcon | No | No | Yes | 113,292 | 500 | Any wetland, any temperate forest, tropical conifer forest, tropical dry broadleaf forest, taiga, any shrubland, any savanna, any grassland, any desert, mountain, tundra | Lays eggs, Benign |
|  | B | Giant polar bear | No | Yes | Yes | 3,268,000 | 500 | Glacier, tundra |  |
|  | P | Giant porcupine | No | No | Yes | 263,430 | 500 | Temperate shrubland, temperate savanna, temperate grassland, temperate conifer forest, taiga, any desert, tundra | Benign |
|  | S | Giant python | No | No | Yes | 1,700,000 | 500 | Tropical moist broadleaf forest | Lays eggs |
|  | R | Giant raccoon | No | Yes | Yes | 249,270 | 500 | Taiga forest, any temperate forest |  |
|  | S | Giant rattlesnake | No | No | Yes | 249,270 | 500 | Any non-freezing biome |  |
|  | R | Giant raven | No | No | No | 208,403 | 500 | Temperate grassland, temperate savanna, temperate shrubland, taiga, any temperate forest, any temperate wetland, tundra, any desert | Lays eggs, Benign |
|  | P | Giant red panda | No | No | Yes | 235,100 | 500 | Any temperate forest | Benign |
|  | S | Giant red squirrel | No | Yes | Yes | 202,101 | 500 | Any temperate forest |  |
|  | M | Giant rhesus macaque | No | Yes | Yes | 235,100 | 500 | Shrubland temperate, savanna temperate, grassland temperate |  |
|  | R | Giant rhinoceros | No | Yes | Yes | 24,000,000 | 500 | Grassland tropical, savanna tropical, shrubland tropical |  |
|  | R | Giant roach | No | Yes | Yes | 200,007 | 500 | Any non-freezing biome |  |
|  | S | Giant skink | No | Yes | Yes | 203,500 | 500 | Any temperate, any tropical, any desert |  |
|  | S | Giant skunk | No | No | Yes | 228,040 | 500 | Any temperate forest, temperate shrubland, temperate savanna, temperate grassland | Benign |
|  | S | Giant sloth | No | No | Yes | 242,160 | 500 | Any tropical forest | Benign |
|  | B | Giant sloth bear | No | No | Yes | 933,000 | 500 | Any tropical forest |  |
|  | S | Giant slug | No | No | No | 200,007 | 500 | Any non-freezing biome | Benign |
|  | S | Giant snail | No | No | No | 200,007 | 500 | Any non-freezing biome | Benign |
|  | O | Giant snowy owl | No | No | Yes | 214,020 | 500 | Tundra | Lays eggs, Benign |
|  | S | Giant sparrow | No | No | No | 200,210 | 500 | Any grassland, any savanna, any shrubland, any temperate forest, any tropical forest, any desert, any wetland | Lays eggs, Benign |
|  | M | Giant spider monkey | No | No | Yes | 259,845 | 500 | Tropical moist broadleaf forest, tropical dry broadleaf forest | Benign |
|  | S | Giant stoat | No | No | Yes | 202,450 | 500 | Taiga, tundra | Benign |
|  | S | Giant swan | No | No | Yes | 270,500 | 500 | Any temperate lake, any temperate marsh | Lays eggs, Benign |
|  | T | Giant tapir | No | No | Yes | 1,700,000 | 500 | Tropical moist broadleaf forest | Benign |
|  | T | Giant thrips | No | No | No | 200,007 | 500 | Any non-freezing biome | Benign |
|  | T | Giant tick | No | No | No | 200,007 | 500 | Any non-freezing biome |  |
|  | T | Giant tiger | No | Yes | Yes | 1,894,500 | 500 | Some savage tropical areas | Trainable |
|  | T | Giant tortoise | No | No | Yes | 300,000 | 50 | Tropical shrubland, tropical savanna | Lays eggs, Benign |
|  | T | Giant tortoise man | Adv | No | Yes | 185,000 | 50 | Tropical shrubland, tropical savanna | Animal person, Lays eggs, Benign |
|  | C | Giant two-humped camel | No | Yes | Yes | 4,055,000 | 500 | any desert |  |
|  | V | Giant vulture | No | Yes | Yes | 263,430 | 500 | Grassland tropical, savanna tropical, any desert |  |
|  | W | Giant warthog | No | Yes | Yes | 933,000 | 500 | Savanna tropical, grassland tropical, shrubland tropical |  |
|  | W | Giant weasel | No | No | Yes | 201,400 | 500 | Any land | Benign |
|  | S | Giant white stork | No | No | Yes | 221,040 | 500 | Any grassland, any wetland | Lays eggs, Benign |
|  | B | Giant wild boar | No | No | Yes | 783,199 | 500 | Any savanna, any grassland, any shrubland, any forest, any wetland | Benign |
|  | W | Giant wolf | No | Yes | Yes | 486,800 | 500 | Tundra, forest taiga, any temperate forest, shrubland temperate |  |
|  | W | Giant wolverine | No | No | Yes | 341,800 | 500 | Taiga, mountain | Benign |
|  | W | Giant wombat | No | No | Yes | 377,750 | 500 | Any temperate forest, temperate shrubland, mountain | Benign |
|  | W | Giant wren | No | No | No | 200,280 | 500 | Any forest, any grassland, any savanna, any shrubland, any wetland, any desert | Lays eggs, Benign |
|  | P | Gigantic panda | No | No | Yes | 1,160,900 | 1000 | Temperate forest | Trainable |
|  | T | Gigantic tortoise | No | No | Yes | 2,478,000 | 1500 | Tropical shrubland, tropical savanna | Lays eggs, Benign |
|  | g | Gila monster | No | No | Yes | 2,000 | 50 | Any desert | Lays eggs |
|  | g | Gila monster man | Adv | No | Yes | 36,000 | 50 | Any desert | Animal person, Lays eggs |
|  | G | Giraffe | No | No | Yes | 1,000,000 | 500 | Tropical savanna, shrubland |  |
|  | G | Giraffe man | Adv | Yes | No | 535,000 | n/a | Savanna tropical, shrubland tropical | Animal person |
|  | g | Goose | No | No | Yes | 4,500 | 10 | Temperate lakes, temperate marshes | Domestic, lay eggs |
|  | G | Gorilla | No | No | Yes | 150,000 | 500 | Tropical broadleaf forest, swamp | Trainable |
|  | g | Grackle man | Adv | Yes | No | 35,060 | n/a | Temperate grassland, temperate savanna |  |
|  | g | Grasshopper man | Adv | No | No | 35,000 | Not tameable | Any non-freezing biome | Animal person, Benign |
|  | g | Gray gibbon | No | No | Yes | 6,000 | 500 | Tropical broadleaf forest |  |
|  | l | Gray langur | No | No | Yes | 15,000 | 50 | Any desert, any grassland, any savanna, any shrubland, any forest |  |
|  | l | Gray langur man | Adv | No | Yes | 42,500 | 50 | Any desert, any grassland, any savanna, any shrubland, any forest | Animal person |
|  | s | Gray squirrel man | Adv | Yes | No | 35,150 | n/a | Any temperate forest |  |
|  | o | Great horned owl | No | No | Yes | 2,000 | 25 | Any forest, any shrubland, any savanna, any grassland, any desert, mangrove swamp, mountain, tundra | Lays eggs |
|  | o | Great horned owl man | Adv | No | Yes | 36,000 | 25 | Any forest, any shrubland, any savanna, any grassland, any desert, mangrove swamp, mountain, tundra | Animal person, Lays eggs |
|  | f | Green tree frog man | Adv | No | No | 35,050 | 10 | Temperate freshwater pool, temperate freshwater lake, temperate freshwater swamp, temperate freshwater marsh | Animal person, Benign |
|  | p | Grey parrot | No | No | Yes | 400 | 10 | Tropical moist broadleaf forest | Lays eggs, Benign |
|  | p | Grey parrot man | Adv | No | Yes | 35,200 | 10 | Tropical moist broadleaf forest | Animal person, Lays eggs, Benign |
|  | g | Grimeling | No | Yes | No | 70,000 | Not tameable | Evil swamps |  |
|  | B | Grizzly bear | No | Yes | Yes | 200,000 | 500 | Taiga, temperate forest | Steals booze, trainable |
|  | B | Grizzly bear man | Adv | Yes | No | 135,000 | n/a | Forest taiga, any temperate forest | Animal person |
|  | g | Groundhog | No | No | Yes | 3,000 | 50 | Temperate savanna, grassland, shrubland |  |
|  | g | Groundhog man | Adv | Yes | No | 36,500 | n/a | Shrubland temperate, savanna temperate, grassland temperate | Animal person |
|  | g | Guineafowl | No | No | Yes | 1,500 | 10 | Mountain |  |
|  | h | Hamster man | Adv | No | No | 35,075 | 10 | Any non-freezing biome | Animal person, Benign |
|  | h | Hare | No | No | Yes | 3,500 | 10 | Temperate savanna, temperate grassland | Benign |
|  | h | Hare man | Adv | No | Yes | 36,750 | 10 | Temperate savanna, temperate grassland | Animal person, Benign |
|  | h | Harpy | No | Yes | No | 60,000 | n/a | Evil savanna, grassland, shrubland, marshes | All harpies are females |
|  | h | Hedgehog man | Adv | No | No | 35,400 | 10 | Temperate shrubland, temperate savanna | Animal person, Benign |
|  | m | Hoary marmot | No | No | Yes | 10,000 | 50 | Mountain |  |
|  | m | Hoary marmot man | Adv | Yes | No | 40,000 | n/a | Mountain | Animal person |
|  | b | Honey badger | No | Yes | Yes | 14,000 | 25 | Any tropical land, any desert | can become enraged at random |
|  | b | Honey badger man | Adv | Yes | No | 42,000 | n/a | Any tropical forest, shrubland tropical, savanna tropical, grassland tropical, any tropical wetland, any desert | Animal person |
|  | h | Hornbill | No | No | Yes | 2,500 | 25 | Any tropical forest | Lays eggs, Benign |
|  | h | Hornbill man | Adv | No | Yes | 36,250 | 25 | Any tropical forest | Animal person, Lays eggs, Benign |
|  | H | Horse | No | No | Yes | 500,000 | 200 | Grassland temperate, savanna temperate |  |
|  | h | Hyena | No | Yes | Yes | 60,000 | 50 | Tropical savanna, tropical grassland, tropical shrubland |  |
|  | h | Hyena man | Adv | Yes | Yes | 64,999 | 50 | Tropical savanna, tropical grassland, tropical shrubland | Animal person |
|  | i | Ibex | No | No | Yes | 50,000 | 50 | Any grassland, any desert | Benign |
|  | i | Ibex man | Adv | No | Yes | 60,000 | 50 | Any grassland, any desert | Animal person, Benign |

---
*Parte 1 de 2 de «Creature». Demais partes em arquivos `...-part-{1..2}.md` na mesma pasta. Fonte: https://dwarffortresswiki.org/index.php/Creature*
