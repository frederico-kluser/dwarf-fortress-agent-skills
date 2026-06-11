# Pressure plate

> Fonte: [Pressure plate](https://dwarffortresswiki.org/index.php/Pressure_plate) — Dwarf Fortress Wiki (GFDL/MIT)

**Pressure plates** act in similar ways to levers, in that they require a pair of mechanisms to link them to a bridge, cage, chain, door, floodgate, hatch, grate (wall or floor), bars (vertical or floor), support, spears/spikes, gear assembly or track stop. They send an "open" signal the instant any of their trigger conditions are met (though linked items retain their normal reaction delay, if any), and reset with an "close" signal after their conditions have not been met for 99 consecutive ticks. Proper trap design will often leave a time delay space for traps based on enemy movement.

Pressure plates are not targeted by building destroyers.

## Trigger conditions

There are currently four possible trigger conditions:

1.  water levels
2.  magma levels
3.  track (minecart) weight (only works on tracks)
4.  creature weight (including a separate toggle for citizens)

The first two can be set to trigger on the presence or absence of liquids, or any particular fluid level range. The latter two can only trigger on present weight within a user-configured range (though they can be set to 'untrigger' when a weight is removed).

Triggering signals for water and magma: CLOSE \`

`Repeater 1           ---O--C--O--C--O--C--O--C`\
`Repeater 2           -----O--C--O--C--O--C--O-`\
`Repeater 3           -------O--C--O--C--O--C--`\
`What the door sees   ---O-OCOCOCOCOCOCOCOCOCOC`

This can be extended, with additional pressure plates, up to a maximum of one cycle every two ticks (one tick for open, and one for close) using 50 pressure plates. While these designs were originally created with fluid-logic, the introduction of minecarts provides a much simpler way to stagger the signals from multiple pressure plates.

Note that only a few targets that don't have a built-in delay can handle switching at such speeds (doors, hatches, and gears).

Keep also in mind that quickly switching buildings will dramatically reduce the performance of your game due to map connectivity information being constantly rebuilt - a single door opening and closing every dozen steps may reduce your frame rate by about a third.

### Priority close

Pressure plates are very timely when detecting a trigger and sending an *open* signal, but require 99 ticks when sending a *close* signal. Unfortunately, there are situations where closing a hatch or door 100 ticks later might just be too late. This limitation can be overcome by constructing multiple pressure plates that are continually refreshed in a cycle less than 100 ticks. When a trigger condition occurs the cycle is stopped, leading the pressure plate that would have been refreshed next to send a *close* signal much sooner. A well-calibrated design should be able to provide a *close* signal in five ticks or less.

## Construction

Pressure plates are built on any floor using , , . You will be prompted to enable what type of things should trigger the plate (water, magma, creatures, minecarts, or some combination of the four). You are then instructed to set up a range between two values of weights - a minimum to a maximum. and affect the minimum weight, and and affect the maximum.

The number of mechanisms required to build a pressure plate depends on how many types of things (water, magma, creatures and/or minecarts) can trigger it. If only one of them can trigger it, it takes one mechanism. If two can (water and magma, water and creatures, or any other pair) then it takes two mechanisms. If all four can trigger it, it will take four mechanisms.

NOTE: The creature selection screen has an additional setting that allows the pressure plate to ignore, or be triggered by, your citizens. "Citizens" include tame animals but not merchants or liaisons. Pressure plates that can be triggered by citizens will remain triggerable by non-citizens as well-- there is no way to make a pressure plate that is triggerable by only civilians, although a pressure plate with a narrow weight threshold could potentially trigger for only goblins and dwarves.

Construction is done by a mechanic, who will require one to four mechanisms. After construction is completed, use the key to view the building, and press to link the pressure plate to choose which trap, floodgate, or other device will be triggered by it. Your mechanic will haul one mechanism to the desired device, work for a while, and then take another mechanism to the pressure plate itself and complete the task. Your pressure plate is now ready for action.

### Choosing Weights

For a table of creatures you can organize by increasing or decreasing weight, see List of creatures by adult size.

The weight of a creature depends on individual build: skinny, small creatures weigh less than enormous, fat ones of the same species. As shown in the list, children and adolescents are usually smaller than fully grown creatures and may not trigger plates adjusted to adults' size. Equipment adds to a creatures weight; dwarves in steel armor will activate plates set to higher triggers.

Creatures with the trapavoid token will not trigger pressure plates, regardless of weight. Vermin do not trigger traps since they aren't treated as actual creatures for the purpose of triggering any sort of trap, and weigh no more than 2000 anyway.

On-screen numbers are shown divided by 10 (rounded down). For example 50,000, the default minimum weight, will appear to be 5,000 in-game. It is easy to double check what you want to set it to by using a lookup and reverse lookup on the list, to compare what the game says about a creature, and what the list says.

and lower the minimum creature weight to which a pressure plate will react, and increase it. and reduce the maximum registered creature size while and increase it. The lowercase letters adjust sensitivity in steps of 10 000 (1000 on-screen), the uppercase letters in steps of 100 000 (10 000 on-screen).

A pressure plate set to trigger on rack can also be adjusted to respond only to Minecarts of defined weights. The default settings are 1 as minimum and "any" as maximum, which responds to carts of any weight. If only carts of specific weights are supposed to trigger a signal, different minimum and maximum values can be chosen, in steps of 50 kg, ranging from 1 to 2000. and lower and increase the minimum, and affect the maximum weight setting. Only carts falling within the limits specified will trigger a signal, carts that are too light or too heavy will not. The gross weight of the cart will be consulted, i.e. the weight of the cart including its cargo (and potentially rider). Differing weights of empty carts only cover part of the choosable weight range - the heaviest empty carts are made from platinum and weigh 856 kg.
