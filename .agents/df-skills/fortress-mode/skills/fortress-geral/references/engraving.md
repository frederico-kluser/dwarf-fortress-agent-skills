# Engraving

> Fonte: [Engraving](https://dwarffortresswiki.org/index.php/Engraving) — Dwarf Fortress Wiki (GFDL/MIT)

The process of **engraving** smoothed or constructed walls and floors increases their value further, and gives them a quality level. It is unknown if dwarves currently look at engravings (in previous versions, they did not), but if they do, it would no doubt satisfy their need to admire art. Engravings made with a quality of -Well-crafted- and higher will usually be in reference to previous events, but they can still be depictions of something the engraver cares about, whether they love it or absolutely hate it. You can examine the contents of an engraving by clicking on it.

Any constructed tile or non- natural tile that has been smoothed can be engraved, even slade and the materials that exist in geological layers only as a result of a glitch. Engraved ice is called "Sculpted Ice".

## Process

You can only engrave non-soil floors and walls, however smooth and constructed walls/floors can both be engraved. The material the tile is composed of has no effect on the process of engraving, so a constructed wood/glass wall can be engraved in the same way as a natural stone wall. Once the area has been smoothed with - (not necessary for constructions), you may designate it to be engraved using -. The dwarf must have the Engraving work detail active to engrave and the Stone Cutting work detail active to smooth a rough cave tile.

Once a tile is designated, the theme or content of the engraving can be selected by first clicking on the designated tile and then clicking the "specify image" button. This must be done before the game is unpaused. If no selection is made, then the contents of the engraving are left to the choice of the engraver performing the job.

Engravings are directional – only a room containing the tile the engraver stood on when it completed will receive the engraving value bonus. There is no way to engrave more than one side of a single wall tile.

Using only highly-skilled engravers will result in high-quality engravings, and therefore higher room and fortress value.

## Toggling

Settings exist in the game for enabling and disabling the display of engravings, but this currently does not work, either by manually designating an engraving as hidden or by changing the in game/init setting. See previous version for how this used to work.

## Removal

Floor engravings of unsatisfactory quality and/or content (e.g. carvings of elephants mauling dwarves) can be removed by designating the carving of minecart racks over them. The tracks can then be removed by smoothing the stone, which results in fresh, smooth stone tiles ready for another attempt at engraving.

There are bugs with engravings on constructed floors that make it tricky to remove them – simply removing the constructed floor and building it back will result in the engraving reappearing, albeit without any description text.

To remove an engraving from constructed floor located on stone, first deconstruct the floor, then smooth the floor; this will cause the engraving to magically reappear, meaning it is now safe to put new constructed flooring over it. As an alternative to smoothing, you can also carve minecart tracks.

To remove an engraving from constructed floor located on soil, first deconstruct the floor, then build a wall, then cut arrow slits into the wall, then destroy the wall, and then rebuild your constructed floor.

Both methods will reset your floor to a fresh state, allowing you to start anew.

Floor engravings can also be removed from natural walls by allowing magma to flow over them, which reverts the tiles to their smooth form.

Wall engravings can only be removed by removing the wall – mining in the case of natural walls, or removing a constructed wall using -.

Removing engraved natural walls/floors will remove the engraving without triggering the negative thought. However, removing a masterwork engraving using any method except construction removal will cause a message and an unhappy thought in the artist who engraved it, as will mining a natural wall with a masterpiece on it.

## Effects on room value

How engravings affect room values has changed considerably, such that even the value of wall and floor tiles must first be understood.1 In a nutshell, however, in almost all cases it is now better to place walls/floors with high-value materials and then engrave those. It doesn't matter whether that placement is done using blocks, a rough boulder, or metal bars, as long as it is a Construction.

For floor tiles, their value calculation is \[floor origin multiplier\] × \[floor material value\] + \[engraving bonus\]

| Origin            | Multiplier |
|-------------------|------------|
| rough cave floor  | 1×         |
| smooth cave floor | 4×         |
| constructed floor | 7×         |

Floor Origin Multipliers

If the floor is engraved, the added engraving bonus is \[10\] × \[floor material value\] × \[quality value modifier\], with those modifiers being:

[TABLE]

The image depicted in the engraving also has a subjective value based on a dwarf's preferences, which is particularly important if a picky noble is going to own that room. If the dwarf likes whatever the picture is depicting, they might decide that an engraving normally worth 100☼ is worth, say, 150☼ to them (and consider the room to be more valuable than another dwarf would). If the dwarf dislikes what's in the image, though, they might decide that it's worth only 10☼ and subsequently complain that their room is substandard (if they happen to be a noble).

So, after all this taken into account, then for example, if you placed a single gold block floor in a room, that floor tile would increase the value of that room by (7) × (30) = 210☼. If that floor tile was then engraved with a Masterwork, it would be worth an additional (10) × (30) × (12) = 3600☼, for a grand total of 3810☼. Since the material value of the floor is used in both calculations, using high-value materials on floor tiles you plan to engrave can make the value of the rooms they're in skyrocket! However, if a floor tile exists in more than one designated room, a strict value penalty multiplier is applied to all overlapping rooms, possibly as high as -99%. Sharing a door that does not have two adjacent wall tiles (i.e. the rooms have double-doors rather than single doors) will also share the floor tile underneath the door. However, having only a single door between two walls will not cause an overlap penalty, which allows internal offices and bedrooms inside of houses to function. You can remove this penalty simply by un-designating any floor tiles that overlap in more than one room's designation. Not all room designations cause this penalty, however. You'll know the penalty has triggered when you see the room's name turn red and gain "Overlapping."

Wall engravings are yet another beast entirely. The initial calculation is similar, being \[Wall Origin × Material Value\], but their multipliers are different than floors, and their engraving bonus works differently.

| Origin            | Multiplier |
|-------------------|------------|
| natural cave wall | 1×         |
| smooth cave wall  | 5×         |
| constructed wall  | 9×         |

Wall Origin Multipliers

Walls also receive an added Engraving Bonus using the same formula as floor engravings (\[10\] × \[material value\] × \[quality value modifier\]), but how their material value is calculated and how their value affects rooms is far more complex. Wall engravings are directional, and they only provide their value to a room which contains the floor tile the engraver was standing on at the time of completion, and instead of simply using the engraved wall's material value, they instead look at a combined tally all of the tiles of the room they're in, both walls and floors, and use the value of the most common material in those tiles. For example, if you had 20 dacite wall tiles, 2 smooth Native Copper wall tiles, 20 dacite floor tiles, 20 platinum wall tiles, and 21 platinum floor tiles, it would use the material value of Platinum as the material value for all wall engravings done in that room, even the dacite and Native Copper walls. However, if you then removed two of the Platinum floor tiles, all engravings in that room would use the Material Value of Dacite instead.

However, unlike floor tiles, walls don't seem to mind being in multiple room designations, so there is no room value penalty if the same wall is in two or more designated rooms. Because of how walls interact this way with rooms and doors, however, and since rooms do not have to be contiguous designations, it is possible to increase the value of all bedrooms in your fortress by exploiting these rules.

## Room Value Exploit

According to Reddit user TBTerra:

1.  Make a line of wall with 1 tile gap either side (if your engravers are really good this might only need to be 2-3 long)
2.  Make the lines of floor either side of this wall out of the most valuable material you can (aluminum or platinum are great, steel and gold also work), and have your best engraver engrave them
3.  Place doors on top of all those engraved tiles, what sort doesn't really matter, as they will be adding 10-100 value to 2-3k value floor tiles
4.  For every room add the doors and the wall(this is a convenient rectangle). the wall makes the doors shareable, and the doors make the engraved floor shareable.

For optimal results hide this to the south east of your area, otherwise the zone icons can get rather confused

## Bugs

- While the quality rating of engravings on ice walls is shown properly, the quality of engravings on ice *floors* is not shown when looking at a tile with , only when hitting to inspect the engraving. This gives the false impression that engraved ice floors have no quality levels. In addition, the engravings are described as "engraved on the wall" instead of "on the floor".

- Engravings on constructed floors magically reappear when removing the floor and placing new floor, or when removing the floor and smoothing the natural floor beneath.
