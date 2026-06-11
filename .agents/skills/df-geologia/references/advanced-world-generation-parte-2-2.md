# Advanced world generation (parte 2/2)

Werebeasts will begin to attack your fort once the fort's total wealth has reached this many dwarfbucks in value. This happens regardless of whether any of the other criteria, such as population, have been met; therefore, even with 1 dwarf, a fort could be attacked if the fort were worth at least this value.

|  |  |  |
|----|----|----|
| Token | Example | Notes |
| `[WEREBEAST_ATTACK_TRIGGER:::]` | `[WEREBEAST_ATTACK_TRIGGER:50:5000:50000]` | 0 = None (disabled). Only one requirement must be met for an attack. |

### Number of Secret Types

The number of secrets that exist in the world. Currently, all secrets are secrets of life and death, and the ones holding these secrets are necromancers, thus, setting this to zero means that no necromancers will appear. Non-necromancer towers can still appear (extremely rarely) with zero secrets, constructed by independent undead groups. The primary difference between having 1 or 1000 secrets is the chance of your world having any necromancer towers at all. With 1, this chance is low. With the default number, it's seemingly guaranteed. Even with 1 secret, if you have any necromancer towers at all, it is likely a great number will quickly appear in world generation (though this isn't guaranteed).

|                    |                      |           |
|--------------------|----------------------|-----------|
| Token              | Example              | Notes     |
| `[SECRET_NUMBER:]` | `[SECRET_NUMBER:52]` | 0 to 1000 |

### Number of Regional Interaction Types

The number of interactions that can be caused in regions, which may incorporate evil rain and cloud types. Currently, only evil region interactions are generated this way.

|  |  |  |
|----|----|----|
| Token | Example | Notes |
| `[REGIONAL_INTERACTION_NUMBER:]` | `[REGIONAL_INTERACTION_NUMBER:20]` | 0 to 1000 |

### Number of Disturbance Interaction Types

The number of different disturbed dead that can exist in the world. Setting this to zero should prevent any mummy from appearing\[Verify\], but it will not prevent the creation of tombs.

|  |  |  |
|----|----|----|
| Token | Example | Notes |
| `[DISTURBANCE_INTERACTION_NUMBER:]` | `[DISTURBANCE_INTERACTION_NUMBER:10]` | 0 to 1000 |

### Number of Evil Cloud / Evil Rain Types

This number specifies how many various face-melting, eye-boiling, and zombifyingly-fun clouds of pure evil may appear in your world. Setting this to zero means you no longer will ever have to deal with encroaching dust walls of doom in that world. It is generally advised to keep this value low...

|                        |                          |           |
|------------------------|--------------------------|-----------|
| Token                  | Example                  | Notes     |
| `[EVIL_CLOUD_NUMBER:]` | `[EVIL_CLOUD_NUMBER:45]` | 0 to 1000 |

The latter number states how many different types of green-ooze drenchers, disconcerting blood-showers, and sickly yellow slime-baths can occur in your world. Compared to evil clouds though, this one hardly is worth stressing out about, usually.... Setting this to zero means the only semi-solid to fully-liquid fluids to fall from the sky will be pure H2O.

|                       |                          |           |
|-----------------------|--------------------------|-----------|
| Token                 | Example                  | Notes     |
| `[EVIL_RAIN_NUMBER:]` | `[EVIL_RAIN_NUMBER:352]` | 0 to 1000 |

### Generate Divine Materials

This turns the generation of divine metals on or off. It does not influence the creation of vaults. Probably determines whenever or not using divination dice spawns weapons.

|  |  |  |
|----|----|----|
| Token | Example | Notes |
| `[GENERATE_DIVINE_MATERIALS:]` | `[GENERATE_DIVINE_MATERIALS:1]` | 1/0 = Yes/No |

### Generate Mythical Materials

|  |  |  |
|----|----|----|
| Token | Example | Notes |
| `[GENERATE_MYTHICAL_MATERIALS:]` | `[GENERATE_MYTHICAL_MATERIALS:1]` | 1/0 = Yes/No |

### Allow Mythical Healing

|  |  |  |
|----|----|----|
| Token | Example | Notes |
| `[ALLOW_MYTHICAL_HEALING:]` | `[ALLOW_MYTHICAL_HEALING:1]` | 1/0 = Yes/No |

