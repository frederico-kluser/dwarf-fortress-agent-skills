# Machine component

> Fonte: [Machine component](https://dwarffortresswiki.org/index.php/Machine_component) — Dwarf Fortress Wiki (GFDL/MIT)

**Machines** are an advanced concept in *Dwarf Fortress*, but although they can be infinitely complex, no fundamental part is very complicated. There are several different types of **machine components**, all available from the achine Components screen in the uild menu. These components can be used to create custom-designed **machinery** of more or less complexity, depending on the situation and the player's design.

In the order listed in the machine components sub-menu, these are:

:\* Screw pump

:\* Water wheel

:\* Windmill

:\* Gear assembly

:\* Horizontal and Vertical axle

:\* Rollers

Another important component to most machines are levers, but they are not, technically, "machine components", nor are they needed for many "always on" machine designs. (But a way to turn a machine off quickly, "just in case", is often a good plan.)

In order for the machines to operate, you must have a power source (wind, water, or dwarf) of some kind. Power can be transferred to machine parts which require it by a system of axles and gear assemblies.

Machines are mostly used for pumping water or magma, or running rail systems. Some complex trap designs incorporate machine components. You do *not* need machinery of this complexity to operate retractable bridges, drawbridges, linked doors, hatches or floodgates, or simple one-tile traps, nor to manually operate pumps.

## Nuts and bolts - the basics

### Power generators

Windmills and water wheels are the machine components that provide limited power. Power generators can be chained together using axles or gear assemblies to combine their power along the same power conduit. Additionally, water wheels can be combined by placing them adjacent to one another in parallel, thereby requiring no extra materials to perform the linkage.

### Uses for power

Currently, the screw pump and the roller are the only machine components that consume power to achieve a purpose. A millstone also requires power to operate, although it is classified as a workshop rather than a machine component.

Screw pumps can also be operated using dwarf labor in place of mechanical power. The millstone likewise has an unpowered alternative, the quern.

### Power conduits

A gear assembly is used to link multiple machine components together. Additionally, a gear assembly can be linked to levers and pressure plates, which can then be used to disengage the gearbox from any linked items. For example, screw pumps can be switched on and off in this way.

Axles are used to transport power over a distance. A horizontal axle ( ) transports power within a z-level, while a vertical axle ( ) transports power across z-levels.

## Construction

Machine components have two basic states in which they can be built: "stable foundation" or "hanging". This state is visible when looking at the constructed machine with .

A machine with a "stable foundation" is just what it sounds like; the machine component has been built on solid ground, and so it has a solid base on which to rest. A "hanging" component is not built on solid ground, but instead has been built beside or on top of an existing machine or component. Its only support comes from the adjacent component. This can be daisy-chained, so that it is possible to build machines which have only one component on solid ground, with the rest hanging out into empty space.

Possible advantages to this include protection from destruction by invading enemies (if they can't get to the machine components, they can't destroy them). However, it can be risky, as the rest of the parts will collapse if the component(s) on solid ground are destroyed.

Levers can be hooked up to a gear assembly in a power conduit (aka "power train"), causing any power transferred through that to "disconnect" when the lever is pulled. If a gear is disconnected in this way, and is serving as the support for hanging machine components, those hanging components will automatically deconstruct into their basic components, as they will no longer have support. As with any deconstructed building, they can be rebuilt.

## Machinery overview

*This is an overview of how the different machine parts work and work together, with some basics about each of them. They all have more details - once you understand the basics, refer to the **main articles** for more complete discussions - these links will be listed in **bold**.*

**Machinery** in Dwarf Fortress consists of more than just machine components. It's the systems of triggers (either levers or pressure plates) that control the windmills and water wheels that provide power to the gear assemblies and axles that transfer that power, and the pumps and millstones that use that power; and let's toss in bridges, because they move and will come into the discussion sooner or later. No one part is very complicated, but combined they can be as complex as one can conceive. You can't do everything with DF machinery, but with creativity you can come close.

### Your friend, the mechanism

The basic part is the mechanism, the same thing that lets you build stonefall traps - that can also become a lever, a pressure plate, or a gear assembly - as well as all the other various simple one-tile traps. Mechanisms are created using the mechanic labor out of stone in a mechanic's workshop, or weapons-grade metal in a forge. The mechanism "quality" makes no observed difference when creating DF machinery, so any mechanism will work as well as others\*, including the very rare, but possible, artifact mechanism.

*(\* Except in magma, which requires magma safe mechanisms - a separate discussion, but that's pretty much the sum of it.)*

Main Articles: **Mechanism**, Trap

### Triggers

The simplest machine use of a mechanism is the trigger, usually a lever. Both levers and pressure plates are "triggers" - they trigger something else to happen. That "something else" is determined by you when you "link" the two - the trigger and the object to be activated.

#### Levers

A mechanism is placed as a lever using uild raps/Levers ever, and then once that's been completed, you go into that "building's" menu ( ) and link it to something else - this takes 2 more mechanisms, one at the object end (first chosen), one at the lever end (second chosen), for a total of 3 mechanisms used: one lever plus a link at each end. Link the same lever to something else and you need 2 more mechanisms, etc. etc. No limit. One pull, they're all activated.

Main Article: **Lever**

#### Pressure plates

A pressure plate works like a lever, but is based on either being stepped on, or fluid reaching a certain depth. The triggering process (and problems) are the same, but you have some variables you can designate when placing the plate - whether friend/foe triggers it and what size they must be (min and max), or fluid depth (1/7, 2/7, 7/7), etc.

A pressure plate is placed with uild raps/Levers ressure plate, and is otherwise identical to the lever - one mechanism, two more to link it, etc.

Main Article: **Pressure plate**

#### Connection and activation

If all you're doing is connecting a lever to an object, then a dwarf pulls the lever to activate that object. If a pressure plate, then it gets stepped on or the fluid reaches the designated depth - it's that simple.

Attached to a support, the support crumbles (and brings down whatever it was supporting, ~IF~ that was in fact the last thing connected to it!) Attach to a cage or chain, it releases its occupant(s). These are both single-use.

Connected to a barrier - a door, a hatch, a floodgate, or a bridge - it becomes the sole means of activation for those. Dwarves cannot open or close doors/hatches that are linked (and cannot open/close floodgates or bridges without one).

Main Articles: **Door**, **Hatch, Floodgate**

#### On/off, open/close

Note that a trigger does not just "toggle" a barrier - it doesn't *always* work "throw and it's open, throw and it's closed". The lever has to be in the right "phase", left or right, to open or close, and if the barrier is out of phase, nothing happens. What this means to you is that you cannot link one door, open it, then link another and have them stay opposite each other, opened/closed - they will get back "in phase" almost right away, both open, then both closed.\* Gear assemblies, however, *can* remain in opposite states if the second assembly is built and linked while the first is disengaged.

There's a complete list **here.**

*(\* But there are ways to achieve this - read main articles for full discussions.)*

#### Activation lag time

Also note that a few types of barriers respond "immediately" while others are delayed - (again, see **that same list** for full details). If delayed, and you open/close the trigger quickly, it will get out of phase, missing the second command while waiting for the first. Also, if a door, hatch or floodgate is propped open the moment it receives a "close" signal, it won't shut, and, again, be out of phase. Then the lever must be pulled twice, once to get it back in phase, and once to activate it the way you wanted. A dwarf or other creature passing through will hold each of the above constructions open and prevent closing, doors and floodgates can also be blocked by items lying in their tile.

### Machine power

You can run a **pump** manually (or use querns instead of millstones for milling), but there are two kinds of power systems that are used to run pumps and millstones: **windmills** and **water wheels**. Both are buildings - you build them just like a workshop. There are some limits and considerations - build them wrong (without support) and they'll collapse.

#### Windmills

A windmill provides 0, 20 or 40 power - it depends on the "wind" on your map, you either have it or you don't - it's constant across a map and time, and you don't know until you build your first windmill. shows you the power for that windmill on your map. Power comes out the bottom, via a gear or axle. Or you can build it directly over the item to be powered - that works too (but there's no way to shut it off then - see below).

Main Article: **Windmill**

#### Water wheels

A water wheel provides 100 power (but water wheels consume 10, including the first one powered up, so call it 90) if it has "flow" under it, say from a river. You can also create artificial flow in your own channels, if you prefer. Line up several, and you have all the power you want. Power comes out the side.

(Note - too much flowing water can kill your framerate. Be careful about getting carried away.)

Main Articles: **Water wheel**, **Power**

#### Power connection - gears & axles

Connecting is easy, especially if you've ever played with tinkertoys. If you build your pump or millstone adjacent to the source, touching side-by-side, they're automatically connected. (Building "over" another, between floors, is tricky - see articles). If there's distance (horizontal or vertical) between power source and destination, there are axles, and gear assemblies. Axles are just logs - 1 log can get you up to 3 tiles in a straight line (though 3 logs can extend to 10 tiles) horizontally, or 1 single tile vertically, and can be connected directly to each other. Placed gear assemblies (more mechanisms) allow you to change direction of the axle line, either horizontally or vertically.

Main Articles: **Axle, Gear assembly**

#### Power consumption

Pumps and mills consume 10 power each (as do water wheels, powered or not). Gear assemblies use 5 power each, and axles 1 per tile. So you can have a windmill that pumps 40 power, and 4 axles over, a gear, 3 axles up, another gear, and a pump and mill adjacent to that gear - that's 4+5+3+5+(10+10) = 37 - no problem. If you wanted more power, you'd need another windmill or a water wheel, and connect it in to the grid.

Wheels, windmills, pumps, mills, axles and gears will all show the power they have and the power the assembly needs when viewed with . If no power, you've done something wrong.

#### Turning powered machinery on/off

Now, you can also link a trigger to a gear assembly, to disengage that gear in the power train - this is how you turn on/off pumps that are attached to power, and how you create fluid traps that "turn on" automatically when their target is in the desired location.

Notes: If powering pumps, build the gear and lever and link them **first**, then throw the lever to disengage the gear before connecting the power - or you'll find your fluid of choice pumping merrily into your fortress until you find a way to shut off what you just built.)''

Also, be aware that disengaging a gear that's directly under a windmill will cause the windmill to collapse, and the same will happen if you disengage a gear assembly that provides the only support to a water wheel. A "disengaging" gear has to be located later in the power train, or the wheel must be supported from the other side, for instance by an axle.

If building a gear assembly over a pump or millstone, that will work, but the floor between must be channeled *first*.

Main Article: **Gear assembly**

There are also quirks to what are "adjacent" items - sometimes floors get in the way, sometimes they don't, depending on the building - read articles on each piece of machinery for those details.

None of these are that hard to build or connect, and doing it is the best way to learn. Plan a little, expect it not to be 100% optimal the first try, and you'll get it right the second time.

- **Switching by "Load"**

Since all connected machinery will either instantly switch off or fail to start working if the power consumption is higher than the power provided, you can also switch machinery off by "overtaxing" the system. This way, you can build your 20 power windmill directly atop the two pumps it runs, attach a gear to one of the pumps which increases the "load" to 25 when engaged, and turn your pumps on or off by toggling that gear. This scheme is somewhat risky, because machinery can spontaneously activate if components are destroyed or deconstructed, reducing the load.

Since this method shuts down all machines connected to the same power supply, it is only really feasible when you have a highly decentralised power infrastructure - you will want to power small arrays of machinery from their own connected windmills. When drawing power from large centralised installations, e.g. large arrays of water wheels, the only practical option is to enable and cut connections in the way laid out in the preceding paragraph.

#### Weather

As you might expect, machinery that is submerged in water comes to a halt if that water freezes. Perhaps less obviously, machinery that is built upon a natural ice floor, like the surface of a frozen pond, will also freeze. Such components will say "Frozen Here" in their information screen, while connected components will say "Frozen Elsewhere".

## Building/connection limitations

**Machinery** (including axles, gear assemblies, and screw pumps) acts differently from other constructions. It can be built in one of two states:

:\* **Stable Foundation** - The machinery is built on top of a floor, either natural or constructed.

:\* **Hanging** - The machinery is built attached to another piece of machinery, typically on top of a gear assembly (to transfer power further down or out horizontally) or a pump. No additional support is required (except for screw pumps, which have their own requirements for support - see below). The supporting machinery needs only to have been designated for the hanging machinery to be built - it doesn't have to be completed, but might need to be before the power-connection is complete (depending on your design). If the supporting machinery is canceled, disabled, or removed the hanging machinery will collapse to base materials.

- **Windmills** may only connect to machinery directly below their center tile.

:\* Windmills built on floors sometimes transfer power through them, but it seems to depend on the build order - for maximum reliability, channel out the floor.

- **Water wheels** may only connect to machinery on either side of their center tile.
- **Screw pumps** may connect to machinery from any tile in any direction. (However, the walkable tile of the screw pump MUST have a floor under it, so it cannot connect directly below the walkable tile)
- **Gear assemblies** connect in all directions.

:\* A gear assembly which has been disconnected by a lever does not support machinery. No machinery can hang on top of it, and anything already hanging on it will fall apart. In \#2 (below), disconnecting the gear assembly would dismantle the windmill and prevent another from being built until it was reconnected.

- **Horizontal axles** connect to either end, or a gear assembly or machine.
- **Vertical axles** connect directly above and below, or a gear assembly or machine.

#### Unusual windmill behavior examples

In the diagram below, brown is the windmill and the floor it stands on, black is floor from another level, the star is a gear assembly. Windmills offer power only to the tile immediately below their central spot.

:\* \#1 will not work if the gear assembly is installed before the windmill is finished. If the gear assembly was installed later **or** if it gets disengaged and re-engaged (e.g. by a lever), it receives power from the windmill. The unbroken floor will always provide support to the windmill and means invaders cannot use the mill-machinery connection to enter the fort.

:\* \#2 works as long as dwarves can reach the building site - any tile adjacent to the windmill will do. It's the same as 1), but is "hanging", the windmill is supported by the gear assembly. You cannot "disengage" this gear without causing the windmill to deconstruct, and flying or climbing attackers can use the tile of open space to get into your machinery.

{\|style="border: 1px solid \#0b0; background: \#dfd"

\|+**Side view** \|- style="font-family: monospace; font-weight: bold; font-size: 135%" \|style="color: \#970; padding: 0; text-decoration: underline"\|- \|style="color: \#970; padding: 0; text-decoration: underline"\|= \|style="color: \#970; padding: 0; text-decoration: underline"\|- \|  \|style="color: \#970; padding: 0"\|- \|style="color: \#970; padding: 0"\|= \|style="color: \#970; padding: 0"\|- \|  \|  \|- style="font-family: monospace; font-weight: bold; font-size: 135%" \|style="text-decoration: underline"\|  \|style="text-decoration: underline"\|\* \|style="text-decoration: underline"\|  \| \|style="text-decoration: underline"\|  \|style="text-decoration: underline"\|\* \|style="text-decoration: underline"\|  \|- style="font-family: monospace; font-weight: bold; font-size: 135%" \| \|1 \| \| \| \|2 \| \|}

## See also

:\* Trigger

:\* Repeater

:\* Computing

:\* Trap design
