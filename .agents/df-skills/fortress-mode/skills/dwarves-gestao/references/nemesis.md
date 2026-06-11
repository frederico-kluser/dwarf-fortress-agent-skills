# Nemesis

> Fonte: [Nemesis](https://dwarffortresswiki.org/index.php/Nemesis) — Dwarf Fortress Wiki (GFDL/MIT)

A **nemesis** is a record that links historical figure identifiers to unit identifiers, in other words, it keeps track of what abstractly happens to an off-map historical figure, and takes it into account when you encounter it on a map (in both fortress and adventure mode), and vice-versa. Nemesis records will, for instance, keep track of a creature's relationship links like parenthood. Creatures that aren't historical figures, obviously don't have a nemesis record.

When historical units are offloaded (e.g. when visitors leave the map in Fortress mode or when you walk away from a settlement in Adventurer mode), they are saved to files named "unit-N.dat" in your world's region folder. In versions 0.34.11 and earlier, corruption of these files could lead to the game crashing with the error "Nemesis Unit Load Failed" - newer versions presumably handle this situation gracefully by generating new unit data.
