# Object testing arena

> Fonte: [Object testing arena](https://dwarffortresswiki.org/index.php/Object_testing_arena) — Dwarf Fortress Wiki (GFDL/MIT)

The **object testing arena** is a special game mode accessible through the main menu where the player can alternate between spawning creatures, manipulating objects and features such as the weather and temperature. It is a tremendously useful place, usable for testing modded raws, or determining which skills to train against which enemies... or you can just have some fun carnage by spawning 50 steel-clad dwarves and setting them on some unarmed elves for that combat log goodness. It's possible to save games in it, in order to continue testing from a previous session.

In this version of the game, there are three choices of arenas: small arena, forest and classic arena, with the last choice being the same arena from older versions of *Dwarf Fortress*. Unlike the older versions of the game, the player can no longer butcher corpses, nor control them as if playing adventure mode, though this is most likely due to the game not yet having adventure mode.

## Spawning creatures

The list of creatures can be seen with the key - press to create a creature, select the creature type, skills and equipment, and then press . Press (or whatever you bound "leave screen" to) to cancel without creating the creature. You cannot delete creatures, but you can, however, press then (in the menu) to create a stone wall, instantly killing anything on that tile. Creatures with the or tokens can't be spawned in the object testing arena, unless the aforementioned tags are removed from their raw files. Note that some creatures with no combat capabilities (such as vermin) cannot be spawned, regardless of having the aforementioned tokens or not. Additionally, many procedurally-generated creatures such as megabeasts, titans, angels and demons are unavailable to be spawned.

### Inventory and skills

While in the creature placement menu, it is possible to add skills to your creatures, such as the fighter skill, or weapons, ammo, and armor. Creatures unable to use the weapons given to them will drop them upon unpausing, but creatures such as dwarves will happily do so, as long as they at least have dabbling-rank in its associated skill. You can also set exactly how much of a certain item you want when you select it, by using the or keys, which is the only way to get a creature to hold more than one piece of ammo, as the arena lacks an option for spawning quivers or backpacks.

### Conditions

A creature can be created with a unique condition from an interaction by pressing in the creation menu. In vanilla games, the available effects are the interactions of necromancers, animated corpses, disturbed dead, accursed, werebeasts and vampires, including any modded interaction with a defined arena name.

### Teams

It is possible to 'Team' creatures up by pressing and in the creation menu which is shown on the top left-hand side. There are 9999 teams (instead of 99 as in the previous versions), as well as "Independent", which is the default and acts as every creature for itself.

In this way, you can create simulated battles against beasts or enemies - for example, twenty sword-users versus twenty macemen - and analyze the battle from gamelog.txt. (Necromancers and disturbed dead that are marked as Independent will **not** be at peace with the zombies that they raise. This is not a bug, because arena independence overrides anything else.)

### Nature of conflict

The level of conflict between creatures or alliances can be controlled in the main screen with the keys and . The available settings are, from most lethal to least:

-

-

-

-

-

-

-

Morale may also be switched on or off, by clicking the option at the right side of the screen.

## Spawning liquids and trees

From the loo/create menu, press to spawn a 7/7 unit of lava, or to spawn 7/7 water on the currently selected tile. If you place water and then lava in the same tile, they will immediately form a 'Rough-hewn Rock Wall' (i.e. before you unpause), resulting in no spillage. However, placing lava and then water fills the tile with lava-hot water, which then instantly turns to steam upon unpausing. It is also possible to spawn rock walls in mid-air, usually causing a cave-in. You can place fluids in a tile that also has a wall in it; the result is a tile with both a wall *and* 7/7 units of the fluid you placed (water or lava). This combination behaves exactly the same as normal water without the wall would, except the area is still considered inaccessible for water to move through.

Multi-tile trees are also available from the loo/create menu, under ree. Using the submenu on the right, you can select the species of tree and set its ge. Pressing will spawn a tree at the cursor using the current settings. Trees can be placed anywhere, even a rock block floor or in *mid-air* (the latter will also cause a cave-in, amusingly replacing intermediate rock block floors with sand). Arena-created trees do not spawn with roots, nor is it possible to chop down a tree, though they can be burned by spawning lava, killing the tree.

## Fighting in the Arena yourself

Loo at any creature, and press to play as them, or to exit back to the main mode.

- The controls here are exactly the same as in adventurer mode, except that attempting to a corpse results in the corpse being butchered.

## Controlling the environment

The arena's environment can be modified in-game by pressing . From this screen, you can adjust Weather, Temperature, and Time. You can also press to cover every map tile in snow, to make everything muddy, and to remove all mud and snow.

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

- Dragonfire -
- Magma -
- Fire -
- Scorching -
- Hot -
- Warm -
- Cool -
- Cold -
- Subterranean -
- Freezing -
- Below freezing -
- Deathly cold -
- Absolute zero -

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

The layout of the arena zone is stored in the (DF)/data/init folder. Modifications to this file will not change the dimensions of the arena; they can only change the initial tiles and fluids present.

The arena is composed of 9 z-levels (including Z=0, from Z=-4 to Z=4) of 144 x 144 tiles; the contents of each tile are specified by a single character:

[TABLE]

1.  Tile will have no floor unless a pillar/wall is constructed on the z-level below.
2.  Only seems to work when placed on map edge; behaves identically to capital `W` otherwise.
3.  Only one type will be present, but it will be randomly selected each time you enter the Arena.

## Trivia

- Due to how "teams" are handled in the testing arena, strange behaviors can occur when necromancers and mummies are resurrecting nearby deceased and detached body parts. For example, a necromancer revives the body parts of a dead, dismembered dwarf in an effort to aid itself in fighting, but because the dwarf was on the "independent" team (or just a different one from the necromancer), the body parts just end up attacking the necromancer that raised them. So said necromancer may end up killing what it resurrected, only to keep resurrecting what it just killed to fight it again, which can happen over and over in an endless loop - all due to the clashing of how the arena handles teams/sides and the necromancer's natural AI in raising the dead to help itself.
