# Ramp

> Fonte: [Ramp](https://dwarffortresswiki.org/index.php/Ramp) — Dwarf Fortress Wiki (GFDL/MIT)

A **ramp** is a map feature that allows dwarves, wagons, and other creatures to move between levels. When hovering the cursor over these tiles, they are called **slopes**, and they occur naturally on most maps, acting as hillsides. Dwarves may make them by digging with from above or with from the same level. They can also be constructed with any available materials, with .

Ramps are the only way that wagons can move between levels in order to access a trade depot. Unless you build your depot above ground or set into a cliff, you will probably have to create ramps to allow access to it.

In ASCII mode, ramps are shown with the ▲ symbol (pointing "up"). The space above a ramp is shown as a ▼ and called a "downward slope". A downward slope is not an actual feature (as opposed to a downward stair), but rather an indication of a ramp below it; it functions otherwise as open space -- much like the game shows to indicate trees or terrain on the level below, the ▼ symbol is a display nicety, not a type of terrain. When the rest of this article refers to ramps, the actual ramp (▲) is meant.

Note that ramps function similarly to floors in that units can walk on them without any problems, even if they are over open space. They will also support adjacent buildings.

## Movement using ramps

For the purposes of unit movement, a ramp connects the ramp bottom to the **tops of walls adjacent to the ramp bottom**. So unlike stairs, where a dwarf moves directly up or down, a dwarf moving via a ramp will move diagonally across Z-levels, changing both horizontal and vertical location in a single move. This can make it seem like a ramp has "direction" or "flow" by itself, but in fact this depends entirely on the spaces adjacent to the ramp.

More formally, a usable ramp requires four tiles:

1.  A ramp tile
2.  An open space tile directly above the ramp
3.  An adjacent "solid" tile on the same Z-level (including diagonals). Some special tiles such as semi-molten rock do not count as "solid" for this purpose.
4.  A "walkable" tile directly above the "solid" tile

If these conditions are met, creatures will be able to move back and forth between the ramp space and the walkable space above the adjacent wall. Otherwise, the ramp will be labeled as "Unusable" when hovering with the mouse.

These conditions mean that if one were to try to create a "stairwell" with ramps, one would have to place the ramps adjacent to one another across Z-levels, rather than underneath one another as they would when building stairs. Each ramp would also have to be supported by a solid tile on the Z-level beneath it; this means that a sequence of ramps will become unusable if, for instance, the player attempted to make a 180º turn and build one ramp on the Z-level directly beneath another. The dwarven fortresses created during worldgen provide examples of ramp implementation, generally using ramps for the main entrance stairwell into the fortress, as well as when changing elevation in the tunnels they build through the caverns.

**Example A** shows a situation where a ramp might be created that is actually unusable. Dwarves cannot ascend or descend (or cross) the ramp as shown because the walkable spaces above the ramp are not walled underneath, therefore dwarves cannot move between the ramp bottom and the spaces by the top of the ramp. If walls were added under the upper floor spaces, the ramp would become usable.

**Note:** Fortifications **can** be used by ramps as the adjacent "solid" tile, provided those fortifications have a walkable space above them (which would apply to all carved out fortifications, or those constructed with additional flooring).

Finally, wagons follow a completely different set of movement rules on ramps. This can be exploited used to create separate paths for wagons and other (walking) creatures creatures"), for example to allow wagons to proceed directly to a depot while directing all other visitors through a trap filled maze.

## Creating ramps

Dwarves may construct ramps out of building materials such as stone, wood, blocks, and bars, but it is more common to dig them from natural walls (see mining).

Digging ramps can be accomplished in two ways. Dwarves can carve ramps from any of the 8 adjacent spaces on the same z-level. Dwarves can similarly channel down from above, which will carve a ramp out of the natural wall below (if any). In both cases the space and floor above the ramp will be carved out as well to make an open space. Note that both levels of digging may produce a stone, so after digging a ramp or a channel, you may be left with 0, 1, or 2 stones.

Note that dwarves will happily dig out or construct ramps that are not immediately usable. Check the criteria above if dwarves do not seem to be using the ramps they have made.

## Collapse

Natural or carved ramps that are adjacent to walls will collapse (disappear) if those walls are mined out. This can strand dwarves, so be careful when removing walls near those ramps. In addition, trying to carve a ramp under something that cannot be dug out (such as a construction, building, or tree) will result a slope, but leave the upper floor intact. This may create a cave-in situation dangerous to your miners.

Constructed ramps will not collapse, and it is possible to create carved freestanding ramps as well, but the ramps will still not be usable without adjacent walls.

## Removing ramps

Natural and carved ramps can be destroyed via the digging orders menu by pressing , using the in-game interface). Like the selection says, only upwards slopes (and carved stairs) can be removed in such a manner, and only from the same level as the (upward) ramp. Selecting a downwards ramp in this manner has no effect, and removing the upward ramp will automatically remove the downward ramp designation from the level above, replacing it with "open space". Ramps at the edge of the map cannot be removed this way (however, you can build a floor on top of that ramp with and deconstruct it later - it will remove the ramp).

Removing ramps is a fast process, on par with digging through sand or soil, and can train your miners quickly.

Constructed ramps can be removed like any other construction via the designation menu with the Remove Construction selection ( -\> ).

## Ramps versus stairways

As explained above, ramps have important limitations, but if constructed correctly they can allow slightly faster movement than stairways. For example, if a dwarf wants to go down and to the north using a stairway, it will have to take two steps: one step down a stairway and one step to the north. Going to the same place using a ramp only requires 1 step. Walking up or down a ramp has the same movement cost as walking on level ground.

Unlike stairs, ramps do not work well with hatch covers. A dwarf standing on a hatch cover over a ramp will drop items he is carrying if the hatch opens, possibly injuring any dwarves below.

## Ramping versus channeling

When digging shafts, ramps don't provoke climbing as easily as channels (which will do so in about five levels). You can channel bare floor with no wall (or only a pillar) below, resulting in a hole with no ramp. Falls can still hurt, though. Digging channels two levels above warm stone allows you to remove it without getting warm stone cancellations, and digging ramps 1z below wet stone similarly allows you to remove that.

Digging progress only accumulates in revealed tiles, which means ramps or channels will behave differently when digging gets interrupted. Channels cannot be designated on buildings (including stockpiles). However, if a *ramp* is dug below one, the floor above remains intact, but items on the tile above the ramp will fall down as if the floor above the ramp had been removed.

A ramp can be dug diagonally upwards while standing on a ramp, thus allowing you to reach 2 z-levels above the miner. This can be done even if there's a building, such as a bridge, above.
