# Fluid logic

> Fonte: [Fluid logic](https://dwarffortresswiki.org/index.php/Fluid_logic) — Dwarf Fortress Wiki (GFDL/MIT)

**Fluid logic** is a form of computing which uses a fluid (generally water), controlled by various means, to trigger pressure plates and hopefully accomplish some desirable result.

## Infinite Flow Gates

These logic gates are relatively simple and cheap to make, but require an infinite amount of flow and infinite drainage to operate. You can build a circuit system to prevent the loss of water, but closing constructions like floodgates will always destroy water, so you'll always have to replace it somehow. The following examples use raising bridges and floodgates, as they have the same delay of 100 steps when reacting to on/off signals. The bridges work as inverted input as they block passage when receiving an on signal while floodgates open in that case. The channel in the gates stands for the drainage.

There are two versions of these gates here.\

**AND**

[TABLE]

An AND gate is simply created by putting two floodgates *in a row*, each one connected to one of the input triggers: . When both floodgates receive an on signal, they will open and let the water from the left side pass. The pressure plate behind the floodgates has to be constructed to react on 4-7 water.

- If you use two 1x1 raising bridges, you'll get a NOR operation instead.
- The output can also be inverted by using a 0-3 pressure plate.
- You can add more floodgates to process more than two signals in the conjunction.
- You can use a 0-3 and a 4-7 pressure plate at the same time to get the result and its inversion at the same time.
- You can use a single floodgate and a 0-3 pressure plate to get a NOT gate.
- You can use a single 1x1 raising bridges and a 4-7 pressure plate to get a NOT gate, too.

**OR**

[TABLE]

An OR gate is simply created by putting two floodgates in *parallel*, each one connected to one of the input triggers: . When one of the floodgates receives an on signal, it will open and let the water from the left side pass. The pressure plate behind the floodgates has to be constructed to react on 4-7 water.

- If you use two 1x1 raising bridges, you'll get a NAND operation instead.
- The output can also be inverted by using a 0-3 pressure plate.
- You can add more floodgates to process more than two signals in the conjunction.
- You can use a 0-3 and a 4-7 pressure plate at the same time to get the result and its inversion at the same time.

**XOR**

[TABLE]

A XOR gate is created by putting 1x1 raising bridges and floodgates together. The red bridge and floodgate are linked to the same input and the green bridge and floodgate are both linked to the other input. When one of the inputs sends an on signal, the bridge will raise/close and the appropriate door will be opened. Only when the floodgate and the bridge at one passage are open, what happens when exactly one input signal is on, the water will flow to the right. The pressure plate behind the bridges has to be constructed to react on 4-7 water.

- If you exchange bridge and floodgate for one of the two inputs, you'll get a XNOR operation instead.
- The output can also be inverted by using a 0-3 pressure plate.
- You can use a 0-3 and a 4-7 pressure plate at the same time to get the result and its inversion at the same time
- Processing more input signals is possible but requires an exponentially increasing number of bridges, floodgates, and mechanisms. It is easier to link the output to another XOR gate.

As mentioned, you can just add more floodgates and bridges and even pressure plates to expand your gates to process more input signals and process more complex operations at once. You can combine floodgates and bridges as you need them. Putting them in a row will connect them as AND. Every time you add a new parallel passage with floodgates and bridges this will work as an OR for each other passage. The XOR gate for example is nothing else than combined logic: A XOR B = (A AND NOT B) OR (NOT A AND B). But sometimes it is easier to use more but simpler gates.

## Fluid Preserving Gates

At the moment there doesn't exist a full concept of a fluid-preserving fluid logic gate. Each design working with floodgates or equivalent components in the gates will have to deal with the destruction of the fluid. A way to handle this can be the usage of hatches. Evaporation is another known problem.

## CMOS Transmission Gate and Inverter Logic

Perhaps the closest to utilizing water as a stand-in for electricity, transmission gate logic can be accomplished by simply having an infinite water source in place of all +Vs, and infinite drainage for all grounds. Simple floodgates behave as standard transmission gates, while bridges are inverted gates. However, unlike the other forms of fluid logic, but as with real world electrical circuits, a dedicated inverter is required, which must be hooked up to +V and ground.

## Advanced Complementary fluid logic Gates

This type of logic uses the different behaviour of raising bridges and floodgates when switched to minimise water consumption and remove the need of a drain. The use of (typically) two buildings for every input, one of which is always open while the other is closed, ensures that only very little water will flow during operation, and only when there is a state change. Thus, this variation of fluid logic is conceptually very similar to real CMOS circuits, which use a similar paradigm to limit power consumption.

### Basic Design

Let's say we want to evaluate the logical expression *f*. It can be a simple **AND** or **OR** gate, or anything more complicated. Follow the following scheme:

[TABLE]

Here, is a set of floodgates and/or drawbridges that let water flow exactly when *f* evaluates to true, is the same except that it lets water flow when *f* evaluates to false, is a pressure plate set to activate on a sufficient water level. Notably, a drain is not needed.

### Examples

In the following examples, is a floodgate, and is a drawbridge. Red ones are connected to input A and green ones to input B.

#### NOT

[TABLE]

The pressure plate must activate on a water level of 5-7. When input turns off, the drawbridge lowers and the floodgate closes. Water can flow onto the pressure plate and fills the tile completely, turning output on.

When input turns on, the bridge raises and cuts off incoming water, while the floodgate opens and the water on the pressure plate's tile spreads over the now two open tiles. Water depth over the pressure plate lowers to 3-4, insufficient to keep the pressure plate active, which will turn off.

Siphoning the water off into a drain is unnecessary: the spread of water into opened tiles is sufficient to reliably produce a measurably different liquid level. This holds for all binary logic gates under this doctrine.

#### AND

[TABLE]

#### OR

[TABLE]

For the AND gate, the pressure plate should respond to 6-7 or 7-7 water. Since the OR gate is in effect a NOR gate with inverted output, the plate must respond to "low" water, 0-5 is recommended.

#### XOR

This is not as straightforward as the previous ones. The *true* expression is the following: (A **and not** B) **or** (**not** A **and** B). The *false* expression: (A **and** B) **or** (**not** A **and not** B).

So the gates look like the following:

[TABLE]

If both inputs have the same value (both on or off), the two closed floodgates or raised bridges will form an impassable wall, blocking inflow of water. The second row of floodgates "behind" the pressure plate ensures that when the gate is deactivated by an "on" signal raising bridges, there is still space opened for water to spread into and lower fluid level. Either combination of one "on" with one "off" input opens a direct path for water to enter. The pressure plate must be set to react to 7/7 fluid, anything less can result in false positives.

### Advantages And Disadvantages

The basic advantage of this design is that it uses much less water than infinite flow gates. A river is enough to supply even the more complex systems, as long as sufficient liquid depth is provided. A drain is not needed.

The disadvantage is that it requires more resources to construct, and more careful planning, since floodgates tend to block paths. The presented drain-less gates depend on precise fluid depth and require that all incoming logic fluid is at the full 7/7 depth. This may necessitate building a reservoir or pumping system to compensate for flow irregularities or overcome the sluggishness of otherwise pressureless fluids. That's especially true when you decide to use magma/lava as fluid.

## Speed Improvements

The main factors that affect the speed of these gates are the delays of floodgates and bridges, and the switch-off delay of pressure plates. These cannot be eliminated, although designs that seek to replace as many buildings as possible with doors and hatches may minimize delays.

Another factor is the flowing speed of the water. It can be improved. First, the water should flow in from a reservoir a few z-levels higher than the gates themselves (the more the better). This way, water will flow in much faster. In infinite-flow gates, you can then replace the pressure plates with up stairs, and make a 2x1 room one z-level above. On one tile is a down stair, and on the other is the pressure plate. Now the water will also flow out faster, or at least the pressure plate will switch off sooner. To minimize latency when deactivated, assuming sufficient inflow, the pressure plate can be set to trigger only on a full 7 units of water. This increases the water consumption a bit, but it still remains relatively low.

## Edge Detector

In some situations, it is beneficial to have logic that triggers during a state *transition* rather than based on steady states - for example, turning a lever "on" could trigger one brief event while turning the lever "off" would trigger a different event (or possibly the same event).

[TABLE]

Both pressure plates should trigger on depth 2-6. Link the bottom pressure plate to machines you wish to activate on *positive* transitions (e.g. stepping onto a pressure plate, or pulling a lever) and the upper pressure plate to machines you wish to activate on *negative* transitions (e.g. stepping off of the pressure plate, or pulling the lever again), then link the trigger itself (a lever or pressure plate) to both floodgates and both raising bridges.

Each time the input trigger is toggled, the appropriate pressure plate will activate, remain active until the water finishes flowing, then deactivate after about 100 steps.

An edge detector can be realized very space efficient in advanced complementary fluid logic (as long as both pressure plates are linked to a single item). Input goes to floodgate and bridge, the pressure plates are working on 0-5 and 6-7, respectively.

[TABLE]

## Memory Cells

Fluid logic offers options for comparatively small memory "memory") cells requiring very few mechanisms. They are usually quite primitive, so that more complicated memory manipulation requires additional machinery, but for simply "holding" a bit of information, they are hard to beat in compactness.

