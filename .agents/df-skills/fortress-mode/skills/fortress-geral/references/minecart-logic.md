# Minecart logic

> Fonte: [Minecart logic](https://dwarffortresswiki.org/index.php/Minecart_logic) — Dwarf Fortress Wiki (GFDL/MIT)

The addition of minecarts to Dwarf Fortress has opened up new and exciting logic and computing options for the ambitious fortress manager. Minecart-based logic gates and memory cells are easy to build, quick to react, and can even be built without power, water, or creatures. The training your doctors will receive is just one of many reasons to compute with minecarts!

## Techniques and Circuits

There exist a great number of different techniques by which a minecart can receive input, compute, and deliver output. This article does not aim for a comprehensive list of techniques and circuits; the interested reader is encouraged to investigate further. The following examples were chosen to demonstrate both a variety of techniques and a few commonly used gates.

#### Key

Adequately diagramming minecart logic devices can be difficult; each tile on each z-level might need to display up to four slices (track, ramp, furniture, minecart) that can lay on top of each other. Ramps are displayed on the furniture layer for the sake of simplicity, and some slices may be omitted when unnecessary. Components of each lower slice are displayed on the higher slice when unchanged by new components to give the reader a sense of position. Wall is typically displayed only where it is essential to the operation of the circuit, and drawn only as sequences of pillars to avoid confusion with track. Unengraved floor is sometimes needed for other components, but of course can be smoothed as desired. Track direction is laid out with and ends in a tile with . Minecarts are accelerated by rollers to the east west north or south and decelerated by track stops . Rollers are controlled via gear assemblies, either engaged or disengaged , typically connected to sufficient power . Pressure plates provide output and, in some cases, modulate the circuit itself. Up and down ramps may be necessary to travel z-levels or alter minecart velocity; they may be roofed or covered with empty space in some views. Hatches and retractable bridges are commonly used to control the path of minecarts. Where necessary, clarification can be found in the descriptions of each circuit.

### Power to signal

In this, the simplest of all designs, the output plate sends an **on** signal when the gear assemblies are powered . When power is lost, the minecart settles onto either the northern or southern roller spaces, and the output plate sends an **off** signal.

This device is very general purpose. Left as an exercise for the reader, alternate construction can result in edge detection or in a repeater design.

### Newton's Cradle Memory

TinyPirate's Newton's Cradle memory "memory") cell is notable both for its small footprint and for demonstrating an important principle of minecarts. When the northern gear assembly is briefly engaged, the northern roller becomes powered, launching the northern minecart into the southern minecart . The southern minecart then leaves the output plate and settles on the southern (unpowered) roller. When the southern gear assembly is briefly engaged, the situation reverses: the southern minecart settles on the output plate, knocking the northern minecart onto the northern (unpowered) roller-- as in its original state.

### Continuous roller OR

Veylon's roller OR continuously evaluates two operands via a minecart traveling counter-clockwise using principles of power transmission through single tile rollers. Should either input or be engaged, power is transmitted to the southernmost, S-\>N roller . Although the minecart is left with diagonal velocity, walls prevent derailment. When neither input is engaged, the minecart continues over the T-junction to the east, missing the output plate .

### Roller switched AND

Larix's roller-switched AND takes advantage of the behavior of rollers to avoid troublesome diagonal velocity. It is potentially confusing both for the counter-intuitive direction of its rollers as well as the way that rollers respond to signals. When the minecart encounters either activated (that is, the last signal received was an **off**) S-\>N roller or , its velocity is completely rewritten and reversed, sending it onto the alternate (clockwise) path. Should neither roller be activated (that is, the last signal received by both was an **on**), the track bends will be ignored and the minecart will travel directly south, over the output plate .

### Resetting bridge-derailment AND

Walls to the east of the gate are for preventing derailment of minecart.

When both the yellow hatch and the green retractable bridge are open, minecarts on this circuit make a continuous loop, triggering the output plate . If either is closed, the plate is never activated. If the bridge is closed, the minecart derails to the southern path, avoiding the plate. If the hatch is closed, the minecart is unable to drop into the northwest ramp, and so sits on the upper, northwestern tile until the hatch opens.

