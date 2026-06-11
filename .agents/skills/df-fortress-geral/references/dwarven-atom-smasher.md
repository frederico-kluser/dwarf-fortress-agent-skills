# Dwarven atom smasher

> Fonte: [Dwarven atom smasher](https://dwarffortresswiki.org/index.php/Dwarven_atom_smasher) — Dwarf Fortress Wiki (GFDL/MIT)

The **Dwarven Atom Smasher** is a nickname for a drawbridge in waste disposal or militarily-significant applications. It exploits the implementation of drawbridges to utterly destroy any objects and most creatures in its target area. A DAS works fine as a trash compactor to smash stone, items, fluids and goblins straight into oblivion.

## Effects

Atom-smashing an item will delete it from the game entirely, though some "soft" references might remain (mainly for owned items and corpse pieces).

Atom-smashing a unit, on the other hand, just kills it - the dead unit will remain forever in the list of Dead Units, and that will potentially contribute toward lag (and also restrict the number of migrants you can receive). The only time units normally get removed from the Units list entirely is when they leave the map (and those tend to come back eventually), and possibly also during a retire/reclaim cycle (which can have its own problems), but there is a DFHack script "fix/dead-units" that fixes this.

## Smashing against the ground

In this design, a drawbridge is built to come down on at least one tile of solid ground. The drawbridge is raised, the targets are placed (or move of their own volition) into position on that ground, and then the drawbridge is lowered, erasing the targets from existence. Most commonly, a garbage dump activity zone is used in order to place items beneath the drawbridge (as stockpiles cannot be placed on top of existing buildings), but other methods such as flowing water have been used with varying degrees of success.

Sand or dye in bags don't get erased while the bag does, creating a small pile of sand or dye on the ground. Similarly, contaminants (e.g. blood, vomit) are not erased when a bridge descends on them. Legendary artifacts subject to atom smashing won't be destroyed, but will receive a "Hidden" flag which will make them invisible and unusable for the rest of the playthrough. This same flag causes them to respawn unharmed in a random location on the site if the fortress is retired and subsequently reclaimed, or if it's visited in adventurer mode.

It is a good idea to make the tile(s) a restricted Traffic area to discourage your dwarves from casually sauntering into the kill zone.

## Smashing upon closing

In this design, a very compact drawbridge (as little as one tile long) is used, and the target area is the one-tile wide anchoring area, where the bridge will close. This often uses walls, locked doors, or other solid objects, leaving the targets nowhere to go. The drawbridge is lowered, the targets are placed (or move of their own volition) into position on the tile(s) that the drawbridge will occupy when closing, and then the drawbridge is raised, squashing the targets flat.

## Immune creatures

A DAS will not work on exceptionally large creatures. Creatures with a size over 1,200,000 (e.g. an elephant, bronze colossus, etc.) will prevent a drawbridge from raising if they are standing on it, and cause a drawbridge to immediately deconstruct if it is lowered upon the creature. See the list of creatures by adult size for a complete listing of creatures immune to bridges.

## See also

- Building Bridges and Atom Smashers: A Guide by Mechanixm

\]\] Ru:Dwarven atom smasher
