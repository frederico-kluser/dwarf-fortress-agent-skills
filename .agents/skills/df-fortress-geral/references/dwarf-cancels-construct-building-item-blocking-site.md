# Dwarf cancels Construct Building: Item blocking site

> Fonte: [Dwarf cancels Construct Building: Item blocking site](https://dwarffortresswiki.org/index.php/Dwarf_cancels_Construct_Building:_Item_blocking_site) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

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

This occurs when a dwarf is trying to clear the tile(s) of a building site, and there is an item which the dwarf is not allowed to pick up, lying on the ground where you want to place the building.

For instance...

- ... the item is forbidden.
- ... the item is marked for dumping.
- ... the item is tasked to be used in a different building.
- ... the item is tasked to be hauled to a stockpile.
- ... the item is tasked to be hauled to the trade depot.
- ... the item is tasked to be used in a workshop.

This can happen often when you have a field of mined stones and you have designated multiple buildings to be built using those stones in that area. If two buildings require stones located at each other's building sites (e.g. "Workshop A"'s stone is in the way of "Wall B", and vice versa), both buildings will be suspended upon the arrival of a builder, since the other's stone can't be moved.

More broadly, this can happen if an item blocking a building site is reserved for another job - for instance, a stone queued to be hauled to a stockpile or a dump will not be touched by a dwarf attempting to build a building on top of that stone. This can happen when several masons are actively using stones in the same area, when an excess of stones are queued to be hauled to a stockpile, or if stones are marked for dumping, among other things.

If an item is reserved for another job, it will probably *(read "hopefully")* be taken away very quickly as that job is handled; you can often just un-suspend the construction and it will complete with no further error. Forbidden items, however, will have to be manually unforbidden in order to make construction possible.

In extreme cases, try the following steps:

1.  pause the game, via spacebar.
2.  forbid any and all items that might possibly be blocking the building. (This can be done via k, then f, *or*, for larger areas, via d, b, f and then either using Enter to designate a large area or left-clicking with the mouse.) This will cancel any tasks associated with all items.
3.  unforbid them again.
4.  remove the workshop/building job, via q, x.
5.  re-designate the same workshop/building job - or a few less than you had before, if several might be overlapping. This is to prioritize that building for your (now idle?) construction dwarves.
6.  and, if it's not obvious, then unpause the game, via spacebar.

In very rare cases, the worst culprit is a piece of clothing that a dwarf has discarded while changing into armour. That personal item may be permanently tasked for retrieval, yet due to a known game glitch the dwarf will never retrieve it. In such cases, alternating the dwarf in question between armour levels, from "clothing" to "leather" to "plate" and back, *repeatedly*, may (eventually) shake them out of it and they'll grab their sock, or whatever has brought construction to a magma-gargling halt. For particularly stubborn cases, DFHack provides several commands that can clear things up: "cleanowned scattered" will confiscate owned items that were abandoned by your dwarves (allowing them to be stockpiled or dumped), and "autodump destroy-here" simply eliminates items under the cursor.

\
