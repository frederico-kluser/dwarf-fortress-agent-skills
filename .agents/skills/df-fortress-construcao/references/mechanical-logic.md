# Mechanical logic

> Fonte: [Mechanical logic](https://dwarffortresswiki.org/index.php/Mechanical_logic) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

!!UNKNOWN!!  · xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Mechanical logic** is one discipline of computing using mechanical power to perform logical operations. In this case powered or unpowered machine components represent the binary information.

The principles of mechanical logic are simple. Gear assemblies linked to levers or pressure plates will be toggled between disengaged and engaged when they receive an on/off signal. In this manner, you can conditionally attach power supply from windmills or water wheels to specially arranged gears to build logic gates.

## Mechanical logic compared with other logic disciplines

### Advantages

- Mechanical logic is very fast. Gears don't have a reaction delay like many components used by fluid logic. If a gear is toggled the flow of power will change immediately, there will be no added delay introduced by the movement of creatures, fluids or minecarts.
- Mechanical logic is very flexible. Gears can toggle, so inverting signals is easy and you don't have to deal with different machine components.
- Mechanical logic is very reconfigurable. You don't have to deal with creatures or fluid before changing anything.

### Disadvantages

- Mechanical logic needs a substantial amount of wood to create and transmit power.
- Mechanical logic still needs converters to trigger something else than machine components, either by applying minecart logic or by using fluid.
- Mechanical logic needs a substantial amount of mechanisms, particularly if you stick to load based mechanical logic.

## General concepts

There are two general concepts. The older and less popular one is the so-called load-based mechanical logic. The other one is the so-called toggle-based mechanical logic. Note that the two can be integrated, however.

### Load based

Load based mechanical logic uses logic gates with a defined amount of power. They have an additional amount of load in terms of mechanism or other machine components, consuming all of the power if connected. The gates are designed in a way that the load is disconnected while the output is true, and connected while the output is false. Every circuit has to have its own power supply. Compact complex circuits are very difficult to design, because power and load need to be controlled for each circuit, and each gate in a circuit needs to be connected to others it interacts with. However, the advantage is that load-based mechanical logic computes instantly.

### Toggle based

Toggle based mechanical logic works more like fluid logic, not controlling the flow of fluid but the flow of power. It uses the fact that gears don't have a defined state when receiving an on or an off signal, but toggle between connected and disengaged, independent of the type of signal. It normally uses a central power supply. It is quite easy to create very complex gates with multiple output signals such as, for example, a binary to decimal converter. The cost of this ease of use and design, however, is that toggle based circuits need to be converted not just for output, but sometimes also for further processing.

### Example

The first example shows a load based XOR gate. It takes input signals from two different triggers. Its output gear (O) is powered when exactly one of the two input triggers is on and the other one is off. This is done as follows:\
The power will be connected to the gear with the P (from the bottom of the diagram or another z-level). One input is linked to gear 1 the other to gear 2. This way power will flow from P to O if either one of the input signals is off. The power input is linked directly to the load L which must be calibrated precisely so that the power provided can move the output and load and *one* of the input-toggled gears, but not *both*. You can build this on top of a power to signal converter as shown on this page.\
As you can see, this gate is complicated to construct. You will need four gears and four more to connect the input in addition to all the components needed for the converter and the load, and your load assembly will need to be precisely calibrated and can only be used for this circuit. When using a common load (shared with other circuits), the gate would have to be linked to it through two signal-driven gears put in line. This would increase the parts count by two installed and four link gears.

**load based XOR**

|  |
|----|
| █ / █ / █ / █ / █ / █ / █ / █ / \* / 1 / \* / O / █ / █ / █ / L / \* / P / \* / 2 / █ / █ |

\
A toggle based XOR gate looks much simpler:

**toggle based XOR**

|                                                                        |
|------------------------------------------------------------------------|
| █ / █ / █ / █ / █ / █ / █ / █ / █ / \* / █ / █ / █ / █ / █ / █ / █ / █ |

In stark contrast to the load-based XOR, it consists of a single gear. While it requires a power source and an output, it can accept power from an axle and serve as output gear by itself. This is how it works:\
Connect it to your source of power, and link it to one of your input triggers. Build a temporary lever anywhere and connect it, too. Pull the lever once. You can deconstruct the temporary lever now. Now the gear is disengaged, and you link the second input trigger to it. Since gears toggle, every time your trigger changes state and sends a signal the gear will change state. Initially both triggers are off, and the gear is disengaged. When one trigger changes state, it will activate the gear. Independent of which trigger changes next, both will have the same state afterwards, and the gear will be disengaged again. So the gear will transport power when both input triggers are at different state: XOR. You can build this on top of a power to signal converter as shown on this page.\
As you can see, you won't need many mechanisms to build this gate. 1 for the gear, 4 to connect to the input and 1 will be lost after disconnecting the temporary lever (that needs 3 temporarily). And of course you will need all the components for the converter, but no load.\

**toggle based XNOR**

- Use a single gear as for the XOR, but omit the temporary lever step.

**toggle based NOR**

- Multiple gears in series, with one (and only one) input connected to each gear. Any single ON(signal) input will produce an OFF(power) output.
- Can be converted to OR by adding an inverter to the output
- No temporary levers, so it uses fewer mechanisms.

**toggle based AND**

- Same as the NOR except use temporary levers to pre-toggle each input gear. For large logic arrays it is probably best to convert your Boolean equations to NOR logic, as that is the quickest simplest and least expensive (in mechanisms) to implement. With the added benefit that all mechanisms can be recovered from gears.

**toggle based NAND**

- A 3x1 gear assembly for each input. Input goes to the center (signal) gear. Power goes to either one of the other gears (the power gear), output is the other outer gear (output gear). Can be expanded indefinitely by adding additional 3x1 arrays in parallel (i.e. 3x2 for a 2 input, 3x5 for 5 input). The theory is that power is transmitted across all of the power gears (which are all connected to each other in parallel. Any single signal gear which has an OFF state (gear engaged) will allow power through to the output gears. It requires every input gear to be disengaged (ON signal) in order to produce an OFF (unpowered) output.

**toggle based OR**

- Same as the NAND except pre-toggle each signal gear.

## Power to signal converter

When you are dealing with mechanical logic, you'll finally want or have to trigger something else than machine components like doors or bridges (or, with toggle-based mechanical logic, another gear assembly). Currently, there exists no trigger in dwarf fortress that reacts on the working state of machine components, that is, the presence or absence of power. The traditional solution to this was to use a hydromechanical power-to-signal converter, remarkably similar to hydromechanical memory "Memory (computing)").

**Z 0**

|  |
|----|
| █ / █ / █ / █ / █ / █ / █ / · / ÷ / ÷ / ► / ► / · / █ / █ / █ / █ / █ / █ / █ |

**Z-1**

|  |
|----|
| █ / █ / █ / █ / █ / █ / █ / ^ / 7 / █ / 7 / █ / 7 / █ / 7 / █ / █ / █ / █ / █ / █ / █ |

\
When the pump is connected to power, it will suck water from the pressure plate and pump it to the right. The water level on the pressure plate will fall to 0. The plate can be constructed to react on 0…3 water. You can invert it to get an off signal instead setting it to 4…7. In both cases the *off signal* will have a delay of about 100 steps. This gate is fluid conserving.

However, the introduction of minecarts have created alternatives that are more compact and don't require water, largely rendering the hydromechanical PTS device obsolete. The following minecart-based PTS converter is fast, easy to build, and extraordinarily compact:

Bloodbeard's Minecart Dwarfputing Ideas thread on the DF forums has other examples of minecart-based PTS.

By extending the track, it's also possible to have a circuit that ignores extra signals until the minecart returns to reset position.

## Load based Mechanical signal-input power-output gates

- These gates can be used either by adding a power -\> link signal converter (also known as a "rotation sensor"), or directly used to control pumps, such as in other logic gates (the unsourced fluid logic gates use these, for instance). The conventional "rotation sensor" consists of a pump powered by the gate's OUTPUT gear, pumping an infinite supply of water onto a water-sensing pressure plate with an infinite drain.
- There are certain things important to all the gates:
- Each gate has an OUTPUT gear, which will be placed next to a pump which the gate will control.
- In diagrams, the OUTPUT gear is below the 'O' gear, connected to it by gears or vertical axles. The P indicates where you should hook power up, and L indicates where load (gears or pumps that don't have a water source) should be connected, and ¦ and - are horizontal axles. The Is are gears linked to INPUTs (some gates have one input, but most have two).
- Gates which incorporate a NOT will have the power network branch off from the 'O' gear, and have a train of power-draining stuff connected to the input gears, whereas gates which do not incorporate a NOT will have the power connected to the input gears instead. The principle behind normal gates is that when the INPUTs are ON, power is connected. The principle behind the NOT gates is that power is always connected, but when the INPUTs are ON, a large enough power requirement is connected to send the power requirements above the power supply, shutting down the system.
- If your windmills produce no power, you'll have to come up with some way to use water wheels for power instead.
- You should build only enough windmills (or water wheels) to power the system, and should not connect the network for one gate to another gate's network, since the load would shut everything down or nothing at all.
- The gates' instructions will explain how much load and power you need to have at each P and L in the more complicated gates.

### Legend

|  |  |
|----|----|
| Symbol | Meaning |
| O | A gear which connects to your OUTPUT gear, which outputs power when the gate is producing an ON output. |
| I | A gear connected to an INPUT. In most gates you will have two Is, with each one connected to a different input. |
| \- / and / ¦ | Horizontal axles |
| P | Power goes here |
| i | Two more gears, each connected to the two different inputs. |
| L | a chain of gears or pumps which serve to add load to the system, generally shutting it off when connected. |
| \* | A gear which isn't linked to any inputs or outputs and just serves to connect the power or whatever. |

### Mechanical identity gate

|     |     |     |     |     |
|-----|-----|-----|-----|-----|
| O   | I   | \-  | \-  | P   |

- This takes an linked input signal and converts it to power without changing it.
- Connected to the input gear, such that they will only be connected to the system if the input gear is receiving an ON signal, are gears with windmills on top of them. Build only enough windmills to power the devices that the gate's OUTPUT gear are connected to (and the gears/axles).
- When the INPUT is ON, the INPUT gear will be active, and the network will provide power to the OUTPUT. When the INPUT is OFF, it will not provide power to the OUTPUT.

### Mechanical NOT gate

|     |     |     |
|-----|-----|-----|
| O   | I   | L   |
| ¦   |     |     |
| ¦   |     |     |
| P   |     |     |

- When the INPUT is ON, the INPUT gear will be active, and the network should need more power than is available. The devices connected to OUTPUT should shut down. When INPUT is OFF, the devices should have power since the INPUT gear will be disconnected.

### Mechanical NAND gate

|     |     |     |     |
|-----|-----|-----|-----|
| O   | I   | I   | L   |
| ¦   |     |     |     |
| ¦   |     |     |     |
| P   |     |     |     |

- This works just like the NOT gate, except that there are two inputs and both have to be active to shut down the system instead of one. Make sure you have enough power to run the system when one of the input gears is active.

### Mechanical AND gate

|     |     |     |     |
|-----|-----|-----|-----|
| O   | I   | I   | P   |

- This works like the identity gate, except that there are two inputs and both have to be active for the system to get power.

### Mechanical OR gate

|     |     |     |
|-----|-----|-----|
| O   | I   |     |
| I   | \*  | P   |

- This works like the identity gate, except that there are two inputs, and if either is active, the system receives power. Note that the entire power network is connected to both inputs, such that if either input is active the entire power network is powering the system.

### Mechanical NOR gate

|     |     |     |
|-----|-----|-----|
| I   | \*  | L   |
| O   | I   |     |
| ¦   |     |     |
| ¦   |     |     |
| P   |     |     |

- This works like the NOT gate, except that there are two inputs, and if either is active, the gear train or pump stack signified by the 'L' will be connected to the system. You need to have enough load to push power requirements above the amount of power produced by the power supply, shutting the system down.

### Mechanical XOR gate

|     |     |     |     |
|-----|-----|-----|-----|
| O   | I   |     |     |
| I   | \*  | \-  | P   |
| .   | i   |     |     |
| .   | i   |     |     |
| .   | L   |     |     |

\

- Except for the 'i's and 'L', this gate is identical to the OR gate. The additional components add the 'exclusive' part of the 'XOR' to the gate.
- The 'i's are additional gears connected to each of your inputs, and the L is additional load (large enough to stop the system, of course).

### Mechanical XNOR gate

|     |     |     |     |     |
|-----|-----|-----|-----|-----|
| .   | .   | I   | \*  | L   |
| .   | .   | O   | I   |     |
| .   | .   | ¦   |     |     |
| P   | \-  | \*  |     |     |
| .   | .   | i   |     |     |
| .   | .   | i   |     |     |
| .   | .   | P   |     |     |

|     |     |       |       |             |        |
|-----|-----|-------|-------|-------------|--------|
| A   | B   | Drain | Power | Extra Power | Result |
| 0   | 0   | No    | Yes   | No          | 1      |
| 0   | 1   | Yes   | Yes   | No          | 0      |
| 1   | 0   | Yes   | Yes   | No          | 0      |
| 1   | 1   | Yes   | Yes   | Yes         | 1      |

- The XNOR gate is an equality gate: The output is ON when both inputs are equal, and OFF when they are not equal.
- This gate may be **even more complicated** to build than the XOR gate!
- First, your 'i's are again gears connected to your two inputs. The extra P below them is additional power source, ideally only one windmill.
- Here's where it gets complicated. The load has to be sufficient to shut down the system when additional power supply is disconnected. However, when BOTH inputs are on, there needs to be enough power from additional P to bring the system back online.
- Thus our gate does what it is supposed to: Produce enough power to have the OUTPUT gear be ON when both A and B are either 0 or 1, but not when they are not equal.