### Allow Divination, Experiments, and Necromancy types

These allow or disallow divination, demon or necromancer experiments, and the more advanced necromancer abilities.

|  |  |  |
|----|----|----|
| Token | Example | Notes |
| `[ALLOW_DIVINATION:]` | `[ALLOW_DIVINATION:1]` | 1/0 = Yes/No |
| `[ALLOW_DEMONIC_EXPERIMENTS:]` | `[ALLOW_DEMONIC_EXPERIMENTS:1]` | 1/0 = Yes/No |
| `[ALLOW_NECROMANCER_EXPERIMENTS:]` | `[ALLOW_NECROMANCER_EXPERIMENTS:1]` | 1/0 = Yes/No |
| `[ALLOW_NECROMANCER_LIEUTENANTS:]` | `[ALLOW_NECROMANCER_LIEUTENANTS:1]` | 1/0 = Yes/No |
| `[ALLOW_NECROMANCER_GHOULS:]` | `[ALLOW_NECROMANCER_GHOULS:1]` | 1/0 = Yes/No |
| `[ALLOW_NECROMANCER_SUMMONS:]` | `[ALLOW_NECROMANCER_SUMMONS:1]` | 1/0 = Yes/No |

### Desired Good/Evil Square Counts

These values change the amount of good or evil tiles on the map, depending on the size of the region they are being considered for. The counts are for all tiles in all subregions of a given size considered together, *not* counts for each subregion considered separately (all tiles in the same subregion share the same surroundings values).

As used here, a "subregion" is a named world area. Subregion names and locations for a generated world are viewable in legends mode under "Regions". Subregions are classified by size the same way for all map sizes: 1-24 tiles is Small, 25-99 tiles is Medium, and 100+ tiles is Large.

The counts used here will always be restricted to regions of the given size, no matter how large the count. Also, the count is more of a goal than a minimum or maximum. As a result, you can end up with many more or many fewer than the requested number of squares in some situations. In particular, if you have something like a case where only 3 large regions exist in a world, and you request "1 evil square" in large regions, you will end up with one of the large regions being *entirely evil*. So any non-zero value in one of these settings essentially means "force at least one region of this size to be all good/evil."

Note that the "evilness" of evil biomes is also impacted by savagery. Certain civilizations cannot exist in good and/or evil squares, so too many of one or the other may limit the size of certain types of civilizations - dwarves, for example, need non-aligned biomes. Creating too many evil biomes seems to lead to the danger of many civilizations' early extinction.

Token
Example
Notes

[GOOD_SQ_COUNTS:::]
[GOOD_SQ_COUNTS:100:1000:2000]
Set count to zero to disable for that region size.

[EVIL_SQ_COUNTS:::]
[EVIL_SQ_COUNTS:100:1000:2000]

### Minimum Biome Square Counts

These numbers control whether or not a world will be rejected based on a lack of different biomes. Raising these numbers will **not** automatically generate the given number of squares of the given biome! For a biome to exist, certain conditions like elevation and rainfall must exist.

These parameters simply filter out worlds that (for example) randomly fail to have enough high elevation squares to support a given number of mountains, etc. Some settings may cause worlds to always be rejected. For example, if for some reason the maximum elevation parameter is set to a value below what will support mountain biomes, it will be impossible to satisfy a non-zero requirement for mountain squares. The same principle goes for other conditions and biomes such as low elevations and oceans, etc.

Certain civilizations require different biomes to exist (such as dwarves and mountains), so eliminating certain biomes will make it impossible for certain civilizations to form.

These parameters often result in infinite world rejection problems. See World rejection for information on solving problems related to worlds always being rejected due to one or more of these parameters.

0 means no minimum for rejection - setting it to 0 does not guarantee 0 squares of that biome.

#### Biome Type Requirement Table

Terrain requirements for various biomes are described below.\[Verify\] Note that some of the exact ranges are unknown.

Biome
Terrain Requirement

Elevation
Rainfall
Temperature
Drainage

Swamp/Marsh
100-299
33-100
Non-Freezing
0-32

Desert/Badland
100-299
0-9
non-freezing
note1

Forest
100-299
66-100
non-freezing
66-100

Mountains
300-400
N/A
N/A
N/A

Ocean
0-99
N/A
N/A
N/A

Glacier
100-299
N/A
Freezing
80(?)-100

