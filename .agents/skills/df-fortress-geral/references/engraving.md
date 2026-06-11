# Engraving

> Fonte: [Engraving](https://dwarffortresswiki.org/index.php/Engraving) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

A dwarf eating cheese

The process of **engraving** smoothed or constructed walls and floors increases their value further, and gives them a quality level. It is unknown if dwarves currently look at engravings (in previous versions, they did not), but if they do, it would no doubt satisfy their need to admire art.\[Verify\] Engravings made with a quality of -Well-crafted- and higher will usually be in reference to previous events, but they can still be depictions of something the engraver cares about, whether they love it or absolutely hate it. You can examine the contents of an engraving by clicking on it.

Any constructed tile or non-[`[SOIL]`](/index.php/Inorganic_material_definition_token#SOIL "Inorganic material definition token") natural tile that has been smoothed can be engraved, even slade and the materials that exist in geological layers only as a result of a glitch.\[Verify\] Engraved ice is called "Sculpted Ice".

## Process

You can only engrave non-soil floors and walls. However, smooth and constructed walls/floors can both be engraved. The material the tile is composed of has no effect on the process of engraving, so a constructed wood/glass wall can be engraved in the same way as a natural stone wall. Once the area has been smoothed with v-m (not necessary for constructions), you may designate it to be engraved using v-g. The dwarf must have the Engraving work detail active and the Stone Cutting work detail active to smooth a rough cave tile.

Once a tile is designated, the theme or content of the engraving can be selected by first clicking on the designated tile and then on the "specify image" button. This must be done before the game is unpaused. If no selection is made, then the contents of the engraving are left to the choice of the engraver performing the job. Note that engraving glass floors will remove their transparency.

Engravings are directional—only a room containing the tile the engraver stood on when it completed will receive the engraving value bonus. There is no way to engrave more than one side of a single wall tile.

Using only highly-skilled engravers will result in high-quality engravings, and therefore higher room and fortress value.

## Toggling

Settings exist in the game for enabling and disabling the display of engravings, but this currently does not work, either by manually designating an engraving as hidden or by changing the in game/init setting. See previous version for how this used to work.

## Removal

Floor engravings of unsatisfactory quality and/or content (e.g. carvings of elephants mauling dwarves) can be removed by designatingv the carving of minecart tracks over them. The tracks can then be removed by smoothing the stone, which results in fresh, smooth stone tiles ready for another attempt at engraving.

There are bugs with engravings on constructed floors that make it tricky to remove them—simply removing the constructed floor and building it back will result in the engraving reappearing, albeit without any description text.

To remove an engraving from constructed floor located on stone, first deconstruct the floor, then smooth the floor. This will cause the engraving to magically reappear, meaning it is now safe to put new constructed flooring over it. As an alternative to smoothing, you can also carve minecart tracks.

To remove an engraving from constructed floor located on soil, first deconstruct the floor, then build a wall, then cut arrow slits into the wall, then destroy the wall, and then rebuild your constructed floor.

Both methods will reset your floor to a fresh state, allowing you to start anew.

Floor engravings can also be removed from natural walls by allowing magma to flow over them, which reverts the tiles to their smooth form.

Wall engravings can only be removed by removing the wall – mining in the case of natural walls, or removing a constructed wall using m-x.

Removing engraved natural walls/floors will remove the engraving without triggering the negative thought. However, removing a masterwork engraving using any method except construction removal will cause a message and an unhappy thought in the artist who engraved it, as will mining a natural wall with a masterpiece on it.

## Effects on room value

The center area of the floor has been engraved. The left and bottom walls are also engraved, but the top one is not.

How engravings affect room values has changed considerably, such that even the value of wall and floor tiles must first be understood.[1] In a nutshell, however, in almost all cases it is now better to place walls/floors with high-value materials and then engrave those. It doesn't matter whether that placement is done using blocks, a rough boulder, or metal bars, as long as it is a Construction.

For floor tiles, their value calculation is \[floor origin multiplier\] × \[floor material value\] + \[engraving bonus\]

|                   |            |
|-------------------|------------|
| Origin            | Multiplier |
| rough cave floor  | 1×         |
| smooth cave floor | 4×         |
| constructed floor | 7×         |

Floor Origin Multipliers

If the floor is engraved, the added engraving bonus is \[10\] × \[floor material value\] × \[quality value modifier\], with those modifiers being:

|               |                  |                  |
|---------------|------------------|------------------|
| Designation   | Description      | Value / Modifier |
| Engraving     | —                | 1×               |
| -Engraving-   | Well-crafted     | 2×               |
| +Engraving+   | Finely-crafted   | 3×               |
| \*Engraving\* | Superior quality | 4×               |
| ≡Engraving≡   | Exceptional      | 5×               |
| ☼Engraving☼   | Masterful        | 12×              |

If a dwarf has a preference for the type of stone in which the engraving was made, its value doubles in their eyes. However, the actual image depicted in the engraving has *no* effect on its value.

Bearing all this in mind, if, for example, you placed a single golden block floor in a room, that floor tile would increase the value of that room by (7) × (30) = 210☼. If that floor tile was then engraved with a Masterwork, it would be worth an additional (10) × (30) × (12) = 3600☼, for a grand total of 3810☼. Since the material value of the floor is used in both calculations, using high-value materials on floor tiles you plan to engrave can make the value of the rooms they're in skyrocket!

However, if a floor tile exists in more than one designated room, all overlapping rooms will have their value reduced to **zero**. Sharing a door that does not have two adjacent wall tiles (i.e. the rooms have double-doors rather than single doors) implies sharing the tile under the door as well. However, having only a single door between two walls will not cause an overlap penalty, which allows internal offices and bedrooms inside of houses to function. You can remove this penalty simply by un-designating any floor tiles that overlap in more than one room's designation. Not all room designations cause this penalty, however. You'll know the penalty has triggered when you see the room's name turn red and gain "Overlapping."

Wall engravings work similarly, being \[wall origin multiplier\] × \[wall material value\] + \[engraving bonus\]

|                   |            |
|-------------------|------------|
| Origin            | Multiplier |
| natural cave wall | 1×         |
| smooth cave wall  | 5×         |
| constructed wall  | 9×         |

Wall Origin Multipliers

If the wall is engraved, the added engraving bonus is \[10\] × \[wall material value\] × \[quality value modifier\], using the same modifiers as above. However, wall engravings are *directional*, only providing their value to the room which contains the floor tile the engraver was standing on at the time of completion.

Unlike floor tiles, walls can be in multiple room designations. There is no room value penalty if the same wall is in two or more designated rooms, though engravings will only count toward one of the rooms (based on the engraving direction). Because of how walls interact with rooms and doors, and rooms don't have to be contiguous, you can increase the value of all bedrooms in your fortress by making use of these rules.

## Room Value Exploit

According to Reddit user TBTerra:

1.  Make a line of wall with 1 tile gap either side (if your engravers are really good this might only need to be 2-3 long)
2.  Make the lines of floor either side of this wall out of the most valuable material you can (aluminum or platinum are great; steel and gold also work), and have your best engraver engrave them
3.  Place doors on top of all those engraved tiles, what sort doesn't really matter, as they will be adding 10-100 value to 2-3k value floor tiles
4.  For every room add the doors and the wall(this is a convenient rectangle). The wall makes the doors shareable, and the doors make the engraved floor shareable.

For optimal results hide this to the south east of your area, otherwise the zone icons can get rather confused

## Bugs

- While the quality rating of engravings on ice walls is shown properly, the quality of engravings on ice *floors* doesn't show when looking at a tile with k, only when hitting enter to inspect the engraving. This gives the false impression that engraved ice floors have no quality levels. In addition, the engravings are described as "engraved on the wall" instead of "on the floor".\[Verify\]

Engraving of a Hindu civilization.

- Engravings on constructed floors magically reappear when removing the floor and placing new floor, or when removing the floor and smoothing the natural floor beneath.
