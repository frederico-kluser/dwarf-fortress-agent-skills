# Object testing arena

> Fonte: [Object testing arena](https://dwarffortresswiki.org/index.php/Object_testing_arena) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

Layout of the classic arena, similar to arena in previous verisons.

The **object testing arena** is a special game mode accessible through the main menu where the player can alternate between spawning creatures, manipulating objects and features such as the weather and temperature. It is a tremendously useful place, usable for testing modded raws, or determining which skills to train against which enemies... or you can just have some fun carnage by spawning 50 steel-clad dwarves and setting them on some unarmed elves for that combat log goodness. It's possible to save games in it, in order to continue testing from a previous session.

In this version of the game, there are three choices of arenas: small arena, forest and classic arena, with the last choice being the same arena from older versions of *Dwarf Fortress*.

## Spawning creatures

Many creatures packed into one area.

The list of creatures can be seen with the k key - press c to create a creature, select the creature type, skills and equipment, and then press enter. Press Esc (or whatever you bound "leave screen" to) to cancel without creating the creature. You cannot delete creatures, but you can, however, press w then l (in the k menu) to create a stone wall, instantly killing anything on that tile. Creatures with the [`[ARENA_RESTRICTED]`](/index.php/Creature_token#ARENA_RESTRICTED "Creature token") or [`[DOES_NOT_EXIST]`](/index.php/Creature_token#DOES_NOT_EXIST "Creature token") tokens can't be spawned in the object testing arena, unless the aforementioned tags are removed from their raw files. Note that some creatures with no combat capabilities (such as vermin) cannot be spawned, regardless of having the aforementioned tokens or not. Additionally, many procedurally-generated creatures such as forgotten beasts or titans are unavailable to be spawned.

### Inventory and skills

While in the creature placement menu, it is possible to add skills to your creatures, such as the fighter skill, or weapons, ammo, and armor. Creatures unable to use the weapons given to them will drop them upon unpausing, but creatures such as dwarves will happily do so, as long as they at least have dabbling-rank in its associated skill. You can also set exactly how much of a certain item you want when you select it, by using the + or - keys, which is the only way to get a creature to hold more than one piece of ammo, as the arena lacks an option for spawning quivers or backpacks.

### Conditions

A creature can be created with a unique condition from an interaction by pressing u in the creation menu. In vanilla games, the available effects are the interactions of necromancers, animated corpses, different ranks of dungeon guardians, disturbed dead, accursed, werebeasts and vampires, including any modded interaction with a defined arena name.

### Teams

It is possible to 'Team' creatures up by pressing s and d in the creation menu which is shown on the top left-hand side. There are 9999 teams (instead of 99 as in the previous versions), as well as "Independent", which is the default and acts as every creature for itself.

In this way, you can create simulated battles against beasts or enemies - for example, twenty sword-users versus twenty macemen - and analyze the battle from gamelog.txt. (Necromancers and disturbed dead that are marked as Independent will **not** be at peace with the zombies that they raise. This is not a bug, because arena independence overrides anything else.)

### Nature of conflict

The level of conflict between creatures or alliances can be controlled in the main screen with the keys shift+C and c. The available settings are, from most lethal to least:

- No Quarter
- Lethal
- Non-lethal
- Brawl
- Training
- Horseplay
- Encounter

Morale may also be switched on or off, by clicking the option at the right side of the screen.

## Spawning liquids and trees

From the look/create menu, press l to spawn a 7/7 unit of lava, or w to spawn 7/7 water on the currently selected tile. If you place water and then lava in the same tile, they will immediately form a 'Rough-hewn Rock Wall' (i.e. before you unpause), resulting in no spillage. However, placing lava and then water fills the tile with lava-hot water, which then instantly turns to steam upon unpausing. It is also possible to spawn rock walls in mid-air, usually causing a cave-in. You can place fluids in a tile that also has a wall in it; the result is a tile with both a wall *and* 7/7 units of the fluid you placed (water or lava). This combination behaves exactly the same as normal water without the wall would, except the area is still considered inaccessible for water to move through.

Multi-tile trees are also available from the look/create menu, under tree. Using the submenu on the right, you can select the species of tree and set its age. Pressing enter will spawn a tree at the cursor using the current settings. Trees can be placed anywhere, even a rock block floor or in *mid-air* (the latter will also cause a cave-in, amusingly replacing intermediate rock block floors with sand). Arena-created trees do not spawn with roots, nor is it possible to chop down a tree, though they can be burned by spawning lava, killing the tree.

## Fighting in the Arena yourself

Look at any creature, and press a to play as them, or ctrl+a to exit back to the main mode.

- The controls here are exactly the same as in adventurer mode, except that attempting to a a corpse results in the corpse being butchered.

## Controlling the environment

The arena's environment can be modified in-game by pressing w. From this screen, you can adjust Weather, Temperature, and Time. You can also press s to cover every map tile in snow, m to make everything muddy, and x to remove all mud and snow.

### Weather

This section has 4 options, each of which can be set to various settings:

- Cumulus
  - No cumulus clouds
  - Scattered cumulus
  - Many cumulus (rain)
  - Cumulonimbus (rain)
- Cirrus (toggle)
- Stratus
  - No stratus
  - Altostratus
  - Stratus (rain)
  - Nimbostratus (rain)
- Fog
  - No fog
  - Thin mist
  - Fog
  - Thick fog

As expected, the options marked with "(rain)" will cause it to start raining.

### Temperature & Time

The arena's temperature and time can be set to one of 13 settings, each:

- Dragonfire - 50000 °U
- Magma - 12000 °U
- Fire - 11000 °U
- Scorching - 10080 °U
- Hot - 10070 °U
- Warm - 10050 °U
- Cool - 10035 °U
- Cold - 10020 °U
- Subterranean - 10015 °U
- Freezing - 9999 °U
- Below freezing - 9968 °U
- Deathly cold - 9850 °U
- Absolute zero - 9508 °U **!**

------------------------------------------------------------------------

- Dawn (5:30am)
- Morning (8:00am)
- Late morning (10:30am)
- Noon (1:00pm)
- Early afternoon (2:00pm)
- Late afternoon (3:30pm)
- Early evening (5:00pm)
- Evening (6:30pm)
- Dusk (8:30pm)
- Night (10:00pm)
- Midnight (12:00am)
- Late night (2:00am)
- Early morning (4:00am)

## Modifying the Arena layout

|                                                    |
|----------------------------------------------------|
| File |
| prefs                                              |
| arena.txt                                          |

The layouts of the default arena zones are stored in `data/init/arena.txt`, and can also be changed by manually placing your own file at `prefs/arena.txt`v52.02; the location of the `prefs` folder depends on the portable mode setting (there is also a `data` folder there, but `data/init/arena.txt` will always be in the game installation folder). Modifications to these files will not change the dimensions of the arena; they can only change the initial tiles and fluids present. Files in both `data/init/` and `prefs/` are read when Dwarf Fortress starts, in that order, with the last value read for an option being used.

The arena is composed of 9 z-levels (including Z=0, from Z=-4 to Z=4) of 144 x 144 tiles; the contents of each tile are specified by a single character:

Character
Description

#
Empty tile [1]

C
Chasm

.
Block floor

P
Block pillar/wall

R
Block ramp

F
Block fortification

+
Water source [1] [2]

W
7/7 water [1]

w
7/7 water + upward ramp

L
7/7 magma/lava [1]

l
7/7 magma/lava + upward ramp

g
Grass [3]

T
Tree [3]

~
Sand [3]

,
Soil [3]

1.  Tile will have no floor unless a pillar/wall is constructed on the z-level below.
2.  Only seems to work when placed on map edge; behaves identically to capital `W` otherwise.
3.  Only one type will be present, but it will be randomly selected each time you enter the Arena.

## Trivia

- Due to how "teams" are handled in the testing arena, strange behaviors can occur when necromancers and mummies are resurrecting nearby deceased and detached body parts. For example, a necromancer revives the body parts of a dead, dismembered dwarf in an effort to aid itself in fighting, but because the dwarf was on the "independent" team (or just a different one from the necromancer), the body parts just end up attacking the necromancer that raised them. So said necromancer may end up killing what it resurrected, only to keep resurrecting what it just killed to fight it again, which can happen over and over in an endless loop - all due to the clashing of how the arena handles teams/sides and the necromancer's natural AI in raising the dead to help itself.