Tundra
100-299
N/A
Freezing
0-66

Grassland
100-299
0-66
Non-Freezing
0-66

Hills
100-299
0-66
Non-Freezing
66-100

note1 drainage: 00-32 sand desert, 33-49 rocky wasteland, 50-65 rocky wasteland but different characters/appearance, 66-100 badlands

#### Minimum Initial Square Count

**Note: The exclusive purpose of these parameters is to cause world rejection.**

This is the minimum number of squares of the given biome that must exist before things like erosion take place. One thing to keep in mind is the maximum number of squares on a map of a given size - if the total number of squares on a map is lower than the sum of all square count parameters, then you will get infinite world rejection.

To determine the number of squares on a map, just multiply the dimensions. In practice these parameters will need to sum to lower than the maximum because some space is needed for "slack".

|          |                   |
|----------|-------------------|
| Map Size | Number of Squares |
| 17×17    | 289               |
| 33×33    | 1089              |
| 65×65    | 4225              |
| 129×129  | 16614             |
| 257×257  | 66049             |

#### Minimum Initial Region Count

This is the minimum number of regions of contiguous biome squares that must exist before other processes such as erosion take place.

#### Minimum Final Region Count

This many regions of the given biome must exist after erosion and similar phases of generation have been completed.

|                                |                                        |
|--------------------------------|----------------------------------------|
| Token                          | Example                                |
| `[REGION_COUNTS:SWAMP:::]`     | `[REGION_COUNTS:SWAMP:1032:7:6]`       |
| `[REGION_COUNTS:DESERT:::]`    | `[REGION_COUNTS:DESERT:1032:7:6]`      |
| `[REGION_COUNTS:FOREST:::]`    | `[REGION_COUNTS:FOREST:4128:13:12]`    |
| `[REGION_COUNTS:MOUNTAINS:::]` | `[REGION_COUNTS:MOUNTAINS:8256:9:9]`   |
| `[REGION_COUNTS:OCEAN:::]`     | `[REGION_COUNTS:OCEAN:8256:7:6]`       |
| `[REGION_COUNTS:GLACIER:::]`   | `[REGION_COUNTS:GLACIER:0:0:0]`        |
| `[REGION_COUNTS:TUNDRA:::]`    | `[REGION_COUNTS:TUNDRA:0:0:0]`         |
| `[REGION_COUNTS:GRASSLAND:::]` | `[REGION_COUNTS:GRASSLAND:8256:13:12]` |
| `[REGION_COUNTS:HILLS:::]`     | `[REGION_COUNTS:HILLS:8256:13:12]`     |

### Erosion Cycle Count

Tells the world generator how long the world has to erode its tall peaks down to mountainsides during the 'running rivers...' stage of world creation. The higher this number, the less jagged the world will be, and the more wide the major rivers will be. If you use the maximum number, your mountains will dissolve before your eyes into plains which can lead to rejections if there aren't enough mountains to use for river start points and dwarven civilization origin points.

|                          |                             |                  |
|--------------------------|-----------------------------|------------------|
| Token                    | Example                     | Notes            |
| `[EROSION_CYCLE_COUNT:]` | `[EROSION_CYCLE_COUNT:250]` | Range: 0 to 1000 |

### Minimum/Desired River Start Locations

This is the minimum number of riverheads that must exist before and after erosion takes place. Worlds will be rejected if they fail to meet these numbers. As with minimum biome counts, raising this number doesn't automatically create this many riverheads. Other conditions like terrain and rainfall must exist for rivers to form.

Extremely high pre-erosion values speed erosion greatly, while low post erosion values are useful for limiting rejects due to lack of river origin points. One can try the 800 value to get more lakes.

|                  |                        |                 |
|------------------|------------------------|-----------------|
| Token            | Example                | Notes           |
| `[RIVER_MINS::]` | `[RIVER_MINS:200:400]` | Range: 0 to 800 |

### Periodically Erode Extreme Cliffs

If enabled, makes every impassable rock wall into a series of ramps. Some prefer to pump up erosion to about 250, and turn the "Desired pre-erosion river count" to 0 for good erosion and no extra canyons.

Normally this is set to Yes (1).

|  |  |  |
|----|----|----|
| Token | Example | Notes |
| `[PERIODICALLY_ERODE_EXTREMES:]` | `[PERIODICALLY_ERODE_EXTREMES:1]` | 1/0 = Yes/No |