#### S/R Latch

[TABLE]

Design by Hussell.

A "set/reset" latch will activate when it receives a "set" signal - opening the door , letting in water and triggering the pressure plate reacting to liquid of levels 5-7 - and stays active when the set signal turns off again. It will only deactivate when it receives an explicit "reset" signal - opening the door behind the plate, allowing water to spread off the plate, lowering liquid depth enough to fall under the activation threshold. Further activity of the reset signal will, once again, not change the cell's state once it has been reset.

As usual in real-world set/reset latches, the inputs should not both be "on" at the same time.

#### D-Latch

[TABLE]

This cell "tests" the state of the "Data" (hence D ) input controlling the door and the pressure plate (set to trigger on 5-7 liquid) will take on that input's state when the "enable" input opens door : if the data input is on, water can pass from the source to the pressure plate and fills the cell. If the data input is off, water will spread from the plate to the door's tile and lower liquid depth over the plate.

This cell will turn "on" whenever both data and enable input are on, but will only turn "off" when the data input is off at the moment the enable input *switches* from off to on, making it a hybrid of a Latch (reacts to changes in data as long as enabled) and a flipflop (only reacts to data state the moment enable changes from off to on). While this is clearly a weakness of the design, it is very compact and uncomplicated, needing a mere four mechanisms to link the doors to the inputs.

#### Toggle Flipflop

[TABLE]

This is a cell which changes state to the opposite whenever its "control" input switches from off to on. The door is activated by the control input, and both the door and the bridge are linked to the pressure plate (triggering on 5-7 water).

The operation is not immediately obvious, thus a breakdown, beginning with the cell in the "off" state:

Water on the plate is 4 or less, the bridge is lowered. When the "clock/control" turns on, the door opens and water rushes onto the plate. The plate triggers and sends "on" signals to both bridge and door. The signal to the door is ignored, since the door's already open. The bridge receives a "raise" signal and reacts to it with a 100 step delay. Neither the bridge raising nor the door closing (when the control turns off again) does anything to the pressure plate's state, it remains "on".

Water on the plate is 5 or more (usually 7), the bridge is raised. When the clock turns on, water spreads from the plate to the door's tile. Water level on the plate falls under the activation threshold. After the normal pressure plate reset delay of 99 steps, "off" signals are sent to the door and the bridge. The door will immediately close, the bridge will lower 100 steps later. The cell is "off" and will remain so until the clock turns on again.
