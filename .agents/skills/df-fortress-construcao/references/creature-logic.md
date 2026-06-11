# Creature logic

> Fonte: [Creature logic](https://dwarffortresswiki.org/index.php/Creature_logic) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

!!UNKNOWN!!  · xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Creature logic** is a form of dwarven computing that functions by taking advantage of a creature's natural path-finding goals to trigger pressure plates. Creature logic is complete-- you can build memory, repeaters, or any sort of logical circuit.

## Creature logic vs other disciplines

Pros:

- Creature logic requires no fluid or wind. In dry, windless environments, circuits are limited to creature logic or minecart logic.
- Similarly, creature logic requires no infrastructure-- you can build your circuits anywhere, without worrying about bringing water or power from one end of your map to the other.
- All creature logic circuits can be designed with only stone and a pick-- although you're free to use wood or metal if you prefer!
- Creature logic doesn't need anything but creatures to send or receive signals. There's no need to translate signals as with mechanical logic.
- Creature logic can be very intuitive. Watching creatures physically travel through your logic pathways simplifies debugging.
- It's fun to watch the creatures run around!

Cons:

- Reliable creature logic requires a ridiculous number of hatches, doors, and mechanisms-- not to mention connections between pressure plates.
- Creature logic requires creatures-- sometimes, a great number of them. Sometimes, those creatures die or have babies. Sometimes, they interrupt your dwarves. Sometimes, your dwarves fill them full of crossbow bolts (*which would be a particular kind of death, per se*).
- Creature logic is vulnerable (surprise) to the presence of unexpected creatures in the logic circuits. Because creature logic circuits require a path either to the map edge, or to the meeting hall (in most cases), this is a real possibility.
- Creature logic requires large amounts of space.

## Free range or one path

There are two incompatible design philosophies associated with creature logic-- mostly, the creatures you use will determine which is appropriate.

Free range creature logic generally gives a path to creatures when certain criteria are met, and otherwise, lets them wander (in a constrained space). This simplifies design and permits constant evaluation of criteria, but any creature that paces in captivity can easily foul up your circuits-- for instance, a pacing creature may prevent a door from closing, causing an AND to evaluate as true even though both operands were never true at the same time. Additionally, it gives no clear indication that an evaluation has been completed-- if you want to evaluate your AND statement, you only ever know that it's been evaluated as true, never as false.

One path design constrains creatures to a single tile when they have no path available. Whenever the creature is permitted movement for evaluation of operands, the creature is guaranteed one and only one path. This requires explicit designation of 'else' paths, and requires that operands be evaluated at specific times rather than undergoing constant evaluation, but guarantees complete reliability, and allows the circuit to return both 'true' and 'false' evaluations, meaning that you can know for sure that a signal has been evaluated, rather than guessing if the creature has had sufficient time to path or not path.

## Animal logic

Animal logic relies on a special case of free range creature logic that is specific to animals that are unable to open doors, by pathing them through tightly closed doors. Animal logic can be very space efficient and easy to build in comparison to most kinds of creature logic, but is somewhat unreliable.

## Gates

Creature logic relies on the ability or inability of a creature to path through a specific area. "One path" design requires explicit 'else' arms. Because of that, the following logic gates are shown in complementary pairs to guarantee a path to the creature.

All of these gates can be easily altered to take more than two operands.

#### Key

In all of the following diagrams, the creature is assumed to start at s (if given). p means that the square contains a path to the creature's pathing goal. Doors ┼ and hatches ¢ are displayed in the same color as the pressure plate ^ that links to them. If no pressure plate exists for a color, furniture of that color is opened or closed from outside of the circuit pictured; if a hatch and a door are the same color, that means they receive signals from the same source. Output pressure plates are displayed in magenta ^, as is any furniture in the circuit that is linked with the output plate. In the rare case that part of a circuit is linked with multiple elements, it will be displayed with foreground and background colors and explained in text-- for instance, ^ is linked both to cyan furniture and output.

### Identity with NOT gate

|     |     |     |     |     |     |
|-----|-----|-----|-----|-----|-----|
|     | ╔   | ═   | ═   | ╗   |     |
| ═   | ╝   | ┼   | ^   | ╚   | ═   |
| s   | \+  | O   | O   | \+  | p   |
| ═   | ╗   | ¢   | \+  | ╔   | ═   |
|     | ╚   | ═   | ═   | ╝   |     |

This function takes a single operand. If the operand is true, the creature travels through the upper path (identity); otherwise, the creature takes the lower path (NOT). The pressure plate signals when the operand is true. This gate is the basis of all to follow.

Identity is also a simple delay. When the path receives a signal, it propagates it after a short period. That period depends on the speed of the creature moving through the gate.

### AND gate with NAND gate

|     |     |     |     |     |     |     |
|-----|-----|-----|-----|-----|-----|-----|
|     | ╔   | ═   | ═   | ═   | ╗   |     |
| ═   | ╝   | ┼   | ┼   | ^   | ╚   | ═   |
| s   | \+  | O   | ═   | O   | \+  | p   |
| ═   | ╗   | \+  | ¢   | \+  | ╔   | ═   |
|     | ╚   | ╗   | ¢   | ╔   | ╝   |     |
|     |     | ╚   | ═   | ╝   |     |     |

The doors at the top are both open if both operands are true (AND); the hatches at the bottom permit path if either operand is false (NAND). The pressure plate will signal when both operands are true.

### NOR gate with OR gate

|     |     |     |     |     |     |     |
|-----|-----|-----|-----|-----|-----|-----|
|     | ╔   | ═   | ═   | ═   | ╗   |     |
| ═   | ╝   | ¢   | ¢   | ^   | ╚   | ═   |
| s   | \+  | O   | ═   | O   | \+  | p   |
| ═   | ╗   | \+  | ┼   | \+  | ╔   | ═   |
|     | ╚   | ╗   | ┼   | ╔   | ╝   |     |
|     |     | ╚   | ═   | ╝   |     |     |

The hatches at the top permit path only if neither operand is true (NOR); the doors at the bottom permit path if either operand is true (OR). The pressure plate will signal when neither operand is true.

### XOR gate with expanded XNOR gate

|     |     |     |     |     |     |     |     |     |
|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|     |     | ╔   | ═   | ╦   | ═   | ╗   |     |     |
|     | ╔   | ╝   | ┼   | O   | ¢   | ╚   | ╗   |     |
| ═   | ╝   | \+  | ┼   | \+  | ¢   | ^   | ╚   | ═   |
| s   | \+  | O   | ═   | ═   | ═   | O   | \+  | p   |
| ═   | ╗   | \+  | ┼   | ┼   | \+  | \+  | ╔   | ═   |
|     | ║   | \+  | O   | O   | \+  | ╔   | ╝   |     |
|     | ╚   | ╗   | ¢   | ¢   | ╔   | ╝   |     |     |
|     |     | ╚   | ═   | ═   | ╝   |     |     |     |

\
As XOR is the intersection of OR and NAND, it is simply an OR followed by a NAND. The XNOR, as the union of AND and NOR, requires two arms. Each operand is linked to one door and one hatch in the XOR path, and to one door and one hatch in the XNOR path. The pressure plate will signal when either operand is true but not both are true. When modifying the XOR to take more than two operands, be careful to leave space between the doors and hatches as shown; this space is unnecessary for evaluation of two operands. Similarly, the expanded XNOR is appropriate when dealing with more than two operands, but a condensed version for taking only two operands exists.

### Multiple use

The gates above are single use gates; the creatures will escape after pathing through each gate. Circuits which return the creature to the beginning of the path are possible via altering the path in-route.

|     |     |     |     |     |
|-----|-----|-----|-----|-----|
|     |     | ║   | p   | ║   |
| ═   | ═   | ╝   | ¢   | ║   |
| s   | ¢   | ^   | O   | ╣   |
| ═   | ═   | ╗   | ┼   | ║   |
|     |     | ║   | p   | ║   |

This is one such device for re-routing creatures mid-path. Upon stepping on the pressure plate, the creature opens two hatches, thus blocking retrograde motion as well as access to its pathing goal, and opens a door, giving access to a new pathing goal. This new pathing goal can lead back to the original position of the creature. This principle is demonstrated in the designs to follow. Because the creature is constrained on the pressure plate, the door can be opened by outside mechanisms rather than being linked to the pressure plate, permitting controlled movement of a creature through one or more arms of a circuit.

### Reversibility

The reader may have noticed the near symmetry of the preceding gates. However, the output works as well when placed before the path-limiting furniture as after! While it's easier to visualize the effects of these circuits when displayed as above, it is often more effective to use a reversed design. When a single creature is used to traverse a large, compound circuit, reverse design can lead to reduced latency. A clever logician might wonder, "But if they can evaluate the signal before traversing the path, why traverse the path at all?" Consider the following XOR/XNOR gate, redesigned both for reuse and reversed operation:

|     |     |     |     |     |     |     |     |     |     |     |     |
|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|     |     |     |     |     | ╔   | ═   | ╦   | ═   | ╗   |     |     |
|     |     |     |     | ╔   | ╝   | ¢   | O   | ┼   | ╚   | ╗   |     |
| ═   | ═   | ═   | ═   | ╝   | ^   | ¢   | \+  | ┼   | \+  | ╚   | ═   |
| p   | ┼   | ¢   | ^   | ¢   | O   | ═   | ═   | ═   | O   | \+  | p   |
| ═   | ═   | ═   | ═   | ╗   | ^   | ¢   | ¢   | \+  | \+  | ╔   | ═   |
|     |     |     |     | ║   | ¢   | O   | O   | \+  | ╔   | ╝   |     |
|     |     |     |     | ╚   | ╗   | ┼   | ┼   | ╔   | ╝   |     |     |
|     |     |     |     |     | ╚   | ═   | ═   | ╝   |     |     |     |

A creature waits at the start point, atop the cyan hatch, until evaluation is triggered by an **off** signal to the cyan hatches (typically following a redundant **on** signal). The creature, suddenly granted path to its goal, races toward either XOR or XNOR, but evaluation occurs earlier than in previous designs. Its original path is blocked upon evaluation and the creature is rerouted back to its start point. (Note that while the creature is reset in this design, furniture is not necessarily reset. Some circuits may require additional furniture to control path without altering operands.)

Whereas the creature needed to travel 8 tiles for evaluation in the previous design, this allows evaluation in 2 tiles, and the refractory period-- the time during which the circuit cannot be used to evaluate another operand-- is improved to an even larger extent.

## Creature memory

|     |     |     |     |     |     |     |     |
|-----|-----|-----|-----|-----|-----|-----|-----|
|     |     |     | ╔   | ═   | ╗   |     |     |
| ═   | ═   | ═   | ╝   | ┼   | ╚   | ═   | ═   |
| p   | ¢   | ^   | ¢   | ¢   | ^   | ¢   | p   |
| ═   | ═   | ╗   | ┼   | ╔   | ═   | ═   | ═   |
|     |     | ╚   | ═   | ╝   |     |     |     |

This is a low latency version (not the simplest version, not the most full-featured) of creature-based memory. Each pressure plate is linked to each adjacent hatch. Memory is set by sending an open (followed closely by a close) to either door.

Note that in this diagram, both ends need to lead to the pathing goal. The creature can enter by either side, but will be constrained to either pressure plate during normal operation.

## Clock generation, repeaters, and delay

A high resolution borg-logic clock or delay can be designed around the rate with which creatures fall. A simpler, low resolution clock can be designed based around the military scheduling menu or minecart routes.

The memory design above, slightly modified, can make a decent (not perfectly regular) repeater.

|     |     |     |     |     |     |     |     |
|-----|-----|-----|-----|-----|-----|-----|-----|
|     |     |     | ╔   | ═   | ╗   |     |     |
| ═   | ═   | ═   | ╝   | ¢   | ╚   | ═   | ═   |
| p   | ¢   | ^   | ¢   | ¢   | ^   | ¢   | p   |
| ═   | ═   | ╗   | ¢   | ╔   | ═   | ═   | ═   |
|     |     | ╚   | ═   | ╝   |     |     |     |

Here, each pressure plate is linked to the two orthogonally adjacent hatches. The southern hatch is linked to the eastern pressure plate, while the northern hatch is linked to western pressure plate. This repeater tends to fire about every 250 ticks, with open and close signals offset by about 125 ticks, when built as shown. It's very effective at rapidly triggering any device with a refractory period of 100. Similar, non-repeating systems can be used to institute delay.

Linking both pressure plates to output doubles its rate, turning it into very effective spike repeater. The period can be increased by introducing floor space into the center of the design.

## Edge Detection

|     |     |     |     |     |     |     |     |     |
|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| ║   | p   | ║   |     |     |     | ║   | p   | ║   |
| ║   | ¢   | ╚   | ═   | ═   | ═   | ╝   | ¢   | ║   |
| ╠   | O   | ^   | ┼   | ^   | ¢   | ^   | O   | ╣   |
| ║   | ¢   | O   | ═   | ═   | ═   | O   | ¢   | ║   |
| ╚   | ╗   | \+  | \+  | ^   | \+  | \+  | ╔   | ╝   |
|     | ╚   | ═   | ═   | ═   | ═   | ═   | ╝   |     |

North of the circuit is the pathing goal. The eastern and western pressure plates are linked to adjacent hatches. Input is linked to the hatch southeast of the eastern pressure plate and to the door. The central and southern pressure plates are linked to output. This circuit generates both an open and a close every time it is sent an open or a close signal from input -- that is, it generates two properly-ordered signals for every properly-ordered signal it is sent, allowing for *edge triggered* logic. Either output pressure plate can be removed to send an open and a close only upon receiving one kind of signal or the other kind of signal. Output can linked to the same device or to two different devices.

Note that the memory design forms a sort of inverse of this circuit, in that a single open-close cycle is translated into a single on or off signal.

## Alternative design

Multiple choices of furniture are available for the doors or hatches in the above diagrams. Various reasons exist for substitution.

#### Doorless design

Of all alternative designs, doorless design is the most practical. All doors are replaced with hatches over stairs or ramps, and the path continues one z-level down or up. This makes it more difficult to visualize the circuit, and some very efficient designs may require more significant changes, but every circuit possible can be created without doors. Use of hatches instead of doors protects against the effects of doors being blocked open by unexpected creatures or objects-- the original bug, after all, took the form of vermin remains. Retracting bridges can be used the same way, but lead to problematic delays.

#### Hatchless design

Hatchless design is much more difficult and of very limited use. Signal inversion can make a door act like a hatch; a raising bridge acts like a hatch. Both of these institute delays in processing that require large expansion of logic circuits and limit the effectiveness of memory, but they may be necessary when using submerged logic or flyers-- bragging rights for a logic system submerged in magma that processes via fire imps may be worth the headache.

#### Bridge design

Bridge design uses bridges instead of both doors and hatches. Doors are replaced with retracting bridges over ramps or staircases; hatches are replaced with raising bridges, or with retracting bridges over channels. Bridge design causes frustrating delays, but it is the only way to use building destroyers in a logic circuit. The irony of making your minotaur run an impossible labyrinth may be worth the design headache. As an added bonus, bridges are nearly unobstructable-- offensive vermin remains in your logic circuits will be smashed from this plane.

## Creature choice

Multiple choices exist for creatures to run logic circuits. Each has its own advantages and disadvantages.

#### Domestic animals

Domestic animals are valid choices for creature logic, but come with a host of disadvantages. Many females are capable of giving birth inside of your logic gates; their children can block the closing of doors or set off pressure plates. Grazers, of course, will starve inside most logic circuits, although some special designs may be capable of supporting a grazer. Some domestics are too small to set off pressure plates; some are capable of flight, requiring hatchless design. All unmodded domestic animals will die of old age, requiring periodic replacement. Most domestic animals have relatively short lifespans. Logic involving domestic animals must be built with pressure plates that can be triggered by citizens, and building these circuits may turn into a nightmare of job cancellations and stranded, starving dwarves. Domestic animals have one huge advantage, however: the location of their pathing goal can be altered with direct, unmediated action of the player, by placement of a meeting zone.

#### Invaders

Invaders are readily available on most maps, rarely or never give birth, and require no sustenance. Pressure plates don't need to be built triggerable by citizens. Elves and goblins will never die of old age. However, invaders cause their own problems. Invaders can cause job cancellations, and in some circuits may escape, wreaking havoc deep in your fortress. Dwarves armed with bolts and crossbows will take potshots at your computers periodically. Finally, invader-based logic must have a path to the map edge for predictable pathing. If your logic circuit is inside of your fortress, walling off, even through something as simple as raising a bridge at your entrance, will lead to unpredictable pathing.

#### Dwarves

Dwarves themselves can be used to run logic circuits, and are perhaps the most interesting choice; logic designs involving dwarves are generally referred to as borg logic. While longer-lived than most domestics, dwarves starve and dehydrate easily, requiring frequent, careful maintenance. Idle dwarves path unpredictably, and dwarves are vulnerable to drowsiness, leading to very high latency. Married female dwarves are fecund. At the same time, dwarves are excellent choices for logic circuits because of their varied pathing goals that can be altered through direct interaction by the player. Dwarves can trigger events both through the use of pressure plates and through the use of levers, while their pathing goals can be controlled by many means-- most easily and predictably, by military scheduling or minecart routes. In fact, one can see the entire game of Dwarf Fortress as one big logic circuit with dwarves as the driving creature. The more philosophically oriented overseer may wonder what cyclopean, ineffable circuit he or she is traversing through the act of playing Dwarf Fortress....

### Undead

Undead are an intriguing choice for creature logic choices. The absence of attribute rust opens up the possibility for a more consistent repeater. They can be used in fully submerged circuits-- even in magma-submerged systems. In some biomes, they are self-repairing. However, undead path like wildlife, which can make it difficult to set up a circuit for them. Without a clear target, they may not behave predictably. One way to work around this is to build a visible target to which the undead path, by walling the circuit with channels instead of walls, and placing a captured invader in clear line-of-sight of the undead logician.

### Other choices

There are a few things to stay away from, but in general, any sufficiently understood creature can be used for creature logic. Building destroyers are problematic, but full-bridge design is possible. Likewise, flyers and swimmers cause difficulty, but nothing that can't be worked around. Creatures with trapavoid are nearly useless, though gremlins might be able to output via levers; stun-able creatures like kobolds can trigger pressure plates when dropped/stunned; and non-web-immune creatures trigger pressure plates that have been webbed. Creatures with a size less than 10000 are too small to set off pressure plates, thus requiring additional "hardware" (such as a tame creature that "flees" or "charges" over a pressure plate). The essence of creature logic, however, is predictable pathing. This may or may not exclude the use of certain types of wildlife.