### Do Orographic Precipitation and Rain Shadows

Toggle that allows terrain height to affect rainfall. For example, moist air coming from the ocean blows over the land. As the terrain gets higher, it forces the moist air up, causing it to rain on the seaward side of a mountain. Eventually, all the rain has fallen if the mountain is tall enough. So, when the breeze goes over the top, there's no moisture left to fall on the other side, creating a rain-shadow. In the current version, regions where drainage is above 50 will also create rain shadows, regardless of the underlying biome and elevation.[6]

Turning this on should create a tendency for more extreme rainfall in regions, creating more forests, deserts, marshlands, and grasslands. Also note that it can create rainfall outside of min-max rainfall settings, so even in a world with a 0 max rainfall you may get rainfall biomes. Turning it off should result in more controllable, less complex rainfall conditions based on rainfall parameters as it adds a random element which can distort or otherwise mess up the climates on a pregenerated map.

This should be disabled if you're importing a map or using a preset map file that has weather.

|  |  |  |
|----|----|----|
| Token | Example | Notes |
| `[OROGRAPHIC_PRECIPITATION:]` | `[OROGRAPHIC_PRECIPITATION:1]` | 1/0 = Yes/No |

### Maximum Number of Subregions

This is the number of separate biomes (the flashing regions you see on embark when you hit F1, F2, etc. when there's more than one biome on the embark location) that are allowed to exist on the entire map.

Setting this to very low values will result in numerous rejections depending on variance parameters. If variance values are set to high numbers, many small biomes will be created causing rejection if this parameter value is not increased beyond the default.

Increasing the value of this tag is often a must when generating "patchwork" worlds with lots of biome variance, but simply increasing it without increasing variance parameters will not guarantee more biomes.

It is also interesting to note that the maximum subregions is 5000 which is more than the total number of squares for a pocket or small map. However, for a medium or large map (16641 or 66049 squares) it quickly becomes a mere fraction of the total number of possible subregions. In fact it would be quite easy on a large map to end up with far too many subregions and get endless rejections of this type.

|                    |                        |                  |
|--------------------|------------------------|------------------|
| Token              | Example                | Notes            |
| `[SUBREGION_MAX:]` | `[SUBREGION_MAX:2750]` | Range: 1 to 5000 |

### Cavern Parameters

Caverns are the hollow areas underground, which dwarves tend to encounter when they're digging around. The **Cavern Layer Number** parameter determines how many cavern systems will be generated, not including the magma layer or the Bottom layer. Defaults to three - setting it to lower values could help FPS. Setting it to 2 will merge cavern 3 species into the 2nd cavern, and setting it to 1 will merge all into one cavern. However, disabling them entirely by setting it to 0 will make it impossible to grow any underground plants, as none will exist for your civilization to cultivate, nor will they be available on embark.

- Setting caverns to a sub-3 number (Spoiler, highlight to view) erases about one-third of HFS spiresBug:10267 and prevents dig deep disasters. Additionally, random plant or animal species can be more frequently absent.

|                         |                          |               |
|-------------------------|--------------------------|---------------|
| Token                   | Example                  | Notes         |
| `[CAVERN_LAYER_COUNT:]` | `[CAVERN_LAYER_COUNT:3]` | Range: 0 to 3 |

#### Cavern Layout Parameters

Open caverns and dense passageways are not mutually exclusive. When both are raised, bizarre results can occur, such as layers showing a combination of open caverns, a cluster of network passages, and natural walls sprinkling the inside of an otherwise open cavern. Reference

If you want the largest open spaces possible, then decrease the density and increase the openness. If you want a labyrinth of passageways, lower the openness and raise the passage density.

Another interesting note about the cavern layers is that the seed and number of demon types affect the layout of the caverns.

-

  Cavern slice with Openness of 0 and Density of 100

-

  Cavern slice with Openness of 100 and Density of 0

-

  Cavern slice with Openness of 100 and Density of 100

-

  Cavern slice with Openness of 50 and Density of 50

##### Layer Openness min/max

Dictates the size of cavern passages. When Passage Density (see below) is set to minimum (0), caverns will be open expanses. Raising the maximum will increase the size of the caverns.

Token
Example
Notes

[CAVERN_LAYER_OPENNESS_MIN:]
[CAVERN_LAYER_OPENNESS_MIN:0]
Range: 0 to 100

[CAVERN_LAYER_OPENNESS_MAX:]
[CAVERN_LAYER_OPENNESS_MAX:100]

##### Layer Passage Density min/max

Determines how many passages form the cavern. If openness (see above) is set to minimum and density increased, then you will get a maze-like network of small criss-crossing passages. Raising the values further increases the number of the maze-like passages.

Caverns will be large, open spaces at 0, and comprised of many small vertical shafts of rock at 100. Setting both values to be the same results in a uniform look for the caverns.\[Verify\]

Token
Example
Notes

[CAVERN_LAYER_PASSAGE_DENSITY_MIN:]
[CAVERN_LAYER_PASSAGE_DENSITY_MIN:0]
Range: 0 to 100

[CAVERN_LAYER_PASSAGE_DENSITY_MAX:]
[CAVERN_LAYER_PASSAGE_DENSITY_MAX:100]

##### Layer Water min/max

Determines the minimum and maximum percentage of water each cavern can contain.

Caverns with a water level of 10 or higher can support creatures and plants from the "Subterranean Water" biome, and caverns with a water level of 90 or lower can support the "Subterranean Chasm" biome; levels of 10-90 support *both* biomes, while levels below 10 or above 90 support only one.

Token
Example
Notes

[CAVERN_LAYER_WATER_MIN:]
[CAVERN_LAYER_WATER_MIN:0]
Range: 0 to 100

[CAVERN_LAYER_WATER_MAX:]
[CAVERN_LAYER_WATER_MAX:100]

#### Magma Layer

This parameter controls whether the magma sea exists.

Setting 1/Yes causes the magma layer to exist, value 0/No prevents it. Appears not to have any impact on volcanoes nor volcanism, so even if 0/No, there will still be embark locations with magma. If a volcano exists, it appears to always tap the magma sea, but the magma sea will not be revealed by revealing the volcano.

|                                  |                           |
|----------------------------------|---------------------------|
| Token                            | Example                   |
| `[HAVE_BOTTOM_LAYER_1:]` | `[HAVE_BOTTOM_LAYER_1:1]` |

#### Bottom Layer

Determines if the space below the magma sea exists. If Yes the "HFS" layer is always present. Normally you want to leave this set to Yes for maximum fun.

If enabled, this will force the magma layer above it.

|                                  |                           |
|----------------------------------|---------------------------|
| Token                            | Example                   |
| `[HAVE_BOTTOM_LAYER_2:]` | `[HAVE_BOTTOM_LAYER_2:1]` |

### Z Levels (Depth) Settings

These parameters control the "thickness" of various "layers" on the map. Note that a "layer" in this case does not refer to one Z-level, but refers to a number of related Z-levels such as "levels above ground".

The following table assumes that you have 3 cavern layers. (out of a minimum of 0-3) The Levels Above Layer settings control how many Z-Levels are above each layer. A layer may itself consist of multiple Z-Levels (and almost always does).

|  |  |  |
|----|----|----|
| Setting Name | Token | Description |
| Above Ground | \[LEVELS_ABOVE_GROUND:\] | The number of Z-levels of air above the highest surface level. / Has no impact on how many Z-levels deep the surface layer is. |
| Above layer 1 | \[LEVELS_ABOVE_LAYER_1:\] | Z-levels of stone above the first cavern layer. Making this higher will guarantee / at least / that many levels to build your fortress, but will have no impact on how many z-levels thick the surface layer is. Also, the top of a cavern may be higher than the rest of a cavern, so in practice there will be more "solid" levels than this above the cavern. / As of version 0.31.25 this setting is inaccurate. The actual number of z-levels may vary in a range of approx. ±5, which may result in non-existence of any solid z-levels between a surface layer and first cavern layer. |
| Above Layer 2 | \[LEVELS_ABOVE_LAYER_2:\] | Z-levels of earth between the very top of the second cavern and the very bottom of the first cavern. |
| Above Layer 3 | \[LEVELS_ABOVE_LAYER_3:\] | Z-levels of earth between the very top of the third cavern and the very bottom of the second cavern. |
| Above Layer 4 | \[LEVELS_ABOVE_LAYER_4:\] | Z-levels of earth between the very highest magma and the very bottom of the third cavern. / Spoiler Hidden (select invisible text to read): / Making this high will give a large area for HFS veins, so that it never touches caverns, giving more to mine / if / it was impacting the cavern previously. |
| Above Layer 5 | \[LEVELS_ABOVE_LAYER_5:\] | Uncertain. May control the number of levels of "Semi Molten Rock" between HFS and Magma, may control number of levels of magma, may impact both. / In experimentation, the overall depth of all magma sea and semi-molten rock levels appears to increase, but not consistent enough to say for certain. / Only valid if Magma Layer present. / Spoiler Hidden: / Often the HFS vein will only extend as high as the highest magma, making this the only guaranteed way to increase amount of HFS to mine, but unfortunately also creating enormous useless semi-molten z-levels |
| At Bottom | \[LEVELS_AT_BOTTOM:\] | Appears to be number of levels of HFS chamber. Only valid if Bottom Layer present, often having no impact. Values larger than default result in strange things. |

Some implications:

- The number of surface layers (e.g. soil), at this time, cannot be controlled. For example, on a map with 1 layer of peat, then a layer of silt, then a layer of obsidian, there is no control to let you increase either one to be, say, 20 z-levels. (though you may get lucky with the obsidian).
- There can be multiple stone layers between the cavern and the surface, so, increasing Levels Above Layer 1 may give you more conglomerate or more granite, and you have no control over which stone layer spans those Z-levels.
- The layers shown on embark span across the cavern layers in an unknown and inconsistent way. Sometimes those 10 different layers of stone are evenly distributed over your 400 z-level deep map, sometimes the first 9 get 1 z-level each and the last gets the other 391 levels. No way to control found yet.
- The HFS chamber, if present, will always extend into the rock layers, and appears to always make contact with the bottom cave. Large values for levels above layer 5 and layer 4 can result in enormous chambers, but the number of levels at the top (the part with undead) appears to be unaffected.
- Unconfirmed whether number of levels between caverns has any impact on cavern height. There will be connecting ramps and/or shafts between cavern layers no matter how many levels are between them.
- **Very Important**: These values appear to apply across a whole 16x16 region, not just embark areas. That means that if a 16x16 region is completely flat, but has one tall mountain in one far corner, even if you set Levels Above Ground low (e.g. 2 z-levels) you still have all the empty air of the highest mountain in every embark tile (e.g. 200 z-levels). Also can happen to the semi-molten layer, and can lead to unexpected behavior.
- Very large or small values can cause strange things to happen.

### Minimum/Maximum Natural Cave Size

It's not clear what effect these currently have, other than changing them can change the location of caves somewhat.\[Verify\]

Token
Example
Notes

[CAVE_MIN_SIZE:]
[CAVE_MIN_SIZE:5]
Range: 1 to 500

[CAVE_MAX_SIZE:]
[CAVE_MAX_SIZE:25]

### Number of Caves

The number of caves generated in mountainous and non-mountainous regions, mountain caves will always be generated on the edge of mountain ranges next to non-mountainous regions. Lurking kobolds set up shop in caves, and store their stolen items there - a setting of 0 in both will stop kobold civilizations from appearing. Special note: a cave is not initially a lair, although beasts can later use them as their lair.

Token
Example
Notes

[MOUNTAIN_CAVE_MIN:]
[MOUNTAIN_CAVE_MIN:100]
Range: 0 to 800

[NON_MOUNTAIN_CAVE_MIN:]
[NON_MOUNTAIN_CAVE_MIN:200]

### Number of Mythical Sites

The number of mysterious sites generated around the world. The extended effects of setting this to 0 has not been determined\[Verify\].

|                        |                           |                 |
|------------------------|---------------------------|-----------------|
| Token                  | Example                   | Notes           |
| `[MYTHICAL_SITE_NUM:]` | `[MYTHICAL_SITE_NUM:200]` | Range: 0 to 800 |

### Make Caves Visible

If set to no (default) then the location of caves will not be marked on the map. If set to yes, caves will appear on the map so that they may be sought out or avoided as desired.

|                                |                         |              |
|--------------------------------|-------------------------|--------------|
| Token                          | Example                 | Notes        |
| `[ALL_CAVES_VISIBLE:]` | `[ALL_CAVES_VISIBLE:0]` | 1/0 = Yes/No |

### Allow Init Options to Show Tunnels

If enabled, you will be able to see the underground tunnels often built by dwarves on the world map, and they will appear as black lines, similar to roads.

|  |  |  |
|----|----|----|
| Token | Example | Notes |
| `[SHOW_EMBARK_TUNNEL:]` | `[SHOW_EMBARK_TUNNEL:2]` | 0 = No / 1 = Only in Finder / 2 = Always |

### Number of Civilizations

This number of civilizations will be placed on the map before history generation begins. These civilizations may later die out due to historical events. It is noteworthy that the chance for any given civilization to be destroyed through megabeasts decreases with a higher total number of civilizations presentdata. The five races are dwarf, elf, human, goblin, and kobold; they will generally be placed in equal numbers until the quota has been reached. If there are not enough biomes or other worldgen prerequisites for an even distribution, certain civs will be much more or less frequent than othersdata. If there is an odd number of civs (not divisible by 5), then the remainder is distributed randomly. Kobold civs require caves to be placed; if no caves exist, then kobolds are skipped and will not appear. This does not cause rejections data. Goblin civilizations require multiple demons, see the number of demon types section above.

Note that a high value here can cause lots of map rejections, particularly on smaller maps as there simply isn't enough room or regions to put them all in.

|                       |                         |                 |
|-----------------------|-------------------------|-----------------|
| Token                 | Example                 | Notes           |
| `[TOTAL_CIV_NUMBER:]` | `[TOTAL_CIV_NUMBER:40]` | Range: 0 to 300 |

### Playable Civilization Required

If this is set to yes (default) then worlds will be rejected if no civilization with CIV_CONTROLLABLE can be placed. In an unmodded game, only the dwarves have this token.

If set to no, the result may be a world that cannot be played in Fortress Mode.

|  |  |  |
|----|----|----|
| Token | Example | Notes |
| `[PLAYABLE_CIVILIZATION_REQUIRED:]` | `[PLAYABLE_CIVILIZATION_REQUIRED:1]` | 1/0 = Yes/No |

### Minimum Number of Mid/Low/High Characteristic Squares

Sets the minimum possible number of squares of certain ranges of each of the region qualities, such as elevation, rain, drainage, volcanism, savagery, and temperature. These need to be changed to reflect your regional meshes and weights, and are responsible for a HUGE number of map rejections. These values can all be set to 0 for much fewer map rejections, particularly in the case of more wacky, non-standard maps.

These values will cause worlds to be rejected unless at least the given number of squares of the given type are randomly generated. Setting these values too high could result in worlds always being rejected if other parameters such as the maximum/minimums for elevation, etc., don't allow enough of those squares to get generated.

Token
Example
Notes

[ELEVATION_RANGES:::]
[ELEVATION_RANGES:8256:16512:8256]
Minimum number of squares that must have low, medium, and high amounts of the given attribute. / 0 = No minimum

[RAIN_RANGES:::]
[RAIN_RANGES:8256:16512:8256]

[DRAINAGE_RANGES:::]
[DRAINAGE_RANGES:8256:16512:8256]

[SAVAGERY_RANGES:::]
[SAVAGERY_RANGES:8256:16512:8256]

[VOLCANISM_RANGES:::]
[VOLCANISM_RANGES:8256:16512:8256]

## World rejection

*Main article: World rejection*

If you are having the common problem of generated worlds always being rejected by the world generator, see Solving World Rejection Problems (v0.31 page) as it contains many detailed suggestions on how to troubleshoot and solve these issues.

## Parameter set examples

If you're trying to do something specific, then the Worldgen examples - complete parameter sets that can be copied directly into your *world_gen.txt* file and customized as desired - might be helpful. If none of the examples suit your needs, Worldgen tricks has strategies and tips on making a world just right for you.

For many, many more examples see:

- DF2012 (v0.34) WorldGen "Cookbook" Thread
- DF2014 (v0.40) WorldGen "Cookbook" Thread
- DF2014 (v0.44.02+) WorldGen "Cookbook" Thread
- DF2014 (v0.47.01+) WorldGen "Cookbook" Thread
- DF2022 (v0.50.01+) WorldGen "Cookbook" Thread


---
*Parte 2 de 2 de «Advanced world generation». Demais partes em arquivos `...-part-{1..2}.md` na mesma pasta. Fonte: https://dwarffortresswiki.org/index.php/Advanced_world_generation*
