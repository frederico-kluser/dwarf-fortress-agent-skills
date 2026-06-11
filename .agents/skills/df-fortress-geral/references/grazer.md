# Grazer

> Fonte: [Grazer](https://dwarffortresswiki.org/index.php/Grazer) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

The grass tastes exactly like ramen to them.

Tame **grazing** animals (those with the [`[STANDARD_GRAZER]`](/index.php/Creature_token#STANDARD_GRAZER "Creature token") token) require a constant source of grass or cave moss to survive. Pastures are currently the easiest such source, however care must be taken to ensure that the pasture is large enough to provide food for all the assigned animals (and any auto-assigned babies). Other sources are animal caretakers feeding chained/caged creatures, and dwarves feeding their pets.

## Grazing animals and pasture size

Grazing animals use the [`[STANDARD_GRAZER]`](/index.php/Creature_token#STANDARD_GRAZER "Creature token") which calculates a value from this formula:

    GRAZER = 20000 × G × (max size)-3/4

***G** can be set in d_init or the game tab in settings, listed as Grazing Coefficient (100 by default)*

***max size** is the maximum size a creature can reach, divided by 10.*

*The minimum resulting GRAZER value is capped at 150, the maximum at 3 million.*

For custom creatures, you could also set the value directly with the `[``GRAZER``:]` token. In either case, this is an inverse number - the GRAZER value signifies how much hunger is reduced when eating a unit of grass. (Hunger increases every tick; a creature dies when it reaches 100,000). A creature with ten times the grazer value needs one tenth the amount of grass (and hence, pasture land) as a creature with a small grazer value. Because of this, it may be wise to give larger animals grazing areas separate from other animals, as the larger animals are likely to not leave enough grass for other animals, which can lead to them starving. If you started your fortress in an undead biome, you may need to assign more space for a pasture, as much of the grass is dead - animals will not eat dead grass and will only eat the still-living patches.

Animals which graze are typically good livestock candidates, as many of them can be milked and three also can be sheared for wool. Creatures with larger sizes consume more grass, but also produce more meat when butchered. Grazing animals who are pets will occasionally be fed by their owners, allowing them to roam free without the need of a pasture, however this is unreliable due to pet feeding being a very low-priority job, often leading to these pets starving and possibly dying if not supervised. If grazing animals consume all the grass on a tile, the tile will be reverted to the base layer material, which may be sand, clay or soil. In this way, you receive a visual clue as to the size of the pasture required.

## List of grazing animals

Take the following numbers with a grain of salt; they ignore the differing abilities of various biomes to replenish grass and are instead based on a rule of thumb that 20000=Grazer\*Required_tiles. Usually you can get along with way smaller pastures. Nevertheless, a fairly large herd can cause overgrazing fast, so keep an eye out for hungry animals and desolate grassless pastures.

|  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|
| Animal | Grazer / value | Creature / Size | Milkable | Shearable | Recommended Pasture Size / per individual | Needed Tiles (per rule-of-thumb) | Sqrt of Needed Tiles |
| Elephant | 106.366 | 5,000,000 |  |  | 19 × 10 | 188.03 | 13.7 |
| Giant bull moose | 119.990 | 4,257,750 |  |  | 14 × 12 | 166.68 | 12.9 |
| Rhinoceros | 156.023 | 3,000,000 |  |  | 13 × 10 | 128.19 | 11.3 |
| Giant moose cow | 176.008 | 2,554,650 |  |  | 13 × 9 | 113.63 | 10.7 |
| Draltha | 178.885 | 2,500,000 |  |  | 14 × 8 | 111.80 | 10.6 |
| Gigantic panda | 318.005 | 1,160,900 |  |  | ~~9 × 7~~ ♠ | ~~62.89~~ ♠ | ~~7.9~~ ♠ |
| Water buffalo | 355.656 | 1,000,000 | Yes |  | 10 × 6 | 56.23 | 7.5 |
| Giraffe | 355.656 | 1,000,000 |  |  | 10 × 6 | 56.23 | 7.5 |
| Yak | 464.736 | 700,000 | Yes |  | 9 × 5 | 43.04 | 6.6 |
| Cow | 521.695 | 600,000 | Yes |  | 8 × 5 | 38.34 | 6.2 |
| Unicorn | 521.695 | 600,000 |  |  | 8 × 5 | 38.34 | 6.2 |
| Bull moose | 576.648 | 525,000 |  |  | 7 × 5 | 34.68 | 5.9 |
| Giant capybara | 578.011 | 523,350 |  |  | 7 × 5 | 34.60 | 5.9 |
| Horse | 598.140 | 500,000 | Yes |  | 7 × 5 | 33.44 | 5.8 |
| Camel (both) | 598.140 | 500,000 | Yes |  | 7 × 5 | 33.44 | 5.8 |
| Mule | 707.107 | 400,000 |  |  | 6 × 5 | 28.28 | 5.3 |
| Cow moose | 845.857 | 315,000 |  |  | 5 × 5 | 23.64 | 4.9 |
| Donkey | 877.383 | 300,000 | Yes |  | 5 × 5 | 22.80 | 4.8 |
| Elk | 877.383 | 300,000 |  |  | 5 × 5 | 22.80 | 4.8 |
| Muskox | 911.793 | 285,000 |  |  | 5 × 5 | 21.93 | 4.7 |
| Giant red panda | 1,053.393 | 235,100 |  |  | ~~5 × 4~~ ♠ | ~~18.99~~ ♠ | ~~4.4~~ ♠ |
| Tapir | 1,189.207 | 200,000 | Yes |  | 6 × 3 | 16.82 | 4.1 |
| Llama | 1,286.991 | 180,000 | Yes | Yes | 4 × 4 | 15.54 | 3.9 |
| Deer | 1,553.939 | 140,000 |  |  | 5 × 3 | 12.87 | 3.6 |
| Reindeer | 1,642.754 | 130,000 | Yes |  | 5 × 3 | 12.17 | 3.5 |
| Panda | 1,642.754 | 130,000 |  |  | ~~5 × 3~~ ♠ | ~~12.17~~ ♠ | ~~3.5~~ ♠ |
| Warthog | 2,000.000 | 100,000 |  |  | 4 × 3 | 10.00 | 3.2 |
| Elk bird | 2,000.000 | 100,000 |  |  | 4 × 3 | 10.00 | 3.2 |
| Kangaroo | 2,164.453 | 90,000 | Yes |  | 4 × 3 | 9.24 | 3.0 |
| Alpaca | 2,613.403 | 70,000 | Yes | Yes | 4 × 2 | 7.65 | 2.8 |
| Goat | 3,363.586 | 50,000 | Yes |  | 3 × 2 | 5.95 | 2.4 |
| Mountain goat | 3,363.586 | 50,000 |  |  | 3 × 2 | 5.95 | 2.4 |
| Ibex | 3,363.586 | 50,000 |  |  | 3 × 2 | 5.95 | 2.4 |
| Impala | 3,363.586 | 50,000 |  |  | 3 × 2 | 5.95 | 2.4 |
| Sheep | 3,363.586 | 50,000 | Yes | Yes | 3 × 2 | 5.95 | 2.4 |
| Capybara | 3,640.161 | 45,000 |  |  | 3 × 2 | 5.49 | 2.3 |
| Wombat | 5,656.854 | 25,000 |  |  | 2 × 2 | 3.54 | 1.9 |
| Gazelle | 6,687.403 | 20,000 |  |  | 2 × 2 | 2.99 | 1.7 |
| Hoary marmot | 11,246.827 | 10,000 |  |  | 2 × 1 | 1.78 | 1.3 |
| Red panda | 18,914.832 | 5,000 |  |  | ~~2 × 1~~ ♠ | ~~1.06~~ ♠ | ~~1.0~~ ♠ |
| Hare | 24,716.044 | 3,500 |  |  | 1 × 1 | 0.81 | 0.9 |
| Groundhog | 27,745.276 | 3,000 |  |  | 1 × 1 | 0.72 | 0.8 |
| Cavy | 74767.439 | 800 |  |  | 1 × 1 | 0.27 | 0.5 |
| Rabbit | 106365.918 | 500 |  |  | 1 × 1 | 0.19 | 0.4 |

Key
♠ the four panda species will eat *only bamboo* (any type), in effect requiring much larger pasture areas even on maps where bamboo does grow, and modding to survive on maps where it doesn't

The giant animals not listed here are not included yet because that's a bunch more work, and I'm unsure how many of them (if any) are still bugged.

## Bugs

- Grass does not grow back on mountain biomes.Bug:4164
- Egg-laying grazers will starve themselves sitting on a nest box.Bug:4637
  - Some workarounds are detailed in this forum thread.
- Grazing juveniles tend to clump in the same tile as their mother, leading to starvation and overcrowding. This is particularly problematic for species with large litters, like giant capybaras.\[Verify\]
- When a civilian alert is active, grazers outside of the alert burrow refuse to eat.Bug:6240