There are many concerns when using a gate like this. Minecarts can be flung when a bridge changes state underneath them (if this happens, minecart seem to gain speed at random direction which can derail or slow down or even stop the minecart), and unfortunately, hatch covers cannot provide the same derailment effect on flat track. Additionally, because your minecart never evaluates both operands at exactly the same moment, it's possible for this gate to output when neither operand is actually true (i.e., last received an **on** signal) at the same moment (it's usually not a very big trouble though, as the delay between minecart stepping on hatch and bridge is around 8 steps).

It's not always a problem, but this behavior is common to AND gates. Paradoxically, one solution is to moderate your inputs via an extra AND gate; this design shows how that can be done. When a large number of circuits such as that shown are created and the hatches of all of them are linked to a single lever, a quick flick (on and off) of that lever can guarantee that all of your circuits fire at the same time-- that is, that all of your inputs for the next computation change state simultaneously. The minecarts then return to their position atop the hatches, ready for another flick of your clock lever.

Worth noting, as well, is the central eastern impulse ramp that allows the minecart to maintain enough velocity to complete this circuit. Impulse ramps like this can be used to make unpowered gates. However, their behavior is unintuitive, and they should only be used with extreme caution.

### MPL NOT

Larix's powerless logic gates avoid the reliability and latency issues that plague many minecart designs through the use of paired impulse ramps and hatches that control not just path, but direction of movement. A minecart traveling the pictured circuit while the input hatch is open will settle into a counter-clockwise path, regardless of the direction of its initial velocity. Yet when the hatch becomes closed, the minecart cannot travel counter-clockwise, but instead is accelerated in the clockwise direction, onto the output plate . It will then oscillate between the far east and far west ramps until the hatch is opened, at which point it will resume counter-clockwise motion.

Use of ramps with high-velocity minecarts may necessitate ceilings as demonstrated on z+2. The exact nature of the ceiling (floor, wall) is unimportant. Some diagrammed walls are unnecessary for the design and are drawn to help the reader in orientation.

### Other techniques and gates

Any logic gate can be made with a combination of those shown. NAND, for instance, is NOT AND; XOR is OR AND (NOT AND). Clocks and edge detection are suggested and proven designs exist, if not on this page. But the examples above were chosen for the disparate techniques they demonstrate. The interested reader is encouraged to further research, or the design of his or her own gates.

Doors can be used to block the travel of a minecart through a circuit, or to prevent derailment, although for reliability's sake, care needs to be taken that the door cannot change state while the minecart is in motion, or it may jam on top of the minecart. Floodgates won't jam in this fashion, although they do introduce some latency. Minecarts of multiple weights, with pressure plates that trigger only on the weight of one, may be used in certain designs; Bloodbeard's fantastically tiny load-adjusted memory cell is a good example. Rollers can be used perpendicularly to a track to derail a cart and impart diagonal velocity. Switchable track stops can prevent or permit derailment. The possibilities are far from exhausted-- and that's assuming one is only interested in *practical* techniques.

## Integration with other disciplines

There's no reason minecart logic needs to be used in isolation. Combining it with other logical disciplines allows one to use each where it is strong, and avoid each where it is weak.

### Mechanical logic

This is the most obvious choice. Mechanical logic offers the potential for incredible speed, yet requires a medium to generate useful signals or to create delay (hence, to create repeaters), and it's hard to use gear assemblies as memory cells. Minecart logic excels at precisely these tasks. Minecart-based power-to-signal and memory are tiny and fast. Minecart-based delay is precisely tunable. The superiority of minecart logic has made water obsolete for these purposes.

### Creature logic

Minecart logic, particularly Larix's powerless MPL logic, has replaced creature logic as the logic-of-last-resort (for when power and fluid are unavailable) or first-resort (for when computation is desired before power can be set up or fluid accessed). However, for the borg logic hobbyist, integration with minecarts suggests interesting possibilities. It is difficult to imagine a simpler clock than a minecart with a "push always after x days" condition, and guided minecarts offer unprecedented control over the path of dwarves.

### Fluid logic

Minecart logic outperforms fluid logic sufficiently to have mostly replaced it. However, the problem of automated fluid delivery may be best solved through some fluid logic techniques, and may suggest some stupid dwarf tricks for those that want to use the fluid capacity of minecarts to compute.

## See Also

- BloodBeard's Minecart Dwarfputing Ideas thread.
- TinyPirate's Minecart Logic 101 instructional video.
- Powerless logic based on hatch-switched minecarts. Logic gates built under this design doctrine.
