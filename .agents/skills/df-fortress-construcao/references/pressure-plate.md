# Pressure plate

> Fonte: [Pressure plate](https://dwarffortresswiki.org/index.php/Pressure_plate) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Pressure plates** act in similar ways to levers, in that they require a pair of mechanisms to link them to a bridge, cage, chain, door, floodgate, hatch, grate (wall or floor), bars (vertical or floor), support, spears/spikes, gear assembly or track stop. They send an "open" signal the instant any of their trigger conditions are met (though linked items retain their normal reaction delay, if any), and reset with a "close" signal after their conditions have not been met for 99 consecutive ticks (or only 3 ticks for adventure mode). Proper trap design will often leave a time delay space for traps based on enemy movement.

Pressure plates are not targeted by building destroyers.

## Trigger conditions

There are currently four possible trigger conditions:

1.  water levels
2.  magma levels
3.  track (minecart) weight (only works on tracks)
4.  creature weight (including a separate toggle for citizens)

The first two can be set to trigger on the presence or absence of liquids, or any particular fluid level range. The latter two can only trigger on present weight within a user-configured range (though they can be set to 'untrigger' when a weight is removed).

Triggering signals for water and magma: CLOSE \< min \<= OPEN \<= max \< CLOSE

Pressure plates are sensitive to some creatures and uninfluenced by others (see Unusual Triggers). They are not sensitive to inert weight or trapavoid creatures. Pressure plates trigger when the accumulated weight of detected creatures reaches a threshold specified by the player (see Choosing Weights).

## Types

**One-use** pressure plates send their signal, then deconstruct the first time they're triggered, *destroying* all mechanisms inside them (and potentially causing unhappy thoughts if any of them were of masterwork quality). As such, only use low-quality mechanisms in one-use pressure plates (and **never** use artifacts)!

**Resetting** pressure plates can be reused as many times as you want. They reset 99 ticks after their trigger is removed. That is approximately 2 hours of Fortress Mode (game world) time passage; since 1 hour = 50 ticks. In adventure mode, pressure plates reset after only 3 ticks. This discrepancy must be accounted for if any complex machines are intended to be visited by adventurers.

## Uses

Pressure plates are used as triggers for a variety of other device actions, such as bridge raising, or traps involving the release of magma or water. Most linked devices are obvious, on the "open" signal they open as expected. Cages and chains "release" their occupants on the open signal.

Pressure plates send an *open* signal the instant their criteria are met, and a *close* signal 99 ticks after their triggering criteria are no longer met. If a pressure plate sends an *open* signal to a device that is already opened, nothing happens. The only exception to this is the gear assembly, which toggles its engaged/disengaged state on every signal from a lever or pressure plate.

(See the individual device pages for complete details of how *open* and *close* signals affect each device.)

#### Bridges

Note that retracting and raising bridges have, effectively, the opposite reaction from an "open" signal, or can, depending on the design. When the "open" signal is sent, both bridges "disappear" from view - the retracting bridge disappears completely, and the raising bridge becomes a wall. But this means that the raising bridge *closes* the passage on the same level with that wall that it creates. This can be used to create either an "open" passage or "closed" passage on the "open" signal, depending on the design.

#### Screw pumps

Pressure plates are not connected *directly* to screw pumps. To trigger fluid flow via screw pumps, either have a pump permanently "on" and use a hatch over the fluid intake tile, or use some other barrier (door, floodgate, bridge, etc) to otherwise restrict the fluid flow as desired, or link to a gear assembly to toggle the power on/off - but note how pressure plates and gear assemblies interact, as mentioned above.

## Operation

Making complicated devices with pressure plates requires a full and detailed understanding of how pressure plates function.

Resetting pressure plates send two signals: an *open* signal when first triggered and a *close* signal, set to occur 99 ticks after the pressure criteria are no longer met. They do not send continuous *open* signals while the pressure criteria are met. A pressure plate that is untriggered then retriggered before it has sent a *close* signal will not send an *open* signal on the second trigger, and will abort the *close* signal scheduled to occur from the untriggering.

Special care must be taken when linking multiple pressure plates to a single device. When doing so, it's possible for one of the plates to become activated before another plate has sent a *close* signal. Unlike with single plates, the triggering of the second plate will not abort the *close* signal scheduled from the first plate, and the triggered device can become deactivated (closed) despite a triggered pressure plate linked to the device.

Similar situations can occur when activating a bridge or other refractory building with a pressure plate: if the pressure plate sends an *open* too rapidly after sending a *close*, the bridge will ignore the *open* and wedge close.

### Build order & delay

One essential consideration with carefully timed devices is build order. Pressure plates can send *open* and *close* signals at different times depending on what sort of building is being triggered and whether the building was built before or after the pressure plate. That is because furniture is evaluated in the reverse order in which it is built-- when you build a pressure plate before the furniture it's linked to, in many cases that furniture will not receive a signal until the tick following pressure plate activation.

- Linked doors and hatches always open the same tick that a pressure plate is triggered, but close depending on build order: if built before the pressure plate, they close 99 ticks after the trigger is removed, and if built after, they close 100 ticks after the trigger is removed.
- Retracting spikes built before a pressure plate retract 40 ticks after triggering and extend 139 ticks after the trigger is removed. If built after the triggering pressure plate, they retract 41 ticks after triggering and extend 140 ticks after the trigger is removed.
- Gear assemblies will appear to be unaffected by build order-- they will engage or disengage on the same tick that a pressure plate is triggered, regardless of build order-- but gear assemblies built after a pressure plate will not transmit (or stop transmitting) power until the tick following pressure plate activation (or 100 ticks after criteria are no longer met), whereas gear assemblies built before a plate linked to them will toggle at 0 and 99 ticks.
- Bridges, vertical bars, floodgates, and grates built before a pressure plate open 100 ticks after the trigger is sent, and close 199 ticks after the trigger is removed. If they are built after a triggering pressure plate, they open 101 ticks after a trigger is sent and close 200 ticks after the trigger is removed.

Essentially, pressure plates send open signals immediately upon triggering and close signals 99 ticks after their trigger is removed; pressure plates built before the device they trigger work a tick later; and doors and hatches are always opened on the exact tick that they're triggered by a pressure plate, regardless of build order, although their close tick is still affected by build order.

### Unusual triggers

Pressure plates will not be set off by dead creatures - if a creature dies upon contact with the ground, as with a fall from a great height, that creature will not set off a pressure plate upon landing. They will be set off by any creatures that fall onto them and survive, even if those creatures fall onto another creature occupying the same tile. Also, pressure plates *will* be set off by a sufficiently large undead corpse *reanimating* on their tile.

A mechanic who completes the first attachment job on a pressure plate will not cause an *open* to be sent to the building being linked, but a *close* will be sent-- when the *open* is sent, the building is not yet linked! This tends to toggle gears upon linkage, and makes futile single-use, civilians-trigger pressure plates. Neither merchants, their pack animals, nor diplomats will set off pressure plates, even pressure plates set to be triggerable by civilians. Should an invading force arrive, they will not activate any pressure plates that have been observed by any diplomat from their civilization. Flyers and swimmers will set off pressure plates in any tile they move through.

Regardless of whether a pressure plate is set to civilians-trigger or not, any creature that is unconscious or webbed will set off a pressure plate-- diplomat, sieging human, trapavoider, or your own dwarf.

### Hanging pressure plates

Like other buildings, pressure plates built on top of a constructed wall remain even after that constructed wall is removedBug:0377. All linkages to such a plate need to be completed before removing the construction supporting the plate. Creatures falling through a hanging pressure plate will not trigger that plate, but fluid falling through or pumped into a square occupied by a hanging pressure plate will trigger that plate as normal. Flyers or swimmers moving through the tile containing the hanging pressure plate will trigger it as normal.

For keeping the plate accessible while still allowing fluids to pass through, digging a downstair into natural floor, building a floor on that downstair, building the plate on the floor, then deconstructing the floor will work. In the case the natural floor is gone, obsidian-casting the plate will suffice for digging stairs.

## Advanced techniques

### Latching Pressure Plates

**Resettable Latching Plate System**.\
Uses scaffolding (not shown) just like a pump stack.

While ordinary one-use plates are easy to use, they deconstruct immediately after triggering and destroy all but one of the mechanisms used. Frequently, it's desirable to have a system that triggers once, then waits to be reset manually. For example, you might have a pressure plate that seals off your entrance and floods it with magma, but you don't want the flood to stop or the drawbridges to open like it would for a resetting pressure plate, but you also don't want to rebuild and reconnect the one-use pressure plate after every siege when half the parts are submerged in magma. This is when you should use a pressure plate linked to a latch "Memory (computing)").

Suppose you want to use a pressure plate to seal off your main entrance. You build the setup shown, being sure to construct the lower pumps before the upper pumps and the gear assembly on top after both pumps are done. Then connect the plate in room 2 to the drawbridges that seal the entrance and hook a resetting, enemy triggered plate from your main hallway to the hatch in room 1. The resetting pressure plate in room 2 should be set to trigger whenever any water is on it. You also connect a lever to the gear assembly above the pumps, which becomes your reset lever, and pull the lever to disengage the gear once its set up. You also connect that gear to a power source with at least 25 power. Lastly, you fill area 1 with 7/7 water (to prevent evaporation) by channeling through the floor and designating a pond zone above it. After it's full, remove the pond zone and build a floor over it for good measure. During construction, you will need scaffolding just like what you use for a pump stack. This setup uses the same trick of channeling through the floor and building the lower pump first to allow them to share their power source. Remember to forbid the access doors when you're done setting everything up.

You can power this from any source, but if your map gives 40 wind power you can just use a windmill. Build a windmill right above where it says "power here" and then build a gear assembly directly below it. Putting a windmill directly on top of a gear you disengage can cause the windmill to collapse, so don't try that unless it says the windmill has a stable foundation. You may also want to construct a wall around your windmill to prevent a building destroyer from smashing it.

Now, whenever your pressure plate is triggered, the hatch will immediately open and dump the water from 1 onto the plate at 2, holding that plate down until you use your reset lever to activate the pump and put the water back on top of the hatch. Don't forget to turn the pumps off after all the water has moved, or it will continue to reset itself until the pumps are stopped. You can eliminate that minor problem by hooking the pressure plates in the toggle system to the gear assembly on top of the pumps instead of a lever, but that's significantly more complex.

### Lightspeed repeater

Pressure plates have a refractory period of 99 ticks, limiting repeaters to triple-digit cycles. However, multiple pressure plates attached to a target can be "staggered" such that the *open* signal from one plate is followed much sooner by the *close* signal from another plate. Using three pressure plates, a repeater can be constructed to toggle a target three times in 100 ticks:

    Time --->

    Repeater 1           ---O--C--O--C--O--C--O--C
    Repeater 2           -----O--C--O--C--O--C--O-
    Repeater 3           -------O--C--O--C--O--C--
    What the door sees   ---O-OCOCOCOCOCOCOCOCOCOC

This can be extended, with additional pressure plates, up to a maximum of one cycle every two ticks (one tick for open, and one for close) using 50 pressure plates. While these designs were originally created with fluid-logic, the introduction of minecarts provides a much simpler way to stagger the signals from multiple pressure plates.

Note that only a few targets that don't have a built-in delay can handle switching at such speeds (doors, hatches, and gears).

Keep also in mind that quickly switching buildings will dramatically reduce the performance of your game due to map connectivity information being constantly rebuilt - a single door opening and closing every dozen steps may reduce your frame rate by about a third.

### Priority close

Pressure plates are very timely when detecting a trigger and sending an *open* signal, but require 99 ticks when sending a *close* signal. Unfortunately, there are situations where closing a hatch or door 100 ticks later might just be too late. This limitation can be overcome by constructing multiple pressure plates that are continually refreshed in a cycle less than 100 ticks. When a trigger condition occurs the cycle is stopped, leading the pressure plate that would have been refreshed next to send a *close* signal much sooner. A well-calibrated design should be able to provide a *close* signal in five ticks or less.

## Construction

Pressure plates are built on any floor using b, t, p. You will be prompted to enable what type of things should trigger the plate (water, magma, minecarts, creatures, or some combination of the four). You are then instructed to set up a range between two values of weights - a minimum to a maximum. Minecart weight ranges can be selected using the \[-\] and \[+\] buttons, while the others are configured by selecting the minimum and maximum weights from the list presented.

The number of mechanisms required to build a pressure plate depends on how many types of things (water, magma, minecarts, and/or creatures) can trigger it. If only one of them can trigger it, it takes one mechanism. If two can (water and magma, water and creatures, or any other pair) then it takes two mechanisms. If all four can trigger it, it will take four mechanisms.

NOTE: The creature selection screen has an additional setting that allows the pressure plate to ignore, or be triggered by, your citizens. "Citizens" include tame animals but not merchants or liaisons. Pressure plates that can be triggered by citizens will remain triggerable by non-citizens as well-- there is no way to make a pressure plate that is triggerable by only civilians, although a pressure plate with a narrow weight threshold could potentially trigger for only goblins and dwarves.

Construction is done by a mechanic, who will require one to four mechanisms. After construction is completed, use the q key to view the building, and press a to link the pressure plate to choose which trap, floodgate, or other device will be triggered by it. Your mechanic will haul one mechanism to the desired device, work for a while, and then take another mechanism to the pressure plate itself and complete the task. Your pressure plate is now ready for action.

### Choosing Weights

The weight of a creature depends on individual build: skinny, small creatures weigh less than enormous, fat ones of the same species.[1] As shown in the list, children and adolescents are usually smaller than fully grown creatures and may not trigger plates adjusted to adults' size. Equipment adds to a creatures weight; dwarves in steel armor will activate plates set to higher triggers.[1]

Creatures with the trapavoid token will not trigger pressure plates, regardless of weight. Vermin do not trigger traps since they aren't treated as actual creatures for the purpose of triggering any sort of trap, and weigh no more than 2000 anyway.

The configuration window allows selection of all weights 10,000 to 2,000,000, though the displayed numbers are divided by 10 and rounded down (so the row for "(75000)" actually corresponds to a size of 750,000). For weights which correspond to actual creatures, one candidate creature will be selected and displayed (e.g. gremlins for 1000, kobolds for 2000, bat men for 3000, etc.). Clicking on an entry which *is* highlighted will set it to both the minimum and maximum, while clicking a non-highlighted entry will set it to be either the minimum or maximum, depending on whether it's below the current minimum or above the current maximum.

A pressure plate set to trigger on Track can also be adjusted to respond only to Minecarts of defined weights. The default settings are 1 as minimum and "any" as maximum, which responds to carts of any weight. If only carts of specific weights are supposed to trigger a signal, different minimum and maximum values can be chosen, in steps of 50 kg, ranging from 1 to 2000. Only carts falling within the limits specified will trigger a signal, carts that are too light or too heavy will not. The gross weight of the cart will be consulted, i.e. the weight of the cart including its cargo (and potentially rider). Differing weights of empty carts only cover part of the choosable weight range - the heaviest empty carts are made from platinum and weigh 856 kg.
