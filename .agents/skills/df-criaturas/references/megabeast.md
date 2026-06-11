# Megabeast

> Fonte: [Megabeast](https://dwarffortresswiki.org/index.php/Megabeast) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

|  |
|:--:|
|   This article or section contains **minor spoilers**. You may want to avoid reading it. |

**Megabeasts** are special and very powerful "boss" creatures who are created during world generation, each associated with a number of spheres. They are named historical figures - the game will announce their presence by name. They are similar to semi-megabeasts, but tend to be larger, rarer and more powerful. Whether they may attack and how often can be adjusted in the difficulty settings.

Graphically, the sprites that titans and forgotten beasts use will be of randomly-generated creatures with random colors that resemble the generated appearance they've been given. This same setup is used for other procedurally-generated creatures, such as demons, experiments and angels.

## Megabeast species

-  / `C` Bronze colossus
-  / `D` Dragon
-  / `?` Forgotten beast
-  / `H` Hydra
-  / `R` Roc
-  / `?` Titan

## Description

Looks like it makes ear-piercing screech sounds.\
*Art by DasTactic*

"Nooo! Our least favorite pharaoh was in that temple."\
*Art by Devilingo*

Megabeasts are created systematically during world generation. Newly-generated worlds are populated by initial populations of historical figures, megabeasts among them. The amount of megabeasts created at world generation is random, but based on two factors: the size of the world ("World Size"), and their prevalence ("Number of Beasts"). Megabeasts' presence (or lack thereof) is a major factor in world history. Over time, they will accumulate long kill lists, and the baddest of the bunch will acquire nicknames and god-like associations with their spheres.

Megabeasts are a distinct and serious threat to early development, threatening many a young outpost; but, inevitably, as the world matures, populations rise, and new settlements are founded, they become increasingly harassed. Although megabeasts will come out on top of almost any encounter, enough dice rolls and they *will* go down, felled by a lucky human - or other sapient creature - clearing the way for their fellows. The longer the world history, the more megabeasts are confronted and killed off, and the safer the world becomes for civilization. In most worlds, calendar ages go through three stages, the Age of Myth, the Age of Legends, and the Age of Heroes, each with a progressively-higher % of megabeasts killed.

Some megabeasts (namely, all but the bronze colossus and procedurally-generated ones) can reproduce during world generation, but such an event is fantastically unlikely, for two reasons: The first is that megabeasts are immensely rare and elusive, and almost never bump into one another. The second is that the starting population of megabeasts is also their population cap, meaning that other megabeasts must die before new ones can be born. Megabeasts will reproduce within players' fortresses if they are lucky enough to cage and train two specimens of opposite sexes.

In world generation, all megabeasts claim and live in a lair, a hunting (or, perhaps, *haunting*) ground from which they will attack other creatures, both wildlife and civilized settlements. A megabeast sharing its lair with another megabeast of the other gender is also far more likely to reproduce, than if the two had been wandering the world. Lairs can and do change, however, sometimes regularly, and older megabeasts have called many a place their home. Also, megabeasts have been found fighting each other, leading to hilarious reports of fireballs and cave ins.

Most megabeasts will not attack the player until they have accumulated a minimum wealth of 100,000☼, exported wealth of at least 10,000☼, *and* a minimum population of 80 dwarves. Titans ignore exported wealth, and the only requirements for forgotten beasts are 50,000☼ in created wealth and a discovered cavern. What megabeasts appear, if any do at all, is also influenced by which ones are closest to the player; a dragon with a lair nearby is far more likely to attack than a roc several weeks away. Nonetheless, force-quitting and loading a fortress from a few days before a megabeast attack may result in a different one arriving on the same day, or later, or nothing arriving at all, depending on what has survived world generation.

Megabeast and night creature attacks are handled the same way as caravan/diplomat visits and migrant waves - at the beginning of the season, the game decides that it's going to happen and sets a timer, and the event happens once the timer runs out. Notably, megabeast and night creature events simply choose a random "eligible" (i.e. able to survive in your fortress's biome) creature from anywhere in the world, and make it instantly appear at your doorstep.

After an attack on a settlement in worldgen, megabeasts tend to be worshipped by dwarves, most likely out of fear and the hope that worshiping the megabeast may persuade it to not eat its worshippers (this currently does not work at all). The megabeast is listed as *object of worship* on the dwarves' relationship screen. This does not change your dwarves' behaviour when confronted with an object of worship, nor the megabeast's behaviour when bumping into its worshippers.

## Attributes

The different types of large, unique creatures have similar, though slightly differing properties. These behaviors are mostly of interest to modders creating custom creatures.

|  |  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|----|
| Attribute | \[MEGABEAST\] / \[SEMIMEGABEAST\] | [`[TITAN]`](/index.php/Creature_token#TITAN "Creature token") | [`[FEATURE_BEAST]`](/index.php/Creature_token#FEATURE_BEAST "Creature token") | [`[POWER]`](/index.php/Creature_token#POWER "Creature token") | [`[UNIQUE_DEMON]`](/index.php/Creature_token#UNIQUE_DEMON "Creature token") | [`[DEMON]`](/index.php/Creature_token#DEMON "Creature token") | [`[NIGHT_CREATURE]`](/index.php/Creature_token#NIGHT_CREATURE "Creature token") | Others |
| Show / \[DESCRIPTION\] / on / histfig / entries / 1 |  | Yes | Yes |  |  | Yes | Yes |  |
| Rampages | Yes | Yes | Yes |  |  |  |  |  |
| Exclude materials from stockpile |  | Yes | Yes |  |  | Yes | Yes | [`[EQUIPMENT]`](/index.php/Creature_token#EQUIPMENT "Creature token") |
| Makes friends in Worldgen |  | No | No |  |  | No | No | [`[EQUIPMENT]`](/index.php/Creature_token#EQUIPMENT "Creature token") can't |
| Can be Experiment |  | No | No | No | No | No |  | [`[SUPERNATURAL]`](/index.php/Creature_token#SUPERNATURAL "Creature token"), and castes with [`[FANCIFUL]`](/index.php/Creature_token#FANCIFUL "Creature token") |
| Record all duels | Yes | Yes | Yes |  |  |  |  | Deities, forces, and positions with precedence 1 |
| Worldgen Beast | Yes |  | Yes | Yes |  |  | [`[NIGHT_CREATURE_HUNTER]`](/index.php/Creature_token#NIGHT_CREATURE_HUNTER "Creature token") only |  |
| Worldgen Monster | Yes | Yes | Yes | Yes |  |  | [`[NIGHT_CREATURE_HUNTER]`](/index.php/Creature_token#NIGHT_CREATURE_HUNTER "Creature token") only |  |
| Can worship gods |  | No | No | No2 |  | No | No |  |
| Can be preferred pet |  | No | No |  | No |  |  | [`[EQUIPMENT]`](/index.php/Creature_token#EQUIPMENT "Creature token") can't |
| Unknown to civilizations (?) |  |  | Yes3 |  |  |  |  |  |

Monster tokens

1: These creatures are usually [`[GENERATED]`](/index.php/Creature_token#GENERATED "Creature token").

2: [`[POWER]`](/index.php/Creature_token#POWER "Creature token") also causes a creature to impersonate a deity.

3: Not listed in image creation interfaces (for engravings, symbols etc.) as long as one caste is a [`[FEATURE_BEAST]`](/index.php/Creature_token#FEATURE_BEAST "Creature token").

Source: User:Putnam3145 on Kitfox Games Discord

A standard winter in-game.\
*Art by IansInventories*
