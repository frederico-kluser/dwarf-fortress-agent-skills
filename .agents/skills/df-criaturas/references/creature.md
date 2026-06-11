# Creature

> Fonte: [Creature](https://dwarffortresswiki.org/index.php/Creature) — Dwarf Fortress Wiki (GFDL/MIT)

In *Dwarf Fortress*, a **creature** is defined as any animate, normally-mobile (and for the sake of this article, non-vermin) being that can interact with the world and any element inside it. The creatures in the game range from being entirely realistic to completely mythical. Although most creatures are animals, dwarves, giant cave spiders, and even megabeasts are all also considered creatures. Various creatures can and will interact with a fortress or adventurer in many different ways.

Some creatures have skills that match what type of creature they are (e.g. monkeys having legendary climbing skill). Though most creatures can be found in any mode, some are exclusive to adventure mode or fortress mode. Some creatures are randomly and procedurally generated, meaning they could have many different sprites in-game. Creatures of that type may have just one to a few sprites showcased out of many in the list below. A question mark placeholder may also be shown instead.

Also note that creatures with the or tokens cannot be spawned in the object testing arena, similarly to vermin (e.g. flies, worms).

Many standard-sized creatures in the game take the space of a single tile, while many giant versions of creatures, including many types of beasts, may take up the space of more than one tile. There are roughly 680 creatures in the game.

## Spawning

The creatures that will spawn on any given fortress map depend on the biome(s) that the fortress is in. Additionally, there are several creature tokens in the raws that deal with creature spawning:

- `[FREQUENCY:X]`: This tag dictates *how often* a creature will spawn. It ranges from 0-100, and is a comparative number, where the higher this number is, the more likely the creature is to spawn.
- `[CLUSTER_NUMBER:X]`: This determines *how many* creatures will appear at one time on a map.
- `[POPULATION_NUMBER:X]`: This determines the *total number* of this type of creature that can ever visit your fortress. The exact number varies, depending on the map.

For example, deer have a `[POPULATION_NUMBER:15:30]`, meaning that if you kill between 15-30 deer, no more deer will ever visit your fortress.

## Reading the Table

\|} The above columns indicate, in order:

- **Graphic:** The sprite assigned to the creature. Seen only in the Steam version.
- **Tile:** The tile assigned to the creature, how you will see it without a graphic set.
- **Name:** The name of the creature as it displays in-game.
- **Playable:** If "No", the creature is not playable in any modes. "Fort" indicates that the creature is playable in fortress mode (). "Adv" indicates that the creature is playable in adventure mode. All creatures except humans must have a population in an civilization in order to be playable in adventure mode; goblins (and other creatures) cannot be played from a goblin civ. Humans can be played whether or not a population exists due to , but an civ still needs to have existed at some point. Creatures with are also playable in adventure mode.
- **Hostile:** If "Yes", then the creature will attack on sight, if "No" then the creature is either neutral, or friendly. Undead creatures are always hostile to living things.
- **Food Source:** If "Yes", then the creature can be butchered into an edible substance that your dwarves will feed on.
- **Adult Body Size:** The average size of the creature when an adult. This can be anywhere from 500 for a rabbit to 25,000,000 for a dragon. This value represents the creature's volume in cm³, which, for creatures made of flesh, more-or-less equals the creature's weight in grams.1 These sizes do not correspond to the sizes which trigger pressure plates. Size is modified with height and broadness (i.e. incredibly skinny and short is below the average weight, while a fat and tall one is above it).
- **Pet Value:** This is the value the creature can be bought and sold for as a pet during trading.
- **Biome:** Where the creature can be found.
- **Features:** Any special features the creature possesses, including things such as causing a syndrome, breathing fire, or spinning webs.

Note: If you wish to view alternate ways of sorting creatures, such as sorting by biomes and location, or sorting domestic creatures by features, there is a new page found here: Alternate creature sorting

## Creatures

### Civilized

#### Main races

These are intelligent creatures that form the dominant civilized races of the world. While most are part of society, many have turned to Banditry.

\|}

1. Whether or not you are hostile with select civilized races depends on the history of your game world, and its length. Shorter histories mean less ongoing wars and less general hostility, good for a newer player to learn the basics.

2. Snatchers try to snatch children of other civilizations. Snatched individuals become part of the Snatcher's civilization.

#### Underground Tribes

Intelligent animal people that form crude civilizations underground, but will not trade with you. They wield some weapons and can join adventurers.

\|}

1. Whether an animal person civilization treats you as hostile or not seems random.

2. Ant-men body sizes depend on their caste.

### Livestock and Domestic Animals

Creatures that have long been domesticated, and either play a part in the meat industry, or are simply pets to keep dwarves company. Note: Except for wagons, domestic animals can be bought at embark, or requested from dwarven caravans. Animals of these types below that are caught in the wild with cage traps can be tamed after only one session with an animal trainer.

\|}

### Beasts and Monsters

All kind of monstrous creatures that roam the land and underground caverns, including: Semi-megabeasts, megabeasts, and randomly generated ones that can take any form. all very powerful and can easily be game-ending.

#### Semi-Megabeasts

\|}

#### Megabeasts

\|}

#### Procedurally generated

These creatures are procedurally generated, and different for every savefile. Their raws may be extracted from the world.dat file in uncompressed save folders. \|}

### Wild Animals

This section includes wild animals as well as their giant and humanoid counterparts. Wild animals are mostly found roaming the wilderness. Many of them are predators, while others are benign, and will not attack unless being attacked first. Some will be drawn to your stockpiles to steal drink food or something shiny. Some can be easily overcome, and yet others can be significant threats, like the dreaded elephant.

#### Above Ground

\|}

#### Subterranean

\|}

#### Aquatic

Note: This does not include subterranean sea creatures. \|}

#### Agitation

Disruption of the environment, such as deforestation or overfishing, may cause the appearance of "agitated" animals. Agitated animals, regardless of their normal behavior, will directly seek out and attack dwarves. Agitation can be removed by taming.

## Night Creatures / Other

### Night creatures

These creatures are either vicious creatures that attack in the night, or are created through certain interactions - be it a condition of the game, or intentionally by another creature. \|}

1. In some worlds, intelligent experiments escape their creators and join normal civilizations. They will then be playable in adventurer mode.\

2. The player cannot normally start out as an intelligent undead, but can unretire a former adventurer that has been resurrected. This can also be done (without unretiring) by using adventurer parties.\

3. The player cannot start out as a necromancer, but can gain necromancer powers by reading a slab or book containing the secrets of life and death.\

4. The player cannot start out as a vampire, but can become one if feeding on spilled vampire blood. Animal people with the ability to suck blood can also gain vampirism by blood-sucking a vampire during combat.

### Hidden Fun Stuff

\|}

†except in a few special cases

### Nonexistent

\|}
