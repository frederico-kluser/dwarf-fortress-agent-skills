# Biome

> Fonte: [Biome](https://dwarffortresswiki.org/index.php/Biome) — Dwarf Fortress Wiki (GFDL/MIT)

A **biome** is a biotic area with homogeneous features, characterized by distinctive plants, animal species and climate. A biome will also contain only one set of stone layers, though these usually expand beyond a single biome. Your dwarves will find different resources depending on which biomes you select when starting a fort.

## Selecting a biome

Biomes are important when choosing a fortress location in order to understand your surroundings. Individual biomes, which form at least one map-tile of your embark location, can be cycled with the function keys; for example, an area with 3 biomes present can be cycled using , and . The selected biome will be highlighted with flashing Xs on the Local Map, and the biome's information will be displayed on the right side of the screen.

## Characteristics of biomes

Selecting different biomes gives you some ability to influence the difficulty of your game. Each biome has a different set of resources; the availability of trees, sand, certain plants or animals, and sometimes water is specific to a particular biome, and different biomes may have different stone layers containing flux, coal or useful ores. Mountains have a lot of ore, but no soil.

Generally it is advantageous to plot your embark location at the convergence of multiple different biomes, the more the better (within reason) - which is made easier if you enlarge your starting embarkation area. However, it is not usually too hard to find three or four biomes using the default size.

*Note: Making the starting plot larger will slow your game down considerably; likewise, a small embark area can dramatically increase framerate. One embark square translates to 48×48 ingame tiles*

By making use of several biomes, you can provide more resources for your fort. Making sure one of your biomes contains either a broadleaf or conifer forest will provide you with an ample supply of trees, even if the rest of your plot extends into badlands and desert.

All biomes also have some kind of "alignment" -- good, neutral, or evil -- and a degree of "savagery", which essentially measures how relatively peaceful the biome is. The combination of alignment and savagery is referred to as the biome's surroundings. However, a named region (which is a contiguous area of one category of biomes, such as forests or wetlands) will be either good, neutral, or evil. It is not uncommon to see a large mountain range with one alignment, and a few mountains, disconnected from the main mountain range by a single region tile, with a different alignment. Therefore, the more biomes you have, the more likely it is to have combinations of different alignments and savageries, if so desired.

If your plot contains only ocean, lake, or mountain biomes, you will not be able to embark (the dwarves would have difficulty parking their wagon "wagon") on water, while mountains are too barren and remote to reach).

## Available Biomes

### Wetlands

Wetlands may be Swamp or Marsh; may be Freshwater or Saltwater; and may be temperate or tropical. In addition, there are mangrove swamps.

### Forests

- Taiga
- Temperate Coniferous Forest
- Temperate Broadleaf Forest
- Tropical Coniferous Forest
- Tropical Dry Broadleaf Forest (\* due a bug, only generates in worlds with poles of a Medium or Large size)
- Tropical Moist Broadleaf Forest

### Plains

Plains include grassland, savanna and shrubland; they may be either temperate or tropical.

### Deserts

Desert biomes are the driest of all the biomes with sparse to no vegetation. There are three varieties of deserts: **Badlands**, **Rocky Wasteland**, and **Sand Desert** characterized by very little arable land, stony plains and billowing sand dunes. Deserts can be hot, or quite cold.

### Oceans

An expansive body of salt water. There are three varieties of oceans, based on temperature: Arctic, Temperate and Tropical.

### Murky Pools

These include Freshwater, Saltwater and Brackish pools, which may be either temperate or tropical.

### Lakes

Like pools, these may be Freshwater, Saltwater or Brackish lakes, and may be either temperate or tropical.

### Rivers

Like pools and lakes, these may be Freshwater, Saltwater or Brackish rivers, and may be either temperate or tropical.

### Underground

- Subterranean Water
- Subterranean Chasm
- Subterranean Magma

### Other

- Mountain
- Glacier
- Tundra

### Groups

Certain creatures and plants use special biome tokens to encompass several similar environments.

- "" includes all land biomes except Mountains, Glaciers, and Tundras. All plants require a "Not Freezing" biome (or a more specific biome group); you will be unable to grow any aboveground crops at all in a Mountain biome.
- "Any Temperate Broadleaf" includes temperate broadleaf forests as well as grasslands, savannas, shrublands, swamps, and marshes.
- "Any Tropical Broadleaf" includes tropical dry/moist broadleaf forests as well as grasslands, savannas, shrublands, swamps (including Mangrove), and marshes.

More information can be found in the Biome token list.

## Generating a Biome

When using advanced world generation or world painter to attempt to create the "perfect" starting location, it helps to understand how biomes are created. Biomes are calculated for each region tile (the center map when choosing an embark), then noise is calculated and applied which causes the irregular region boundaries on the local map. For the most part, a region's biome is a factor of elevation, drainage, rainfall, and temperature, as explained in this old forum thread for 40d.

When determining the biome, elevation comes first; any terrain with an elevation of 0-99 is ocean, while any terrain with an elevation of 300-400 is mountain. All other biomes lie in between these two extremes. The remaining base biomes are determined by the combination of drainage and rainfall.

All other biomes are variations on the corresponding base biome shown above. For example, salinity determines the type of lake, swamp, and marsh. A salinity of 0 is a freshwater biome, 33 is a freshwater swamp or marsh but a brackish lake, 66 is a saltwater biome, and 100 is an ocean. Temperature determines tropical and frozen variants. Region tile temperatures at or below -5 convert all base biomes with drainage below 75 to Tundra, and biomes with drainage 75+ to Glaciers. Similarly, Arctic Oceans replace Temperate Oceans. Between -4 and 9 (inclusive) Conifer Forests become Taiga. At the other end of the temperature scale, biomes become tropical at around 85+; generally speaking you'll need Hot and Scorching temperatures. Tropical Saltwater Swamps are converted to Mangrove Swamps when drainage is 9 or less. Unfortunately, temperature is harder to affect directly in world gen because, according to Toady One, it's affected by latitude, elevation, and moisture. Additionally, when the pole setting is none, the tropical or frozen biome variants do not respect the otherwise static divisions.

## Bugs

- Different biomes can exist in layers above the surface. This can lead to odd behavior like evil rain above a "good" biome.
