# Z-axis

> Fonte: [Z-axis](https://dwarffortresswiki.org/index.php/Z-axis) — Dwarf Fortress Wiki (GFDL/MIT)

*For information on the key, see Status screen*

The third axis is known in math as the **z-axis**. It measures "up and down" distances. A z-level is one layer of the map that can be viewed at a time. Changing z-levels is done with the (up) and (down) keys.

## Three dimensions

It's easy to think of a graph with an x-axis and a y-axis, right?

In the *Dwarf Fortress* map view, traveling east or west moves you along the x-axis, and traveling north or south moves you along the y-axis. Traveling higher or deeper moves you along the z-axis.

The z-axis, as you can see, is perpendicular to both the x-axis and the y-axis to create a 3D coordinate system, which is what *Dwarf Fortress* is based in.

Thus, objects described with only two axes are two-dimensional, whilst objects with depth measured along the z-axis are three-dimensional.

The z-axis is believed to be in part of the game engine that calculates accuracy of weapons based on where dwarves are, how missiles fly, and other similar considerations.

To move up and down, use and (which are and in most keyboard layouts). You can also move up and down using the numpad with and , which is especially convenient for players who use the numpad for horizontal navigation.

## Keeping track of where you are

In fortress mode, the right-hand margin shows your location on the z-axis. Blue is above ground, brown is below ground, and the bright spot in the middle (yellow or cyan) shows the current level. This reflects the elevation profile for the spot the cursor is currently over. Moving up or down will not change the position of the bright marker, but will instead shift the whole bar under it. The number at the top shows how many levels above or below the surface the spot currently is. The number at the bottom is the elevation of the current level relative to the world's lowest ocean depth.

The top number (red or green) represents the number of z-levels away from ground level *at the center of the screen*. If there are mountains, or any form of uneven terrain on your map, these numbers will vary in the same z-level. There isn't currently a way around this. To view the z-level at a certain point, loo often works (although it can be a bit unreliable with hills). This is useful for viewing the z-level near the map edge, which can't be centered on.

## Boundaries between layers

There are effectively two parts to z-layers - the layer itself (the z-level where stuff happens, things exist and dwarves work), and the boundary\* *between* those layers/levels. These "boundaries" are just that - boundaries - they have no thickness, dwarves and items are never found there, and nothing ever happens there - but they act as barriers between adjacent layers. Boundaries are also referred to as "floor tiles" (not to be confused with floors).

*(\* The word "boundary" is not an in-game term. You will never see a boundary, only see the effects when one is pierced, giving access, desired or undesired, between levels. You can think of the "boundary" as the "floor", but that's not perfectly accurate in all situations - but close enough to start.)*

So you have something like this...

`Level 0 `\
`__________`\
` LEVEL-1`\
`__________`\
` LEVEL-2`\
`__________`\
` LEVEL-3`\
`__________`\
` (etc...)`

...where each line is the boundary between the level above and below it.

The barrier is invisible - you only see the different layers. But once pierced, creatures and items can move/fall through a boundary, and miasma and fluids can pass through as well. With some actions, you remove just a layer, and with some you also pierce the boundary.

Mining is simply tunneling - you dig out the stuff of the level itself, and never touch the upper or lower boundary. Tunnels, rooms, and even up stairs exist on single z-levels. (Downstairs or up/down stairs pierce the lower boundary.)

When you dig a ramp, you pierce the barrier *above* you into the z-level above the level you are on. *(The ramp is on the lower level only, but is also visible from the upper.)*

When you dig a down-stair or a channel, you pierce the barrier *below* the level you are on. *(Note that an upstairs does*not'' (usually) pierce the layer above it, but requires a down-stair to pierce the boundary above it to provide a path between levels.

Boundaries also act as "support" for building, constructions, and natural formations above them. If you completely channel out around something, and there is no "layer" supporting it either from above or below, it will collapse.

In open space, the boundaries have already been removed. Constructions, such as floors, walls, and up stairs, can replace boundaries between levels, re-sealing them.

## See also

- Z-level
- Water
- Magma
- Flooding
- Miasma

## External links

- DF Map Archive - a community site for sharing maps, lets visitors browse vertically through z-levels in exported maps
