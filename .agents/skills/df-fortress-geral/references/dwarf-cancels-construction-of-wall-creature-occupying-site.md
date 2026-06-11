# Dwarf cancels construction of Wall: Creature occupying site

> Fonte: [Dwarf cancels construction of Wall: Creature occupying site](https://dwarffortresswiki.org/index.php/Dwarf_cancels_construction_of_Wall:_Creature_occupying_site) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Error Messages FAQ**
- **Dwarf cancels task: Hunting vermin for food**
- **Dwarf cancels Store Item: Job item misplaced**
- **Dwarf cancels Store Item: Item inaccessible**
- **Dwarf cancels Construct Building: Item blocking site**
- **Dwarf cancels task: Dropoff inaccessible**
- **Dwarf cancels task: Dangerous terrain**
- **Dwarf cancels task: Could not find path**
- **Dwarf cancels task: Forbidden area**
- **Dwarf cancels task: Job item lost or destroyed**
- **Dwarf cancels Pickup Equipment: Equipment mismatch**
- **Dwarf cancels task: Interrupted**
- **Dwarf cancels task: Handling dangerous creature**
- **Diplomacy Stymied - A diplomat has left unhappy**
- **Dwarf cancels construct "Rock object": Needs non-economic rock**
- **Cat cancels Store Item in Stockpile: Too injured**
- **Digging designation canceled: Warm / Damp stone located**
- **Miner cancels dig: Inappropriate dig square**
- **Dwarf cancels fill pond: Inappropriate building**
- **Their wagons have bypassed your inaccessible site**
- **Dwarf cancels Construct Building: cannot reach site**
- **Dwarf cancels construct "Rock short sword": Needs sharpenable rock**
- **Dwarf cancels construction of Wall: Creature occupying site**
- **Needs butcherable unrotten nearby item.**
- **Add a question to this FAQ**
- **Back to the Main FAQ**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

Dwarf cancels construction of Wall: Creature occupying site

This error occurs all-too-often when a dwarf is trying to build a wall, and chooses to stand in the tile of the wall-to-be-built.Bug:5991 This appears to be fallout from the change to prevent dwarves from walling themselves out of the fortress.

To resolve this problem, try the following (roughly in order of ease):

- Cancel the construction, then reissue the job.
- Designate "restricted" traffic areas to force the dwarf to approach the build site from a more favorable direction.
- If the wall is being placed on soil or another natural floor, channel the building site to prevent the dwarf from standing there (walls can be built on open space, as long as there is an adjacent floor tile). Note that this will **not** work if the only access to the building site is diagonal.
- Create an alternate path to the build site (dig a tunnel, remove a wall, or build a floor).

\
To avoid this problem, attempt to follow best practices:

- Don't submit building jobs on a tile where a dwarf is standing.
- For constructions in tight quarters, submit any "problematic" tiles first, wait for them to be built, then submit the rest.
- For large constructions in the open, submit all the jobs at a single time by using u or k.
- Don't issue build orders that will intentionally strand the builder--rather than wall themselves out, they will cause this error (which is still better than silently starving to death).
- If you expect problems, preemptively designate restricted traffic areas or channel the build site.

Another way of bypassing this is to build a floor on the tile then remove it and immediately build the wall in its place, the dwarf will be standing to the side of the wall from building the floor.

\

## Explanation

To successfully build a wall, the builder's path to the construction site must pass through an adjacent tile from which construction is allowed. There are several reasons why this might not occur, leading the builder to stand on the building site:

If the builder is already standing on the construction site then no pathing is performed; the builder will simply "choose" the construction site. Canceling and resubmitting the work order when the builder is not standing on the construction site will resolve this problem.

If the builder's chosen path is later rendered impassable (say, by another construction being built), the builder will choose to stand on the construction site instead of selecting another valid adjacent tile. In this case, canceling and reissuing the build order will cause the builder to re-path, solving the problem.

If the shortest path to the build site only crosses unsuitable tiles (most often because of ramps) then the builder will choose to stand on the construction site. In this case reissuing the build order is insufficient; the builder must be encouraged to approach the build site from a different direction (using traffic designations, constructions, locked doors, etc.).

In all cases rendering the building site impassable (by channeling) will force the builder to path through and stand on an acceptable adjacent tile; if no such path exists the build order cannot be submitted.

\
