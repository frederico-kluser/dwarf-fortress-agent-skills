# Computing

> Fonte: [Computing](https://dwarffortresswiki.org/index.php/Computing) — Dwarf Fortress Wiki (GFDL/MIT)

Computing in *Dwarf Fortress* is the practice of setting up complex constructions to perform logical operations and calculations; ideally, to control some functionality of your fortress. Even if it isn't a young concept anymore, there is still much room for improvement and development. One reason is that there are many ways to solve one problem. Innovation and invention are encouraged.

### Binary information

Binary information can have one of two possible states: true or false, respectively 1 or 0. In dwarf fortress they can be represented by different entities:

- on/off state or signal of a trigger (pressure plate or lever)
- power or connection state of a machine component
- open or closed state of a door or similar buildings
- low/high or flowing/standing fluid
- present creatures and borgs
- present minecarts on track

Electronic devices and computers are based on this elementary form of information, and if you want to go into computing, you’ll have to familiarize yourself with it: propositional calculus

### Input/Output

Input can be any device which can be linked to another device with mechanisms, such as levers or pressure plates. Pressure plates can measure water or magma depth, or creature or minecart weight, and can be set to react to your own dwarves if measuring creature weight. If measuring water or magma you specify the minimum and maximum levels at which it should output 'on', and at all other levels it will output an 'off' signal. Regardless of the actual amount of water or magma or the exact weight of a creature or cart on your pressure plate, the plate can only output an 'on' or 'off' signal (1 or 0) to whatever devices it is linked to. So everything you build will have a binary base.

#### Input elements

- manual: lever -\> binary on/off signal
- triggered: pressure plate -\> binary on/off signal

According to input, output can be anything that is able to react to an on/off signal. This can be doors, bridges, floodgates allowing or stopping flow, gears controlling pumps and much more. In some special configurations - when mechanical logic is involved - output may not be an on/off signal but power, thus running or not running a machine component.

Currently, to convert from power to an on/off signal, the only way is to use a kind of power to signal converter. This can be a screw pump connected to that power source, and a pressure plate to measure whether water is being pumped, or a minecart moved by a roller over a closed track with a pressure plate activated by its passage.

#### Output elements

- signal: pressure plate -\> binary on/off signal -\> linkable Object(s)
- power: gear assembly -\> binary power on/power off -\> machine

### Binary logic

Basic binary logic takes one or two input bits and creates an output based on them. The devices that perform these operations are commonly called **logic gates**.

- NOT - takes one input and returns the opposite of the input

| input A | NOT |
|---------|-----|
| 0       | 1   |
| 1       | 0   |

- AND - takes two inputs and returns true if both inputs are true
- OR - takes two inputs and returns true if at least one input is true
- XOR - takes two inputs and returns true if exactly one input is true
- NAND - takes two inputs and returns true if either input is false
- NOR - takes two inputs and returns true if both inputs are false
- XNOR - takes two inputs and returns true if both inputs are identical

| input A | input B | AND | OR  | XOR | NAND | NOR | NXOR |
|---------|---------|-----|-----|-----|------|-----|------|
| 0       | 0       | 0   | 0   | 0   | 1    | 1   | 1    |
| 0       | 1       | 0   | 1   | 1   | 1    | 0   | 0    |
| 1       | 0       | 0   | 1   | 1   | 1    | 0   | 0    |
| 1       | 1       | 1   | 1   | 0   | 0    | 0   | 1    |

The most human-understandable logic system requires NOT, AND and OR gates, but having a design for either a NAND or a NOR gate is enough to build any of the other gates. Some gates are easier to create or need fewer components than others depending on what discipline your logic relies on. Designing each individual gate that you will need (or using designs that had each individual gate designed) rather than building a gate out of multiple NAND gates or the like will generally result in your dorfputer reacting faster and using less resources (power, water, kittens, construction materials, what-have-you).

### Complex gates

- Latch - storing and reading a single binary value
- Repeater - sending a repeating signal
- Counter/Adder "Counter/Adder") - binary calculation

## Disciplines

There are four main disciplines of dwarfputing, depending on what would drive the dwarfputer. Each of them has its assets and drawbacks.

The four disciplines are:

### Fluid logic

Fluid logic is controlling the *flow of fluid* over different pressure plates. Fluid logic can be easily constructed and every known logic gate in dwarf fortress has already been built with it. On the other hand, this discipline depends on a somehow unlimited source of the used fluid to deal with its evaporation and destruction.

### Mechanical logic

Mechanical logic uses systems of axles and gear assemblies to build logical gates. Mechanical logic reacts very fast and can be easily constructed. Since every gear can itself be linked to a trigger (or multiple triggers), and automatically connects to adjacent gears for transferring either power or load, mechanical logic gates are very flexible and don't require anywhere near the number of different devices that tend to be used in fluid logic gates. On the negative side, this discipline uses a LOT of mechanical power and basic mechanic gates output no signals but power. If you need a signal as output, either to control signal-operated buildings like doors or bridges or to perform further logical operations, you will need power-\>signal converters. There is, however, a fully functional fluid-preserving "rotation sensor" design. With the advent of Minecarts, compact fluid-less power-\>signal converters have become available, making Minecart logic an attractive alternative for deploying mechanical logic in your fortress. Along with advanced techniques to construct logic gates by "pre-toggling" a gear assembly (see Pre-Toggled Mechanical Logic), any logical circuit can be built, given enough space in the game to do it.

### Creature logic

Creature logic uses pressure plates and constraints on creatures' movement through buildings such as doors and hatches, in conjunction with their pathing behavior, to build logic gates. Creature logic is very space intensive, but requires no power, fluid, or valuable materials. Every kind of logical circuit can be built with creature logic.

