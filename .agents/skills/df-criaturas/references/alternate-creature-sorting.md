# Alternate creature sorting

> Fonte: [Alternate creature sorting](https://dwarffortresswiki.org/index.php/Alternate_creature_sorting) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

In *Dwarf Fortress*, a **creature** is defined as any animate, normally-mobile being that can interact with the world. Although most creatures are animals, dwarves, giant cave spiders, and even megabeasts are all also considered creatures. Various creatures can and will interact with a fortress or adventurer in many different ways. When learning about what creatures there are and the purposes they serve, sometimes it helps to be able to sort them in different ways, such as by where they are found, what features they may have, and similar things. This page was created to allow people to sort creatures by different means to suit other purposes.

## Common table labeling

**Tile:** The tile assigned to the creature, how you will see it without a graphic set.

**Name:** The name of the creature as it shows up in-game.

**Type:** This divides the creatures up into a number of groups. "Person" refers to the main races, "Animal Person" refers to the intelligent, bipedal animal people, "Animal" refers to the majority of creatures, "Megabeast" will include both megabeast and semi-megabeasts, and "Vermin" which refers to any creature below 2 kg that is frequently unnoticeable.

**Playable:** If "No", the creature is not playable in any modes. "Fort" indicates that the creature is playable in fortress mode ([`[SITE_CONTROLLABLE]`](/index.php/Entity_token#SITE_CONTROLLABLE "Entity token")). "Adv" indicates that the creature is playable in adventure mode. All creatures except humans must have a population in an [`[ALL_MAIN_POPS_CONTROLLABLE]`](/index.php/Entity_token#ALL_MAIN_POPS_CONTROLLABLE "Entity token") civilization in order to be playable in adventure mode; goblins (and other creatures) cannot be played from a goblin civ. Humans can be played whether or not a population exists due to [`[OUTSIDER_CONTROLLABLE]`](/index.php/Creature_token#OUTSIDER_CONTROLLABLE "Creature token"), but an `[ALL_MAIN_POPS_CONTROLLABLE]` civ still needed to have existed at some point. Creatures with [`[LOCAL_POPS_CONTROLLABLE]`](/index.php/Creature_token#LOCAL_POPS_CONTROLLABLE "Creature token") are also playable in adventure mode.

**Area:** This refers to general areas that creatures are found in. "Above Ground" creatures are found on the surface, "Subterranean" creatures are found below ground, "Domestic" are creatures that are exclusively domestic, "Aquatic" creatures will refer only to creatures exclusively found in non-subterranean water, "Semi-Aquatic" are creatures found exclusively near water, but can go on land.

**Hostile:** If "Yes" then the creature will attack on sight, if "No" then the creature is either neutral or friendly, and if "Variable" it can vary randomly if the creature will be hostile. This is most seen in animal people. Undead creatures are always hostile to living things.

**Food Source:** If "Yes" then the creature can be butchered into an edible substance that your dwarves will feed on.

**Adult Body Size:** The average size of the creature when an adult. This can be anywhere from 1 for a fly to 25,000,000 for a dragon. The creature's volume in cm3, which for creatures made of flesh more or less equals the creature's weight in grams.[1] These sizes do not correspond to the sizes which trigger pressure plates. Size is modified by height and broadness (i.e. incredibly skinny and short is below the average weight, while a fat and tall one is above it).

**Pet Value:** This is the value the creature can be bought and sold for as a pet during trading.

However, these are just the universally used labels, each table will have additional labels to allow more variety in sorting.

## Complete Creature List

A complete list of every creature in the game, including vermin.

|  |  |  |  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|----|----|----|
| Tile | Name | Type | Playable | Area | Hostile | Food Source | Adult Body Size | Pet Value (×) | Biome | Other |
| a | Aardvark man | Animal person | Adv | Above ground | No | Yes | 60,000 | 50 | Tropical shrubland, tropical savanna, tropical grassland | Benign |
| a | Aardvark | Animal | No | Above ground Above ground | No | Yes | 50,000 | 50 | Tropical shrubland, tropical savanna, tropical grassland | Benign |
| • | Acorn fly | Vermin | No | Semi-aquatic | No | No | 20 | N/A | Any pool | Savage |
| a | Adder man | Animal person | Adv | Above ground | No | Yes | 35,075 | 50 | Temperate grassland, temperate savanna, temperate shrubland, any temperate forest, any temperate wetland | Lays eggs |
| a | Adder | Animal | No | Above ground | No | Yes | 150 | 50 | Temperate grassland, temperate savanna, temperate shrubland, any temperate forest, any temperate wetland | Lays eggs |
| a | Albatross man | Animal person | Adv | Aquatic | No | Yes | 39,000 | 10 | Any ocean | Lays eggs, Benign |
| a | Albatross | Animal | No | Aquatic | No | Yes | 8,000 | 10 | Any ocean | Lays eggs, Benign |
| A | Alligator man | Animal person | Adv | Aquatic | Yes | No | 235,000 | n/a | Temperate freshwater swamp, temperate freshwater marsh, swamp tropical freshwater swamp, tropical freshwater marsh, temperate freshwater river, tropical freshwater river, temperate brackishwater river, tropical brackishwater river |  |
| T | Alligator snapping turtle | Animal | No | Aquatic | No | Yes | 80,000 | 25 | Temperate freshwater river, temperate brackishwater river, temperate freshwater lake, temperate brackishwater lake, temperate freshwater pool, temperate brackishwater pool | Lays eggs |
| A | Alligator | Animal | No | Semi-aquatic | Yes | Yes | 400,000 | 650 | Freshwater swamps, marshes, rivers | Amphibious |
| a | Alpaca | Animal | No | Domestic | No | Yes | 70,000 | 200 | N/A | Domestic, milkable and can be sheared |
| M | Amethyst man | Animal | No | Subterranean | Yes | No | 70,000 | Not tameable | Caverns (3) | Leaves behind an amethyst |
| a | Amphibian man | Animal people | No | Subterranean | Variable1 | No | 20,000 | Not tameable | Underground | Amphibious |
| A | Anaconda man | Animal person | Adv | Above ground | Yes | Yes | 85,000 | 200 | Any tropical swamp |  |
| A | Anaconda | Animal | No | Above ground | Yes | Yes | 100,000 | 200 | Any tropical swamp |  |
| α | Anchovy | Vermin | No | Aquatic | No | Yes | 200 | N/A | Temperate oceans |  |
| s | Angelshark | Animal | No | Aquatic | No | Yes | 15,000 | 200 | Any ocean |  |
| a | Anole man | Animal person | Adv | Above ground | Yes | No | 35,045 | n/a | Any tropical forest |  |
| ∙ | Anole | Vermin | No | Above ground | No | No | 90 | 10 | Any tropical forest |  |
| ∙ | Ant | Vermin | No |  | No | No | 1 | N/A | Not freezing |  |
| a | Antman | Animal people | No | Subterranean | Variable1 | No | Variable2 | Not tameable | Underground | Four castes |
| a | Armadillo man | Animal person | Adv | Above ground | No | Yes | 38,750 | 20 | Tropical savanna, tropical grassland, tropical shrubland, any tropical forest | Benign |
| a | Armadillo | Animal | No | Above ground | No | Yes | 7,500 | 20 | Tropical savanna, tropical grassland, tropical shrubland, any tropical forest | Benign |
| a | Axolotl man | Animal | Adv | Aquatic | No | No | 35,100 | 10 | Tropical saltwater lake, tropical brackishwater lake, tropical freshwater lake |  |
| ∙ | Axolotl | Vermin | No | Aquatic | No | No | 200 | 10 | Tropical saltwater, brackish and freshwater lakes |  |
| a | Aye-aye man | Animal person | Adv | Above ground | No | Yes | 36,250 | 50 | Tropical dry broadleaf forest, tropical moist broadleaf forest | Benign |
| a | Aye-aye | Animal | No | Above ground | No | Yes | 2,500 | 50 | Tropical dry broadleaf forest, tropical moist broadleaf forest | Benign |
| b | Badger man | Animal person | Adv | Above ground | No | Yes | 42,500 | 25 | Taiga, any temperate forest, temperate shrubland, temperate savanna, temperate grassland | Benign |
| b | Badger | Animal | No | Above ground | Yes | Yes | 15,000 | 25 | Taiga, any temperate savanna, grassland, shrubland, forest |  |
| α | Banded knifefish | Vermin | No | Aquatic | No | Yes | 200 | N/A | Tropical freshwater lakes and rivers |  |
| s | Bark scorpion man | Animal person | Adv | Above ground | No | No | 35,001 | Not tameable | Any desert, tropical grassland, tropical savanna, tropical shrubland, tropical conifer forest |  |
| ∙ | Bark scorpion | Vermin | No | Above ground | No | No | 3 | N/A | Tropical grasslands, savannas, shrublands, coniferous forests and any desert | Hateable |
| b | Barn owl man | Animal person | Adv | Above ground | No | Yes | 35,250 | 25 | Any wetland, any temperate forest, tropical conifer forest, tropical dry broadleaf forest, any shrubland, any savanna, any grassland, any desert | Lays eggs, Benign |
| b | Barn owl | Animal | No | Above ground | No | Yes | 500 | 25 | Any wetland, any temperate forest, tropical conifer forest, tropical dry broadleaf forest, any shrubland, any savanna, any grassland, any desert | Lays eggs, Benign |
| S | Basking shark | Animal | No | Aquatic | No | Yes | 15,000,000 | 1000 | Any ocean |  |
| b | Bat man | Animal people | Adv | Subterranean | Variable1 | No | 70,000 | Not tameable | Underground | Can fly |
| ò | Bat ray | Vermin | No | Aquatic | No | Yes | 200 | N/A | Temperate and tropical oceans |  |
| ∙ | Bat | Vermin | No |  | No | No | 100 | 10 | Not freezing, subterranean chasms | Hateable |
| B | Beak dog | Animal | No | Semi-aquatic | Yes | Yes | 150,000 | 50 | Evil marshes | Can be mounted by goblins |
| b | Beaver man | Animal person | Adv | Semi-aquatic | No | Yes | 45,000 | 25 | Any temperate lake, any temperate river | Benign |
| b | Beaver | Animal | No | Semi-aquatic | No | Yes | 20,000 | 25 | Any temperate lake, any temperate river | Benign |
| b | Beetle man | Animal person | Adv | Above ground | Yes | No | 35,000 | n/a | Any non- freezing biome |  |
| • | Beetle | Vermin | No |  | No | No | 1 | N/A | Not freezing |  |
| g | Bilou | Animal | No | Above ground | No | Yes | 6,000 | 500 | Tropical broadleaf forest |  |
| B | Black bear man | Animal person | Adv | Above ground | Yes | No | 95,000 | n/a | Forest taiga, any temperate forest |  |
| B | Black bear | Animal | No | Above ground | Yes | Yes | 120,000 | 300 | Taiga, temperate forest | Steals booze |
| α | Black bullhead | Vermin | No | Aquatic | No | Yes | 200 | N/A | Tropical brackish and freshwater lakes |  |
| s | Black mamba man | Animal person | Adv | Above ground | No | Yes | 37,500 | 50 | Tropical savanna, tropical shrubland, any tropical forest, any tropical swamp | Lays eggs |
| s | Black mamba | Animal | No | Above ground | No | Yes | 5,000 | 50 | Tropical savanna, tropical shrubland, any tropical forest, any tropical swamp | Lays eggs |
| g | Black-crested gibbon | Animal | No | Above ground | No | Yes | 6,000 | 500 | Tropical moist broadleaf forest | Benign |
| g | Black-handed gibbon | Animal | No | Above ground | No | Yes | 6,000 | 500 | Tropical moist broadleaf forest | Benign |
| s | Blacktip reef shark | Animal | No | Aquatic | Yes | Yes | 15,000 | 200 | Any ocean |  |
| B | Blind cave bear | Animal | No | Subterranean | Yes | Yes | 200,000 | 500 | Caverns (1,2) |  |
| O | Blind cave ogre | Animal | No | Subterranean | Yes | Yes | 7,000,000 | 500 | Caverns (2,3) |  |
| M | Blizzard man | Animal | No | Above ground | Yes | No | 300,000 | Not tameable | Tundra, glacier |  |
| • | Blood gnat | Vermin | No | Semi-aquatic | No | No | 1 | N/A | Any pool | Hateable, evil, rots food |
| M | Blood man | Animal | No | Subterranean | Yes | No | 70,000 | Not tameable | Evil Caverns (3) |  |
| ∙ | Blue jay | Vermin | No | Above ground | No | No | 100 | 30 | Temperate grasslands, savannas, shrublands, broadleaf and coniferous forests |  |
| p | Blue peafowl | Animal | No | Above ground | No | Yes | 4,000 | 10 | Tropical broadleaf forest |  |
| S | Blue shark | Animal | No | Aquatic | Yes | Yes | 300,000 | 400 | Any ocean |  |
| α | Bluefin tuna | Animal | No | Aquatic | No | Yes | 600,000 | 200 | Any ocean |  |
| α | Bluefish | Animal | No | Aquatic | No | Yes | 15,000 | 200 | Any ocean |  |
| b | Bluejay man | Animal person | Adv | Above ground | Yes | No | 35,050 | n/a | Grassland temperate, savanna temperate, shrubland temperate, forest temperate broadleaf, forest temperate conifer |  |
| b | Bobcat man | Animal person | Adv | Above ground | No | Yes | 39,000 | 75 | Any forest, any desert, tropical freshwater swamp, tropical saltwater swamp, temperate freshwater swamp, temperate saltwater swamp, mangrove swamp, mountain |  |
| b | Bobcat | Animal | No | Above ground | No | Yes | 8,000 | 75 | Any forest, any desert, tropical freshwater swamp, tropical saltwater swamp, temperate freshwater swamp, temperate saltwater swamp, mangrove swamp, mountain |  |
| b | Bonobo | Animal | No | Above ground | No | Yes | 50,000 | 500 | Tropical broadleaf forest, shrubland |  |
| C | Bronze colossus | Megabeast | No | Above ground | Yes | No | 20,000,000 | Not tameable | All land | Made of bronze, fairly hard to kill, drops masterwork bronze statue on death |
| ~ | Brook lamprey | Vermin | No | Aquatic | No | Yes | 200 | N/A | Tropical saltwater, brackish and freshwater lakes, tropical oceans |  |
| α | Brown bullhead | Vermin | No | Aquatic | No | Yes | 200 | N/A | Temperate brackish and freshwater lakes |  |
| s | Brown recluse spider man | Animal person | Adv | Above ground | No | No | 35,000 | Not tameable | Temperate broadleaf forest |  |
| ∙ | Brown recluse spider | Vermin | No | Above ground | No | No | 1 | N/A | Temperate broadleaf forests | Hateable, produces web |
| b | Bugbat | Animal | No | Subterranean | No | Yes | 10,000 | 20 | Caverns (2,3) |  |
| S | Bull shark | Animal | No | Aquatic | Yes | Yes | 150,000 | 500 | Any ocean |  |
| • | Bumblebee | Vermin | No | Above ground | No | No | 1 | N/A | Not freezing |  |
| s | Bushmaster man | Animal person | Adv | Above ground | No | Yes | 39,250 | 50 | Tropical moist broadleaf forest | Lays eggs |
| s | Bushmaster | Animal | No | Above ground | No | Yes | 8,500 | 50 | Tropical moist broadleaf forest | Lays eggs |
| b | Bushtit man | Animal person | Adv | Above ground | No | No | 35,002 | 30 | Any temperate forest | Lays eggs, Benign |
| ∙ | Bushtit | Vermin | No | Above ground | No | No | 5 | 30 | Any temperate forest |  |
| b | Buzzard man | Animal person | Adv | Above ground | Yes | No | 35,700 | n/a | Marsh temperate freshwater, marsh temperate saltwater, grassland temperate, savanna temperate, any desert | lays eggs |
| b | Buzzard | Animal | No | Above ground | Yes | Yes | 1,400 | 30 | Any desert, temperate grassland, savanna, marsh | Steals food, lays eggs |
| ∙ | Cap hopper | Vermin | No | Subterranean Aquatic | No | No | 200 | 10 | Subterranean water |  |
| c | Capuchin man | Animal person | Adv | Above ground | No | Yes | 36,750 | 50 | Any tropical forest, mangrove swamp |  |
| c | Capuchin | Animal | No | Above ground | No | Yes | 3,500 | 50 | Any tropical forest, mangrove swamp |  |
| c | Capybara man | Animal person | Adv | Above ground | No | Yes | 57,499 | 100 | Any wetland |  |
| c | Capybara | Animal | No | Above ground | No | Yes | 45,000 | 100 | Any wetland | Makes sounds in Adventure mode |
| c | Cardinal man | Animal person | Adv | Above ground | Yes | No | 35,025 | n/a | Grassland temperate, savanna temperate, shrubland temperate, forest temperate broadleaf, forest temperate conifer |  |
| ∙ | Cardinal | Vermin | No | Above ground | No | No | 50 | 30 | Temperate grasslands, savannas, shrublands, broadleaf and coniferous forests |  |
| α | Carp | Animal | No | Aquatic | No | Yes | 40,000 | 50 | Freshwater river, freshwater lake |  |
| c | Cassowary man | Animal person | Adv | Above ground | No | Yes | 60,000 | 100 | Tropical moist broadleaf forest | Lays eggs, Benign |
| c | Cassowary | Animal | No | Above ground | No | Yes | 50,000 | 100 | Tropical moist broadleaf forest | Lays eggs, Benign |
| c | Cat | Animal | No | Domestic | No | Yes | 5,000 | 20 | N/A |  |
| o | Cave blob | Animal | No | Subterranean | No | No | 20,000 | 50 | Caverns (3) | Causes syndrome |
| C | Cave crocodile | Animal | No | Subterranean | Yes | Yes | 600,000 | 750 | Caverns (1,2) |  |
| D | Cave dragon | Animal | No | Subterranean | Yes | Yes | 15,000,000 | 10000 | Caverns (3) | Trainable |
| f | Cave fish man | Animal people | Adv | Subterranean | Variable1 | No | 70,000 | Not tameable | Underground | Amphibious |
| α | Cave fish | Vermin | No | Subterranean Aquatic | No | Yes | 1000 | N/A | Subterranean water |  |
| f | Cave floater | Animal | No | Subterranean | No | No | 40,000 | 50 | Caverns (2,3) | Causes syndrome |
| ¥ | Cave lobster | Vermin | No | Subterranean Aquatic | No | Yes | 600 | N/A | Subterranean water |  |
| ∙ | Cave spider | Vermin | No | Subterranean | No | No | 50 | N/A | Subterranean water and chasm | Hateable, produces web |
| s | Cave swallow man | Animal people | Adv | Subterranean | Variable1 | No | 70,000 | Not tameable | Underground | Can fly |
| ∙ | Cave swallow | Vermin | No | Subterranean | No | No | 100 | 30 | Subterranean chasm |  |
| c | Cavy | Animal | No | Above ground | No | No | 800 | 3 | Tropical savanna, grassland, and shrubland |  |
| c | Chameleon man | Animal person | Adv | Above ground | Yes | No | 35,075 | n/a | Any tropical forest, shrubland tropical, savanna tropical, any desert |  |
| ∙ | Chameleon | Vermin | No | Above ground | No | No | 150 | 10 | Any tropical forest, tropical shrublands and savannas, any desert |  |
| α | Char | Vermin | No | Aquatic | No | Yes | 200 | N/A | Temperate brackish and freshwater lakes |  |
| c | Cheetah man | Animal person | Adv | Above ground | Yes | No | 60,000 | n/a | Savanna tropical, grassland tropical, shrubland tropical |  |
| c | Cheetah | Animal | No | Above ground | Yes | Yes | 50,000 | 200 | Tropical savanna, grassland, shrubland |  |
| c | Chicken | Animal | No | Domestic | No | Yes | 3,000 | 10 | N/A |  |
| c | Chimpanzee | Animal | No | Above ground | No | Yes | 50,000 | 500 | Tropical broadleaf forest, shrubland |  |
| c | Chinchilla man | Animal person | Adv | Above ground | No | Yes | 35,250 | 3 | Mountain | Benign |
| c | Chinchilla | Animal | No | Above ground | No | Yes | 500 | 3 | Mountain | Benign |
| c | Chipmunk man | Animal person | Adv | Above ground | Yes | No | 35,150 | n/a | Any temperate forest |  |
| ∙ | Chipmunk | Vermin | No | Above ground | No | No | 300 | 10 | Any temperate forest |  |
| α | Clown loach | Vermin | No | Aquatic | No | Yes | 200 | N/A | Tropical brackish and freshwater lakes |  |
| α | Clownfish | Vermin | No | Aquatic | No | Yes | 200 | N/A | Tropical oceans |  |
| c | Coati man | Animal person | Adv | Above ground | No | Yes | 38,000 | 50 | Any temperate forest, any tropical forest |  |
| c | Coati | Animal | No | Above ground | No | Yes | 6,000 | 50 | Any temperate forest, any tropical forest |  |
| c | Cockatiel man | Animal person | Adv | Above ground | No | No | 35,045 | 30 | Any desert, temperate grassland | Lays eggs, Benign |
| ∙ | Cockatiel | Vermin | No | Above ground | No | No | 90 | 30 | Any desert, temperate grasslands |  |
| α | Cod | Animal | No | Aquatic | No | Yes | 50,000 | 200 | Any ocean |  |
| C | Coelacanth | Animal | No | Aquatic | No | Yes | 80,000 | 200 | Any ocean |  |
| ò | Common skate | Animal | No | Aquatic | No | Yes | 100,000 | 200 | Any ocean |  |
| t | Common snapping turtle | Animal | No | Aquatic | No | Yes | 30,000 | 25 | Temperate freshwater river, temperate brackishwater river, temperate freshwater lake, temperate brackishwater lake, temperate freshwater pool, temperate brackishwater pool | Lays eggs |
| ~ | Conger eel | Animal | No | Aquatic | No | Yes | 50,000 | 400 | Any ocean |  |
| s | Copperhead snake man | Animal person | Adv | Above ground | No | Yes | 35,250 | 50 | Temperate broadleaf forest, any temperate swamp |  |
| s | Copperhead snake | Animal | No | Above ground | No | Yes | 500 | 50 | Temperate broadleaf forest, any temperate swamp |  |
| c | Cougar man | Animal person | Adv | Above ground | Yes | No | 65,000 | n/a | Any temperate forest, any tropical forest, shrubland temperate, shrubland tropical |  |
| c | Cougar | Animal | No | Above ground | Yes | Yes | 60,000 | 100 | Any forest, any shrubland |  |
| C | Cow | Animal | No | Above ground | No | Yes | 600,000 | 300 | Grassland temperate, savanna temperate |  |
| c | Coyote man | Animal person | Adv | Above ground | No | Yes | 42,500 | 50 | Mountain, tundra, taiga, any temperate forest, temperate savanna, temperate grassland, temperate shrubland, any temperate wetland, any desert |  |
| c | Coyote | Animal | No | Above ground | No | Yes | 15,000 | 50 | Mountain, tundra, taiga, any temperate forest, temperate savanna, temperate grassland, temperate shrubland, any temperate wetland, any desert |  |
| c | Crab man | Animal person | Adv | Aquatic | No | Yes | 39,000 | Not tameable | Any ocean |  |
| c | Crab | Animal | No | Aquatic | No | Yes | 8,000 | Not tameable | Any ocean |  |
| e | Creeping eye | Animal | No | Subterranean | No | Yes | 20,000 | 50 | Caverns (3) |  |
| \* | Creepy crawler | Vermin | No | Subterranean | No | Yes | 1000 | 20 | Underground chasm | Evil, rots food |
| c | Crow man | Animal person | Adv | Above ground | No | No | 35,250 | 10 | Temperate grassland, temperate savanna, temperate shrubland, taiga, any temperate forest, any temperate wetland | Lays eggs, Benign |
| ∙ | Crow | Vermin | No | Above ground | No | No | 500 | 10 | Temperate forests, grasslands, savannas, shrublands and wetlands, taiga |  |
| c | Crundle | Animal | No | Subterranean | Yes | Yes | 10,000 | 50 | Caverns (2,3) |  |
| c | Cuttlefish man | Animal person | Adv | Aquatic | No | No | 35,500 | 10 | Any ocean |  |
| ♂ | Cuttlefish | Vermin | No | Aquatic | No | Yes | 1000 | 10 | Any ocean |  |
| C | Cyclops | Megabeast | No | Above ground | Yes | Yes | 8,000,000 | Not tameable | All land | One eyed |
| d | Damselfly man | Animal person | Adv | Aquatic | No | No | 35,000 | Not tameable | Any pool |  |
| ∙ | Damselfly | Vermin | No | Semi-aquatic | No | No | 1 | N/A | Any pool |  |
| g | Dark gnome | Animal | No | Above ground | Yes | No | 15,000 | Not tameable | Evil mountain | Steals booze |
| d | Deer man | Animal person | Adv | Above ground | Yes | No | 105,000 | n/a | Forest taiga, any temperate forest |  |
| D | Deer | Animal | No | Above ground | No | Yes | 140,000 | 50 | Taiga, temperate forest | Benign |
| ∙ | Demon rat | Vermin | No | Above ground | No | No | 300 | 20 | Not freezing | Evil |
| t | Desert tortoise man | Animal person | Adv | Above ground | No | Yes | 37,750 | 50 | Any desert | Lays eggs, Benign |
| t | Desert tortoise | Animal | No | Above ground | No | Yes | 5,500 | 50 | Any desert | Lays eggs, Benign |
| d | Dingo man | Animal person | Adv | Above ground | Yes | Yes | 45,000 | 50 | Any non-freezing biome |  |
| d | Dingo | Animal | No | Above ground | Yes | Yes | 20,000 | 50 | Any non-freezing biome |  |
| d | Dog | Animal | No | Domestic | No | Yes | 30,000 | 30 | N/A |  |
| D | Donkey | Animal | No | Domestic | No | Yes | 300,000 | 200 | N/A |  |
| D | Dragon | Megabeast | No | Above ground | Yes | Yes | 25,000,000 | 10000 | All land | Breathes fire, trainable |
| d | Dragonfly man | Animal person | Adv | Aquatic | Yes | No | 35,000 | n/a | Any pool |  |
| ∙ | Dragonfly | Vermin | No | Semi-aquatic | No | No | 1 | N/A | Any pool |  |
| D | Draltha | Animal | No | Subterranean | No | Yes | 2,500,000 | 500 | Caverns (1,2) |  |
| d | Drunian | Animal | No | Subterranean | No | Yes | 50,000 | 50 | Caverns (1,2) | Steals food and items |
| d | Duck | Animal | No | Semi-aquatic | No | No | 1,000 | 10 | Any lakes, any wetland |  |
| ☺ | Dwarf | People | Fort, Adv | Above ground | No | No | 60,000 | Not tameable | Mountain halls, dwarf fortresses, hillocks | Trading race |
| e | Eagle man | Animal person | Adv | Above ground | No | Yes | 37,000 | 25 | Any wetland, any forest, any shrubland, any savanna, any grassland, any desert, mountain, tundra | Lays eggs, Benign |
| e | Eagle | Animal | No | Above ground | No | Yes | 4,000 | 25 | Any wetland, any forest, any shrubland, any savanna, any grassland, any desert, mountain, tundra | Lays eggs, Benign |
| e | Echidna man | Animal person | Adv | Above ground | No | Yes | 40,000 | 50 | Any temperate forest, temperate shrubland, temperate savanna, temperate grassland, any desert | Lays eggs, Benign |
| e | Echidna | Animal | No | Above ground | No | Yes | 10,000 | 50 | Any temperate forest, temperate shrubland, temperate savanna, temperate grassland, any desert | Lays eggs, Benign |
| E | Elephant man | Animal person | Adv | Above ground | Yes | No | 2,535,000 | n/a | Any tropical forest, shrubland tropical |  |
| S | Elephant seal man | Animal person | Adv | Aquatic | No | Yes | 1,535,000 | 400 | Arctic ocean | Benign |
| S | Elephant seal | Animal | No | Aquatic | No | Yes | 3,000,000 | 400 | Arctic ocean | Benign |
| E | Elephant | Animal | No | Above ground | No | Yes | 5,000,000 | 500 | Tropical forest, shrubland | Trainable |
| e | Elf | People | Adv | Above ground | Variable1 | No | 60,000 | Not tameable | Forest retreats | Trading race |
| E | Elk bird | Animal | No | Subterranean | No | Yes | 100,000 | 400 | Caverns (1,2,3) |  |
| E | Elk man | Animal person | Adv | Above ground | Yes | No | 185,000 | n/a | Tundra, grassland temperate |  |
| E | Elk | Animal | No | Above ground | No | Yes | 300,000 | 100 | Tundra, temperate grassland |  |
| p | Emperor penguin | Animal | No | Aquatic | No | Yes | 30,000 | 10 | Arctic ocean |  |
| E | Emu man | Animal person | Adv | Above ground | No | Yes | 52,500 | 100 | Temperate shrubland, any temperate forest | Lays eggs, Benign |
| E | Emu | Animal | No | Above ground | No | Yes | 35,000 | 100 | Temperate shrubland, any temperate forest | Lays eggs, Benign |
| E | Ettin | Megabeast | No |  | Yes | Yes | 8,000,000 | Not tameable | All land | Has two heads |
| ∙ | Fairy | Vermin | No | Above ground | No | No | 100 | 10 | All except pools, rivers, and underground | Good, fanciful |
| i | Fire imp | Animal | No | Subterranean | Yes | Yes | 6,000 | Not tameable | Magma | Throws fireballs |
| M | Fire man | Animal person | No | Subterranean | Yes | No | 70,000 | Not tameable | Magma | Throws fireballs and leaves behind ashes |
| ∙ | Fire snake | Vermin | No | Subterranean | No | No | 1000 | 10 | Subterranean lava | Hateable |
| f | Firefly man | Animal person | Adv | Above ground | Yes | No | 35,000 | n/a | Any non-freezing biome |  |
| ∙ | Firefly | Vermin | No | Above ground | No | No | 1 | N/A | Not freezing |  |
| o | Flesh ball | Animal | No | Subterranean | No | Yes | 70,000 | 10 | Subterranean water - Cavern (3) |  |
| % | Floating guts | Animal | No | Subterranean | No | Yes | 20,000 | 10 | Caverns (2,3) |  |
| α | Flounder | Vermin | No | Aquatic | No | Yes | 200 | N/A | Temperate oceans |  |
| ∙ | Fluffy wambler | Vermin | No | Above ground | No | No | 2000 | 20 | Any land | Good |
| f | Fly man | Animal person | Adv | Semi-aquatic | Yes | No | 35,000 | n/a | Any non-freezing biome, any pool |  |
| • | Fly | Vermin | No | Semi-Aquatic | No | No | 1 | N/A | Not freezing, any pool | Hateable |
| s | Flying squirrel man | Animal person | Adv | Above ground | No | No | 35,100 | 10 | Any temperate forest | Benign |
| ∙ | Flying squirrel | Vermin | No | Above ground | No | No | 200 | 10 | Any temperate forest |  |
| b | Foul blendec | Animal | No | Above ground | Yes | Yes | 60,000 | 250 | Most evil forest |  |
| f | Fox man | Animal person | Adv | Above ground | Yes | No | 38,000 | n/a | Forest taiga, any temperate forest |  |
| ∙ | Fox squirrel | Vermin | No | Above ground | No | No | 2000 | 100 | Any temperate forest | Savage |
| f | Fox | Animal | No | Above ground | No | Yes | 6,000 | 25 | Taiga, temperate forest |  |
| s | Frill shark | Animal | No | Aquatic | Yes | Yes | 60,000 | 500 | Any ocean |  |
| M | Gabbro man | Animal person | No | Subterranean | Yes | No | 70,000 | Not tameable | Caverns (3) | Leaves behind gabbro |
| g | Gazelle man | Animal person | Adv | Above ground | Yes | No | 45,000 | n/a | Savanna tropical, grassland tropical |  |
| g | Gazelle | Animal | No | Above ground | No | Yes | 20,000 | 50 | Tropical savanna, grassland |  |
| A | Giant aardvark | Animal | No | Above ground | No | Yes | 560,000 | 500 | Tropical shrubland, tropical savanna, tropical grassland | Benign |
| A | Giant adder | Animal | No | Above ground | No | Yes | 201,049 | 500 | Temperate grassland, temperate savanna, temperate shrubland, any temperate forest, any temperate wetland | Lays eggs |
| A | Giant albatross | Animal | No | Aquatic | No | Yes | 256,320 | 500 | Any ocean | Lays eggs, Benign |
| A | Giant alligator | Animal | No | Aquatic | Yes | Yes | 3,268,000 | 500 | Swamp, marsh, river |  |
| A | Giant anaconda | Animal | No | Above ground | Yes | Yes | 933,000 | 500 | Any tropical swamp |  |
| A | Giant anole | Animal | No | Above ground | Yes | Yes | 200,629 | 500 | Any tropical forest |  |
| A | Giant armadillo | Animal | No | Above ground | No | Yes | 252,750 | 1000 | Tropical savanna, tropical grassland, tropical shrubland, any tropical forest | Benign |
| A | Giant axolotl | Animal | No | Aquatic | No | No | 201,400 | 500 | Tropical saltwater lake, tropical brackishwater lake, tropical freshwater lake |  |
| A | Giant aye-aye | Animal | No | Above ground | No | Yes | 217,525 | 500 | Tropical dry broadleaf forest, tropical moist broadleaf forest | Benign |
| B | Giant badger | Animal | No | Above ground | No | Yes | 306,000 | 500 | Taiga, any temperate forest, temperate shrubland, temperate savanna, temperate grassland | Benign |
| S | Giant bark scorpion | Animal | No | Above ground | No | No | 200,021 | 500 | Any desert, tropical grassland, tropical savanna, tropical shrubland, tropical conifer forest |  |
| B | Giant barn owl | Animal | No | Above ground | No | Yes | 203,500 | 500 | Any wetland, any temperate forest, tropical conifer forest, tropical dry broadleaf forest, any shrubland, any savanna, any grassland, any desert | Lays eggs, Benign |
| B | Giant bat | Animal | No | Subterranean | Yes | Yes | 200,000 | 750 | Caverns (1,2) | Trainable |
| B | Giant beaver | Animal | No | Aquatic | No | Yes | 341,800 | 500 | Any temperate lake, any temperate river | Benign |
| B | Giant beetle | Animal | No | Above ground | Yes | Yes | 200,007 | 500 | Any non-freezing biome |  |
| B | Giant black bear | Animal | No | Above ground | Yes | Yes | 1,084,800 | 500 | Forest taiga, any temperate forest |  |
| S | Giant black mamba | Animal | No | Above ground | No | Yes | 235,100 | 500 | Tropical savanna, tropical shrubland, any tropical forest, any tropical swamp | Lays eggs |
| B | Giant bluejay | Animal | No | Above ground | Yes | Yes | 200,700 | 500 | Grassland temperate, savanna temperate, shrubland temperate, forest temperate broadleaf, forest temperate conifer |  |
| B | Giant bobcat | Animal | No | Above ground | No | Yes | 256,320 | 500 | Any forest, any desert, tropical freshwater swamp, tropical saltwater swamp, temperate freshwater swamp, temperate saltwater swamp, mangrove swamp, mountain |  |
| S | Giant brown recluse spider | Animal | No | Above ground | No | No | 200,007 | 500 | Temperate broadleaf forest |  |
| S | Giant bushmaster | Animal | No | Above ground | No | Yes | 259,845 | 500 | Tropical moist broadleaf forest | Lays eggs |
| B | Giant bushtit | Animal | No | Above ground | No | No | 200,035 | 500 | Any temperate forest | Lays eggs, Benign |
| B | Giant buzzard | Animal | No | Above ground | Yes | Yes | 209,804 | 500 | Marsh temperate freshwater, marsh temperate saltwater, grassland temperate, savanna temperate, any desert |  |
| B | Giant buzzard | Animal | No | Aquatic | Yes | Yes | 209,804 | 500 | Temperate marsh |  |
| C | Giant capuchin | Animal | No | Above ground | No | Yes | 224,560 | 500 | Any tropical forest, mangrove swamp |  |
| C | Giant capybara | Animal | No | Above ground | No | Yes | 523,350 | 500 | Any wetland | Makes sounds in Adventure mode |
| C | Giant cardinal | Animal | No | Above ground | Yes | Yes | 200,350 | 500 | Grassland temperate, savanna temperate, shrubland temperate, forest temperate broadleaf, forest temperate conifer |  |
| C | Giant cassowary | Animal | No | Above ground | No | Yes | 560,000 | 500 | Tropical moist broadleaf forest | Lays eggs, Benign |
| S | Giant cave spider | Animal | No | Subterranean | Yes | Yes | 200,000 | 2500 | Caverns (1,2) | Spins/throws webs and causes syndrome |
| C | Giant cave swallow | Animal | No | Subterranean | No\[Verify\] | Yes | 200,000 | 700 | Caverns (1,2) | Trainable |
| T | Giant cave toad | Animal | No | Subterranean | Yes | Yes | 200,000 | 750 | Caverns (1,2) |  |
| C | Giant chameleon | Animal | No | Above ground | Yes | Yes | 201,049 | 500 | Any tropical forest, shrubland tropical, savanna tropical, any desert |  |
| C | Giant cheetah | Animal | No | Above ground | Yes | Yes | 560,000 | 500 | Tropical savanna, grassland, shrubland | Trainable |
| C | Giant chinchilla | Animal | No | Above ground | No | Yes | 203,500 | 500 | Mountain | Benign |
| C | Giant chipmunk | Animal | No | Above ground | Yes | Yes | 202,101 | 500 | Any temperate forest |  |
| C | Giant coati | Animal | No | Above ground | No | Yes | 242,160 | 500 | Any temperate forest, any tropical forest |  |
| C | Giant cockatiel | Animal | No | Above ground | No | No | 200,629 | 500 | Any desert, temperate grassland | Lays eggs, Benign |
| S | Giant copperhead snake | Animal | No | Above ground | No | Yes | 203,500 | 500 | Temperate broadleaf forest, any temperate swamp |  |
| C | Giant cougar | Animal | No | Above ground | Yes | Yes | 633,600 | 500 | Any temperate forest, any tropical forest, shrubland temperate, shrubland tropical |  |
| C | Giant coyote | Animal | No | Above ground | No | Yes | 306,000 | 500 | Mountain, tundra, taiga, any temperate forest, temperate savanna, temperate grassland, temperate shrubland, any temperate wetland, any desert |  |
| C | Giant crab | Animal | No | Aquatic | No | Yes | 256,320 | 500 | Any ocean |  |
| C | Giant crow | Animal | No | Above ground | No | No | 203,500 | 500 | Temperate grassland, temperate savanna, temperate shrubland, taiga, any temperate forest, any temperate wetland | Lays eggs, Benign |
| C | Giant cuttlefish | Animal | No | Aquatic | No | No | 207,010 | 500 | Any ocean |  |
| D | Giant damselfly | Animal | No | Aquatic | No | No | 200,007 | 500 | Any pool |  |
| D | Giant deer | Animal | No | Above ground | Yes | Yes | 1,237,600 | 500 | Forest taiga, any temperate forest |  |
| S | Giant desert scorpion | Animal | No | Above ground | Yes | Yes | 200,000 | 2500 | Savage desert | No pain, no stun, no emotion; deadly Syndrome |
| T | Giant desert tortoise | Animal | No | Above ground | No | Yes | 238,645 | 500 | Any desert | Lays eggs, Benign |
| D | Giant dingo | Animal | No | Above ground | Yes | Yes | 341,800 | 500 | Any non-freezing biome |  |
| D | Giant dragonfly | Animal | No | Aquatic | Yes | Yes | 200,007 | 500 | Any pool |  |
| E | Giant eagle | Animal | No | Above ground | Yes | Yes | 228,040 | 500 | Savage mountain | Trainable |
| W | Giant earthworm | Animal | No | Subterranean | No | Yes | 200,000 | 500 | Caverns (1,2) |  |
| E | Giant echidna | Animal | No | Above ground | No | Yes | 270,500 | 500 | Any temperate forest, temperate shrubland, temperate savanna, temperate grassland, any desert | Lays eggs, Benign |
| S | Giant elephant seal | Animal | No | Aquatic | No | Yes | 24,119,999 | 500 | Arctic ocean | Benign |
| E | Giant elephant | Animal | No | Above ground | Yes | Yes | 40,000,000 | 500 | Any tropical forest, shrubland tropical |  |
| E | Giant elk | Animal | No | Above ground | Yes | Yes | 2,478,000 | 500 | Tundra, grassland temperate |  |
| E | Giant emu | Animal | No | Above ground | No | Yes | 450,100 | 500 | Temperate shrubland, any temperate forest | Lays eggs, Benign |
| F | Giant firefly | Animal | No | Above ground | Yes | Yes | 200,007 | 500 | Any non-freezing biome |  |
| F | Giant fly | Animal | No | Above ground | Yes | Yes | 200,007 | 500 | Any non-freezing biome, any pool |  |
| F | Giant fly | Animal | No | Aquatic | Yes | Yes | 200,007 | 500 | Any non-freezing biome, any pool |  |
| S | Giant flying squirrel | Animal | No | Above ground | No | No | 201,400 | 500 | Any temperate forest | Benign |
| F | Giant fox | Animal | No | Above ground | Yes | Yes | 242,160 | 500 | Forest taiga, any temperate forest |  |
| G | Giant gazelle | Animal | No | Above ground | Yes | Yes | 341,800 | 500 | Savanna tropical, grassland tropical |  |
| G | Giant gila monster | Animal | No | Above ground | No | Yes | 214,020 | 500 | Any desert | Lays eggs |
| G | Giant giraffe | Animal | No | Above ground | Yes | Yes | 8,030,000 | 500 | Savanna tropical, shrubland tropical |  |
| G | Giant grackle | Animal | No | Above ground | Yes | Yes | 200,840 | 500 | Grassland temperate, savanna temperate |  |
| G | Giant grasshopper | Animal | No | Above ground | No | No | 200,007 | 500 | Any non-freezing biome | Benign |
| L | Giant gray langur | Animal | No | Above ground | No | Yes | 306,000 | 500 | Any desert, any grassland, any savanna, any shrubland, any forest |  |
| S | Giant gray squirrel | Animal | No | Above ground | Yes | Yes | 202,101 | 500 | Any temperate forest |  |
| O | Giant great horned owl | Animal | No | Above ground | No | Yes | 214,020 | 500 | Any forest, any shrubland, any savanna, any grassland, any desert, mangrove swamp, mountain, tundra | Lays eggs |
| F | Giant green tree frog | Animal | No | Above ground | No | No | 200,700 | 500 | Temperate freshwater pool, temperate freshwater lake, temperate freshwater swamp, temperate freshwater marsh | Benign |
| F | Giant green tree frog | Animal | No | Aquatic | No | No | 200,700 | 500 | Temperate freshwater pool, temperate freshwater lake, temperate freshwater swamp, temperate freshwater marsh | Benign |
| P | Giant grey parrot | Animal | No | Above ground | No | Yes | 202,800 | 500 | Tropical moist broadleaf forest | Lays eggs, Benign |
| B | Giant grizzly bear | Animal | No | Above ground | Yes | Yes | 1,700,000 | 500 | Forest taiga, any temperate forest |  |
| G | Giant groundhog | Animal | No | Above ground | Yes | Yes | 221,040 | 500 | Shrubland temperate, savanna temperate, grassland temperate |  |
| G | Giant grouper | Animal | No | Aquatic | No | Yes | 600,000 | 200 | Any ocean |  |
| H | Giant hamster | Animal | No | Above ground | No | No | 201,049 | 500 | Any non-freezing biome | Benign |
| H | Giant hare | Animal | No | Above ground | No | Yes | 224,560 | 500 | Temperate savanna, temperate grassland | Benign |
| H | Giant harp seal | Animal | No | Aquatic | No | Yes | 1,428,900 | 500 | Arctic ocean | Benign |
| H | Giant hedgehog | Animal | No | Above ground | No | No | 205,600 | 500 | Temperate shrubland, temperate savanna | Benign |
| H | Giant hippo | Animal | No | Above ground | Yes | Yes | 12,030,000 | 500 | River tropical saltwater, river tropical brackishwater, river tropical freshwater, lake tropical saltwater, lake tropical brackishwater, lake tropical freshwater |  |
| H | Giant hippo | Animal | No | Aquatic | Yes | Yes | 12,030,000 | 500 | Any river, lake |  |
| M | Giant hoary marmot | Animal | No | Above ground | Yes | Yes | 270,500 | 500 | Mountain |  |
| B | Giant honey badger | Animal | No | Above ground | Yes | Yes | 298,900 | 500 | Any tropical forest, shrubland tropical, savanna tropical, grassland tropical, any tropical wetland, any desert |  |
| H | Giant hornbill | Animal | No | Above ground | No | Yes | 217,525 | 500 | Any tropical forest | Lays eggs, Benign |
| C | Giant horseshoe crab | Animal | No | Aquatic | No | Yes | 214,020 | 500 | Any ocean |  |
| H | Giant hyena | Animal | No | Above ground | Yes | Yes | 633,600 | 500 | Tropical savanna, tropical grassland, tropical shrubland |  |
| I | Giant ibex | Animal | No | Above ground | No | Yes | 560,000 | 500 | Any grassland, any desert | Benign |
| I | Giant iguana | Animal | No | Above ground | Yes | Yes | 228,040 | 500 | Any tropical forest |  |
| I | Giant impala | Animal | No | Above ground | No | Yes | 560,000 | 500 | Tropical savanna, tropical grassland | Benign |
| J | Giant jackal | Animal | No | Above ground | No | Yes | 306,000 | 500 | Tropical shrubland, tropical savanna, tropical grassland |  |
| J | Giant jaguar | Animal | No | Above ground | Yes | Yes | 745,500 | 500 | Savage tropical areas, any desert | Trainable |
| J | Giant jumping spider | Animal | No | Above ground | No | No | 200,007 | 500 | Any non-freezing biome |  |
| K | Giant kakapo | Animal | No | Above ground | No | Yes | 221,040 | 500 | Temperate shrubland, temperate savanna, temperate grassland, any temperate forest | Lays eggs, Benign |
| K | Giant kangaroo | Animal | No | Above ground | No | Yes | 857,700 | 500 | Temperate grassland, temperate savanna, temperate shrubland, any desert | Benign |
| K | Giant kea | Animal | No | Above ground | No | Yes | 207,010 | 500 | Any temperate forest, temperate shrubland, mountain | Lays eggs |
| K | Giant kestrel | Animal | No | Above ground | No | Yes | 201,750 | 500 | Tropical freshwater marsh, tropical saltwater marsh, temperate freshwater marsh, temperate saltwater marsh, any shrubland, any savanna, any grassland | Lays eggs, Benign |
| K | Giant kestrel | Animal | No | Aquatic | Yes | Yes | 201,750 | 500 | Marsh |  |
| K | Giant king cobra | Animal | No | Above ground | No | Yes | 242,160 | 500 | Any tropical forest | Lays eggs |
| K | Giant kingsnake | Animal | No | Above ground | No | Yes | 210,510 | 500 | Any temperate forest, temperate shrubland, mountain, any desert | Lays eggs |
| K | Giant kiwi | Animal | No | Above ground | No | Yes | 217,525 | 1000 | Any temperate forest, temperate shrubland | Lays eggs, Benign |
| K | Giant koala | Animal | No | Above ground | No | Yes | 270,500 | 500 | Temperate broadleaf forest | Benign |
| L | Giant leech | Animal | No | Aquatic | No | No | 200,700 | 500 | Any pool, any lake |  |
| G | Giant leopard gecko | Animal | No | Above ground | No | No | 200,350 | 500 | Any desert |  |
| L | Giant leopard seal | Animal | No | Aquatic | No | Yes | 3,268,000 | 500 | Arctic ocean | Benign |
| L | Giant leopard | Animal | No | Above ground | Yes | Yes | 560,000 | 500 | Savage tropical areas, any desert | Trainable |
| L | Giant lion tamarin | Animal | No | Above ground | No | No | 204,302 | 500 | Tropical moist broadleaf forest | Benign |
| L | Giant lion | Animal | No | Above ground | Yes | Yes | 1,700,000 | 500 | Tropical savanna, Tropical grassland, Tropical shrubland | Trainable |
| L | Giant lizard | Animal | No | Above ground | Yes | Yes | 201,400 | 500 | Any non-freezing biome |  |
| L | Giant loon | Animal | No | Aquatic | No | Yes | 242,160 | 500 | Temperate saltwater lake, temperate brackishwater lake, temperate freshwater lake | Lays eggs, Benign |
| L | Giant lorikeet | Animal | No | Above ground | No | No | 201,400 | 500 | Tropical moist broadleaf forest, mangrove swamp | Lays eggs, Benign |
| L | Giant louse | Animal | No | Above ground | No | No | 200,007 | 500 | Any non-freezing biome |  |
| L | Giant lynx | Animal | No | Above ground | No | Yes | 377,750 | 500 | Taiga |  |
| M | Giant magpie | Animal | No | Above ground | No | No | 201,400 | 500 | Temperate grassland, temperate savanna, temperate shrubland | Lays eggs, Benign |
| M | Giant mandrill | Animal | No | Above ground | Yes | Yes | 341,800 | 500 | Forest tropical moist broadleaf |  |
| M | Giant mantis | Animal | No | Above ground | No | No | 200,007 | 500 | Any non-freezing biome |  |
| L | Giant masked lovebird | Animal | No | Above ground | No | No | 200,629 | 500 | Any tropical forest | Lays eggs |
| M | Giant mink | Animal | No | Aquatic | No | Yes | 205,600 | 500 | Any temperate lake, any temperate river | Benign |
| m | Giant mole | Animal | No | Subterranean | No\[Verify\] | Yes | 200,000 | 350 | Caverns (1,2) | Steals food and booze |
| B | Giant monarch butterfly | Animal | No | Above ground | Yes | Yes | 200,007 | 500 | Any non-freezing biome |  |
| M | Giant mongoose | Animal | No | Above ground | No | Yes | 221,040 | 500 | Tropical savanna, tropical shrubland | Benign |
| M | Giant monitor lizard | Animal | No | Above ground | No | Yes | 933,000 | 500 | Tropical grassland, tropical savanna, tropical shrubland, any tropical forest | Lays eggs |
| S | Giant moon snail | Animal | No | Aquatic | No | No | 201,400 | 500 | Temperate ocean |  |
| M | Giant moose | Animal | No | Above ground | No | Yes | 4,257,750 | 1000 | Taiga, any temperate forest | Benign |
| M | Giant mosquito | Animal | No | Above ground | No | No | 200,007 | 500 | Any non-freezing biome, any pool |  |
| M | Giant mosquito | Animal | No | Aquatic | No | No | 200,007 | 500 | Any non-freezing biome, any pool |  |
| M | Giant moth | Animal | No | Above ground | No | No | 200,007 | 500 | Any non-freezing biome | Benign |
| G | Giant mountain goat | Animal | No | Above ground | Yes | Yes | 560,000 | 500 | Mountain |  |
| M | Giant muskox | Animal | No | Above ground | Yes | Yes | 2,362,650 | 500 | Tundra, grassland temperate |  |
| N | Giant narwhal | Animal | No | Aquatic | No | Yes | 9,624,000 | 2000 | Arctic ocean | Benign |
| N | Giant nautilus | Animal | No | Aquatic | No | No | 203,500 | 500 | Any ocean |  |
| O | Giant ocelot | Animal | No | Above ground | No | Yes | 377,750 | 500 | Any tropical forest, mangrove swamp, tropical savanna, tropical grassland |  |
| O | Giant octopus | Animal | No | Aquatic | No | Yes | 235,100 | 500 | Any ocean |  |
| O | Giant olm | Animal | No | Subterranean | Yes | Yes | 200,000 | 750 | Caverns (1,2) |  |
| C | Giant one-humped camel | Animal | No | Above ground | Yes | Yes | 4,055,000 | 500 | any desert |  |
| O | Giant opossum | Animal | No | Above ground | No | Yes | 221,040 | 500 | Any temperate forest, temperate shrubland, temperate savanna, temperate grassland | Benign |
| O | Giant orca | Animal | No | Aquatic | No | Yes | 20,000,000 | 500 | Any ocean | Benign |
| O | Giant oriole | Animal | No | Above ground | Yes | Yes | 200,280 | 500 | Forest temperate broadleaf |  |
| O | Giant osprey | Animal | No | Above ground | No | Yes | 214,020 | 500 | Any ocean, any lake, any river, tropical freshwater marsh, tropical saltwater marsh, temperate freshwater marsh, temperate saltwater marsh | Lays eggs, Benign |
| O | Giant osprey | Animal | No | Aquatic | No | Yes | 214,020 | 500 | Any ocean, any lake, any river, tropical freshwater marsh, tropical saltwater marsh, temperate freshwater marsh, temperate saltwater marsh | Lays eggs, Benign |
| O | Giant ostrich | Animal | No | Above ground | No | Yes | 857,700 | 1000 | Tropical savanna, tropical grassland, any desert | Lays eggs, Benign |
| O | Giant otter | Animal | No | Aquatic | No | Yes | 270,500 | 500 | Any pool, any lake, any river | Benign |
| P | Giant pangolin | Animal | No | Above ground | No | Yes | 235,100 | 500 | Tropical grassland, tropical savanna, tropical shrubland, any tropical forest | Benign |
| P | Giant parakeet | Animal | No | Above ground | No | No | 200,840 | 500 | Tropical grassland, tropical savanna, tropical shrubland, any tropical forest | Lays eggs, Benign |
| L | Giant peach-faced lovebird | Animal | No | Above ground | No | No | 200,419 | 500 | Temperate grassland, temperate savanna, temperate shrubland, temperate broadleaf forest | Lays eggs |
| P | Giant penguin | Animal | No | Aquatic | No | Yes | 228,080 | 500 | Arctic ocean | Lays eggs, Benign |

---
*Parte 1 de 3 de «Alternate creature sorting». Demais partes em arquivos `...-part-{1..3}.md` na mesma pasta. Fonte: https://dwarffortresswiki.org/index.php/Alternate_creature_sorting*
