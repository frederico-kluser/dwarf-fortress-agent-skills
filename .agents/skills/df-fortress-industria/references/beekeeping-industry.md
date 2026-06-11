# Beekeeping industry

> Fonte: [Beekeeping industry](https://dwarffortresswiki.org/index.php/Beekeeping_industry) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

The **beekeeping industry** is an agricultural process that involves farming honey bees in built hives to produce honeycombs and royal jelly, the former of which is further processed into honey and wax. The primary skill and labor used in the industry is beekeeping.

## Setup

### Finding wild bees

Beekeeping industry flowchart

Wild colonies of honey bees must be present on the map. Since live vermin cannot be bought during embark, wild bees are necessary to start beekeeping. Colonies of honey bees can appear in any non-freezing land biome, which excludes mountains, glaciers, and tundras. While they are common in places they appear (`[``FREQUENCY``:100]`), bees are not [`[UBIQUITOUS]`](/index.php/Creature_token#UBIQUITOUS "Creature token"), thus are not guaranteed to appear in every region.

Bumblebees cannot be used in beekeeping.[1] They do possess their own version of honey, royal jelly, wax, and even mead, all of which are unobtainable in normal gameplay.

Honey bees are one of the [`[VERMIN_SOIL_COLONY]`](/index.php/Creature_token#VERMIN_SOIL_COLONY "Creature token") creatures, which includes bumblebees, ants, and termites. Maps have a hard limit to how many wild colonies can appear simultaneously. If new colonies stop appearing, it means this limit has been reached. Therefore, honey bee colonies might be unable to spawn because the "space" is occupied by other vermin colonies. Building dirt roads over existing colonies frees up space for new ones to generate.

If a colony cannot be found after searching, set up a single hive and leave it for about a year as a last-ditch effort. Beekeepers will immediately be able to find an accessible honey bee colony that may have gone unnoticed or spawned inconspicuously.

### Building hives

|  |  |  |
|----|----|----|
| Material | Workshop | Labor |
| Ceramic | Kiln or magma kiln | Pottery |
| Glass | Glass furnace or magma glass furnace | Glassmaking |
| Metal | Metalsmith's forge or magma forge | Metalcrafting |
| Stone | Craftsdwarf's workshop | Stonecrafting |
| Wood | Craftsdwarf's workshop | Woodcrafting |

Workshop and labor requirements

Hives are a tool. They can be made in a variety of hard materials from their respective workshops and labors. Beekeepers themselves do not craft them. Hives are stored in finished goods stockpiles.

Hives can be built (bofh) on any hard surface, both indoors and outdoors from the Workshops FARMING tab. Only beekeepers can haul and place hives.

Tile attributes affect honey production. In order for hives to produce, they must be built adjacent to (or on) an above ground tile. Subterranean hives cannot produce anything, but can store colonies to be split later. Clicking on a hive will show whether it has "Outdoor access" or "No outdoor access" - relating to the above ground or subterranean attribute respectively. So long as hives are placed adjacent to or on an above ground tile, they can be completely enclosed with constructions from outside while still creating products, allowing beekeepers to work safely at all times.

## Hive management

Managing hives is fairly automated–beekeepers will perform most of the necessary jobs on their own when available. There are two options in the building settings that can be toggled to control beekeepers from installing colonies or from gathering products in a hive. Hives are set by default to allow colony installation and product gathering.

In the t Task menu, two notable beekeeping jobs are:

- Install Colony In Hive – when a beekeeper installs a colony to a new hive.
- Collect Hive Products – when a beekeeper gathers the products from a hive.

### Examining hives

Clicking on the hive will display:

- Which options have been set for that hive:
  - Install colony when ready or Do not install colony.
  - Gather any products or Do not gather products.
- Whether it has Outdoor access or No outdoor access.
- If the hive is Ready to be split or Not ready to be split.
- If there are too many colonized hives on the map (due to a limit).

To see if a hive has a colony, click the hive to open the hive menu. If a colony is present, it will show a stack of live honey bees inside a built hive. It will also show if the hive contains a honeycomb or royal jelly.

### Colony installation

Beekeepers automatically haul colonies to new hives as long as they have access to a wild colony or another colony that is ready to be split from another hive. They must have their setting set to Install colony when ready. Hives set to Do not install colony will not accept new colonies, even after existing colonies are destroyed. If the settings change or the hive gets slated for removal before the beekeeper reaches the hive to install a new colony, then the job gets cancelled, and the hauled colony is removed from the beekeeper.

Beekeepers usually go for the closest available colony to install, whether it's a wild colony or a colony in a hive. Assigning beekeepers to burrows can prevent them from seeking other hives.

### Splitting colonies

Colonies can split in three months after installation. A split-able colony is indicated in the building settings as Ready to be split. Splitting colonies produce new colonies that are installed to other hives, thereby increasing the colony count. In order to split the colony, an empty hive and a beekeeper must be present. A beekeeper will perform a splitting automatically if an empty hive is set to allow colony installation. After splitting, beekeepers haul the new colony to an empty built hive. Doing this leaves the original hive populated, and after another three months, it will become ready for splitting again.

Splitting a colony does not reset the honeycomb and royal jelly production. Forbidding a hive or its colony will not prevent beekeepers from using the hive's colony for splitting. If a hive is slated for removal but has not been removed yet, then the split-able colony inside can still be used for installation.

### Gathering products

Hives containing colonies produce a single honeycomb and royal jelly. Honeycombs and royal jelly are "part" of the building, as indicated by the  or \[-\] symbol next to their names when viewing the building's items. When a beekeeper gathers them, the items are released from the hive, which allows a food hauler to carry the items to a stockpile. An empty jug is required to gather the products, since royal jelly must be stored in a container.

Hives must be set to Gather any products for beekeepers to go and gather their products. A honeycomb and royal jelly must both be present in a hive before they can be gathered. When these requirements are met, a beekeeper will automatically find an empty jug and gather the products for hauling. Beekeepers usually go for the closest accessible hive to gather first. If the settings change, or the hive gets slated for removal before the beekeeper reaches the hive to collect the products, then the job gets cancelled, and the jug is stored back.

The gathering process always destroys the colony inside the hive, which disappears instantly when destroyed. A new colony must be installed every time the products are gathered in order for the hive to produce more. To avoid colony extinction from gathering products, it is recommended to save a few hives just for splitting by changing their settings to not gather products. This would ensure a permanent supply of bees at all times.

### Limit

There is a soft limit of 40 colonies, which empty hives and wild or hauled colonies do not count against. When the number of colonies on the map reaches 41 or more, honeycomb and royal jelly no longer have a 100% possibility of spawning six months after installation. If the colony does not produce a honeycomb or royal jelly, then it has a chance to produce again every six months. The likelihood of spawning affects products individually, so it is possible that a honeycomb appears while royal jelly does not, and vice versa. The soft limit does not affect colonies that were installed before the limit had passed. Hives that contain colonies will have the following warning in the building settings when the soft limit is exceeded:

Too many hives\
\* Output restricted

The maximum limit of active colonies for honey production is 59. When the colony count reaches 60, no more hive products appear. It also resets all ongoing production, so any colony that was in the process of producing must wait at least six months again to produce honeycomb and royal jelly after the max limit is brought back down. When the max limit is reached, the warning message in the building settings reads:

Too many hives\
\* No output

The limits do not affect the spawning of wild colonies, nor the amount of time needed for colonies to become ready to split.

The total number of colonies can be checked in the stocks under "Small live animals" and hitting Tab to display individual stacks. Each stack represents a single colony. The number of colonies can exceed 60 by installing colonies into new hives (by splitting or collecting wild bees), but nothing is gained from doing this. To lower the number of colonies, either dismantle colonized hives, dump the colony, or allow beekeepers to gather existing products in the hive, which destroys the colony. To attain high output efficiency, keep the number of active hives below 41.

### Removing hives

Built hives can be removed using the hive menu (). A beekeeper is required to remove the hive. After the building is removed, the item is carried back to a finished goods stockpile by an item hauler. Hives can also be destroyed by building destroyers, cave-ins, and magma.

Deconstructing a hive releases the colony inside (it cannot be retrieved), as well as dropping any honeycomb, royal jelly, or jug left inside. Fallen honeycombs and jugs can be hauled back, but spilled royal jelly cannot.

## Production and processing

Six months after installing a colony, a hive produces one honeycomb `∞` and one royal jelly `≈`. Products have a 100% chance of spawning, unless the colony count exceeded the limit. Only one honeycomb and royal jelly will spawn at a time, and no further products will appear until they are gathered from the hive. The colony size does not affect the output speed; neither do the surroundings, plants, weather, or seasons affect production.

Royal jelly is a liquid food used as an ingredient in prepared meals, but it can only be cooked if another solid food item is included in the meal.

Honeycombs are classified as tools, and stored with other finished goods. As an intermediate product, honeycombs do not have any applications on their own, but when pressed at a screw press, each honeycomb produces two items: honey `≈` and pressed wax (or wax cake) `≈`, both of which are stored in food stockpiles. To press a honeycomb, add a new task in a screw press and select "Press honey from honeycomb", or search and select "Press honey from honeycomb" in the manager screen. An empty jug is needed for the job to store the honey.

Honey, like royal jelly, is a liquid food that can be cooked into a meal. Additionally, it can be brought to a still and brewed into mead, the only obtainable non-plant-based alcoholic drink. Wax can be processed into various crafts by a wax worker, which all have a material value of one.

## Bugs

- Stacks of honey bees in their hives can be mangled by forest fires, but will still live, resulting in some odd descriptions.Bug:4101
- Filled jugs may be stored in bins as finished goods, preventing the use of their contents in the food industry.Bug:4229

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\

The entire beekeeping industry is a bug exploit.(*with regards to the Apis genus, to be exact*)

You get used to the buzzing sounds. Honest.