Animal logic is a special kind of creature logic that relies on animals attempting to path through tightly closed doors. Animal logic circuits can be much more space-efficient than other forms of creature logic, but are somewhat unreliable.

### Minecart logic

Minecart logic involves the control of the paths of minecarts over pressure plates to build logical gates. Minecart logic integrates easily with mechanical logic. Power, perhaps surprisingly, is optional. Minecart logic is complete and compact. It lacks the brute speed of which mechanical circuits are capable, but minecart circuit design may be much simpler and more intuitive to some architects.

### Examples of things you could do with logic gates

- Repeater: Repeatedly toggling hatches open and closed, or spikes up and down.
- Latch: Making resettable one-use pressure plates which are reset by a lever.
- NOT gate: Reversing the effect of a switch or creature-sensing pressure plate, generally linked to a latch device.
- AND gate: Requiring more than one condition to be true for something to occur. For instance, you could have a group of AND gates, with a system on/off switch, and other triggers, with each trigger linked to a different AND gate with the system on/off switch linked to the second input on all the AND gates, so that when the system on/off switch is OFF the output will be OFF on all the AND gates.
- OR gate: You could link two 1-7 water sensors to an OR gate, and link that to a NOT gate, and link that to some floodgates or doors which act as emergency bulkheads, closing when water is detected in the area. Or, link the OR gate to bridges which raise instead (but you may crush things, and bridges are slower than doors).
- XOR gate: You could use pressure plates hooked to latches at different points in your fort to detect enemy intrusion, and set them up to seal off the area with both an interior and exterior bulkhead when the intrusion occurs, but hook your latches up with an XOR gate and hook the output to the interior bulkhead to unseal that one if your pressure plates have detected that the enemy has gotten past it.
- NOR gate: A NOR gate returns TRUE (ON) only if both inputs are FALSE. Instead of using the OR gate example with a NOT gate, you could use a NOR gate linked to two 1-7 water sensors, whose output goes to doors or floodgates. When the pressure plates are both waterless, the floodgates will be open. When one detects water, the floodgates close. (If you used 0-0 pressure plates with an OR, you would get an OFF signal if both plates detected water, or an ON signal otherwise (which is the same as 1-7 NAND 1-7))
- NAND gate: A NAND gate returns TRUE (ON) whenever both inputs are not both TRUE (e.g. ON NAND ON is OFF, but every other combination is ON). Instead of the OR NOT or NOR example, you could link two 0-0 water sensors to a NAND gate, and link the NAND gate's output to raising bridges. 0-0 NAND 0-0 is the same as 1-7 OR 1-7. If there is no water on both pressure plates, the NAND gate will output an OFF signal. If, however, either has water, it will output an ON signal.

- And here's a more complicated example, omitting the details of what gates to use: An automated swimming training room, where you pull a lever to close exit doors and open hatches to drop water into it, then pressure plates detect when there's enough water and close the hatches, and after a certain amount of time (using a very slow repeater, for instance), drains and exit doors open and the system resets until you pull the lever again. Or, the lever could be taken out entirely and the system could be made fully automatic (with dwarves set to train in the room, for instance) using the repeater.

## Examples

There are a few examples of a really useful dwarfputer and some concepts which have the potential to become useful for others. But in most cases, they are made just for fun. That's not to diminish their designers' achievements, because these are in general the more complex ones. At the moment there are no known examples of animal or borg logic.

### Useful

- Magma trap
  - This is an example of a useful dwarfputer controlling a magma trap. It automatically floods an area with lava, cleans up and resets afterwards. The timing is perfectly adjusted to let the victims vanish only leaving their valuable metal behind
    - video:
    - design:

### Concepts

- repeater
  - mechanical logic
- adding machine
  - mechanical logic, 6-bit:
  - fluid logic, 8-bit:

### Such a doddle

- decimal display for 4-bit binary input
  - mechanical logic, decimal with overflow-bit:
  - probably fluid logic:
  - fluid logic, hexadecimal:
- tic tac toe
  - mechanical logic
- Armok Invaders
  - mechanical & minecart logic:

## Related user pages

- User:BaronW - The Almighty Dwarven Calculator and Armok Invaders
- User:Jong/Dwarven_Computer - The first fully programmable digital Dwarven Computer
- User:SL/Logic Gates - These use mechanisms for connecting gates and devices and so forth, but fluid for logic. They're built on top of a body of water, and require power (for a pump or two per gate).
- User:Kyace/Adder - A full adder built using fluid logic, with a video of a rough prototype. Trivial to combine 8 of these to make a fluid device capable of adding two 8 bit numbers together.
- User:Soundandfury#Logic_Gates - These have a water supply reservoir above and a drain below. The drained water can be pumped back into the supply reservoir.
- User:Bidok - Animal logic with all gates, memory, repeater and counter. All powered by kittens.
- User:LordOOTFD#Animal_Logic - Animal logic with fast complex gates, building upon Bidok's kitten-powered systems.
- User:Hussell#Assorted_Devices - Fluid logic
- User:Gammon - Fluid logic. Very detailed CMOS gates.
- User:Root Infinity - Misc. logic gates.
- User:Vasiln/Goblin Logic 1 - Theory and practice of invader-based creature logic.
- User:Larix - Various engineering projects, including the second fully programmable Dwarven Computer (arguably the first capable of autonomous execution) and a thorough treatment of logic based on moving minecarts.
- User:Gnidan - Minecart routing system, to move goods point-to-point using shared track
