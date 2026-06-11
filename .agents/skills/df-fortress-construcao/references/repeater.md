# Repeater

> Fonte: [Repeater](https://dwarffortresswiki.org/index.php/Repeater) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

!!UNKNOWN!!  · xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

In *Dwarf Fortress*\*, a **repeater** is a device which creates a cyclic pattern of on and off signals. The simplest repeater design is a dwarf pulling a lever on repeat. However, numerous fully-automated designs are possible which can be made to operate at varying rates and linked to other systems for precise timing. Most repeaters use minecarts, fluids, or creatures to trigger pressure plates cyclically.

As a general warning, always have a way to turn off the repeater, and/or allow your dwarves later access for repairs or modifications.

(\* In almost any other context, especially engineering or "technical" discussions, the term "repeater" refers to a signal re-transmitter, and what this article describes is generally called an "oscillator" or "clock generator".)

### Lever repeater

A lever with a pull job on repeat provides the simplest repeating cycle. After taking the first job, one dwarf will typically continue to pull the lever until becoming hungry, thirsty, or tired, at which point another dwarf will take over. A lever repeater is generally fast (less than 100 ticks per cycle), with varying lengths of inactivity as dwarves switch out. Unfortunately, the cycle length cannot be modified, nor can the repeater be synchronized with other systems. The occasional periods of inactivity can also prove problematic in critical applications, though a vampire can be significantly more reliable than a group of living dwarves.

### Traffic repeater

For low-priority tasks, a civilian-triggered pressure plate built in a hallway of the fortress can provide a simple oscillating signal automatically. The signal from such a repeater varies widely, though it can be adjusted somewhat by choosing hallways with more or less traffic. The lack of precision means that traffic repeaters are best utilized where a task needs to occur occasionally, but the timing is unimportant (such as triggering an atom smasher at the bottom of a garbage chute).

### Wave repeater

A wave repeater is simply a wave traveling through a channel containing a pressure plate, as described in this forum post.

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| ╔ | ═ | ═ | ═ | ═ | ═ | ═ | ╗ |   |   |   | ╔ | ═ | ═ | ═ | ═ | ═ | ═ | ╗ |
| ║ | ^ | . | . | . | . | . | ║ | - | - | \> | ║ | 7 | 7 | 7 | 7 | 7 | 6 | ║ |
| ╚ | ═ | ═ | ═ | ═ | ═ | ═ | ╝ |   |   |   | ╚ | ═ | ═ | ═ | ═ | ═ | ═ | ╝ |

A single 6/7 water tile flows through the channel, occasionally triggering a pressure plate set to trigger on 0-6/7 water. To get the right amount of water in it, it's simplest to fill it all the way, then designate it as a water source (and perhaps another location as a pond) until a dwarf takes away a single bucket full of water.

As designed (5 tiles of non-triggering water, 1 tile of triggering water), this setup triggers rapidly, on par with the repeaters described below. Counter-intuitively, making it smaller or removing more water slows the action of the repeater because the pressure plate never gets a chance to recover from triggering, which takes 100 ticks. Unfortunately, liquids behave semi-randomly, which means the period of this repeater can vary, making it unsuitable for fine timing applications.

Note about pond/pit filling the repeater. Pond/pits can only be filled to 6/7 so you will need to set the pressure plate accordingly to trigger on 0-5/7.

It's possible to make a design that can be easily started and stopped, even one that conserves water, but such systems are complex, when the beauty of this design is its simplicity. If it needs to be stopped for maintenance, one is probably best off simply dropping another bucket of water in it.

### Fluid logic repeater

The traditional repeater design is probably this fluid-based one (described on the forum by AncientEnemy):

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
|   | ≈ | ≈ | ≈ | ≈ | ≈ |   |   | - |   | i | n | f | i | n | i | t | e |   | s | o | u | r | c | e |   | o | f |   | w | a | t | e | r |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   | ═ | ╗ | ≈ | ╔ | ═ |   |   | - |   | w | a | l | l |   | t | o |   | c | h | a | n | n | e | l |   | o | u | t |   | a | f | t | e | r |   | c | o | n | s | t | r | u | c | t | i | o | n |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   | ╠ | X | ╣ |   |   |   | - |   | s | h | u | t | o | f | f |   | f | l | o | o | d | g | a | t | e |   | ( | l | i | n | k | e | d |   | t | o |   | e | x | t | e | r | i | o | r |   | l | e | v | e | r | ) |   |   |   |   |   |   |   |
|   |   | ║ | \# | ║ |   |   |   | - |   | 1 | - | t | i | l | e |   | d | r | a | w | b | r | i | d | g | e |   | ( | l | i | n | k | e | d |   | t | o |   | p | r | e | s | s | u | r | e |   | p | l | a | t | e | ) |   |   |   |   |   |   |   |
|   |   | ║ | ^ | ┼ |   |   |   | - |   | p | r | e | s | s | u | r | e |   | p | l | a | t | e |   | ( | s | e | t |   | t | o |   | 7 | - | 7 |   | w | a | t | e | r | ) | , |   | a | n | d |   | a | c | c | e | s | s |   | d | o | o | r |   |
|   |   | ╠ | X | ╣ |   |   |   | - |   | f | l | o | o | d | g | a | t | e |   | ( | l | i | n | k | e | d |   | t | o |   | p | r | e | s | s | u | r | e |   | p | l | a | t | e | ) |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   | ╚ | ═ | ╝ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |

So long as the shutoff floodgate isn't closed, water from an infinite source flows on to the pressure plate, causing the raising bridge to block access to the water source and destroy water in the circuit, while the opening of the southern floodgate compensates for the space taken up by this bridge. This water destruction mechanic means that, unlike many fluid logic circuits, this repeater needs no drainage. The single pressure plate works both to regulate the repeater, and as output.

This repeater toggles fairly slowly, about once every 300 steps, making it suitable for operating repeating bridges, floodgates, and upright spikes. Off signals tend to follow on signals about 200 ticks later. As an added bonus, the southern wall can be removed and connected to a cistern whose water level will be automatically maintained at a level between 3 and 4 deep-- perfect for swimming!

For an alternate water-based repeater, consider the design at User:SL/Logic_Gates#Repeater which demonstrates a two level, hybrid repeater.

### Goblin repeater

Designs based on creature logic are also possible. The following example is compact, reliable, and fairly predictable.

|  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|
|   |   |   | ╔ | ═ | ╗ |   |   |
| ═ | ═ | ═ | ╝ | ¢ | ╚ | ═ | ═ |
| p | ¢ | ^ | ¢ | ¢ | ^ | ¢ | p |
| ═ | ═ | ╗ | ¢ | ╔ | ═ | ═ | ═ |
|   |   | ╚ | ═ | ╝ |   |   |   |

A captured goblin placed between the two pressure plates drives this system in his attempts to reach map edge through paths ¢p. ^ is linked to all ¢, and ^ is linked to all ¢, as well as to output. This gives the goblin a path away from his constrained tile every 100 ticks. Delays in picking up path tend to make it run a cycle every 250 ticks. with on and off signals separated by about 120 ticks. Its rate of repetition can be doubled by hooking both ^ to output, although this leads to close placement of on and off signals.

### Minecart repeater

In the simplest application, a hauler can guide a minecart across a pressure plate and around a circular track on a set schedule. A hauling route stop set to guide after X days has a fixed minimum interval (X days), but the maximum cycle time is somewhat variable (depending on how long it takes a hauler to accept the job and walk to the minecart). This type of repeater can be useful for triggering occasional time-insensitive events, like enabling a mist generator for a few days every month.

To remove the dwarf timing uncertainty, a roller can propel the minecart around the circular track instead. Due to the fixed speed provided by rollers and the deterministic behaviour of minecarts, this type of minecart repeater provides a cycle with an absolutely constant repeat time. The exact period of such a powered repeater is relatively easy to regulate by choosing the operation speed of the roller, by adjusting the length of the track and by adding medium- and low-friction track stops to reduce movement speed.

The impulse ramp exploit allows for the design of completely autonomous minecart-based repeaters. Changing the length and friction of the route provides the ability to fine-tune the period of the repeater.

This design uses a 7 by 8 by 3 Z-level footprint, and was used for upright spike traps. It was originally posted in this forum thread.

    z              z-1            z-2
    1234567890     1234567890     1234567890
    wwwwwwwwww  1  wwwwwwwwww  1  wwwwwwwwww     where
    wwwwwwwwww  2  wwwwwwwwww  2  wDDDDDDDDw     w = unchanged wall
    wwwwwwwwww  3  wwwwwwwwww  3  wDwwwwwwDw     D = dig prio 4
    wwwwwwwwww  4  wwwwwwwwww  4  wDwwwwwwDw     h = channel prio 4
    wwwwwwwwww  5  wwwwwwwwww  5  wDwwwwwwDw     H = channel prio 5
    wwwwwwwwww  6  wwwwwwwwww  6  wDwwwwwwDw
    wwwwwwwwww  7  wwwwwwwwww  7  wDwwwwwwDw
    wwwwwwhDhw  8  wwwwwhwwHw  8  wDDDDwwwww
    wwwwwwwwww  9  wwwwwwwwDw  9  wwwwwwwwww

1.  Carve a track at all the 'D' tiles in the obvious direction.
2.  Carve N/E impulse ramps at the three ramps (2 on Z - 2, one on Z - 1)
3.  Place a hatch cover over the east chute on Z and define a track stop there (with a mine cart, of course).
    1.  Remove the default movement orders for the stop.
    2.  Hook the hatch to a start/stop lever. (not pictured)
4.  Build a mine cart activated pressure plate anywhere on the flat track (i.e. not any ramp), for example, 2 tiles N of the drop chute starting the repeater.
5.  Hook the pressure plate up to the focus of the repeater (spike traps, danger room, bridge, etc).
6.  Clear out or forbid all the debris in the tunnel, or you run the risk of creating road kill as someone goes to pick it up.
7.  Use the lever to start and stop the process.

\
See this forum thread for other designs tuned for bridge and upright spike traps.

See this forum thread for a super-compact design.

Minecart repeaters can be calibrated to periods usable in the construction of clocks, like 200, 300 or 400 steps. Powered repeaters of this type will require nothing but a single roller and the power to run it, one pressure plate and a bit of space for the track. Repeaters using ramps to create perpetual motion don't need the roller or power but tend to be a bit more difficult to calibrate to useful periods and need additional infrastructure to stop their operation.

Minecart repeaters can also be synchronized with other systems. Adding additional pressure plates to the tracks can allow a single repeater to provide multiple offset signals, and/or a combined high-frequency signal. Alternatively, a pressure plate can trigger another independently-timed system.

## Clock Generation

Although the law of big numbers means that, over large enough intervals, the abovementioned irregular repeaters (the fluid and goblin logic ones) can be used to run a clock, designs that generate perfect clock signals have been known for a while.

This mechanical-fluid hybrid repeater was the first proposed device to produce completely regular signals, at a frequency determined by the speed of pressure plate recovery. The basic design consists of 4 screw pumps and 4 pressure plates but other versions are possible, depending on the number of separate steps you need.

\

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| L | e | v | e | l |   | │ | L | e | v | e | l |   | │ | L | e | v | e | l |   |
| 0 |   |   |   |   |   | │ | - | 1 |   |   |   |   | │ | - | 2 |   |   |   |   |
| ─ | ─ | ─ | ─ | ─ | ─ | ┼ | ─ | ─ | ─ | ─ | ─ | ─ | ┼ | ─ | ─ | ─ | ─ | ─ | ─ |
|   |   |   |   |   |   | │ |   |   |   |   |   |   | │ |   |   |   |   |   |   |
|   |   | ☼ |   |   |   | │ |   |   | ÷ | ÷ |   |   | │ |   | ^ |   |   | ^ |   |
|   | ☼ | ☼ | ☼ | ═ | ═ | │ |   | ÷ |   |   | ÷ |   | │ |   |   |   |   |   |   |
|   |   |   | ☼ | ☼ |   | │ |   | ÷ |   |   | ÷ |   | │ |   |   |   |   |   |   |
|   |   |   | ☼ |   |   | │ |   |   | ÷ | ÷ |   |   | │ |   | ^ |   |   | ^ |   |
|   |   |   |   |   |   | │ |   |   |   |   |   |   | │ |   |   |   |   |   |   |

÷÷ is a screw pump which pumps from the light side to the dark side. ^ is a pressure plate which disengages gear ☼ when water of depth 1-7 lands on it. The red, green, blue, and yellow pressure plates and gears are color coded only to show which is linked to which. In the game they'll all look like ^ and ☼. Building a pump after the gear which powers it or a gear after the pressure plate which disengages it will introduce a 1-step delay; so, depending on build order, the repeater might have a period between 400 and 408 steps. If the pumps, gears, and pressure plates are built in that order, then this system will repeat every 400 steps, exactly. Start the repeater by using a pond zone to dump 2 buckets of water onto any one of the plates.

The device as depicted uses 47-62 power during operation, and requires 62 power for startup. Drive train to power may, of course, lead to higher requirements. Once the two units of water are introduced to the system, water is conserved perfectly.

See User:MrFake/NStepCyclicRepeater for generalizable n-step clock generator instructions.

User:Hash/SelfPoweredHaltableRepeater demonstrates clock generation with integrated water reactor.

Forum thread has more description and explanations.

DFMA movie shows the action of pump-based clock generation.

### Delay

Clock generation is closely related to the concept of delay: making a signal reach a target a certain amount of time after it is created. Any non-mechanical circuit introduces delay in a signal-- the simplest form of delay is an identity gate. The clock signal generator described above is remarkable for introducing a consistent delay. Any consistent delay can be used for clock generation. Before the introduction of minecarts, there were three known consistent intervals in *Dwarf Fortress* with which to fashion a clock signal generator: the reset delay associated with a pressure plate sending a *close* signal; the rate with which a creature falls; and the amount of time that a screw pump will continue to pump after losing power.
