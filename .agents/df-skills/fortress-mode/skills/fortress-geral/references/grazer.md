# Grazer

> Fonte: [Grazer](https://dwarffortresswiki.org/index.php/Grazer) — Dwarf Fortress Wiki (GFDL/MIT)

Tame **grazing** animals (those with the token) require a constant source of grass or cave moss to survive. Pastures are currently the easiest such source, however care must be taken to ensure that the pasture is large enough to provide food for all the assigned animals (and any auto-assigned babies). Other sources are animal caretakers feeding chained/caged creatures, and dwarves feeding their pets.

## Grazing animals and pasture size

Grazing animals use the which calculates a value from this formula:

`GRAZER = 20000 × G × (max size)`^(`-3/4`)

***G** can be set in d_init or the game tab in settings, listed as Grazing Coefficient (100 by default)*

***max size** is the maximum size a creature can reach, divided by 10.*

*The minimum resulting GRAZER value is capped at 150, the maximum at 3 million.*

For custom creatures, you could also set the value directly with the token. In either case, this is an inverse number - the GRAZER value signifies how much hunger is reduced when eating a unit of grass. (Hunger increases every tick; a creature dies when it reaches 100,000). A creature with ten times the grazer value needs one tenth the amount of grass (and hence, pasture land) as a creature with a small grazer value. Because of this, it may be wise to give larger animals grazing areas separate from other animals, as the larger animals are likely to not leave enough grass for other animals, which can lead to them starving. If you started your fortress in an undead biome, you may need to assign more space for a pasture, as much of the grass is dead - animals will not eat dead grass and will only eat the still-living patches.

Animals which graze are typically good livestock candidates, as many of them can be milked and three also can be sheared for wool. Creatures with larger sizes consume more grass, but also produce more meat when butchered. Grazing animals who are pets will occasionally be fed by their owners, allowing them to roam free without the need of a pasture, however this is unreliable due to pet feeding being a very low-priority job, often leading to these pets starving and possibly dying if not supervised. If grazing animals consume all the grass on a tile, the tile will be reverted to the base layer material, which may be sand, clay or soil. In this way, you receive a visual clue as to the size of the pasture required.

## List of grazing animals

Take the following numbers with a grain of salt; they ignore the differing abilities of various biomes to replenish grass and are instead based on a rule of thumb that 20000=Grazer\*Required_tiles. Usually you can get along with way smaller pastures. Nevertheless, a fairly large herd can cause overgrazing fast, so keep an eye out for hungry animals and desolate grassless pastures.

[TABLE]

Key
♠ the four panda species will eat *only bamboo* (any type), in effect requiring much larger pasture areas even on maps where bamboo does grow, and modding to survive on maps where it doesn't

The giant animals not listed here are not included yet because that's a bunch more work, and I'm unsure how many of them (if any) are still bugged.

## Bugs

- Grass does not grow back on mountain biomes.
- Egg-laying grazers will starve themselves sitting on a nest box.
  - Some workarounds are detailed in this forum thread.
- Grazing juveniles tend to clump in the same tile as their mother, leading to starvation and overcrowding. This is particularly problematic for species with large litters, like giant capybaras.
- When a civilian alert is active, grazers outside of the alert burrow refuse to eat.
