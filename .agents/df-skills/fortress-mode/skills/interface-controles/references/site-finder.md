# Site finder

> Fonte: [Site finder](https://dwarffortresswiki.org/index.php/Site_finder) — Dwarf Fortress Wiki (GFDL/MIT)

The **site finder** is a menu on the embark screen that helps the player search for embark positions based on preferences. It can be invoked from the embark screen by pressing .

The highlighted feature can be switched by using and , the setting can be selected using and or the analogous keys on the keypad ( and ).

A selection set to N/A will not influence the search, while a setting other than that does not guarantee a hit - if we use the example of a 2x2 location with a river, no aquifer, and multiple deep and shallow metals, it is quite possible that there is no such site on your world map. The finder will then display a **candidate** that fits as many as possible of the selected settings in the desired size.

The search will check the entire world. If there are multiple sites that match your settings, the site finder will mark all acceptable sites on the Region and World maps and allow you to examine them for yourself.

More information on some of the settings can be found on the World generation page.

## X Dimension / Y Dimension

Range for either: 2 to 16

This setting controls the initial size of the embark rectangle. The finder searches the world map for the selected features using a rectangle of the selected size. A larger rectangle will usually lead to a higher chance of finding all selected features due to the site being larger, but will impact game performance (the larger the rectangle, the lower the FPS).

## Savagery

Range: N/A, Low, Medium, High

These settings mean the same as the **Benign, Neutral, Savage** settings on the Regions page.

## Evil

Range: N/A, Low, Medium, High

These settings relate to the **Good, Neutral, Evil** designations on the Regions page.

It also seems to be an average for the selected area: an area evenly divided between Good and Evil will show up on a search for "Medium", while "Good" will usually turn up a predominantly good area.

## Elevation

Range: N/A, Low, Medium, High

If this is set to low, the result will be mostly flat land. Medium and high search for hills/mountains respectively.

## Temperature

Range: N/A, Low, Medium, High

This does not correspond directly to Freezing/Cold, Temperate/Warm, Hot/Scorching (see Climate).

The low setting will only show freezing biomes.

Medium will show most of the biomes including cold, temperate, warm, hot and the majority of the scorching ones.

The high setting shows only a fraction of the scorching biomes.

## Rain

Range: N/A, Low, Medium, High

Selects the amount of rain/snow to expect (see Weather).

## Drainage

Range: N/A, Low, Medium, High

This, along with other factors, determines the terrain type to look for. High drainage areas include glaciers and deserts. Low drainage areas include swamps and marshes.

## Flux Stone

Range: N/A, No, Yes

Controls whether a candidate must have flux stone. It may be a good idea to check the layers list to confirm you have flux close to the surface, since the site finder will happily count a marble layer 1 z-level above the magma sea as an embark site that does contain flux.

## Aquifer

Range: N/A, No, Yes

Controls whether a candidate must have an aquifer.

## River

Range: N/A, No, Yes

Controls whether a candidate must have a river.

## Shallow Metal

Range: N/A, None, Yes, Multiple

Controls whether a site must have shallow metal(s).

Metals appear to be classified as "shallow" if they occur within the first 2 stone layers, except for Sand Deserts and Shallow Oceans which count the first *5* stone layers.

## Deep Metal

Range: N/A, None, Yes, Multiple

Controls whether a site must have deep metal(s).

## Soil

Range: N/A, None, ≤ Little, ≤ Some, ≤ Deep

Controls how much soil a site is allowed.

## Clay

Range: N/A, No, Yes

Controls whether a candidate must have clay.
