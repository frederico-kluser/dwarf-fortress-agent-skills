# Roller

> Fonte: [Roller](https://dwarffortresswiki.org/index.php/Roller) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **b - m - r**
- **╤ or ╢ X**
- **╤ or ╢:** X
- **X**
- **Icon**
- **Construction**
- **Materials:** Labors
- **1 or more Mechanisms 1 Rope:** Mechanics
- **Power**
- **Uses 2 power per tile (independent of speed).**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

A **roller** is a powered machine component for the automated propulsion of minecarts. They are built over the top of existing tracks with (b-m-r), requiring a mechanic, *(length/4)+1* mechanisms and a rope. Rollers are very useful to maintain a cart's momentum along long routes, to get them to climb Z-levels without dwarfpower involved, and to get them to reach speeds unattainable by guiding dwarves. These devices are variable-length (1+), variable-direction and variable-speed (see here), all set prior to construction. A roller uses two units of power per tile of length.

Rollers do not provide acceleration but rather set the cart's velocity to a new value: if a cart moves across an active roller in the direction the roller works and moves slower than the roller's specified speed, the cart will be set to the roller's speed. Carts going faster than the roller are unaffected.

Relative Speeds:

|                |       |
|----------------|-------|
| Feature        | Speed |
| Down ramp¹     | 4900  |
| Dwarf push²    | 20000 |
| Roller lowest  | 10000 |
| Roller low     | 20000 |
| Roller medium  | 30000 |
| Roller high    | 40000 |
| Roller Highest | 50000 |

¹ Ramps provide acceleration rather than setting a new velocity, and are subject to friction in the same tile.\
² A dwarf push sets the speed of the vehicle, but is subject to friction and starts moving from halfway through the tile.\
(see the Minecart page for details)

A cart going against a roller's movement direction will be sent back the way it came (once again at the roller's speed), unless it was moving extremely fast, well over derailing speed. A cart crossing over a roller perpendicular to its current movement direction will gain the roller's amount of speed in the perpendicular direction without directly changing its forward motion. Without an adjacent wall to constrict its movement, this will typically send a cart off the rails on a diagonal path, completely unable to follow any tracks until it collides with a wall or is otherwise brought to rest.

Rollers may be placed directly on ramps to help pull carts up Z-levels. Currently rollers can only be placed on up or down ramps or open spaces if this results in being connected to designated powered components (gears, axles, or pumps). The components do not need to be constructed, only designated, so you can designate a gear that would power a roller if the gear were powered, designate the roller on a ramp, and remove the gear designation, all without unpausing.

Care must be taken in glaciers and other extremely cold biomes, since rollers (and the machinery used to power them) will not operate when constructed on natural ice floors[1]. Rollers can be constructed over trackless floor or without any floor at all (supported by other machinery) but will not affect carts in either case.

Because of their one-way nature, rollers are unsuitable for most two-way minecart tracks. However, a minecart set to be *guided* is not affected by rollers at all[2] — this allows a one-way track to be used in both directions. In addition, unpowered rollers do not affect minecarts: switching mechanisms (such as a pressure plate attached to powering gear assembly) can be used to create complex paths.

All rollers transmit power *perpendicular* to their activity direction. Rollers that are only one tile long transmit power in all four cardinal directions, on the same level, and can thus serve as a replacement for gear assemblies when switching power on/off or vertical connection is not required; the roller takes a mechanism and a rope to build, but only consumes two power. Longer rollers can *also* transmit power along their activity direction (along the tracks) if the 'build order' is correct, but the rules are complicated and such power transmission will permanently cease or never become available if the conditions are not met. It's generally better not to rely on such transmission.

Rollers cannot be powered from above. If desired, the impassable tile of a screw pump can transfer power while blocking movement, but it does not count as a wall for ramp movement purposes.
