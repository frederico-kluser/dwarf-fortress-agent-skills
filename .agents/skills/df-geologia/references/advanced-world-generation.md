# Advanced world generation

> Fonte: [Advanced world generation](https://dwarffortresswiki.org/index.php/Advanced_world_generation) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*This article contains information on advanced world generation. For information on basic world generation, see World generation.* *See World token to more easily find information by the names used in the world_gen.txt file, World rejection for information on solving problems related to worlds always being rejected, and Worldgen examples for example worlds.*

The advanced world generation screen.\
*(Click to enlarge)*

**Advanced world generation**, also labeled as **detailed mode**, allows substantially more detail-oriented options of customization than standard, basic world generation. This gives the player much more control over how their world is generated. To better understand this article, it is advised that one should read about **basic world generation** first.

The advanced world generation screen is reached by clicking "Create new world" at the main menu, then clicking "Detailed mode". Once at that screen, clicking "Basic options" will return the user to the standard world generation screen.

## Parameter sets

There are multiple default sets of all the advanced world generation parameters hard-coded in *Dwarf Fortress*, which will be overridden by the `prefs/world_gen.txt` file in the main *Dwarf Fortress* directory, if it exists. It does not exist by default, you must create it, either by saving the default sets, or saving a copy from the world_gen.txt wiki page or elsewhere. This file can then be edited with a text editor, and you can copy and paste other players' sets of parameters into it. For sources of such parameter sets see Parameter set examples below.

To get back the default sets, move the existing `prefs/world_gen.txt` to somewhere else (like Documents), or delete it if you do not want to keep the changes, then load the sets in the game, it will then use the hardcoded defaults.

## User interface

First, there is a line of text inputs and buttons along the top of the screen, from left to right:

- The drop down menu of currently defined parameter sets, click the down arrow to select a set that you want to work with. The currently selected set can be renamed by clicking the current name or the  button. The first set in the file is selected by default, usually "LARGE ISLAND". See Parameter set title.
- The dimensions of the world for the selected set, see World dimensions.
- A text entry box to set all of the seed options to the same seed, will show "Random seed", "Various seeds", or, if all four seeds are set to use the same value, that value. See Seed values and Seed notes.
- The Copy Button to make a copy of the currently selected set and appends it to the bottom of the list.
- The red Delete button to delete the currently selected set, you will be prompted to confirm the deletion.
- The New parameter set to create a new parameter set and appends it to the bottom of the list. This seems to just copy the default "LARGE REGION" set.
- The Save button to save all of the current sets to the `prefs/world_gen.txt` file.
- The Load button to load from the same file, there is no confirmation, **any unsaved changes will be lost**. If that file does not exist, this resets all of the sets to the defaults.

\
Most of the middle is the parameters themselves, with a scroll bar to the right. Each row of the list can include:

- The name of the option
- The range of accepted values; not every option has this, and does not always match the displayed value, for example "0 to 1" might show as "No" and "Yes".

- Sometimes the range might not initially show on rows that it should, reloading the sets with the Load button sometimes fixes that.Bug:13176

- A plus button to increase the value or cycle through options, when applicable (this button will be missing if the range is missing.)
- The current value; can be clicked to edit, to actually set a value you must press enter, without doing that, clicking another entry box or right clicking will instead reset to the currently set value.
- An edit button to show that the previous box is editable, same as clicking on the text box.
- A minus button to decrease the value or cycle through options, when applicable (this button will be missing if the range is missing).
- A red button to disable this parameter, when applicable, usually setting the value to 0, or -1.

All of the buttons below leave this screen and do not prompt to save the sets, so unsaved changes may be lost.

At the bottom right are 3 or 4 more buttons:

- The Create world button to do just that using the currently selected set, **unsaved changes are lost**.
- The Basic options button to go back to the normal world generation screen, unsaved changes are not lost if you come directly back to Detailed mode.
- The Mods button to go to the mod selection screen, unsaved changes are not lost if you come directly back to Detailed mode. Only shown if mods are available.
- Back to main menu button to do just that, **unsaved changes are lost**.

### World painter

*Main article: World painter*

The **world painter** tool is not in the current version of *Dwarf Fortress*; it allowed you to paint features onto a map. **However**, those maps can still be used when generating a world by pasting world painter parameter set maps created in old versions into the `prefs/world_gen.txt` file. Perfect World DF is a utility that uses the same parameter functionality as the world painter to paint a map, and it also can work with the current version of *Dwarf Fortress*.

## Generating a world

You can either use an already-defined parameter set, or you can edit them, though it is highly suggested to edit a copy of one of the defaults. Once you are happy with the parameters you should save the values you just edited before you click the Create world button. Information about each parameter is documented below.

The phases of the world generation process are (this order is not completely correct):

- Preparing elevation...
- Setting temperature...
- Running rivers...
- Forming lakes and minerals...
- Growing vegetation...
- Verifying terrain...
- Importing wildlife...
- Recounting legends...
- Placing civilizations...
- Making cave civilizations...
- Making cave pops...
- Placing other beasts...
- Placing megabeasts...
- Placing good/evil...
- Placing caves...
- Prehistory generation
- Finalizing civ mats...
- Finalizing art...
- Finalizing uniforms...
- Finalizing sites...

## Seed notes

The world generation process uses a PRNG (Pseudo Random Number Generator) algorithm. A PRNG will produce a sequence of numbers that "looks" random, even though the actual sequence of numbers will always be the same if the PRNG is started with the same seed value. Basically this means that if you run world generation with a certain seed value on your computer, and someone else runs world generation with the same seed value on their computer, the same sequence of random numbers will be generated on both computers. The practical impact of this is that someone else can generate exactly the same world that you generated by entering the same seed value that you used.

In the current version, the seed values for the world itself and the names seem to produce the same result, but you will get changes in events which will result in a very different world history.Bug:6934 Keep this in mind if you want to regenerate a particular world.

The way that a world is generated can also be affected by certain world tokens. Changing them causes that code to use more or fewer PRNG values, causing later uses to get different parts of the sequence. So, you cannot for example, change the minimum and maximum rainfall and get 'the same world but drier or wetter', instead, a different world is generated. That said, it would also seem that certain small changes to these world tokens can occasionally generate a very similar world, however, other tokens are more sensitive. For more information see the forum thread here.

The following are tokens which use the PRNG values in ways that changing them will likely cause broader changes:

- \[DIM:X:X\]
- \[ELEVATION:X:X:X:X\]
- \[RAINFALL:X:X:X:X\]
- \[TEMPERATURE:X:X:X:X\]
- \[DRAINAGE:X:X:X:X\]
- \[VOLCANISM:X:X:X:X\]
- \[SAVAGERY:X:X:X:X\]
- \[ELEVATION_FREQUENCY:X:X:X:X:X:X\]
- \[RAIN_FREQUENCY:X:X:X:X:X:X\]
- \[DRAINAGE_FREQUENCY:X:X:X:X:X:X\]
- \[TEMPERATURE_FREQUENCY:X:X:X:X:X:X\]
- \[SAVAGERY_FREQUENCY:X:X:X:X:X:X\]
- \[VOLCANISM_FREQUENCY:X:X:X:X:X:X\]
- \[PARTIAL_OCEAN_EDGE_MIN:X\]
- \[COMPLETE_OCEAN_EDGE_MIN:X\]
- \[HAVE_BOTTOM_LAYER_1:X\]
- \[MINERAL_SCARCITY:X\] [\[1\]](/index.php/Talk:Advanced_world_generation#Mineral_scarcity "Talk:Advanced world generation")

Many other world parameters, such as end year and embark points, can, however, be changed without it having any effect on the geography of the world generated from the seed values.

Normally, you don't enter these seed values, the game comes up with values based on some other sort of pseudo-random information from things like the current date and time.

When generating a world, *Dwarf Fortress* records the seeds it used in gamelog.txt; they can also be found with `gui/gm-editor world.worldgen.worldgen_parms` in DFHack.

## Advanced parameters

There are essentially 4 types of controls for the generation of the surface map;

**Terrain parameters**: as described below, these 5 variables define the basic background world, how hot or cold it is, how much rainfall, how high the mountains are. The world automatically goes through the temperature range along the Y axis, although sometimes it will be hotter in the north, other times in the south, or cold at both. Minimum, maximum and X,Y variance can drastically alter the world.

**Weighted meshes**: these are a way to fine-tune the amount of the 5 basic variables on the map. They can be used to set the specific distribution of different elevations or rainfall areas for example.

**Feature parameters**: such as rivers, mountain peaks, volcanoes, and oceans, which can cause rejections if the terrain parameters don't allow enough suitable locations for the features to be placed.

**Rejection parameters**: *Dwarf Fortress* uses a 'belt-and-braces' approach to world generation. The above controls allow you to shape the world, then the rejection parameters throw it out if it does not meet certain criteria. There are a number of rejection parameters for the number and degree of the 5 basic variables, for biome types, etc. If the world does not meet the requirements of any one rejection parameter the world is rejected and re-randomised. Also see World rejection.

Leaving tokens out of a set in `world_gen.txt` will cause the game to use default values which are not adjusted for smaller world sizes, this may cause smaller worlds to always be rejected.

If you are experimenting with world design, there is also a game setting that will log the rejection reasons to map_rejection_log.txt. With that information you can then either adjust the rejection parameters to allow those worlds, or the other parameters to prevent them from trying to generate. *Dwarf Fortress* will keep adding to the file, so you may want to trim or delete it occasionally.

The parameters are described below in the order that they appear in the list in the game, which is not necessarily the order they appear in `world_gen.txt`. See world token for an index that will help you look things up by token name. The tokens used in `world_gen.txt` are at the bottom of each of the following parameter descriptions.

### Parameter set title

This sets the name of the parameter set itself, as used in the list of sets (this has nothing to do with the name of the generated world).

|            |                         |          |
|------------|-------------------------|----------|
| Token      | Example                 | Notes    |
| `[TITLE:]` | `[TITLE:MEDIUM ISLAND]` | Required |

### World dimensions

The size of the map for the current set can be changed by changing the Width and Height values at the top next to the set title. You will need to confirm this, since changing the dimensions of the world will change other parameters, because many of them have different defaults depending on the surface area available.

Larger maps usually take longer to generate and may reduce FPS in-game, though this is really a matter of larger worlds usually having more civilizations, sites, historical figures, and events; restricting the number of those can speed up the process. Non-square maps may result in crashesBug:2928.

|  |  |  |
|----|----|----|
| Token | Example | Notes |
| `[DIM::]` | `[DIM:257:257]` | Valid values are 17, 33, 65, 129, and 257, other values will use one of those. Changing the size in the file without adjusting other parameters can cause many rejections. |

### Seed values

Enables the use of, and specifies seed values for, different parts of the world generation process. Just entering a specific seed does not enable it, that must be done separately, although using the box at the top to set all the seeds to the same value does enable them all. Enabling a seed puts the token in using what ever is in the text box below. If you enable a seed, but do not enter a seed, the string "Seed text" will be used (`[SEED:Seed text]`). Trying to use a `]` in the string in the file will end the seed there, since it closes the token, any text after that will be ignored. Normally, just leave these set to Random, unless trying to reproduce the results of a previous world generation. See also the seed notes section above.

Token
Example
Notes

[SEED:]
[SEED:31337]
For each of these not in the config file, a random seed will be used, and the first seed is not used to generate the others. The seeds used are output to / gamelog.txt / when world generation starts.

[HISTORY_SEED:]
[HISTORY_SEED:31337]

[NAME_SEED:]
[NAME_SEED:31337]

[CREATURE_SEED:]
[CREATURE_SEED:31337]

### World name

As previously mentioned, the title of the parameter set doesn't affect the name of the world. You can specify a particular name for your world, or leave the value blank for a random one. (The DFHack utility adds an option to rename the world using the in-game languages.)

|  |  |  |
|----|----|----|
| Token | Example | Notes |
| `[CUSTOM_NAME:]` | `[CUSTOM_NAME:Realm of Cheese Engravings]` | For a random name, simply don't use this token. |

### Embark Points

The number of points for equipment and animals when embarking in fortress mode (there is no equivalent setting for adventure mode). Normally, the default of 1504 is fine, but can be increased for various purposes like experimentation or to help dwarves survive in a particularly evil world, or reduced for certain challenges.

|                    |                        |             |
|--------------------|------------------------|-------------|
| Token              | Example                | Notes       |
| `[EMBARK_POINTS:]` | `[EMBARK_POINTS:1504]` | 0 to 10,000 |

### End year

The maximum number of years generated for the world, although generation can be paused and the world used as is any time after the second year; the same as the History parameter in basic world gen, except that you can enter an exact value. A too-short history can limit the materials available to civilizations, and certain adventure mode features are only available after certain site events, while too long a history often leads to civilizations dying.

For more information on the history aspect of the game, see Legends and Ages.

|               |                  |             |
|---------------|------------------|-------------|
| Token         | Example          | Notes       |
| `[END_YEAR:]` | `[END_YEAR:250]` | 2 to 10,000 |

### Population cap after civ creation

A soft limit to the total number of historical figures alive at the same time during generation across all civilizations, only preventing the birth of new historical figures.[2] Each civilization is allotted a percentage of the total by the percentage of sites they control.[3] Civilizations also have non-historical populations, and there is no setting to limit those (in early versions, all civilization members were historical figures, this is also why the name of this setting is misleading). Each entity also has limits from their raws, see the population entity tokens, and setting this to unlimited will not remove those.

Huge historical figure populations can slow generation and the game in general.

|  |  |  |
|----|----|----|
| Token | Example | Notes |
| `[TOTAL_CIV_POPULATION:]` | `[TOTAL_CIV_POPULATION:15000]` | -1 to 100,000, -1 is no limit |

### Site cap after civ creation

Total number of sites that can be directly created by all civilizations combined like hillocks, hamlets, dark pits, forest retreats, etc. Does not prevent the placement of initial civilization sites, though they will then be counted for the limit. Does not affect creature sites like caves or lairs, group sites like castles, monasteries, towers "Tower (necromancy)"), forts, or camps, or unpopulated sites like tombs. After this limit is reached, no civilization will be able to place new sites. See the placement entity tokens for other ways that civilization site placement can be limited.

Increasing this will slow generation down and reduce the available places for player sites. Since the [`[MAX_SITE_POP_NUMBER]`](/index.php/Entity_token#MAX_SITE_POP_NUMBER "Entity token") entity token limits the historical figure population per site, this site cap can also limit the total historical figure population of all civilizations combined, and some expand faster than others getting more sites before the limit is reached.

|               |                   |                               |
|---------------|-------------------|-------------------------------|
| Token         | Example           | Notes                         |
| `[SITE_CAP:]` | `[SITE_CAP:1500]` | -1 to 100,000, -1 is no limit |

### Beast control

These parameters don't usually matter too much, but may matter for small numbers of beasts.

#### Percentage of Megabeasts and Titans Dead for Stoppage

The world starts out with a certain number of powerful megabeast and titan entities in existence. If a percentage of the megabeast and titan population dies out during history generation, then history generation will stop early. For example, if the elimination value is 80%, and the generated history starts with 200 entities and 160 of those 200 entities are eliminated by historical events before the End Year is reached, history generation will stop immediately.

If you want to end the creation of your world at the beginning of a certain age, choose the following values:

- Age of Legends: ~34%
- Age of Heroes: ~67%

If there are three or fewer titans or megabeasts in your world, the age will be given a special name reflecting the remaining megabeasts/titans, instead.

#### Year to Begin Checking Megabeast Percentage

The percentage of dead megabeasts and titans for stoppage will not be checked until this year is reached in history generation. This can be used to ensure that a world reaches a certain year even if all of the megabeasts in the world are slain earlier.

If the number of living megabeasts and titans starts at or drops to less than four, then world generation will always stop if the current year is equal to or greater than the Year to Begin Checking Megabeast Percentage *regardless* of how many megabeasts and titans are dead — Percentage of Megabeasts and Titans Dead for Stoppage is ignored. The number of megabeasts and titans at the start of the world is set by the sum of the Max Megabeasts Caves and Titan Number parameters.

|  |  |  |
|----|----|----|
| Token | Example | Notes |
| `[BEAST_END_YEAR::]` | `[BEAST_END_YEAR:200:80]` | Use -1 as percentage to disable. Year must still be at least 2. |

### Cull Unimportant Historical Figures

Whether to remove unimportant dead historical figures after history generation; a short CPU-intensive step, but saves space which can speed up loading, saving, and running games with large histories. Legends mode will refer to culled creatures as "an unknown creature", and they will not appear in engravings, but likely would not have anyway.

Exactly what is considered important is not clear. A member of an abstract group killing a named creature is not. Creating an artifact is not, even if that artifact had important history. Unculled historical figures can have parentage described as "The identity of" that parent "has been lost to time", so just having children is not, though having living direct relations seems to prevent culling.

|  |  |  |
|----|----|----|
| Token | Example | Notes |
| `[CULL_HISTORICAL_FIGURES:]` | `[CULL_HISTORICAL_FIGURES:0]` | 0 = No, 1 = Yes |

### Reveal All Historical Events

Setting this to Yes will allow access to most information about the history of the world in Legends mode. All events will be revealed, but some historical figures, sites, regions, and civilizations and other entities may not be, possibly because they are not known to any civilization. If set to No, then you will have to discover historical information in adventure mode or by instructing dwarves to make engravings.\[Verify\]

|                                 |                           |                 |
|---------------------------------|---------------------------|-----------------|
| Token                           | Example                   | Notes           |
| `[REVEAL_ALL_HISTORY:]` | `[REVEAL_ALL_HISTORY::1]` | 0 = No, 1 = Yes |

### Terrain Parameters

These set limits and variance for terrain elevation, rainfall, temperature, drainage, volcanism, and savagery which determines how those values are generated. What biomes exist are then determined by how these factors overlap with each other.

#### Minima and Maxima

These are the absolute minimum and maximum values that can ever be generated for a particular map square characteristic. By *subtly* tweaking the min and max values, vastly different maps can be made. Changing these can cause the occurrence of certain biomes to become impossible, so you may want to use Weighted Ranges instead.

#### X and Y Variance

These control how wildly things like elevation and rainfall can vary between adjacent map squares. For example, if these values are set to the maximum of 3,200 for elevation then you will end up with more very low areas right next to very high areas. The number for X determines the east-west variance and the number for Y determines the north-south variance. By setting only one of these to a high value you can, for example, create horizontal or vertical bands of areas which are more similar to each other.

Generally speaking, raising both of these values will create a more random "patchwork" of many small biomes while setting both x and y values to 0 will cause every square on the map to use a single random value for the given characteristic.

For "patchwork" worlds to avoid being rejected, Maximum Number of Subregions will probably need to be increased from the default.

#### Elevation

This controls the range of terrain elevations that can occur in the world. Usually, you just want to leave the min/max values alone. Raising the minimum elevation can, for example, make it impossible for oceans to exist. This does **not** directly control the number of available Z-levels at a particular site, though high maximum values may contribute to peaks, which can raise the number of above ground Z-levels - in other words, a maximum elevation of 400 and minimum of 1 does not mean you get 400 Z-levels, but it might increase the number of Z-levels somewhat in some regions compared to others. Raising the variance will result in a more bumpy, uneven landscape.

Some biomes/features that are impacted by elevation:

- A high minimum (above 99) means no oceans, as they need elevations below 100.
- A low maximum (below 300) means no mountains, as mountains need elevations above 300.
- Rivers will be placed when the elevation maximum is 104 or higher. Therefore, keeping both values above 100 and below 104 will prevent all water tiles from appearing.
- Mountain peaks can only form at elevations of 400.

#### Rainfall

Controls the amount of rainfall in each map square/area. Setting the minimum or maximum too high or low can make the formation of certain biomes impossible. Rainfall causes it to rain more in a given area, which can have various effects. Also makes more rivers appear on the world map.

Note that if orographic precipitation and rain shadows is on, then mountains will cause additional variance in rainfall, so (for example) rainfall below the specified minimum can occur in the shadow of a mountain. If you want the minimum and maximum for this parameter to be absolutely respected, you must turn off the orographic precipitation option.

Additionally, with 'Orthographic Precipitation' turned on, orthographic precipitation and rain shadows will only occur in regions with greater than or equal to 50 drainage. [Report, reproduced 2022\]

#### Temperature

These parameters control how hot or cold various areas will be. If you lower the minimum and maximum values, the world will be colder overall, for example. As with the others, changing these values too much could make it impossible for certain biomes to exist. The temperature scale used in this setting is related to regular degrees Urist by the equation "local temp = world temp \* 0.75 + 10000".[4] This scale doesn't seem to be used anywhere else in the game. See Climate for more info.

These parameters form the "base" temperature for an area, and describe peak summer temperature in a scale that isn't used elsewhere in the game. This number also does not correspond 1:1 with the final climate. Temperature is always influenced by a number of variables, including elevation, time of year, thick forestation, and if poles are enabled, latitude. These other variables are factored in after the temperature mesh is applied, and frequently bring temperatures above and below their set minimum and maximum values. *The inclusion of Poles is particularly strong in this regard, as it allows latitude to raise and/or lower temperatures by more than 75 degrees Celsius! That said, the temperatures aren't raised or lowered by more than about 65 degrees past the set minimum and maximum. Furthermore, for typical ranges, the temperature will never be raised more than about 25 degrees past the maximum (but will still drop up to about 65 degrees Celsius below the minimum).* (unsure about exact values, research needed)

Elves can spawn where the temperature is 10 degrees or warmer, and humans can spawn where the temperature is 0 degrees or warmer.

#### Drainage

Changing drainage parameters will change the way water-affected biomes are formed. Low drainage will contribute to the formation of lakes, rivers, and swamps. High drainage will cause water to sink into the ground rather than sit on the surface, which is important for forming hills.

Lower drainage values have been reported to contribute to the formation of thicker soil layers, though it is currently unknown exactly how other factors (such as elevation or perhaps rain) impact soil formation.

#### Volcanism

Volcanism controls the occurrence of igneous layers, and the formation of volcanoes. For a volcano to form, a square must have a volcanism value of 100, so reducing the maximum from 100 will make volcanoes impossible. Raising the minimum will increase the rarity of non-igneous layers.

Setting the minimum to a high value is not a good way to produce multiple volcanoes, as you are likely to get a "Volcanism not evenly distributed" rejection. Instead, use the Minimum Number of Volcanoes parameter, and possibly adjust the weighted ranges for volcanism as described below.

#### Savagery

These parameters control the level of savagery on the map. Raising the minimum savagery too high may make it impossible for certain races to exist, and similarly lowering the maximum too far can make it impossible for certain creatures to exist. The largest chance of having unusable maps comes from a too-high savagery value.

#### Configuration Tokens

|  |  |  |
|----|----|----|
| Token | Example | Notes |
| `[ELEVATION::::]` | `[ELEVATION:1:400:401:401]` | Range: 0 to 400 / Maximum of 400 required for mountain peaks. / Variance range: 0-3200 |
| `[RAINFALL::::]` | `[RAINFALL:0:100:200:200]` | Range: 0 to 100 / Variance range: 0-3200 |
| `[TEMPERATURE::::]` | `[TEMPERATURE:25:75:200:200]` | Range: -1000 to 1000 / Variance range: 0-3200 |
| `[DRAINAGE::::]` | `[DRAINAGE:0:100:200:200]` | Range: 0 to 100 / Variance range: 0-3200 |
| `[VOLCANISM::::]` | `[VOLCANISM:1:100:200:200]` | Range: 0 to 100 / Maximum of 100 required for volcanoes. / Variance range: 0-3200 |
| `[SAVAGERY::::]` | `[SAVAGERY:1:100:200:200]` | Range: 0 to 100 / Variance range: 0-3200 |

### Terrain Mesh Sizes and Range Weights

A large world generated with an Elevation Mesh Size of 32×32 and range weights set to 1:0:0:0:1 (i.e., only extreme high and low elevations). Note how the grid intersections are either set very high (mountains) or very low (oceans) and the space between them is smoothed out.

These parameters influence the relative proportions of terrain feature ranges, without making other ranges impossible. For example, to have many more low-elevation squares exist, without making it impossible for high elevations; this makes changing these parameters often preferable to simply changing the above min/max values. See the image on the right for an example.

The basic steps of applying weighted ranges are as follows:

1.  Divide the world into a grid of quantity `2`*`MeshSize`*` - 1` areas in both X and Y direction.
2.  At each grid intersection, set the value according to the weighted ranges.
3.  Smooth out the areas between the intersection points.
4.  Add noise according to the variance parameters.

Where *MeshSize* is the raw parameter value found in the `world_gen.txt`.

#### Interaction between Mesh Size and Weighted Ranges

Mesh size determines how many intersection points the world will have. As an example, setting it to 2×2 means the world will be divided into 4 areas, 2 across and 2 tall, and there will be a total of 9 intersection points (3×3), including the outer-most corners. The grid intersection points are in the middle of world tiles, and the minimum size for a grid area is a span of 9 world tiles in either direction, with adjacent areas sharing an overlapping world tile. On a pocket world, this means one grid tile will span 9×9 world tiles, whereas on a large world, one grid tile will span 129×129 world tiles. A pocket world will always use a 2×2 grid of 9×9 world tiles, since it has only 17×17 tiles total (even if the game UI allows setting those worlds to a 4×4 grid, which can happen when changing the world size; changing the world size doesn't adjust mesh size limits, but saving then reloading the parameters does). A world that is 17 tiles wide, but 257 tall, and set to a 32×32 mesh size, will have 3×33 intersection points.

Setting mesh size to something other than Ignore, will apply random values at those intersections, with those random values being more likely to be in the ranges with higher weights. Setting to Ignore will cause the weighted range settings to be ignored for that terrain characteristic; instead setting the 4 corners of the world to completely random values and smoothing between those, or in other words, using a 1×1 grid for square worlds; while for rectangular worlds, using the same ratio as the world dimensions with 1 in the narrow dimension (for example, a 1×16 grid for a 17×257 world).

For example, if the Elevation Weighted Range parameters are set to `60:10:10:10:10` (starting with the 0-20 range, and these values do not need to add up to any particular number), and elevation min and max are left at the defaults of 1 and 400 respectively, then about 60% (on average) of the grid line intersection points will be set to an elevation in the range of 1-80 (0% to 20%), and the other ranges will be represented by around 10% of the intersection points each. The exact distribution is still left up to chance, though *on average* it will be close to this specification. This allows random number generation to be non-linear for the given terrain characteristic.

Setting the weight for a range to None only prevents intersection points from being set to a value in that range; terrain between intersection points can still be smoothed to values in ranges set to None that are between the intersection point values. Setting all the weights to None just puts them all at the same weight, the same as the default of all at 1.

Weighted ranges do not make rejection checks, although they can be responsible for many rejections if you neglect to adjust or disable some of the Minimum Number of Mid/Low/High Characteristic Squares, for example.

#### Interaction between these and Variances

The end result can vary greatly depending on how the corresponding X and Y Variance parameters are set. First of all, if the variance is too high, the noise it adds can completely negate the effect of the weighted ranges. For instance, with a 2×2 mesh, the default variance parameters are high enough that usually the mesh grid can hardly be recognized. How strong the variance's effect is, is also dependent on the mesh size. Having a larger mesh size (i.e. smaller grid tiles) means the variance also has to be higher for a visible effect. For instance, with a variance of 400, the effects are clearly visible with a 2×2 mesh and barely visible at all with a 8×8 mesh. Note that this effect is directly dependent on the mesh size and not, as one might expect, on the actual size of the grid tiles. This means, that a large world with a 32×32 mesh will look essentially the same as a pocket world with a 2×2 mesh, only stretched to 256 times the size.

Also see this forum post for more details.

#### Configuration Tokens

Token
Example
Notes

[ELEVATION_FREQUENCY::::::]
[ELEVATION_FREQUENCY:2:1:2:3:4:5]
Valid mesh values: / 1 = Ignore / 2 = 2x2 / 3 = 4x4 / 4 = 8x8 / 5 = 16x16 / 6 = 32x32 / (limited by world size)

[RAIN_FREQUENCY::::::]
[RAIN_FREQUENCY:3:1:2:3:4:5]

[DRAINAGE_FREQUENCY::::::]
[DRAINAGE_FREQUENCY:4:1:2:3:4:5]

[TEMPERATURE_FREQUENCY::::::]
[TEMPERATURE_FREQUENCY:1:1:1:1:1:1]

[SAVAGERY_FREQUENCY::::::]
[SAVAGERY_FREQUENCY:5:1:2:3:4:5]

[VOLCANISM_FREQUENCY::::::]
[VOLCANISM_FREQUENCY:1:1:1:1:1:1]

### Poles

With this, you can influence how polar regions are added. The poles can be on the north or south edge, and the equator will be on the opposite edge, or in the middle if there are two poles. If poles are set to NONE, then there will be no seasonal changes in the weather (e.g. no winter snow in temperate biomes).

|  |  |  |
|----|----|----|
| Token | Example | Notes |
| `[POLE:]` | `[POLE:NORTH]` | Viable options: NONE, NORTH_OR_SOUTH, NORTH_AND_OR_SOUTH, NORTH, SOUTH, NORTH_AND_SOUTH |

### Minimum Mountain Peak Number

This will cause the world to be rejected if fewer than this many peaks (based on elevation) are present on the map. EG: elevations of 400 must be possible for mountain peaks to occur. If set to zero, then worlds will not be rejected based on number of peaks.

You may need to adjust elevation parameters, such as the highest weighted range, in order to get the desired number of elevation-400 squares needed for larger numbers of peaks. Like volcanoes, mountain peaks can make embark zones more interesting, but other than that, they don't appear to "do" anything special. Reportedly, they do increase the highest Z-level above ground in all embark zones in the same region, even if the selected embark zone does not include the peak.

|  |  |  |
|----|----|----|
| Token | Example | Notes |
| `[PEAK_NUMBER_MIN:]` | `[PEAK_NUMBER_MIN:20]` | Elevations of 400 must occur for peaks to form. |

### Minimum Partial Edge Oceans

This will cause a world to be rejected unless there are at least this many oceans touching an edge of the map. If set to zero then worlds will not be rejected based on this criterion. Setting both this parameter and Minimum Complete Edge Oceans to values that total more than 4 when added together may cause all worlds to be rejected as you can't have both a partial and complete edge ocean on a given edge.

|                             |                              |              |
|-----------------------------|------------------------------|--------------|
| Token                       | Example                      | Notes        |
| `[PARTIAL_OCEAN_EDGE_MIN:]` | `[PARTIAL_OCEAN_EDGE_MIN:2]` | Maximum of 4 |

### Minimum Complete Edge Oceans

This will cause a world to be rejected unless there are at least this many oceans which completely cover an edge of the map. Since a square map only has 4 edges, the maximum value possible is 4. If set to zero then worlds will not be rejected based on this criterion but still might end up with complete edge oceans by chance.

Note that the ability for this many edge oceans to exist will be limited by elevation. Therefore, to actually create large oceans you will probably need to change things like the Elevation Mesh Size and Weighted Ranges to increase the number and distribution of very low elevation squares on the map. In addition, if Complete Edge Oceans is set to any value *other* than 0 or 4, you may need to lower elevation variance for at least one of the axes: if set too high, such as a variation of 1600 for both X and Y axes (the default for Large Island and Medium Island parameter sets), the game may generate worlds very slowly or even hang.Bug:565

Given appropriate weight, range, and variance values for things like elevation, a setting of: 1 results in a world that seems like a chunk of coastline. One edge of the map will be completely underwater and there will be ocean taking up much of the map on that side (think the east or west coast of the United States, the north coast of Canada, or southern Europe). If your edge ocean happens to pick your world's frozen side, most of it will be glacier.

- 2 results in another coastline along with the first one -- the map could end up looking something like Panama if the oceans pick opposite sides of the map.
- 3 results in a peninsula, like Florida in the US. There will be oceans surrounding 3 sides of the map, and land touching only one side of the map.
- 4 results in one or more island(s) depending on things like elevation variance and weights. Regardless of whether you get one island or multiple islands, the entire map will be surrounded by water.

Unfortunately, there's no easy way to control which oceans end up on which edges, except perhaps setting X/Y variance to different values.

Edge oceans will take up part of the other edges too. For example, a full edge ocean on the east side will have part of the north and south sides underwater, but that does *not* add to the *partial* edge oceans count.

|                              |                               |              |
|------------------------------|-------------------------------|--------------|
| Token                        | Example                       | Notes        |
| `[COMPLETE_OCEAN_EDGE_MIN:]` | `[COMPLETE_OCEAN_EDGE_MIN:0]` | Maximum of 4 |

### Minimum Volcano Number

The game will attempt to place this many volcanoes, but there must be at least this many squares with a volcanism of 100, if there are not the world will be rejected. Therefore, maximum volcanism above must be set to 100, and adjusting the volcanism weighted range above for 80-100 to a higher value can increase the number of those squares.

|  |  |  |
|----|----|----|
| Token | Example | Notes |
| `[VOLCANO_MIN:]` | `[VOLCANO_MIN:15]` | Volcanoes require a volcanism of 100 to occur. |

### Mineral Scarcity

Controls the frequency at which minerals occur; setting this value higher will decrease both the number of different types and amounts of ore and gems present on a map. The default value will result in many metal ores, while the old default of *sparse* would be only a few ores, which may be limiting until other metals can be requested and traded for.

The options "Very Rare", "Rare", "Sparse", "Frequent", and "Everywhere" in the basic world generation menu use the values 50000, 10000, 2500, 500 and 100 respectively.

According to research by Shandra in v0.31.25, this is the relationship between the value of this setting and the approximate number of gems and ore:

This is for the same 8x8 embark region in a world which is otherwise the same, except for the mineral scarcity parameter (although most of the detailed information comes from experiments with previous versions). (The chart legend has an error, the first "Pot.(Types)" should read "Pot.(Amount)".)

|                       |                          |                       |
|-----------------------|--------------------------|-----------------------|
| Token                 | Example                  | Notes                 |
| `[MINERAL_SCARCITY:]` | `[MINERAL_SCARCITY:100]` | Range: 100 to 100,000 |

### Max Megabeast Caves

This is the number of megabeasts placed at the beginning of history. Megabeasts are hydras, bronze colossuses, rocs, and dragons, which are all placed in equal proportions data.

Increasing this value can lead to early extinction of civilizations.

|  |  |  |
|----|----|----|
| Token | Example | Notes |
| `[MEGABEAST_CAP:]` | `[MEGABEAST_CAP:75]` | Megabeasts count towards BEAST_END_YEAR calculation. |

### Max Semi-Megabeast Caves

This is the number of semi-megabeasts placed at the beginning of history. Semimegabeasts are giants, ettins, minotaurs, and cyclops, which are placed in equal proportions data.

|  |  |  |
|----|----|----|
| Token | Example | Notes |
| `[SEMIMEGABEAST_CAP:]` | `[SEMIMEGABEAST_CAP:150]` | Semimegabeasts do not count towards the BEAST_END_YEAR calculation. |

### Titan Parameters

#### Number

This controls the number of titans that exist at the beginning of historydata. The number of forgotten beasts is unaffected by this parameter data.

|  |  |  |
|----|----|----|
| Token | Example | Notes |
| `[TITAN_NUMBER:]` | `[TITAN_NUMBER:33]` | Titans count towards BEAST_END_YEAR calculation. |

#### Attack Population Requirement

Titans will begin to attack your fort once at least this many dwarves inhabit it, regardless of whether any other attack criteria have been met.

This number defaults to 80, which isn't usually too difficult to deal with.

#### Exported Wealth Requirement

Titans will begin to attack your fort once you have exported at least this many dwarfbucks-worth of goods, regardless of whether or not any other criteria have been met. This parameter defaults to None (disabled).

#### Created Wealth Requirement

Titans will begin to attack your fort once the fort's total wealth has reached this many dwarfbucks in value. This happens regardless of whether any of the other criteria, such as population, have been met; therefore, even with 1 dwarf, a fort could be attacked if the fort were worth at least this value.

|  |  |  |
|----|----|----|
| Token | Example | Notes |
| `[TITAN_ATTACK_TRIGGER:::]` | `[TITAN_ATTACK_TRIGGER:80:0:100000]` | 0 = None (disabled). Only one requirement must be met for an attack. |

### Number of Demon Types

Demons are similar to titans and forgotten beasts, in that they are procedurally generated, but most are not unique. Thus, many different types of demons can exist in the world, but there will also be many individuals of most types. Thanks to certain fun things, fewer demon types also means fewer goblin civilizations.[5] You need at least 2 demon types, or else goblin civilizations won't exist initially, though if dwarves breach the underworld during world generation, at least one will be generated then.

|                   |                     |           |
|-------------------|---------------------|-----------|
| Token             | Example             | Notes     |
| `[DEMON_NUMBER:]` | `[DEMON_NUMBER:52]` | 0 to 1000 |

### Number of Night Troll Types

The number of different night trolls, also procedurally generated, that will exist in the world. Setting this to zero means that the world will have no night trolls, custom or otherwise.

|                         |                           |           |
|-------------------------|---------------------------|-----------|
| Token                   | Example                   | Notes     |
| `[NIGHT_TROLL_NUMBER:]` | `[NIGHT_TROLL_NUMBER:77]` | 0 to 1000 |

### Number of Bogeyman Types

The number of different bogeyman forms that will exist in the world. Bogeymen are procedurally generated, though their forms do not vary by much. Setting this to zero means that the world will have no bogeymen, custom or otherwise.

|                      |                        |           |
|----------------------|------------------------|-----------|
| Token                | Example                | Notes     |
| `[BOGEYMAN_NUMBER:]` | `[BOGEYMAN_NUMBER:27]` | 0 to 1000 |

### Number of Nightmare Types

The number of different nightmare forms that will exist in the world. Nightmares are procedurally generated. Setting this to zero means that the world will have no nightmares, custom or otherwise.

|                       |                         |           |
|-----------------------|-------------------------|-----------|
| Token                 | Example                 | Notes     |
| `[NIGHTMARE_NUMBER:]` | `[NIGHTMARE_NUMBER:27]` | 0 to 1000 |

### Number of Vampire Curse Types

The number of different types of vampires that will exist in the world. Although they are generated at the start of a new world, they aren't different from each other. Setting this to zero means no vampires will exist.

|                     |                       |           |
|---------------------|-----------------------|-----------|
| Token               | Example               | Notes     |
| `[VAMPIRE_NUMBER:]` | `[VAMPIRE_NUMBER:72]` | 0 to 1000 |

### Werebeast Parameters

#### Number of Werebeast Curse Types

The number of different types of werebeasts that can exist in the world. It is common for werebeasts, unlike vampires, to assume many different forms and variations, the most well-known of these amount to different species of animals, from lizards, to wolves, to even bears. Setting this to zero means no werebeasts will exist, and will also remove a large amount of fun from the game.

In vanilla, there are only 82 possible unique werebeast species. Any further species will generate as wereblobs.Bug:13308

|                       |                         |           |
|-----------------------|-------------------------|-----------|
| Token                 | Example                 | Notes     |
| `[WEREBEAST_NUMBER:]` | `[WEREBEAST_NUMBER:58]` | 0 to 1000 |

#### Attack Population Requirement

Werebeasts will begin to attack your fort once at least this many dwarves inhabit it, regardless of whether any other attack criteria have been met. This number defaults to 50 which will often be reached in the second year of the fort.

#### Exported Wealth Requirement

Werebeasts will begin to attack your fort once you have exported at least this many dwarfbucks-worth of goods, regardless of whether or not any other criteria have been met. This parameter defaults to 5000.

#### Created Wealth Requirement


---
*Parte 1 de 2 de «Advanced world generation». Demais partes em arquivos `...-part-{1..2}.md` na mesma pasta. Fonte: https://dwarffortresswiki.org/index.php/Advanced_world_generation*
