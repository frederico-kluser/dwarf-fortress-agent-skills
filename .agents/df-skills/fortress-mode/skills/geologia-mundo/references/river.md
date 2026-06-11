# River

> Fonte: [River](https://dwarffortresswiki.org/index.php/River) — Dwarf Fortress Wiki (GFDL/MIT)

A **river** is a body of water flowing from the mountain springs towards an ocean or a lake. Rivers serve as a terrain feature and gameplay element, coming in a variety of sizes and types. Larger ones will impede movement and may serve as a natural defensive boundary, while brooks, being the smallest type of river, can be crossed safely without needing to swim, risk of drowning, or even getting one's feet wet. In hilly terrain, particularly with cliffs, waterfalls can be found. Rivers can be the lifeblood of a fortress, potentially providing a renewable source of water and wildlife for fishing, hunting or danger when traveling near them. They can also freeze.

## Overview

There are five different kinds of surface rivers: major rivers, rivers, minor rivers, streams and **brooks**. For most purposes, each kind will simply be referred to as rivers or brooks. The only differences between the first four types are their appearance on the world map, their width, and possibly their rate of flow.

### River

Rivers are represented by dark blue and water tiles stretching from one edge of the map to another, with banks bounded by downward slopes , or when frozen. Rivers come in a variety of sizes, from tiny brooks only three or four tiles wide, to major rivers spanning as wide as 40 tiles. If flow amounts are turned off in `d_init.txt`, river tiles will also be constantly blinking to indicate that the water has flow. Rivers are an effectively unlimited source of water, entering the map at the upstream end and leaving at the downstream end.

To determine which end of a river is downstream, you can carefully look at the ends of the river using . The end that has multiple tiles of less than 7/7 water is the downstream end. (This strategy doesn't always work on freshly-generated maps, as the river can still be completely full of water.) Flow amounts can be enabled in d_init.txt, which eliminates the need to use but also removes flow indicators. A dwarfier method would be to kill something, get its blood in the river, and observe the direction of the blood's movement.

Dwarves will not swim across rivers in fortress mode, regardless of their swimming skill, and unskilled dwarves that end up in a river can quickly drown in the current. Dwarves will only seek dry routes across rivers, such as a bridge, floor, or tunnel.

As a biome, there are six types of rivers, divided by climate and the salinity of the water (see table below). The biome greatly affects the creatures of the water and surrounding land. Additionally, rivers are more prone to having an aquifer close to the surface, and most riverbeds are made of layers of clay or sand.

|  | **Freshwater** | **Brackish water** | **Saltwater** |
|----|----|----|----|
| **Temperate** | Temperate freshwater river | Temperate brackish river | Temperate saltwater river |
| **Tropical** | Tropical freshwater river | Tropical brackish river | Tropical saltwater river |

### Brook

Brooks are the smallest type of river. They have a unique property that allows creatures (including wagons) to travel across them without swimming, or even getting wet. Water and other fluids can fall through the surface of a brook, and fisherdwarves can stand on the surface of a brook to fish. Otherwise, brooks function like any other river.

### Appearance on the regional map

On the regional map, there are five different classifications of rivers, identified by their appearance and the text displayed at the right side of the screen when they are selected in the local map view (major rivers, rivers, minor rivers, streams and brooks). Representing the connectivity hierarchy of how the river from small headwater brooks up to large river mouth emptying into the ocean. Brooks are not directly visible on the regional or world maps, but can still be seen in the local map and will also be indicated at the right if you select a tile containing a brook.

[TABLE]

## Other important facts

- Rivers contain an unlimited amount of water and cannot be drained like murky pools. They can, however, be dammed if you can *temporarily* drain part of them to 1/7 or less for long enough to construct walls or install floodgates. Despite being an unlimited source of water, river source tiles will only refill up to the level of the river's source - it will not overflow if you dam it up. This video demonstrates one way to drain and dam a river: 1. Another way to dam a river is to direct magma into it, producing obsidian in the squares where it encounters water.
- Even if dammed, a dry riverbed will refill when it rains, similar to a murky pool.
- A dammed river will cease to produce additional water once all of its tiles reach 7/7, even if the dam is subsequently opened, until the water level near the river's source drops below 7/7.
- After a river has been drained, the tiles will still appear as "river" when viewed. These appear to have no effect, but can be removed by flooring over them or mining. If a construction is built on a river tile and removed, furrowed soil will appear.
- Sometimes, the dwarves end up parking on the ice in cold regions, on arrival to a new settlement area. Needless to say, in places where ice can melt, this is quite dangerous and might result in a lot of fun when retrieving all the necessary stuff.
- If embarked on the source of a river, there will be a delta-looking feature that water flows **from**. i.e., the source tiles for the head of a river are not at the border of the map, but rather the network of 1-2 tile wide rivulets that converge into the river proper. If you wish to dam this at the source you will need to either go downstream far enough from the source tiles and dam as usual, or use a screw pump to pump out enough water to wall off the tile. Given the volume of water it outputs, this is difficult and can lead to FUN.

## Wildlife

### Creatures

[TABLE]

**In savage rivers:**

[TABLE]

### Vermin

[TABLE]
