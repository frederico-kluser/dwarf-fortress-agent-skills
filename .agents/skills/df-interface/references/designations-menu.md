# Designations menu

> Fonte: [Designations menu](https://dwarffortresswiki.org/index.php/Designations_menu) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

The **Designations menu** can be accessed along the bottom center of the screen, and provides the means to mark tiles with various designations including mining, wood cutting, plant gathering, stone detailing as well as removing constructions, controlling traffic and other miscellaneous designations.

To designate an area (b), select the desired designation from the menu, place your cursor over the first tile, click once, then drag your cursor over to another tile - which will create a rectangle, then click again. You can also choose to "paint" an area (B), which lets you specifically designate tiles one by one. Depending on the designation, this also works across z-levels, allowing 3-dimensional designations in the shape of a cuboid.

To cancel a designation, use Remove Designations (x).

All designations can be prioritized, with 1 being the highest priority and 7 being the lowest. Note that if two different designations have the same priority, one type may still be favored over the other (allthough such obeserved behavior could just be a result of different distances - in the maximum norm - to the tiles in question). They also can be assigned as "Blueprint only", which is similar to the job being suspended, as it marks tiles in a blue-colored square. This is useful for planning out designations and rooms without dwarves suddenly moving in to do anything yet.

Also note that for any and all designations (wood cutting, plant gathering, smoothing etc.) a dwarf currently doing such a job will when choosing the next job of that type always pick an accessible, designated tile (which has not been flagged as the current/next working tile of another dwarf) with the minimum distance (in the maximum norm) from the current position, regardless of how long the path to actually get there is. And when starting to do such a job the first tile is choosen by the same metric (minimum distance in the maximum norm). If more than one tile have the same distance then it is random which tile is picked first.

## Designations Menu

-

  Designations, both normal and marked (blue).

  Mine (mm) - Mark tiles to be mined out. Removing stone/soil walls and leaving stone/soil floors. May leave stone/ore/gems. (req. Mining labor)

- Channel (mu) - Mark tiles to be channeled out. Removing the stone/soil wall on that tile, the floor, and replacing the stone/soil floor below with a ramp. May leave stone/ore/gem. (req. Mining labor)

- Remove Up Stairs/Ramps (mx) - Mark tiles to remove natural ramps and dug ramps/stairs. (req. Mining labor)

- Create Stairway (mt) - Mark walls to be dug out and replaced with stairs going up or down. (req. Mining labor)

- Upward Ramp (mr) - Mark walls to be dug out and replaced with upward ramps (req. Mining labor)

- Chop Down Trees (l) - Mark trees to be chopped down. (req. Wood cutting labor)

- Gather Plants (g) - Mark shrubs to be gathered. (req. Plant gathering labor)

- Smooth Stone (vm) - Mark stone walls to be smoothed. (req. Stonecutting labor)
- Engrave Stone (vg) - Mark smoothed walls to be engraved. (req. Stone engraving labor)
- Carve Fortifications (vf) - Mark walls to have fortifications carved. (req. Stonecutting labor)
- Carve Track (vt) - Mark stone walls to be turned into track for minecarts. (req. Stonecutting labor)

- Toggle Blueprint Mode (M) Toggle existing designations between blueprint mode and standard mode (see below).
- Remove Designation (x) - Remove all designation markings.
- Remove Construction (mx) - Mark constructions to be removed
- Bulk designation of items: (i)
  - F: Reclaim Items/Buildings - Mark area of objects to be claimed.
  - f: Forbid Items/Buildings - Mark area of objects to be forbidden.
  - m: Melt Items - Mark area of objects to be melted.
  - M: Remove Melt - Remove melt marking from area.
  - p: Dump Items - Mark area of objects to be dumped.
  - P: Remove Dump - Remove dump marking from area.
  - H: Unhide Items/Buildings - Remove hide marking from area.
  - h: Hide Items/Buildings - Mark area of objects to be hidden.
- Set Traffic Areas (T) - Traffic area values determine where dwarves will travel. Large values for cost mean that dwarves will avoid that area if at all possible; smaller costs mean they will prefer that path even if it is longer than “normal”.
  - h: High Traffic Area - Mark areas with the “cost” listed in “High Traffic Cost”
  - x: Normal Traffic Area - Mark areas with the “cost” listed in “Normal Traffic Cost”
  - l: Low Traffic Area - Mark areas with the “cost” listed in “Low Traffic Cost”
  - r: Restricted Traffic Area - Mark areas with the “cost” listed in “Restricted Traffic Cost”

## Designations modification

Mining mn can also be modified to change behavior:

- v: Designate all - Standard behavior.
- V: Automining Ore/Gems - Once this tile has been processed, all neighboring tiles will be marked for mining, if they contain the same ore or gems. Can only be designated on revealed ores/gems. Will appear green.
- o: Designating Ores/Gems - What it says on the tin. Only works on revealed tiles.
- g: Designating Gems - See above.

## Priority

Designations can be assigned a priority by clicking -. By default, all designations are made with a priority of , but higher priority jobs can be marked by using priorities -, and lower priority ones with -. Note that  is the *highest* priority, and  the *lowest*.

When a dwarf has several jobs of different priority to do, the ones with higher priority are executed first, regardless of how convenient they are for the dwarf in question; a job marked  on the other side of the map will take precedence over a job marked  right next to them.

Care should be taken not to set important tasks on too low of a priority, as many other incoming and existing tasks will take precedent over those lowest priority tasks, meaning those tasks will never get done unless their priority is changed manually.

## Blueprint mode

Designations can be placed in the default standard mode—the jobs are eligible to begin as soon as the game is unpaused—or in blueprint mode. Switch the mode of new designations with M. Blueprint mode designations appear cyan instead of beige.

Dwarves will not actually undertake blueprint mode designations. This can be used to plan future projects, and it offers a few advantages:

- There is no need to designate the entire project at once. Doubtful portions can be deferred until nearby terrain is revealed, for example.
- Blueprint designations will not disrupt jobs already underway.
- The full range of priorities is available, as opposed to delaying the project by forcing low priorities. Thus the new project can take priority over existing designations when it's ready, without the need to remove the old designations.

When it is time for your dwarves to begin a blueprint-mode project, designate a k standard toggle and choose an area that contains all the blueprint designations you wish, in all three dimensions. All blueprint-mode designations within will change to standard mode, and vice versa. The opposite (L) can be used to temporarily deactivate existing standard designations as well.

## Notes

- With DFHack installed, there is also be a setting available in the mining menu Ctrl+d that allows to configure whether your miners will ignore warm or damp stone.
