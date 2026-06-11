# World rejection

> Fonte: [World rejection](https://dwarffortresswiki.org/index.php/World_rejection) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*Dwarf Fortress* uses a "belt and braces" method of world generation in that, whilst the map properties are configurable by world tokens, there are also tokens which will cause the rejection and 'reroll' or re-randomisation of the world. By way of example, if you were to leave the world at its default settings, but set a rejection parameter which required there to be a large number of "minimum desert tiles", then a large number of worlds might be rejected until one (by random chance) was finally generated that met that requirement. Because of the high number of possible rejections, this is an inefficient way of generating a world with many deserts; instead, it's recommended to work with broader parameters, such as Weighted Ranges, to generate the world you want. It is possible to set the parameters in such a way as to result in endless rejections, because they specify a world which is incredibly unlikely or impossible to be generated.

If a certain number of rejections of the same type happen during world gen, then you will get a notification telling you what is causing the rejections. This can happen after a few hundred rejections or it may take thousands. This is possibly due to the fact that you may have more than one type of rejection occurring, and as such it takes thousands of rejections until any one type hits the threshold for the warning message.

A message that appears when one of the rejection types hits its threshold

To log all rejections into a file, enable the relevant setting on the Game tab in the settings. The next time a world is generated, this will create a file called `map_rejection_log.txt` in the main *Dwarf Fortress* folder, into which the rejection reasons will be saved. Reading this file will give you a better insight into why the world was being rejected than the notification message shown above.

## Rejection parameters

The following are the primary rejection parameters, their sole purpose is to cause rejections, they do not affect the generation of the world in any way:

      [REGION_COUNTS:SWAMP:0:0:0]
      [REGION_COUNTS:DESERT:0:0:0]
      [REGION_COUNTS:FOREST:0:0:0]
      [REGION_COUNTS:MOUNTAINS:0:0:0]
      [REGION_COUNTS:OCEAN:0:0:0]
      [REGION_COUNTS:GLACIER:0:0:0]
      [REGION_COUNTS:TUNDRA:0:0:0]
      [REGION_COUNTS:GRASSLAND:0:0:0]
      [REGION_COUNTS:HILLS:0:0:0]

\

      [ELEVATION_RANGES:0:0:0]
      [RAIN_RANGES:0:0:0]
      [DRAINAGE_RANGES:0:0:0]
      [SAVAGERY_RANGES:0:0:0]
      [VOLCANISM_RANGES:0:0:0]

**Note: the above values are arbitrary although these settings effectively disable the region/range counts.**

## Placement tokens

The following tokens are not rejection parameters, but instead *force* the placement of certain features. This can cause rejections if the world generated does not support the placement of the features in sufficient quantities, or at all. For example, a volcano requires the square to have a volcanism of 100, if the maximum volcanism for the world is less than 100, then no volcanoes can be placed. See advanced world generation for more details.

      [VOLCANO_MIN:3]

      [PEAK_NUMBER_MIN:12]

      [PARTIAL_OCEAN_EDGE_MIN:1]
      [COMPLETE_OCEAN_EDGE_MIN:0]

      [RIVER_MINS:300:300]

      [MOUNTAIN_CAVE_MIN:25]
      [NON_MOUNTAIN_CAVE_MIN:50]

      [TOTAL_CIV_NUMBER:40]
      [PLAYABLE_CIVILIZATION_REQUIRED:1]

## Others

It is unknown if the following tokens can cause rejection:

      [REGIONAL_INTERACTION_NUMBER:28]
      [DISTURBANCE_INTERACTION_NUMBER:28]

## Placement tokens that will not cause rejections

Counts exceeding the number of available squares will just make all squares in the desired region size the desired type.

      [GOOD_SQ_COUNTS:0:0:0]
      [EVIL_SQ_COUNTS:0:0:0]
