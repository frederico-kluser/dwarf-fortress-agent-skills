# Contaminant

> Fonte: [Contaminant](https://dwarffortresswiki.org/index.php/Contaminant) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Contaminants** are substances that can be spilled or smeared onto a floor or a wall. These include mud, snow, ash, stone dust, salt, blood, ichor, extracts, vomit, mucus, and pus.

## Hazards

Some contaminants, like those from evil biome weather or rare, deadly extracts given off by some creatures, can cause syndromes on contact. Barefoot creatures, like pets, or dwarves that have no footwear on can be affected if they step in the contaminant on the floor.

Contaminants can get on objects in some circumstances. This can be particularly dangerous if a dangerous contaminant gets on food.

## Creating mud

Any time a tile is covered in water, mud will be created on that tile. It seems that magma will remove this mud upon evaporation.

## Spreading contaminants

### Tracking

The tracking of contaminants is a configurable setting, which defaults to **NO** in Fortress mode and **YES** in adventure mode; the default in fortress mode is because contaminants were often spread excessively and uncontrollably.Bug:296

When this feature is enabled, contaminants on the feet of dwarves and other creatures are tracked onto other tiles that they pass through. Dustings and spatterings, which represent small amounts of a contaminant, do not appear to be tracked around. Larger amounts of contaminants will be picked up by a dwarf's left foot, and can then be transferred to other tiles. (contaminant tracking behavior may need to be verified for the current version)\[Verify\]

With or without tracking enabled, rain, waterfalls, and water tiles will wash contaminants off creatures, leaving them on the tile they were on.

### Flowing

Could have been avoided with one screw pump.

Water that flows over contaminants can pick them up, multiply them, and redistribute them as the water moves. Water does not appear to move mud, although mud will be created any time water covers a tile. The mechanics of redistributing contaminants using water is not well understood although there have been some observations of strange behavior when mixing blood and water.

- adding 7/7 water on top of a pool of blood creates more pools of blood at the edge of the water as it moves and evaporates.
- an overflowing reservoir that contains some blood creates blood everywhere the water flows.
- water will create mud on any non-muddy tile, and moving water will frequently redistribute the mud.

## Removing contaminants

#### From floors and walls

Removing contaminants can be accomplished in several ways:

- Contaminants can be removed by dwarves performing a cleaning task. This requires a contaminant to be on a floor tile, and will (as a side effect) also remove contaminants from adjacent walls. A contaminant that is on a wall, with no adjacent contaminated floor, will never be cleaned.

- Contaminants are also removed if *any* real building is built on them (dirt roads are not buildings), even if that building is subsequently removed.

- Contaminants on walls can also be removed by smoothing the wall.

- Mist, e.g. from water falls or screw pumps, will also remove contaminants.

Note that atom smashing a square with a contaminant on it will *not* remove the contaminant.

#### From creatures

Contaminants can be moved from creatures to floor tiles with water or mist. The simplest and most effective way is to have the creature walk through a 2/7 or 3/7 water tile. All contaminants will be transferred from the creature to the floor, and it will walk away wet (water coverings in inventory) but otherwise uncontaminated. However, that water is now contaminated, and will then contaminate any other creatures or items (such as minecarts) passing through it.

example of a mist generator

Another way is to drop water on a creature as it's walking over a floor grate (e.g. a waterfall). This is much more complex to set up, and has an additional drawback: a dwarf who attempts to clean the contaminated floor grate tile will be interrupted by the sudden influx of water, resulting in job cancellation spam, and an uncleaned grate (unless you temporarily turn off the waterfall).

To the right is an example of a mist generator over a bathtub. Since mist is able to destroy contaminants, this example is self-cleaning as long as it's running. Once pumps are built and started, water can be added at a pump intake, and should stop filling automatically when a 7/7 water tile is in the system. Statues below are used to block movement, as any 7/7 tile would produce cancellation spam if a creature was caught in it. Putting one of these in the only path to your booze stockpile(s) will regularly decontaminate everyone in the fort (who isn't a vampire).
