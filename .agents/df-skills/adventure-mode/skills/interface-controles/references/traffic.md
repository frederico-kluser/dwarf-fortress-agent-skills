# Traffic

> Fonte: [Traffic](https://dwarffortresswiki.org/index.php/Traffic) — Dwarf Fortress Wiki (GFDL/MIT)

**Traffic designations** determine preferred paths for dwarves going around in your fortress. Normally, dwarves use the shortest route possible; using these designations, you can force them to take a different route. This way you can set up main hallways or rarely used side corridors. Only your dwarves will obey your traffic designations, and then only when they can. If a job requires that they go into a restricted zone, they will. Other creatures will not recognize your traffic designations, and even domestic animals or caravans will follow their own pathing.

Traffic designations can't solve all traffic problems. However, some issues can be prevented by good fortress design. For example, you might make hallways that are likely to be busy two or more tiles wide, and place stockpiles close to relevant workshops. Other difficulties may be reduced by designating traffic areas.

Vegetation (saplings) will tend to die if repeatedly trampled upon, leaving dead saplings or shrubs and quickly exposing bare soil. This may be desirable as trees block dwarves' and caravans' paths, but unchecked traffic may trample entire areas of forest regrowth.

## Setting Traffic Areas

The combination sets **traffic areas**, which are zones used to manipulate the movements of dwarves. Traffic areas can be designated as high, normal, low, or restricted. When walking from one point to another, dwarves consider these designations in finding the shortest path. Costs per tile for the pathfinding AI set for traffic levels are as follows: **high** costs 1 point, **normal** (default, undesignated) costs 2, **low** costs 5, and **restricted** costs 25. You can change the default PATH_COST values in d_init.txt, or per-fortress values with .

- It is often a good idea to set any water source in a biome with seasonal freezing to a Restricted area so your dwarves will be less likely to be caught on it when it melts.
- Some dwarves get disturbed if they walk through a butcher's shop and see an animal being slaughtered, so you may wish to designate the shop or a band around it as Restricted.
- Setting Restricted traffic areas over undisturbed webs or saplings is a good way to prevent dwarves from destroying them.
- If an area occasionally gets flooded, or is dangerous for some reason, routing dwarves around it could be lifesaving.
- Setting high traffic areas along roads outdoors prevents vegetation from being needlessly trampled.
- An important use of traffic designations is to restrict movement in the tile where a ballista's firing arrow originates. This will prevent tragic siege training accidents. Note that pets can and will be killed by firing ballista even if movement is Restricted.

Setting Restricted does not forbid a dwarf from traveling over those squares, but rather makes them willing to walk around them – for the normal cost table, 12.5 times further, or up to 25 times longer if there is an alternative high-traffic path. If you have an area that absolutely must not be stepped on by dwarves, consider walls, or if you still need access now and then, a locked door.

## Examples

This section will provide visual examples, to help further explain the mechanics of traffic. *Note: These examples may be changed in the future for better factual accuracy.*

In this scenario, where all the tiles are undesignated, normal traffic, the dwarf will obviously go straight to the goal/destination; since simply going straight is the shortest path, with the least cost.

Though the setup is similar here, the shortest path is now designated with low traffic. The dwarf instead goes around the obstacle to reach his destination, as going around through the normal traffic tiles is less costly than going straight in the low traffic tiles.

Another similar setup, but the shortest path is now designated with restricted traffic, and the two next shortest travel distances are marked with low traffic. The dwarf now goes the longest way around, as the high traffic tiles have the least cost of all other travel options. If the high traffic tiles weren't there, the dwarf would still go the long way around, using normal traffic tiles instead.

Another example where the dwarf goes the long way around. Despite having a shorter way to reach the goal *and* there being lowest-cost high traffic tiles in that area, the lower, much longer path is taken by the dwarf. Similar to the previous examples, the longer path accumulates less cost.

If a dwarf has an important job to do, he/she will ignore any traffic designations and take the shortest path to their destination. If the dwarf was doing a less important task, he/she would have taken the upper route instead.

## Limitations

Traffic designations only affect path preferences when pathfinding. Dwarves generally choose their jobs without weighing the pathfinding costs. For example, one cannot use traffic designations to direct a dwarf to confine his digging to a specific area. He will still take whatever path necessary to get to the job he has chosen to work. The best option to restrict a dwarf to a certain area is to make use of burrows.

Additionally, traffic designations cannot be used to restrict where a dwarf will stand when building/digging. In other words, traffic designations will not prevent a dwarf from placing himself on the outside of the fort when the last tile of a moat or wall is completed. One workaround is to build a statue on a tile to prevent dwarves from standing there.

## Using traffic areas to improve framerate

In cavernous rooms that handle large amounts of through traffic but have a small number of exits (a large central dining room, for example) designating a few high-traffic paths ("freeways") between the doors can help reduce the pathfinding cost for dwarves who are just passing through. There may also be benefits to adding low-traffic edges to these freeways to keep the search algorithm from looking for shortcuts. Likewise, any large dead-end room that branches off a major hallway should have the area around its doorway marked low or restricted traffic to prevent dwarves from searching it for shortcuts. As noted above in **Limitations**, this should not affect the dwarves who have a legitimate reason to hang out in the dining hall or visit the storage room - they will path to their destination regardless. Users may see up to a 10% increase in FPS by implementing these changes throughout their fortress.

## See also

:\* Path
