# Mist

> Fonte: [Mist](https://dwarffortresswiki.org/index.php/Mist) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Mist** is created by water falling from one Z-level to another, from ocean waves, items or creatures skipping across water or just standard splashing. The mist is generated on levels below the top level (from which the water drops), but spreads out similarly to miasma and, therefore, can appear even on the top level, and lingers and spreads for a short time after any water stops falling.

Walking through mist generates a happy thought for most intelligent creatures, and can act to clean various contaminants off of dwarves. Even hostile creatures attempting to siege a fortress will get a pleasant feeling from mist.[1]

Mist is separate from magma mist and steam.

Rampant screw pumps are a great mist source.

## Generating Mist

### Constructed waterfall

The easiest method is simply to use a constant source of water (pumped or channeled) and let it fall more than 1 z-level next to a path that dwarves use regularly. The actual tile (you only need one) that the water drops should not be part of the path, as dwarves will believe they are in 7/7 water and cancel jobs - a statue on that tile will prevent this nicely, or place the fall itself to the side of the path and make that a restricted traffic tile.

Floor grates or bars on every\* tile adjacent to the water flow should be used as part of the drainage system (which should be larger than the intake system, just to be safe!), and to avoid mud on adjacent tiles. Use a door, hatch, floodgate or bridge linked to a lever to turn off the flow if/when desired.

(\* when designing this, remember that grates/bars do not support floor tiles!)

The problem with this setup is that this amount of constantly falling/flowing water can have a negative impact on your fps rate. Using a repeater to allow a non-constant flow, or linking the flow to a pressure plate, where it will only fall when dwarves approach, will help this.

### Ring generator

Mist ring generator (z = 1)

Mist ring generator (z = 0)

AncientEnemy [1] devised a convenient way to generate mist. This method relies on the fact that screw pumps pump water faster than water spreads out.

AncientEnemy's original simple mist generator.

Simply put, screw pumps are daisy-chained (output to input) in a circle and then water is added to the system. Water is typically added by designating one of the inputs to the pump as a Pond and having dwarves fill it up. Once water is dropped from the floor above it is immediately sucked up by the next pump. Since there is falling water, mist is generated. Ahh, lovely waterfalls!

Below is an example of a simple mist generator. The Z=0 level can be anything, a booze stockpile, barracks or even your atom smasher. The z=-1 layer can also be identical to the z=0 level. Mist will also be generated there. Because the water never touches the floor there, you don't have to worry about muddy tiles.

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| P | u | m | p |   | F | l | o | o | r |   | ( | z | = | 1 | ) |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| ▒ | ▒ | ▒ | ▒ | ▒ | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| ▒ | \_ | ÷ | ÷ | \_ | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| ▒ | ÷ | . | . | ÷ | ▒ |   | T | h | e |   | w | a | t | e | r |   | c | a | n |   | g | o |   | c | l | o | c | k | w | i | s | e |   | o | r |   | c | o | u | n | t | e | r |   | c | l | o | c | k | w | i | s | e | . |
| ▒ | ÷ | . | . | ÷ | ▒ |   | M | a | k | e |   | s | u | r | e |   | y | o | u | r |   | p | u | m | p | s |   | a | r | e |   | c | o | r | r | e | c | t | l | y |   | a | l | i | g | n | e | d | . |   |   |   |   |   |
| ▒ | \_ | ÷ | ÷ | \_ | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| ▒ | ▒ | ▒ | ▒ | ▒ | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |

A movie [2] best illustrates the operation.

\
It is advisable to put statues under the holes in the bottom layer, so dwarves cannot go under the water, to displace the water, requiring a refill.

Note that if you put grates on the z = 1 layer, the mist will not spread upward, if that is desired.

### Stack generator

A two-pump-stack can be used to lift a single tile of water and drop it back into the reservoir, generating mist (and cleaning dwarves, if desired).

|  |  |  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|----|----|
|   | s | i | d | e | v | i | e | w |   |
|   |   |   |   |   |   |   |   |   |   |
|   |   |   | % | % | \_ |   |   |   |   |
|   |   |   | % | % | \_ |   |   |   |   |
|   | ░ | ░ | ░ | ░ | ▄ | ░ | ░ | ░ |   |
|   | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ |   |

The lower (brown) pump (pumping right to left) raises the water from the reservoir on the right to floor level on the left, then the upper (green) pump (pumping left to right) raises that water to the air +2 z-levels above the reservoir. The water then falls through the floor grates ( \_ ) into the reservoir, and the cycle can be repeated. Pump build order is important; build the upper (green) pump first, then the lower (brown) pump, to ensure the water is raised in a single tick. Since the water never sits at floor level, no containment walls are necessary (though mud will be created in the tile left of the brown pump). You can toggle power to the pumps as often as desired to provide happy thoughts without constant lag. If used for dwarf-cleaning, a water level of 2/7 or 3/7 will avoid job cancellations.

### Light aquifer

If your embark location has a light aquifer, it is possible to build an unpowered mist generator-plus-bathing unit combination. You need two floors under the aquifer - lowest floor is for dwarves, second floor is for water to fall a z-level to create mist and to control the amount of water flow. It is also possible to dig out more of the aquifer to increase water flow if needed. You can use this water elsewhere or let it evaporate.\[Verify\]

## General comments

- Evaporation is nonexistent as long as the pumps are working and the water is moving, even above ground.\[Verify\]

- Job cancellation spam is possible if the water is filled to 4/7 or greater and a dwarf walks where the water falls. Even then, this can be greatly reduced by setting them as restricted traffic areas, or completely prevented by blocking access to these tiles without blocking the water, such as by placing a statue underneath.

- Mud will form wherever the water falls. Subterranean trees can sprout up and clog the system. Solutions to this problem include: statues, paved roads, constructed floors or fortifications, or to simply channel out the space once the mist generator is running.

- These systems work best with a single tile of water (7/7, at most) due to the way water descends z-levels. Any additional water will overflow into nearby tiles.

- Automated mist generators may significantly lower your FPS, particularly if multiple generators are used.\[Verify\] This might be remedied by triggering via a repeater with a long delay or by one or more pressure plates (perhaps set to activate by a passing dwarf).\[Verify\]

If skin pores could orgasm.

|  |
|----|
| "Mist" in other / Languages / Dwarven / : / sôd / Elven / : / enure / Goblin / : / guslo / Human / : / sitsu |
