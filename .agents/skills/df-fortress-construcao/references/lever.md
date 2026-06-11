# Lever

> Fonte: [Lever](https://dwarffortresswiki.org/index.php/Lever) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **b - m - l**
- **Icon**
- **Construction**
- **Materials:** Labors
- **1 Mechanism:** Mechanics
- **Power**
- **Uses 0 power.**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

A **lever** is a building constructed from one mechanism on an empty tile. It can be built from the Workshops menu, Machines/fluids, Lever (b-m-l). Once in place, it can be linked to one or more devices such as doors, bridges or supports, permitting you to control these other devices remotely. Order the lever to be pulled by clicking on it and selecting the Pull lever button. A dwarf with the lever operation labor will get assigned the job of pulling the lever. This dwarf might be a long way away, and the delay in pulling the lever can result in Fun. Like workshops, levers can be assigned to a specific dwarf, which will prevent other dwarves from pulling the lever. Levers also make good furniture choices when constructed with high-quality mechanisms.

Pressure plates are like levers, but are triggered by creatures or fluids directly rather than by giving an order to a dwarf. If levers are too much fun, a pressure plate may be a better choice. There is more information on trap design here.

## Activation of the devices

When a lever is pulled, the connected device(s) activate. What happens during activation depends on the linked device:

- Doors, hatches, floodgates, and grates open and close.
- Supports collapse, potentially causing a cave-in (pulling the lever again won't re-assemble the support, cave-in or not).
- Bridges raise and lower, or retract and extend, depending on the type of bridge.
- Gear assemblies *toggle* between engaged and disengaged (disengaged assemblies can't support other machinery).
- Restraints release the creature assigned to them (leaving the restraint attached to the creature, only recoverable by dumping the restraint or killing the creature).
- Cages are deconstructed, releasing their occupants (needless to say, this is irreversible!)
- Spikes raise and lower.
- Bars retract and extend.
- Track stops deactivate and reactivate.

Different objects take different amounts of time to respond to activation; generally this is only a brief pause, but it can be enough for a charging goblin to cover more than a few tiles.

## Other uses

A lever not linked to anything can still be pulled. This is a rather high-priority job, and it has the effect that the dwarf pulling it will end up near the lever (usually on top of the pulled lever) with the "no job" status (allthough if the lever is in a zone belonging to a location instead of "no job" the "socialize" activity might be displayed instead). If there is not much to do in the fortress and the dwarf does not immediately get a new job, this feature can be used to do low-priority jobs in the vicinity, or on the way back. In Dwarf Fortress parlance this functionality is called *Urist's lever*; It can be used to convince dwarfs to clean remote cavern sections, enter the library to then discuss or ponder important things, enter the temple for those who never pray and are unhappy about it, or generally move to a place where they would not go voluntarily, for instance to create an unfortunate accident for them. If only one dwarf is the target, assign the lever to them.

Pairs of adjacent levers (in a tavern location) can also be used to make sure that two dwarves, who are related or are friends (and are assigned to the levers), do socialize with a friend or with family and thus do fullfill that need - allthough it might be needed to make sure that no story telling and art performance is currently ongoing in the zone, but again these can be easily be aborted by having the performer do a lever pulling job somewhere else. Of course it might also be needed to temporarily take both dwarves of any other duties as otherwise the two dwarves might not stay long enough adjacent to each other (but will nearly immediatly take another job). And for some dwarves it might also be necessary (at least if the levers are in a tavern) that the levers are set on repeat to break up any chanting, story telling or chanting of one of the dwarves (as these activities prevent other social interaction between the dwarves), until they did speak to each other.

Children, who pull a lever in a zone assigned to a guild hall (which is not only open for members), will end up with the "socialize" activity, if there is currently a guild demonstration in progress (and if the child does not immediatly decide to eat, drink, sleep or pickup equipment). They will afterwards join in any new organized guild demonstration, if, after the current guild demonstration ends, there is still someone to organize (and teach) a new guild demonstration (and the child did not decide to eat, drink, sleep or pickup equipment), otherwise the children will usually start to play (and the micromanagment was for naught). So levers can be used to give all children some basic education in some moodable skill, allthough, as children cannot be directly assigned to a lever, it must be made sure, that no adult, who is allowed to pull that lever, can access the lever and also that some children (who ie. are already watching a guild demonstration) or have gotten some education in the moodable skill are not allowed to pull the lever (eg. only children, who should watch a guild demonstration and are not currently socializing in the guildhall, are set to do chores under standing orders). If a child is in progress to pull a lever, the child can safely be set to do no chores as the child will still pull the lever (and only afterwards not do any more chores). For maximum effect it is also advised that lever pulling is the only chore for children (and all other duties are temporarily disabled for children).

## Linking

One mechanism is required to construct a lever, and two more are required to **link** the lever with a device. You need a dwarf with the Mechanic labor enabled to link a lever to a device. The link is made by first selecting the lever with the mouse and choosing **Link lever**, which will bring up a window showing the mechanisms which will be used and which end of the link they will be used on. Then use the mouse to select the object the lever is to be linked to.

The linkage interface will give you the warning **Cannot link to** if the object is already linked, or tasked to be linked, to the lever in question. Buildings that are currently forbidden will also show the same warning message. A lever cannot be successfully linked to a locked door, as the dwarves must stand on the door to complete the link. The task will be suspended with a message that they cannot find a path.

Currently (as of 50.04) you cannot choose which specific mechanisms you want to use to connect the device to the lever; they will be automatically chosen in order of the oldest available mechanisms. The quality of a mechanism affects the accuracy of traps, but not the speed of activation. The first mechanism listed is for the device end, the second for the lever end. This is important when working with magma. One workaround is to order levers be constructed with mechanisms as you build them, but pause the construction of the lever as soon as the mechanism is delivered to the lever location. Then, when you want to use specific mechanisms, you can cancel the lever to make that lever's mechanism drop on the floor and become available for use. Alternatively, you can forbid all of the mechanisms you do not want to use before linking the lever.

A single lever can be linked to any number of valid objects, and each object can have any number of levers controlling it.

There is no way to de-link an object without disassembling either the object, or lever. When using a lever for a single-use purpose (cages or supports), the mechanism in the lever will remain in the lever, but the object and its mechanism will deconstruct. In this manner, a single lever might accumulate many mechanisms. Deconstructing the lever will free all these mechanisms and allow their reuse, so it is advisable to keep your permanent and one-time linkages to separate levers.

In contrast with pressure plates, build order does not affect the timing of levers whatsoever. In any given tick, any levers will send their signals before any furniture receives those signals, thus levers behave as if they'd been built after the furniture they link to. In rare cases, it is possible for the order of arrival of the dwarf pulling the lever to affect the precise timing of lever-linked devices, as when using a hatch to drop a dwarf-- if the falling dwarf arrived later than the lever pulling dwarf, the dropping dwarf will take an extra tick to fall.

## On/Off vs Open/Close

Levers normally have an "on" and "off" state, distinguished by the visual appearance of the lever (see below). Upon being pulled, the state of the lever changes, and everything they're connected to updates to the *corresponding* state of that lever, and does not just *change* states ("toggle"). This becomes important if you have several levers attached to the same device, or one trigger attached to several systems.

Example: 2 levers (both in "off" position) are connected to a drawbridge. After pulling the first lever, the bridge will lift. Pulling the second lever tells the bridge to "open", which it already has done - no visible effect. When it is pulled a second time it will let the bridge down. This in turn requires the *first* lever (still in "open/lift" position) to be pulled twice to trigger a change (lift again), and so on.

The "on" and "off" state is fixed and dependent on the lever, not the object that lever is linked to.

In DF Premium,

- "lever to the left" () is **on**
- "lever to the right" () is **off**

While in DF Classic,

- "dash to the right" ( `ó` ) is **on**
- "dash to the left" ( `ò` ) is **off**

Note, however, that gear assemblies are *the sole exception* to this: Instead of On/Off triggers, they indeed **do** toggle.

Several devices, such as floodgates and bridges, have a delayed response to all incoming signals, and will not respond to subsequent signals until the first has taken effect. For instance, if you pull a lever attached to a floodgate on then off in rapid succession, the floodgate will only respond to the first signal, independent of the position the lever rests in eventually.

In the unusual case that a device receives both an on and an off trigger in exactly the same tick, the device will change states -- an open device will close, and a closed device will open.

## On/Off states

Objects that can be controlled by levers include:

##### Multiple Uses

A "step" is not a step that a dwarf makes, and not based on FPS. It's one "step" that the game advances. When paused (via spacebar ), you can manually advance the game "1 step" by hitting the period ( . ) key.

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
- Restraint – Deconstructs the chain/rope and releases whatever creature it held. The restraint's mechanism will be left on the floor nearby, and the restraint itself will be placed in the creature's inventory (attached to its upper body); again, you recover the mechanism used on the restraint but you do not recover the mechanism used in the lever until deconstructing the lever itself.
- Support – Deconstructs the support, ideally without a dwarf next to it. Most commonly used to cause controlled cave-ins. The support's building material and its attached mechanism can both be recovered (unless they happen to get destroyed in said cave-in).

## Keeping track of levers

Since pulling the wrong lever can lead to lots of fun, it's worth making sure you know what your levers do.

- From a building controlled by a lever, you can go to "Show linked buildings" to locate the lever it is controlled by;
- From a lever, you can go to "Show linked buildings" to locate the buildings it controls;
- Finally, it's helpful to give your levers descriptive names to make them easier to locate.

## Toggling Passages

Since all activatable devices apart from gear assemblies have predefined "on" and "off" states, you cannot directly link a lever to two doors in such a way that a single lever flip opens one and closes the other. You can, however, make use of the differences between different linkable devices:

- while doors and floodgates prevent passage when "off" and allow passage when "on", a bridge prevents passage by raising or retracting upon receiving an "on" signal and returns to its passable state when "off".
- hatches, floor bars and floor grates can be placed over a channelled-out tile creating a gap in a passage. When closed (switched "off"), those structures now provide a path across the gap, but block passage when switched "on" and opening. Hatches, like doors, react immediately to signals, which makes them particularly useful for this purpose.

So, to "switch" between paths with a single lever, you could connect functionally different devices to it, e.g. a floodgate in one passage and a raising bridge in another. Whenever the lever is switched now, it will send the necessary signals to open one path and at the same time close the other.

If you want to "toggle" two buildings which follow the same switching rules, you will probably need to build a Logic device to do the job.

## Bugs

- Linked devices that were prevented from operating on a previous trigger may engage immediately on the next trigger.
