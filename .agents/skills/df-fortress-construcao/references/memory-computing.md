# Memory (computing)

> Fonte: [Memory (computing)](https://dwarffortresswiki.org/index.php/Memory_(computing)) — Dwarf Fortress Wiki (GFDL/MIT)

Memory is used for storing values and states in dwarven computing. Typically, binary memory is used, but this isn't strictly necessary. There are multiple ways to set up a memory cell, depending on whether one is using mechanical, fluid, creature logic, or minecart logic. With binary memory, each cell has two possible states, generally referred to as 0 and 1, or true and false.

### Flip-flops versus latches

The most basic characteristic of memory in *Dwarf Fortress* is that it acts as a signal splitter: given a series of on-off signal cycles, it outputs a series of alternating on or off signals. Memory that does this, and only this, acts like a flip-flop: every time you trigger the memory, it changes state. Such memory is perfect for devices such as counters "counters"). However, it's common to desire the ability to write state directly to your memory, rather than toggling it-- that is, to write either **true** or **false** to memory directly, without knowing the current state of the memory. This can be described with a chart where the memory value feeds back into itself:

| input | latch state | output | new latch state |
|-------|-------------|--------|-----------------|
| 0     | 0           | none   | 0               |
| 0     | 1           | off    | 0               |
| 1     | 0           | on     | 1               |
| 1     | 1           | none   | 1               |

===Performance=== Memory systems in a fortress, thankfully, are very good at maintaining their value (in the absence of any trolls), but they are still plagued by problems with latency and long refractory periods. Latency refers to the length of time before which a change in value will register, and the refractory period refers to the period after writing to memory during which one cannot reliably write to it a second time. Because of the delays involved with pressure plates, latency and refractory period for a given memory cell often depend on which state the memory is being changed to. For instance, the mechanical hybrid cell below has nearly no latency when being written as true, but around 100 ticks of latency when being written as false.

Some designs can trade simplicity or material needs for costs in performance.

## Fluid Logic

Simple fluid logic latches rely on an infinite source and infinite drain, storing information in the form of the presence or absence of water in a particular location.

In this design, water flows from an infinite source over an output pressure plate toward an infinite drain . Its flow is controlled by two floodgates, , and , linked to two separate inputs. When is open and closed , water will cover and remains so, regardless of the state of .

If is opened while is closed, water will leave and the tile will remain empty of water until opens again.

This design has relatively high latency, because of the 100 tick delay associated with floodgates. Replacing the floodgates with doors, which have no reaction delay, greatly accelerates the response of the latch, but the overall performance is still limited by the reset period of pressure plates. Given careful enough design and sufficient water pressure, the latency of a write to true can approach 10, with the latency of a write to false around 110.

## Creature Logic

In this circuit, a creature placed between in the middle seeks its pathing goal but is constrained by the hatches and , each linked to the pressure plate of the same color. When the door is opened, the creature can move to the left (false) , and when the door is opened, the creature can move to the right (true) , thus outputting to anything linked to that pressure plate. This is an example of memory for which it is possible to write a particular state, rather than just toggling, which allows for simpler design for some applications. Note also that rather than writing on a single on or off signal, it depends on an on-off cycle.

This design has good latency for creature logic systems, resulting in on signals around 40 ticks after writes and off signals around 150 ticks after writes. It has a 110 tick refractory period, representing the time necessary for the hatch covers to close.

## Mechanical Logic

A gear assembly can function all on its own as a memory cell, being either active or disengaged. However, some complicated applications suggest the use of hybrid mechanical-fluid memory.

In this design, two separately powered pump stacks, and , are placed over each other-- the lower one, pumping to the right, and the higher one pumping to the left. When the water is lying in the rightmost (true) cell, it activates a pressure plate . To write true to the memory, one triggers the lower gear assembly , activating the lower pump, and to write false, one activates the higher gear assembly and pump stack. Like the creature logic memory above, this cell can be written as specifically true or false, and depends on an on-off cycle as input.

This design has very good latency (from almost nothing for a write as true to 100 ticks for a write as false) and no real refractory period-- it can be written to immediately following a previous write, although it does depend on the completion of the previous write signal (receiving the off component of the signal) before writing again.

### Memory versus Power-to-signal

It can be tricky to differentiate memory from power to signal conversion. Through feedback, power-to-signal devices can often be changed into memory cells, and powered memory devices can be adapted into power-to-signal. Previous to the introduction of minecarts, the most common power-to-signal device bore strong resemblance to the memory cell described above. There is, however, a large difference between memory and power-to-signal. While memory designs receive on-off signal cycles and output discrete **on** or **off** signals in return, power-to-signal converters translate one type of binary information (power on/off) into another (signal on/off). That is, a signalling device that receives then loses power should return a full on-off signal cycle.

## Minecart Logic

There are numerous ways for minecarts to hold information. Some memory designs use movement or the absence of movement; others use just the position of a minecart. Advanced designs could use the weight or direction of movement of a minecart. The following powered minecart design by Bloodbeard is the smallest memory circuit currently known to dwarvenkind:

`      Key:`\
`O     O Wall`\
`[#0:0][@6:0][%254][#2:1][@][%15]    [#0:0][@6:0][%254][#@] Copper minecart`\
`[#0:0][@7:0][%254][#@]     [#0:0][@7:0][%254][#@] Iron minecart`\
`[#7:1][@][%207][#2:0][%15][#]    [#2:1][%15][#2:0][%15][#] Gears`\
`O     [#7:1][%207][#] Rollers`\
`      [#5:1]^[#] Pressure plate`\
`O     [#7:1][%186][#] Minecart tracks`\
`[#7:1][%207][#2:1][@][%15]    [#7:1][%210] [%208][#] Track ends`\
`[#5:1]^`\
`[#7:1][%207][#2:0][%15][#]`\
`O`\

`O`\
`[#7:1][%210][#2:1][@][%15]`\
`[#7:1][%186]`\
`[%208][#2:0][%15][#]`\
`O`\

The diagram shows the minecart layer at the top, the roller/furniture layer in the middle, and finally the track layer at the bottom. When the northern gear assembly is activated, powering the northern roller, a heavy minecart (copper, in this example) is pushed southwards. This pushes a lighter minecart (iron here) south, and triggers a pressure plate that is built to only signal on the weight of a copper minecart, and not on the weight of the lighter iron minecart. With the activation of the southern gear assembly, the situation reverses. The iron minecart pushes on to the pressure plate, and an **off** signal is sent.

## Memory addressing

In complicated designs, one may wish to use a memory cell abstractly-- to represent any number of different values. To use multiple such abstract cells, it's necessary to specify exactly which memory cell one wishes to read from or write to at any given moment.

This is simplest in mechanical logic. A grid of gear assemblies can represent rows and columns, and by disengaging control gears for all but the cell that lies at that particular row/column intersection, one can easily refer to a specific cell. Strict fluid logic can do something similar, by controlling the input of water to memory cells, although this involves long delays. With the creature logic design, one can use additional doors to restrict writes to any cells not referenced.

## Alternate design

Because most memory is used for a specific application, there is no single best design. It is not uncommon to see functionality built into memory circuits-- a simple circuit that increments contains its own memory. Alternate designs are important when memory needs to be written to in various ways (toggle versus specific value) or when latency and refractory period are unimportant compared to resource requirements such as space.
