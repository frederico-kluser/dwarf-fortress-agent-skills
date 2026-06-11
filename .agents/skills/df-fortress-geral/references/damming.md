# Damming

> Fonte: [Damming](https://dwarffortresswiki.org/index.php/Damming) — Dwarf Fortress Wiki (GFDL/MIT)

You can dam off a (4 tile) river with just the starting 7 dwarves using the following steps:

1\) Find out which way is upstream: loo(k) at the edge tiles, the downstream edge will sometimes be 5/7 or 6/7 when the water "falls off the edge" before being replaced. The upstream edge is always 7/7

2\) Build a 2-wide floor 5 tiles away from the upstream edge (so 5 empty squares between edge and floor). If the river isn't straight, channel some tiles to create a straight edge.

3\) Build raising bridges to wall off the upstream section. I used two walls on the corners but you can also make the bridges one longer:

4\) Build pumps on the floor "bridge" that pump from downstream, e.g. south in my case, and raise the bridges with a lever. You've now created a box around the upstream section lined by bridges on the sides, the map edge and the inaccessible pump squares:

5\) Set all pumps to pump manually. The dwarves will start pumping the downstream water back into the walled off upstream section, where dwarven physics allows the overflow to drain off the northern edge.

6\) Build a wall to dam off the river: Keep an eye on the water in the downstream section just away from the pumps. It should go down pretty quickly. Once it reaches 1/7 with some regularity designate walls a couple tiles away from the section that's being pumped (you don't want to build the walls directly under the pump as then with every completed wall section one pump becomes nonoperational)..

This is somewhat annoying as the water level will fluctuate, and every time it is 2/7 the job is suspended. So just (q)uery the building every couple seconds and unsuspend when needed. Every time a dwarf arrives when there is 1/7 it will do a bit of construction, going from "waiting" to "initiated" etc, and at some point the wall is done:

7\) You can have the dwarves stop pumping now. This can be a bit tricky as dwarves are stupid near water, so it might be best to designate the river banks and bed as restricted to discourage pathing through the dry bed which will soon not be dry anymore. Or just hope that they learn to swim in time :). But getting a corpse upstream of the wall would be annoying, so maybe best do the designation.

If you wanted to dam the river permanently, you're done now. However, I usually want to build a raising bridge in the bank instead so I can do stuff downstream and later allow the river to start flowing again.

8\) Wait for the downstream river section to dry up. This will probably take a couple months. Then, build a raising bridge in the dry bed:

9\) Link the bridge to a lever and pull. Restart pumping so the section N of the wall is drained again, and remove the wall when it is dry (should be quick now since there are only a couple tiles to drain:

10\) Now you can deconstruct the pumps, bridges etc, and you're done. You have the river back in (more or less) original state, but you can dam off the river at any moment by pulling the lever that raises the constructed bridge:

For larger rivers, the principle is the same, just add more pumps/dwarves.

Note: I guess it should be possible to create a bridge immediately, but at least in my experience a bridge is much harder to construct in water than walls, since the walls are built one tile at a time, while the bridge (I think) requires all tiles to be 1/7 to prevent suspension. So, it's easier to build a temporary wall first, and then a permanent structure just downstream of it.

Also note that this can be done with the starting 7 (5 pumpers and 2 builders), but keep an eye on the pump operators becoming tired, since if they stop pumping you don't want any builders in the river bed. Once I noticed one of the builders going off to bed, I suspended the builds, stopped the pumps, and restarted when everyone was awake again.

Finally, it would be somewhat easier to use water wheels (at least for the dwarves), but this requires a bit of extra effort as downstream will get drained (stopping the pumps), while upstream will get flooded. So, you probably need to create an extra channel (with a diagonal connection to prevent overflow) from upstream to build a water wheel --- which is annoying since you have to drain it somewhere to get "flow". Thus, it might be easier to juist build some wind mills.
