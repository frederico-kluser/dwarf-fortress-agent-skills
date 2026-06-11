# Bridge

> Fonte: [Bridge](https://dwarffortresswiki.org/index.php/Bridge) — Dwarf Fortress Wiki (GFDL/MIT)

**Bridges** are buildings which provide a temporarily walkable floor that can either be removed ("retracting" bridges) or turned into a wall ("raising" bridges) via linked mechanisms. Bridges are useful for crossing empty space and dangerous terrain, serve a vital role in fortress defense, and have a host of ancillary uses. For example, using a single large bridge to control fluids can save a ton of mechanisms and time when replacing the likes of floodgates, especially when the fluid in question requires a wide opening.

## Building bridges

When first built, any bridge is just a static walkway, often (but not necessarily) over open space. They can be used as is, and use less materials than a constructed floor of the same size serving the same purpose. if you want them to raise or lower, they must be linked to a trigger (see below).

Bridges can be built ( -\> -\> ) of metal, stone or wood. They are designed and built by a specialist worker in the material used\* (e.g. a mason for a stone bridge, etc.). The size of the bridge can be altered using the mouse to expand from the initially selected point while placing it, up to a maximum size of 31 squares in each direction (31x31)\*\*.

(\* See note re "core material" under Materials, below)\

(\*\* You can place additional bridges side by side to make them infinitely wider. You can also place a second bridge on the *other* side of a wide gap to span as much as 60 tiles. Any more requires some solid anchor to provide another 30 tile maximum (in both directions).)

Raising bridges must be anchored to a solid surface on the "raising" edge. Before placing a raising bridge, ensure that the bridge raises from the direction you want it by selecting the appropriate icon. The direction points to the side of the bridge which will become a wall when the bridge is raised.

Since a retracting bridge completely disappears, direction doesn't matter. Retracting bridges are the default, but if you selected "raising" by mistake, there is a separate option shown to the right for a retracting bridge.

##### Placement requirements

The error message 'Needs walkable perimeter' suggests that access is required all the way around the perimeter of the bridge, however, only one accessible adjacent tile is required. Placement of the bridge also requires that all of the tiles it occupies not have more than 1/7 water on them at the time of construction.

### Materials

Bridges require stone, logs, and/or blocks - they can be mixed - with blocks being placed significantly faster during the actual construction. The formula for the number of building materials needed is: number of tiles in the bridge divided by four, rounded down, plus one, or {size/4, rounded down}+1.

So, for example, a 3-tile bridge takes {3 tiles/4=3/4 -\> 0} +1 = 1 building material. A 4-tile bridge takes {4/4=1} +1 = 2. A 5x10 bridge would require {50/4=12 1/2 -\> 12} +1 = 13, and so on.

The "core" material of the bridge is the *oldest* individual building material used (i.e. the first item that was created in the fortress or that entered the map). The core material determines the color, style, and description of the bridge, as well as the labor required for construction.

Care should be taken when choosing materials for bridges that will be exposed to fire or magma: Bridges built with non-magma-safe materials will heat up and eventually melt if the center tile (with bias towards the northwest if the center doesn't fall on a single tile) gets covered in magma or exposed to fire, whether the bridge is raised, lowered, or even retracted. The ability of a bridge to withstand heat is limited by the *least* fire-resistant item involved - a single non-magmaproof building block or mechanism will cause the whole bridge to deconstruct when exposed to sufficient heat. Dragonfire almost immediately melts nearly all bridges (slade being the prime exception).

## Raising and retracting bridges

When designating a bridge to be built, you can choose to make it "retracting" (the default) or "raising". A retracting bridge disappears when it is "up" and become invisible, and a raising bridge is a "drawbridge", forming a visible wall when it's up. The "wall" is always just 1 z-level high x 1 tile thick (and as wide as the bridge is wide), no matter how long the "drawbridge" is when it's down. For raising bridges, you select which direction you want it to raise when you designate it to be built. This cannot be changed later, which would require deconstructing and rebuilding a new bridge.

All bridges can be either raised or retracted by linking it to a trigger with mechanisms - this requires a dwarf with the mechanics labor activated. Once the trigger (either a lever or pressure plate) is in place, use uery on that trigger and select "link to ridge". You will then get a pop-up map where you can cycle through all bridges that you have currently built in your fortress. Select one, and then select the 2 specific mechanisms you want to use to link the bridge. Quality of mechanism has no effect on the raising/lowering of the bridge, nor the time to install the mechanisms.

Any bridge, retracting or raising, of any size, will respond to the trigger signal 100 ticks after the signal is sent. You can link more than one bridge to the same trigger and they will all respond simultaneously.

If a bridge is set to retract when trigger is activated, the bridge essentially disappears, *tossing* anything (friend, foe, or object) on the bridge onto whatever is underneath. Clearly this can be used to drop your enemies to rocky/watery/fiery deaths (or anything more imaginative you can think up!). Note that the creatures and objects are "tossed" with a semi-random initial velocity; this can reduce the lethality of pit traps (creatures bouncing off the walls lose the precious momentum that would otherwise result in an unsurvivable splat at the bottom), interfere with the reproducibility of dwarven !!SCIENCE!!, and be exploited as the key mechanic in coinstar training.

If a bridge is set to raise when a lever is pulled, the bridge will become a wall along the edge selected with the keys when placing the bridge. When activated, the bridge "raises" very quickly, flinging anything on the bridge into the air, with unpleasant if not always deadly side effects. The resulting wall is always one z-level tall, watertight, and invulnerable to building destroyers. Raising "drawbridges" can be used to block fortress entrances and corridors. When lowered, bridges will destroy most anything on the underlying tiles. By "destroying", we mean dwarves, foes, and items will entirely disappear from the game, a rare event which led to the creation of the term dwarven atom smasher.

Any water displaced by a raising bridge is destroyed regardless of how much open space is on each side or above. Water resting atop a retracting bridge falls straight down after the bridge retracts.

#### And levers

Note that, depending on the design, retracting and raising bridges can provide the opposite reaction from an "open" signal. When the "open" signal is sent, both bridges "disappear" from view - the retracting bridge disappears completely, and the raising bridge becomes a 1-tile high, 1-tile thick wall. But this means that the raising bridge closes the passage on the same level with that wall that it creates on the "open" signal. This can be used to create either an "open" passage or "closed" passage on the "open" signal, depending on the design.

Of course, this is true for bridges and pressure plates as well.

## Notes

Bridges will not operate if any one creature of size 1,200,000 or larger is on them. This weight limit is not cumulative - a bridge will still retract if a hundred goblins are standing on it, but a single rutherer accompanying those goblins will prevent the bridge from operating. Attempting to lower a drawbridge onto such a creature (in order to atom-smash it) will cause the bridge itself to deconstruct. Attempting to "unretract" a bridge while such a creature is in any of the bridge tiles will similarly cause the bridge to deconstruct. The size limit does not apply to creatures inside cages.

It is impossible to channel out stone that is directly under a bridge, raised or not. Likewise digging a ramp under a bridge will not remove the floor tile. To remove these floor tiles, the bridge must be deconstructed. Note that obsidian casting can *create* new floor tiles under a bridge, which then behave in the manner above.

Big bridges can take weeks or even months to complete. You can shorten construction time by moving the materials to the site before starting construction, and by using blocks instead of stones. The material-gathering time is somewhat shorter for blocks due to their lesser weight, and the actual construction is three times faster for blocks.

**Warning:** while bridges do not provide structural support, the game will still allow you to place constructions adjacent to them. Any construction that is completed when attached only to a bridge will cause an immediate cave-in, often tossing the unlucky mason off the edge, to a horrible death any bystanders' great entertainment. However, a construction that connects to an existing supported construction when completed will not cause a cave-in, even if it is also adjacent to a bridge. To build constructions next to a bridge safely, ensure that *all* unbuilt constructions adjacent to a bridge are also adjacent to a construction that has already been completed. When building large constructions, it may be useful to suspend all tiles adjacent to a bridge until the neighboring constructions have been completed.\
**Example:**

|  |  |
|----|----|
| Will cause a cave-in | Will **not** cause a cave-in |
| \ ╔═╗\[#3:0\]▓\[#\] ║+║\[#0:0\]\[@6:0\]O\[#@\] ╚═╝\[#3:0\]▓\[#\] \[#2:1\].,'\[#3:0\]▓\[#\] \ | \ ╔═╗\[#3:0\]▓\[#\] ║+║\[#0:0\]\[@6:0\]O\[#@\] ╚═╝║ \[#2:1\]\`,.\[#\]O \ |

Deconstructing bridges can be hazardous, as dwarves are not as compunctuous as with constructions and diggings to make sure no one is standing on them before destroying them.

A raised bridge cannot be linked to a lever from the inside - the mechanic must be able to access the center tile of the bridge when lowered.

If you aren't sure whether or not a 1 tile thick bridge is raised or lowered, try to build a piece of furniture, like a statue, on it. If it says blocked, the bridge is raised, if it says building present, it is lowered. You can also link another (longer) drawbridge to the same lever, to use as a visual indicator of the other bridge's status. Since this takes additional time and mechanisms, this is best reserved for when it's especially important that you know at a glance whether that bridge is blocking things.

## Uses

Perhaps the most straightforward use of a bridge is spanning empty space or dangerous terrain. Bridges only need roughly 25% of the material that building floors would require, and can be completed relatively quickly as well. Bridges are limited to a span of 20 tiles across open space; greater distances will require columns or other means of support. ("Floating" retracting bridges can be built into spans longer than 20 tiles, but they will deconstruct when support is checked.)

### Remote controlled gateways

Lever-controlled bridges are one of the safer ways to control access. They are immune to building destroyers, though care must be taken to avoid operating them in the presence of exceptionally large creatures. Magma safe material should be used in the construction if there is any chance magma might flow over the bridge.

Retracting bridges built covering the top of a ramp or stairway can never be destroyed from beneath.

### Floodgates

Raising bridges make a good replacement for most floodgate uses (e.g. flow and access control). They have the advantage of not being as easily jammed: they fling or atom smash all items and all but the largest enemies on their tile/s when they open or close, whereas a floodgate or door will jam open with a discarded sock in it. Further, bridges cannot be destroyed by building destroyers, while floodgates can be. A single bridge can also be made up to ten tiles wide, potentially replacing ten floodgates and saving many mechanisims and much work. One minor downside of bridges compared to floodgates is, in classic mode, that bridges with a width of 1 look the same when raised as when lowered, so it is easy to confuse whether they are closed or not. This is not the case for the Steam version. If you are unsure of a bridge's status, check the control lever if there is one (in most tilesets, lever to the right means closed), or try to build furniture on top of the bridge and check the resulting warning message ("blocked" means the bridge is raised, "building present" means it's lowered).

### Waste disposal

Lowering raised bridges can be used as waste disposal for unwanted stones, refuse, goblins (dead or alive), legendary cheese makers and nobles, to name a few. Even fluids get destroyed. Note, however, that lowering a drawbridge onto a sufficiently large creature (such as a forgotten beast) simply causes the bridge to deconstruct.

### Traps

Using two bridges at opposite ends of a corridor creates a very large and simple trap by walling in enemies. Or... Smashing them to tiny bits if placed to raise facing each other, with no space in between. For added effect, place pressure plates on both ends to raise the bridge when stepped on, to fling the units. If there is a floor directly above, they will be stunned. If there is a floor beneath the bridge, and if nobody is on the pressure plate, they will likely be smashed when the bridges come back down. If there is nothing above, they will land rather far away. Bonus points for making them land in a particularly nasty spot. If there is no floor beneath the bridge, they will fall, sometimes into something very, very bad.

### Minecart routing

Lowered/extended bridges "cover" Minecart track corners constructed or carved underneath, allowing carts to travel in a straight line instead. This can let you change minecart routes via pulling levers.

### Cave-ins

Since bridges don't support adjoining rock, it is possible to set up a cave-in so that dust can't come up, dwarves can't fall down, and flying creatures can't come up from beneath the cave-in before you set it off. Bridges are also instrumental in magma piston applications.

### Improvised ceilings

Building an outdoor structure, such as an Archery tower, requires considerable expense and time. The reduced material requirements make bridges a viable alternative to roofing it up tile by tile. While it'll still be immune to Building destroyers, a proper constructed ceiling is superior if you expect it to be exposed to extreme temperatures.

### Improvised walls

Walls cannot be built along map edges above ground, but raising bridges can. Because these bridges can be raised to act as walls, they can be used to control where wildlife, enemies, and caravans spawn on the map edges.

A similar technique can be used to prevent fliers from spawning above ground, but it requires bridges to be built at *every* z-level. This requires considerable effort, as each bridge needs to be accessible to the dwarves building it, as well as needing support for each bridge. It can also be somewhat risky if a dangerous creature suddenly spawns near a dwarf working on the bridge (especially in evil biomes). Note that this technique, when completed, will also prevent fliers from leaving the map.

### Ocean drains

Designate ramps on the 2nd level below an ocean. Build a retracting bridge directly above the ramps (immediately under the ocean) leaving the ramps in place, and link it to a trigger. In order to build the bridge (and link it) you will need access to the level of the bridge. Now seal that access off (the constructed wall in the below diagram) so the chamber above the bridge is water tight. Now with the bridge in place, designate ramps up to the ocean adjacent to the bridge. Diggers with access to the level *below* the bridge can dig those ramps up from the level of the bridge, allowing the ocean to fill the chamber; even with the ramp squares underwater they can still dig them out. And not a drop of water will touch them... provided they clear out before you pull the lever.

Shown below is a 2x1 bridge (any size bridge can be used) before and after designating the ramps adjacent to the bridge. The stairs and passage on Z2 satisfy the 'Needs walkable perimeter' requirement and provide access to the top of the bridge for linking to a trigger. The passage is then blocked with a wall to make it water tight.

`        Before breaking through      After`\
`        side X       side Y          side X       side Y  `\
`  Z3    ≥≥≥≥≥≥≥      ≥≥≥≥≥≥≥≥≥≥      ≥≥>≥>≥≥      ≥≥≥≥≥≥≥≥≥≥`\
`  Z2    ###B###      ##Z_X_BB##      ##^B^##      ##Z_X_BB##`\
`  Z1    ###^###        Z   ^^##      ###^###        Z   ^^##`\
`  Z0    #######      ##########      #######      ##########`\
`  `\
`  ≥ = Water with floor     > = Water without floor  Z = Stairs`\
`  ^ = Ramp      # = Solid Rock    X = Constructed Wall  _ = Floor (not constructed)`

### Caravan exits

A bridge to nowhere, built well above ground level at the edge of the map, can sometimes serve as a handy exit for caravans and diplomats when your fortress is under siege.

### Stops on the elevator

Designate a dumpsite or set up a floodgate at the top of a shaft; use multiple remote-controlled bridges to decide on which level the stuff, water, magma etc. gets off. (bonus: use water falling at one end of the bridge to flush stuff off that was dropped onto the other end without the manual labor)

### Single lever airlock

Raising bridges and retracting bridges controlled by a single lever will be in opposite states of being open or closed. When one is closed (raised) the other is open (retracted) and vice versa. This fact can be used to construct airlocks that are not vulnerable to building destroyers or mistimed lever pulls e.g.

`  Side View:`\
`  Z1    XXXXXXR____      D = Raising drawbridge   / = Ramp   _ = Floor`\
`  Z0    D_____/XXXX      R = Retracting bridge    X = Solid Rock or Constructed Wall`

With a suitably long distance between the two bridges, the controlling lever can be placed within the airlock, and by setting the profile of the lever specific dwarves can be moved between isolated areas.

### Decorations

Bridges benefit from the skill of the builder, and that multiplier is also applied to any attached mechanisms. High-quality bridges can inspire happy thoughts in your dwarves and help meet room value needs. Bridges may also be used to form mosaics or even animations.

### Coinstar training

The mechanical "tossing" action of retracting bridges can be used for training armor user and associated traits by repeatedly flinging small items at the trainee. See Danger room for more information. Alternatively, this design can be used as a trap: invaders atop a retracting bridge inside locked room will get thrown around and optionally pummelled with "ammunition" like stones or weapons placed in the room.

## Bugs

- Metal bridges can be constructed by dwarves with any of the "metalsmith" skills enabled, however the builder's blacksmith skill is used to determine quality
- Trees grow through bridges, may make the bridges unusable
- Retracting bridges can be built without support, but will deconstruct when support is checked
