# Cleaning

> Fonte: [Cleaning](https://dwarffortresswiki.org/index.php/Cleaning) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

!!UNKNOWN!!  · xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

|                                         |
|-----------------------------------------|
| **Cleaning**                            |
| Skills used |
| —                                       |
| Tasks                                   |
| Clean                                   |

**Cleaning** is a type of labor used by dwarves in order to clean tiles. In order for dwarves to perform this task, it must be enabled inside the labor menu's Other Jobs tab. Dwarves clean a 3x3 tile area at a time, removing contaminants such as vomit, blood, and broken arrows. Cleaning is enabled by default in all dwarves.

Dwarves automatically clean interior floors of contaminants other than mud. Creatures can track and spread blood, ichor, and various hostile extracts across floors (though direct tracking is disabled in fortress mode by default in v0.43.05). Dwarves also clean melted ice off the beautiful frozen (Inside) ground when ice melts in places where the temperature is conveniently high enough. Rain will clean any tiles exposed to it (typically outdoors tiles,) and natural or generated mist will clean any creature passing through it and gradually wash the tile it is in. It is not possible to manually order dwarves to clean up specific tiles.

In order to initiate a cleaning task, a dwarf needs to be idle 'near' a mess (within X tiles on the same z-level). You can encourage cleaning by ensuring that dwarves with the appropriate labor regularly complete jobs in the vicinity. Defining a meeting area might get the dwarves to clean that area more often. An effective way to get an area clean is to select a dwarf for the task, remove all their professions except Cleaning, and assign them to a small burrow designated around the area to be cleaned. Burrowing a dwarf with only Cleaning assigned will keep an area much cleaner than it would remain on its own.

A method requiring less micromanagement is to build levers in the remote corners of the map, also in the caverns. If the dwarf building it, or the dwarf later pulling it, happens to have "no job" on their way back they will clean whatever lays in their path. This works only during periods when there is not much to do in the fortress; Any task taken on the return trip will prevent cleaning.

What also works is creating a small "nothing" stockpile (ie, one without any item type selected). Dwarves will quickly clean the surface under the stockpile, even if it is outside.

Dwarves occasionally clean themselves, using any water source, and soap if available (see bug below.) They will do so even if they are restricted from the cleaning labor. Any blood and other substances will be washed to the floor to spread to other dwarves and animals; barefoot creatures, like animals, children, and many dwarves, can become afflicted with possibly-poisonous substances washed off another's body, clothing or weapons. A grating beneath the dwarf will permit washed substances to drain.

## Cleaning Your Dwarves

A simple Dwarven Bathtub constructed out of microcline. For style points, construct the ramps out of soap.

Given the number of diseases carried by forgotten beasts and the risks of infection, and the threat of evil weather in evil biomes, it's a good idea to try to keep your dwarves clean. However, this might be a little less important if tracking contaminants is disabled. Even without tracking, dirty dwarves are more likely to get infected if they're injured.

While dwarves do a decent job of keeping themselves clean with a water source and soap, they don't always bathe immediately and pets and livestock can't wash themselves. Fortress cleanliness can be helped along in a few ways, such as by setting up a Dwarven Bathtub as described below, by creating a waterfall in an area that your dwarves will walk through, or using complex mist generation schemes.

### Dwarven Bathtub

A simple method to clean your denizens is the Dwarven Bathtub, but note that while these will remove and contain infectious contaminants, the contaminants themselves remain dangerous. Because of this, Dwarven Bathtubs set up without complex sealing, washing, and draining functions will keep the contagion inside them, potentially exposing dwarves and objects to contaminants and contaminated water each time they pass through. A single "pile of forgotten beast extract", sitting inside a Dwarven Bathtub in a high traffic area, can easily infect your entire fort as each dwarf walks through it.

Combine a Dwarven Bathtub with a mister suspended above it to form a Dwarven Shower. The tub ensures that visitors are clean, while the mist destroys contaminants in the tub and gives happy thoughts.

To set up a basic Dwarven Bathtub, just make a channel and fill it with 3/7 water via a pond zone, being careful to remove or deactivate the zone before it gets too full. If you do it outdoors in one of the warmer biomes, build a roof over it so that the water tiles become Inside to prevent evaporation. Be careful not to put these outside in any biome which freezes, because freezing water will kill anyone in the tub when it freezes over. They should be safe from freezing so long as all the tiles with water show up as Subterranean when you look at them. Because nobody would want that to happen! The warmer biomes don't have this worry.

One of these across each fortress entrance, each cavern entrance and the hospital entrance will go a long way towards keeping contamination under control. If you need to clean specific civilian dwarves, create a lever that does nothing at the end of a hallway on the far side of a Dwarven Bathtub, assign the lever to that dwarf (this part requires a Manager noble), and order the lever to be pulled. This also works to clean contaminated pets, if you find the pet owner and order them to pull the lever. Unowned animals, of course, can just be butchered or thrown into the tub (change your pond zone to a pit zone and drop them in). Military dwarves can simply be stationed on the other side of the tub.

### Dwarven Shower

Regularly dropping small amounts of water on passing dwarves is a great way to keep them clean. The design below uses water from an aquifer above and empties into a portable drain below, making it completely unpowered.

-

  aquifer buffer level

-

  flow control level

-

  shower hall level

-

  catch basin level

-

  drain level

|  |
|----|
| "Cleaning" in other / Languages / Dwarven / : / lecad / Elven / : / reya / Goblin / : / ustu / Human / : / enil |

The diagonal access in the middle image ("shower hall level") prevents any chance of muddying nearby tiles in the hallway.

## Cleaning Your Items

If a dangerous extract/blood/poison kills your dwarves, it will most likely leave traces of the deadly substance on their items. These items can be cleaned by having flowing water or mist go over them. A single 1x1 square with water pumping into and out of it will suffice. For ease of use, you can specify a dump zone on top of the 1x1 square of water, and have your dwarves dump all contaminated items right there. Once the water has flowed over the items, you can un-dump the items and start using them again safely. Make sure your dwarves carrying these items wear gloves!

## Bugs

- There is currently a bug leading to spam of messages "cannot clean self" whenever soap is available; the only known workaround is to ensure that all of your soap is stored in chests in your hospital.
