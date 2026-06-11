# Animal logic

> Fonte: [Animal logic](https://dwarffortresswiki.org/index.php/Animal_logic) — Dwarf Fortress Wiki (GFDL/MIT)

**Animal logic** functions by taking advantage of the pathfinding algorithm in *Dwarf Fortress*; all domestic animals seek to find the shortest (lowest cost) path to their desired targets (activity zone, parents, dwarves, valuable objects, etc.) Furthermore, animals tend to continue to path through tightly closed doors, despite them not being able to pass. This defines the difference between animal and creature logic: animal logic does not need to regulate paths actually travelled by a creature, only potential paths. Using these features of animal pathfinding, it is possible to create very complex logic gates.

Animal logic has three principal advantages: speed, compactness, and simplified functions. However, animal logic is slower than mechanical logic, and less reliable than either fluid or mechanical logic.

## Definitions

For clarity, definitions of the terms used in animal logic are listed here:

**Ground**: for simplicity, the thing the animal is pathing to is referred to as *ground*, as that is the ground state which it wishes to reach. Ground is always the left unless otherwise noted.

**Purge**: Path to ground with no inputs

**Path cost**: The number of steps the animal must make to reach ground

**Fusion Gate**: Simply one or more logic gates built into the same system-- this efficiently replicates the functionality of stringed gates

**Compound Gate**: Gate which uses two or more gates set to different path costs.

**AND Gate**: AND takes 2 or more inputs and returns TRUE if ALL are TRUE.

**NAND Gate**: NAND takes 2 or more inputs and returns TRUE if ANY are FALSE.

**ANDOR Gate**: ANDOR takes 2 or more inputs and returns TRUE if X-Y are TRUE. (this gate is exclusive to animal logic, and is a single step fusion of AND and OR)

**OR Gate**: OR takes 2 or more inputs and output TRUE if ANY are TRUE.

**NOT Gate**: NOT takes a single input and inverts it to the opposite state.

**XOR Gate**: XOR takes 2 or more inputs and output TRUE if ANY are TRUE but NOT ALL are TRUE.

**NOR Gate**: NOR takes 2 or more inputs and returns TRUE if ALL inputs are FALSE.

**XNOR Gate**: XNOR takes 2 or more inputs and returns TRUE if ALL are TRUE, or ALL are FALSE.

For a better explanation of gates see:

Notation:

**\#**: wall

**^**: pressure plate

**X**: floodgate, grate, bars, bridge, etc. (explained per entry)

**D**: door, open, but kept tightly shut(pet impassable)

**d**: door

**input value not specified Letters**: doors/floodgates, grates, bar, etc. Specified inputs(these are generally interchangeable, if not this will be noted in the entry), generally controlled by mechanism

**g**: Ground, some entries need it for clarity.

**C**: Either an input in diagrams, or the state Carry is refereed to as a state within an adder.

Gates will always be capitalized in the way they are within the entry, e.g. AND, OR, ANDOR, XNOR, etc.

Since animal logic is based on the interaction between animals and this particular setting of doors, all doors not wired to mechanisms need to be unlocked but tightly closed.

There are three principal logic gates in any logic system, AND, OR, and NOT. Animal logic can easily create all logic gates and is able to handle multi input-output, and fusion gates. The principal reason for this is pathfinding always prefers the shortest path to ground, and by controlling this path you can control the animal within the gate. The advantage of animal pathing is that the gate can have multiple states allowing more than a single ON or OFF signal. For simplicity and streamlining these systems only use binary information, but theoretically they could be made to compute in decimal or some other system; however, such gates are maddeningly complex and very hard if not impossible to build.

## SIMPLE GATES

There are two primary ways to make a gate, single path and dual path, the single path gate only allows the animal a single exit and this forces it into a non pathing state until there is input at which point it will "wake up" and move; however, this kind of gate is slow and unreliable. Dual path gates always have an open path keeping the animal constantly pathing out of its enclosure. This constant pathing allows the gate to respond more quickly and retain higher reliability; however, the constant pathing may cause noticeable frame rate drops with large logic sets. I will only be discussing the dual path gates, as they're more effective for general use.

### AND

This simple gate is made by confining the animal into a straight corridor; the ground path will have two or more doors which are connected to the input, while the second longer path remains clear. The gate can be configured as an NAND gate by simply moving the pressure plate. If the plate is by the ground path it functions as an AND gate returning TRUE if the ground path is open, and if the plate is by the purge path it will return FALSE when the inputs are TRUE.

`#########`\
` ABCD^ D`\
`#########`

### Multi AND

`############`\
` ANYNUMD^ D`\
`############`

### NAND

Reconfigured AND gate, see AND.

`#########`\
` ABCD ^D`\
`#########`

### OR

Basic gate, returns TRUE if either input is TRUE.

`#####`\
`AD^ D`\
`B####`\
`#####`

### Multi OR

`#######`\
`A #####`\
`N #####`\
`Y D^ D`\
`N #####`\
`U #####`\
`M #####`\
`#######`

### NOR

Basically a reconfigured OR gate.

`#####`\
`AD ^D`\
`B####`\
`#####`

### NOT

The simplest gate, it takes a single input and inverts it. FALSE -\> TRUE, TRUE -\> FALSE.

`#######`\
` AD ^D`\
`#######`

## Compound Gates

Basically two or more gates arranged with different path costs to ground. These gates can be configured in a number of different ways, these being the simplest. It may be possible to make these gates as single gates but that would require inverting some of the input. Simple compound gates use two simple gates and handle two inputs; complex compound gates have more than two simple gates and need more than two inputs. A complex compound gate might be used to convert decimal numbers into binary using And gates.

### XOR

Compound of AND and OR, when ONLY ONE is TRUE returns TRUE If A and B are FALSE the animal moves to the FALSE position by Purge, if A or B is TRUE, the animal moves to the TRUE position at the OR gate, if both A and B are true the animal moves to the FALSE position by the AND gate.

`#g########`\
`# ABD  D #`\
`# ####^# #`\
`# ####D# #`\
`# ###BA# #`\
`#        #`\
`##########`

AND path cost: 4\
OR path cost: 10\
Purge path cost: 14

### XNOR

Inverse of XOR: Return TRUE if BOTH are TRUE or FALSE If A and B are FALSE the animal moves to the TRUE position by Purge, if A or B is TRUE, the animal moves to the FALSE position at the OR gate, if both A and B are true the animal moves to the TRUE position by the AND gate.

`#g#########`\
`#         #`\
`##B###### #`\
`###A## DA # `\
`####D^##B #`\
`#####D### #`\
`######    #`\
`###########`

AND path cost: 4\
OR path cost: 10\
Purge path cost: 15

### Complex Compound gate, Octal display ALU

Inputs are 1, 2, 4 these correspond to the binary values of the inputs, outputs are A, B, C, D, E, F, G, H being 0, 1, 2, 3, 4, 5, 6, 7 respectively in the output display. I used octal for sanity, but this could be easily scaled to work for decimal (up to 10, beyond that you need a converter not an if switch) or hexadecimal(hex will be easy to handle, and probably easier to convert down to decimal)

`#################`\
`                #`\
`# # # # # # #1# #`\
`# # #1# #1#2#2# #`\
`#1#2#2#4#4#4#4# #`\
`#D#D#D#D#D#D#D#D#`\
`#               #`\
`#################`

`# ######`\
`# 1  D #`\
`# #### #`\
`# 2  D #`\
`# #### #`\
`# 12 D #`\
`# #### #`\
`# 4  D #`\
`# #### #`\
`# 14 D #`\
`# #### #`\
`# 24 D #`\
`# #### #`\
`# 124D #`\
`# #### #`\
`#    D #`\
`########`

## Fusion gates

These are gates which are constructed by physically combining the two gates to get a specific output.

### ANDOR

This gate will evaluate if either of x AND statements are TRUE. This gate is built as a straight line similar to the AND gate.

`######`\
`#C####`\
`ABD^ D`\
`C#####`\
`######`

### NANDOR

Reconfigured ANDOR gate, see ANDOR.

`######`\
`#C####`\
`ABD ^D`\
`C#####`\
`######`

### ORANDOR

This gate returns true if either A or B and either C or E is true.

`######`\
`AC####`\
`BED^ D`\
`######`

### ORANDAND

This gate returns true if either A or B is true, and E and C are true.

`#######`\
`A######`\
`BCED^ D`\
`#######`

## Complex Gates

The development of more complex gates requires careful calibration of the path cost of each path to allow the gate to switch states correctly and display the correct result.

## Adders

A full adder can be made as a Compound Fusion gate, by combining AND, ANDOR, and OR gates

### Binary Adder

A binary adder is constructed of two or three "sum" gates and a purge path. A half adder only adds two numbers and only needs two sum gates, 1 and 2. Full adders using carry to allow chaining require three sum gates, 1, 2 and 3. Because binary is base two that translates to 01, 10, 11 as the sums, when the second bit is a 1, the gate is "carrying" the value up to the next level.

When building the adder, the highest path must have the most preferential path to ground or it will not properly function.

Standalone adders (they don't carry into another adder) require 22 mechanisms, and 14 doors. Start adders (They feed into the next adder and include a carry) require 32 mechanisms, and 14 doors. Chain adders (The receive Carry, and pass a Carry bit up) require 32 mechanisms, and 14 doors The gates only take up 13x9 tiles each.

## Hatch-based logic

Hatches can be used in many logic designs for alternate designs. A hatch over a ramp serves as a door that cannot be wedged open; a hatch over a channel functions as a naturally inverted door, blocking pathing when open rather than when closed. Although the designs on this page all use doors to restrict path, careful use of hatches can be more effective for some circuits.

Reference pictures

Image:Xnor,Xor,Nand,Or prototype adder STATE 1.PNG\|Prototype digital adder Image:And,Or,AndOr, Prototype adder STATE 3.PNG\|sum 11 Image:And,Or,AndOr, Prototype adder STATE 2.PNG\|sum 10 Image:And,Or,AndOr, Prototype adder STATE 1.PNG\|sum 01 Image:And,Or,AndOr, Prototype adder STATE 0.PNG\|sum 00 Image:9bit adder prototype interface pannel.PNG\|9bit adder interface Image:9bit adder prototype.PNG\|9bit adder Image:9bit adder prototype 10100010notes.PNG\|9bit adder, notes show the decimal value of each adder's bit

### Decimal Adder

While it can be done, it's significantly more complex than simply making a set of decimal converters working with binary adders.

### Hexadecimal Adder

A hexadecimal adder works on a similar level to the binary adder, however it uses 64 sum gates ranging from 0 to 31. User:LordOOTFD is developing a prototype adder which utilizes a floating carry bit to function as a full adder.

### Subtractors

Inverse adder, simple but not yet tested.

## Animals

Choosing the animal which works as the logic core for an animal logic systems is somewhat important, depending on your needs and the available animals. The main requirements are that the animal must be large enough to activate pressure plates and able to stay alive while locked up in a logic cell. As long as these conditions are met, pretty much anything will do as long as you can remember which animal belongs into which gate (to avoid designating the same animal for more than one pit).

### Minimum weight

A creature must have a size of 10, 000 in order to trigger pressure plates at all. Everything smaller will not generate output. This excludes cats and many children of animals like puppies.

For reference, this List of creatures by adult size gives a full listing of *average* sizes of creatures, with relevant cutoffs for pressure plates already marked in.

Pigs and dogs are an easy choice as animals to use. They are heavy enough to trigger pressure plates if adolescent or adult. They will normally path to a meeting area. While they have other uses as war animals or a prime source of meat, they are fast-breeding domestic animals that can be brought on embark.

### Viability

Children are presumed superior to adults due to an extra pathing goal (to their mother), but keep in mind that they are generally much smaller than adults and thus may be too small to activate pressure plates.

Female animals can become pregnant and have children. Such children may disrupt the pathing of their mother or send signals by themselves. Grazers are likely to starve to death before you get any logic out of them.

Exotic animals undeniably add style to your computing zone. A GCS powered computer would be awesome. Such uses prevent other potential applications, like using the spider to create valuable silk. Flyers may ignore hatch-based logic blocks.

### Invaders

Invaders such as elves or goblins will not work with any of the designs on this page, unless you managed to dehand them before capture-- securely closed doors are no barrier to them. Any mounts or warbeasts, on the other hand, might work, and exotics are unlikely to bear any children, and can be extraordinarily long-lived. Job cancellation may be a problem with more complicated designs. Invader animals path to the map edge following capture. Be careful of any flyers or building destroyers.

## Putting it all together

When it comes time to automate your systems the first thing you need to know is what needs to be automated and what should remain manual. An obsidian farm with completely autonomous control of the casting process is all well and good, until it drowns all your legendary miners when it prematurely triggers. All systems should have manual controls and failsafes to help avoid Fun (but because we all love Fun sometimes you forget to fully connect that emergency drain, or that failsafe system you built somehow failed.)

Once you know the steps you need in your system, it comes time to select the parts you need to automate, whether it be basic logic gates or more sophisticated multiple trigger systems.
