# Designations menu

> Fonte: [Designations menu](https://dwarffortresswiki.org/index.php/Designations_menu) — Dwarf Fortress Wiki (GFDL/MIT)

The **Designations menu** can be accessed by and provides the means to mark tiles with various designations including Mining, Wood Cutting, Plant Gathering, Stone Detailing as well as removing constructions, controlling traffic and other miscellaneous designations.

If is pressed when the view is centered on an outside/above ground tile, the designation defaults to Chop down trees - . If the view was centered inside/below ground, the designation defaults to Mine - .

To designate an area, select the desired designation from the menu, pick a tile and press to select one corner of a rectangle, then pick a second tile and press again to mark the other corner. This also works across z-levels, allowing 3-dimensional designations in the shape of a cuboid.

To cancel a designation, use Remove Designations ().

As of 0.40.20, all designations can be prioritized, with 1 being the highest priority and 7 being the lowest. Note that if two different designations have the same priority, one type may still be favored over the over. They also can be assigned as "Marker only", which is similar to the job being suspended.

Mouse controls: Left Click: paint, Right Click: move marker, Right click on screen border: Move screen. The main designations menu is mouse-enabled, but sub-menus are not.

## Designations Menu

- Mine () - Mark tiles to be mined out. Removing stone/soil walls and leaving stone/soil floors. May leave stone/ore/gems. (req. Mining labor)
- Channel () - Mark tiles to be channeled out. Removing the stone/soil wall on that tile, the floor, and replacing the stone/soil floor below with a ramp. May leave stone/ore/gem. (req. Mining labor)
- Remove Up Stairs/Ramps () - Mark tiles to remove natural ramps and dug ramps/stairs. (req. Mining labor)
- Upward Stairway () - Mark walls to be dug out and replaced with upward stairs (req. Mining labor)
- Downward Stairway () - Mark walls or floors to be dug out and replaced with downward stairs (req. Mining labor)
- Up/Down Stairway () - Mark walls to be dug out and replaced with upward/downward stairs (req. Mining labor)
- Upward Ramp () - Mark walls to be dug out and replaced with upward ramps (req. Mining labor)
- Chop Down Trees () - Mark Trees to be chopped down. (req. Wood cutting labor)
- Gather Plants () - Mark Shrubs to be gathered. (req. Plant gathering labor)
- Smooth Stone () - Mark stone walls to be smoothed. (req. Stone detailing labor)
- Engrave Stone () - Mark smoothed walls to be engraved. (req. Stone detailing labor)
- Carve Fortifications () - Mark smoothed walls to have fortifications carved. (req. Stone detailing labor)
- Carve Track () - Mark stone walls to be turned into track for minecarts. (req. Stone detailing labor)
- Toggle Engravings () - Mark tiles to display/hide engravings.
- Toggle Marker () Toggle existing designations between marker mode and standard mode (see below).
- Remove Designation () - Remove all designation markings.
- Remove Construction () - Mark constructions to be removed
- Bulk designation of items: ()
  -
    Reclaim Items/Buildings - Mark area of objects to be claimed.

  -
    Forbid Items/Buildings - Mark area of objects to be forbidden.

  -
    Melt Items - Mark area of objects to be melted.

  -
    Remove Melt - Remove melt marking from area.

  -
    Dump Items - Mark area of objects to be dumped.

  -
    Remove Dump - Remove dump marking from area.

  -
    Hide Items/Buildings - Mark area of objects to be hidden.

  -
    Unhide Items/Buildings - Remove hide marking from area.
- Set Traffic Areas () - Traffic area values determine where dwarves will travel. Large values for cost mean that dwarves will avoid that area if at all possible; smaller costs mean they will prefer that path even if it is longer than “normal”.
  -
    High Traffic Area - Mark areas with the “cost” listed in “High Traffic Cost”

  -
    Normal Traffic Area - Mark areas with the “cost” listed in “Normal Traffic Cost”

  -
    Low Traffic Area - Mark areas with the “cost” listed in “Low Traffic Cost”

  -
    Restricted Traffic Area - Mark areas with the “cost” listed in “Restricted Traffic Cost”

  -
    Move between type of areas to change with .

  -
    Change cost by -5/-1/1/5.

## Designations modification

Mining, stair carving, and ramp carving can also be modified to change their behavior. These modifiers can be switched with .

- Designate all: Standard behavior.
- Automining Ore/Gems: Once this tile has been processed, all neighboring tiles will be marked for mining, if they contain the same ore or gems. Can only be designated on revealed ores/gems. Will appear green.
- Designating Ores/Gems: What it says on the tin. Only works on revealed tiles.
- Designating Gems: See above.

## Priority

Designations can be assigned a priority using and . By default, all designations are made with a priority of 4, but higher priority jobs can be marked by using priorities 1-3, and lower priority ones with 5-7. Note that *reduces* priority; 1 is the highest priority, and 7 the lowest. When a dwarf has several jobs of different priority to do, the ones with higher priority are executed first, regardless of how convenient they are for the dwarf in question; a job marked '1' on the other side of the map will take precedence over a job marked '2' right next to them.

Notably, when in the designations menu, many designations such as mining will flash, repeatedly displaying their priority number. If this is not desired, it can be resolved by removing all designations of priority other than 4 (and if this fails, all designations), then saving and quitting. This will prevent the flashing or display of designation priority which some players may find annoying.

Care should be taken not to set important tasks on too low of a priority, as many other incoming and existing tasks will take precedent over those lowest priority tasks, meaning those tasks will never get done unless their priority is changed manually.

## Marker Mode

Designations can be placed in the default standard mode—the jobs are eligible to begin as soon as the game is unpaused—or in marker mode. Switch the mode of new designations with . Marker mode designations appear cyan instead of beige.

Dwarves will not actually undertake marker mode designations. This can be used to plan future projects, and it offers a few advantages:

- There is no need to designate the entire project at once. Doubtful portions can be deferred until nearby terrain is revealed, for example.
- Marker designations will not disrupt jobs already underway.
- The full range of priorities is available, as opposed to delaying the project by forcing low priorities. Thus the new project can take priority over existing designations when it's ready, without the need to remove the old designations.

When it is time for your dwarves to begin a marker-mode project, esignate a arker/standard toggle and choose an area that contains all the marker designations you wish, in all three dimensions. All marker-mode designations within will change to standard mode, and vice versa. This can be used to temporarily deactivate existing standard designations as well.
