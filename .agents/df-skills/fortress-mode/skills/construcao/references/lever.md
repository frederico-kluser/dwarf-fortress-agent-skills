# Lever

> Fonte: [Lever](https://dwarffortresswiki.org/index.php/Lever) — Dwarf Fortress Wiki (GFDL/MIT)

A **lever** is a building constructed from one mechanism on an empty tile. It can be built with ,,. Once in place, it can be linked to one or more devices such as doors, bridges or supports, permitting you to control these other devices remotely. Order the lever to be pulled through its menu. A dwarf with the lever operation labor will get assigned the job of pulling the lever. This dwarf might be a long way away, and the delay in pulling the lever can result in Fun. Levers also make good furniture choices when constructed with high-quality mechanisms.

Pressure plates are like levers, but are triggered by creatures or fluids directly rather than by giving an order to a dwarf. If levers are too much fun, a pressure plate may be a better choice. There is more information on trap design here.

## Activation of the devices

When a lever is pulled, the connected device(s) activate. What happens during activation depends on the linked device:

- Doors and hatches open and close.
- Supports collapse, potentially causing a cave-in (pulling the lever again won't re-assemble the support, cave-in or not).
- Bridges raise and lower, or retract and extend, depending on the type of bridge.
- Floodgates open and close.
- Gear assemblies toggle between engaged and disengaged (disengaged assemblies can't support other machinery).
- Restraints release the creature assigned to them (leaving the restraint attached to the creature and, at present, unrecoverable).
- Cages are deconstructed, releasing their occupants (needless to say, this is irreversible!)
- Spikes raise and lower.

Different objects take different amounts of time to respond to activation; generally this is only a brief pause, but it can be enough for a charging goblin to cover more than a few tiles.

## Linking

One mechanism is required to construct a lever, and then two more are required to **link** the lever with a device. You need a dwarf with the Mechanic labor enabled to link a lever to a device. The link is made by selecting the lever with , choosing the type of object you want to link the lever to, and then using and to choose the particular object. The list is chronological by order of construction, most recently designated last, and the map will recenter on each object as you scroll through the list.

In addition, you can choose the building to link to with the cursor, moving via arrow keys and up/down. The interface will offer and highlight the nearest applicable building. This choice by cursor was introduced in DF 0.40 and is only available when linking to levers, not pressure plates.

The linkage interface will not give you the option to link buildings already linked to the trigger in question, or tasked to be linked. Buildings that are currently forbidden aren't offered, either. This allows limiting the choices offered to you by deliberately forbidding buildings you don't wish to link.

Once a building is picked, you can choose what specific mechanisms you want to use to connect the device to the lever. The quality of a mechanism affects the accuracy of traps, but not the speed of activation. The first mechanism you choose is for the device end, the second for the lever end. This is important when working with magma.

A lever cannot be successfully linked to a locked door, the dwarves must stand on the door to complete the link. The task will be suspended with a message that they cannot find a path.

A lever can be linked to any number of objects, and each object can have any number of levers controlling it.

There is no way to de-link an object without disassembling either object or lever. When using a lever for a single-use purpose (cages or supports), the mechanism in the lever will remain in the lever, but the object and its mechanism will deconstruct. In this manner, a single lever might accumulate many mechanisms. Deconstructing the lever will free all these mechanisms and allow their reuse - keep your permanent and one-time linkages to separate levers.

In contrast with pressure plates, build order does not affect the timing of levers whatsoever. In any given tick, any levers will send their signals before any furniture receives those signals, so it as if levers are always considered to be built after the furniture they link to. In rare cases, it is possible for the order of arrival of the dwarf pulling the lever to affect the precise timing of lever-linked devices, as when using a hatch to drop a dwarf-- if the falling dwarf arrived later than the lever pulling dwarf, the dropping dwarf will take an extra tick to fall.

## On/Off vs Open/Close

Levers normally have an "on" and an "off" state, seen as whether the small tag at the top of the lever is to the left ("off" state) or the right ("on" state). Upon being pulled, the state of the lever changes, and everything they're connected to updates to the *corresponding* state of that lever, and does not just *change* states ("toggle"). This becomes important if you have several levers attached to the same device, or one trigger attached to several systems.

Example: 2 levers (both in "off" position) are connected to a drawbridge. After pulling the first lever, the bridge will lift. Pulling the second lever tells the bridge to "open", which it already has done - no visible effect. When it is pulled a second time it will let the bridge down. This in turn requires the *first* lever (still in "open/lift" position) to be pulled twice to trigger a change (lift again), and so on.

"On" and "off" state is fixed and dependent on the lever, not the object that lever is linked to:

- "dash to the right" ( **ó** ) is **on**
- "dash to the left" ( **ò** ) is **off**

Note, however, that gear assemblies are *the sole exception* to this: Instead of On/Off triggers, they indeed **do** toggle.

Several devices, such as floodgates and bridges, have a delayed response to all incoming signals, and will not respond to subsequent signals until the first has taken effect. For instance, if you pull a lever attached to a floodgate on then off in rapid succession, the floodgate will only respond to the first signal, independent of the position the lever rests in eventually.

In the unusual case that a device receives both an on and an off trigger in exactly the same tick, the device will change states-- an open device will close, and a closed device will open.

## On/Off states

Objects that can be controlled by levers include:

##### Multiple Uses

A "step" is not a step that a dwarf makes, and not based on FPS. It's one "step" that the game advances. When paused (via ), you can manually advance the game "1 step" by hitting the period ( ) key.

- Bridge – Activates 100 steps after being triggered (see bug below)
  - **On:** Turns the bridge into either a raised drawbridge, or a retracted bridge, depending on which option was chosen when the bridge was constructed.
  - **Off:** Returns the bridge to normal.

- Door – Activates instantly. Note that once you connect a door, it is either completely open or sealed shut. There is no "*closed, but can be opened by a dwarf*" state anymore.
  - **On:** Opens the door.
  - **Off:** Closes the door.

- Floodgate – Activates 100 steps after being triggered.
  - **On:** Opens the floodgate.
  - **Off:** Closes the floodgate.

- Floor hatch – Activates instantly. Note that, like doors, once you connect a hatch, it is either completely open or sealed shut.
  - **On:** Opens the hatch.
  - **Off:** Closes the hatch.

- Grate – Activates 100 steps after being triggered. When it is open, it just disappears. Liquids go through it just the same, but it will no longer function as a floor/wall (depending on its orientation).
  - **On:** Opens the grate.
  - **Off:** Closes the grate.

- Bars – Activates 100 steps after being triggered. When it is open, it just disappears. Liquids go through it just the same, but it will no longer function as a floor/wall (depending on its orientation).
  - **On:** Opens the bars.
  - **Off:** Closes the bars.

- Upright Spear/Spikes – Activates 40 steps after being triggered.
  - **On:** Retracts spears/spikes.
  - **Off:** Extends spears/spikes.

- Gear assembly – Activates instantly. When it is disengaged, no power goes through it and anything that is being kept up by its presence (like a windmill right on top of it) falls down.
  - **On:** Toggles gear state.
  - **Off:** Toggles gear state.

- Track stop – Disables without delay, enables 40 steps after being triggered. When disabled, trackstops behave like the track (or floor) underneath them, and minecarts occupying the tile will not auto-dump or experience friction.
  - **On:** Disables the track stop.
  - **Off:** Enables the track stop.

##### One-Shot

These items, when activated, deconstruct, and/or cannot be triggered again until re-linked.

- Cage – Activates instantly. Deconstructs the cage and releases all of its contents. The cage and its attached mechanism will be left on the floor nearby; you recover the mechanism used on the cage but you do not recover the mechanism used in the lever until you deconstruct the lever itself.
- Restraint – Deconstructs the chain/rope and releases whatever creature it held. The restraint's mechanism will be left on the floor nearby, and the restraint itself will remain attached to the creature's neck; again, you recover the mechanism used on the restraint but you do not recover the mechanism used in the lever until deconstructing the lever itself.
- Support – Deconstructs the support, ideally without a dwarf next to it. Most commonly used to cause controlled cave-ins. The support's building material and its attached mechanism can both be recovered (unless they happen to get destroyed in said cave-in).

## Labeling

There is no built-in indication of what a lever does, and pulling them to see what will happen can be immensely fun. Naming the levers using - is the most foolproof way of labeling levers; color-coding of levers can give some indication too. If you really don't want to name your levers, using the note function can fulfill the same purpose.

However, it is possible to ascertain whether or not a building has been linked to a lever by finding the building under "View Rooms/Buildings" and then selecting "Zoom to building items". A device that is actuated by a lever not only lists the components of the building but will also include a mechanism item. Viewing the lever itself this way will display one mechanism for each building the lever is linked to (plus one mechanism from the construction of the lever itself).

There is way to ascertain which lever is linked to what, but it becomes very hard when you have many linkable items. Find the lever, use "q" and then select "add new task". Try for every linkable thing in your fortress, to link the lever to it. If an object isn't available for linking, that's because it is already linked. Though this method isn't very usable to find the single linked item in all of them, it is useful when you forgot whether the left or the right lever was linked to the support.

Finally, the utility DFHack provides a new GUI command "gui/mechanisms" (bound to - by default) which allows you to list and navigate mechanical connections from inside the game itself. This is by far the easiest and least tedious method to review your levers.

## Toggling Passages

Since all activatable devices apart from gear assemblies have predefined "on" and "off" states, you cannot directly link a lever to two doors in such a way that a single lever flip opens one and closes the other. You can, however, make use of the differences between different linkable devices:

- while doors and floodgates prevent passage when "off" and allow passage when "on", a bridge prevents passage by raising or retracting upon receiving an "on" signal and returns to its passable state when "off".
- hatches, floor bars and floor grates can be placed over a channelled-out tile creating a gap in a passage. When closed (switched "off"), those structures now provide a path across the gap, but block passage when switched "on" and opening. Hatches, like doors, react immediately to signals, which makes them particularly useful for this purpose.

So, to "switch" between paths with a single lever, you could connect functionally different devices to it, e.g. a floodgate in one passage and a raising bridge in another. Whenever the lever is switched now, it will send the necessary signals to open one path and at the same time close the other.

If you want to "toggle" two buildings which follow the same switching rules, you will probably need to build a Logic device to do the job.

## Bugs

- Linked devices that were prevented from operating on a previous trigger may engage immediately on the next trigger.
