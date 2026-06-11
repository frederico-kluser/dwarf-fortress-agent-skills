# Building destroyer

> Fonte: [Building destroyer](https://dwarffortresswiki.org/index.php/Building_destroyer) — Dwarf Fortress Wiki (GFDL/MIT)

**Building destroyers** are creatures with the token and will actively seek out various furnishings, workshops and other buildings and topple or destroy them. Uncompleted constructions are vulnerable, but completed ones are not. They come in two varieties, the first being annoying, and the second dangerous. Most buildings will be "toppled" (deconstructed), leaving the building material or furniture unbuilt but otherwise unharmed, however doors, hatch covers, and floodgates will be damaged until destroyed, not deconstructed.

Creatures with this tag are gifted with an incredible ability to sense exactly where your buildings are, and will generally charge a building from 10 tiles away, with the exception of forgotten beasts and (semi-)megabeasts. Plan your defenses accordingly. Building destroyers still prefer to attack creatures, and if a valid creature target for their aggression is or becomes visible to them, they will abandon building destruction in favor of classic creature destruction.

The time it takes for a building destroyer to destroy a building depends on the quality of the building. Artifact quality furniture can never be damaged or destroyed, but some kinds of artifact furniture will be deconstructed by a building destroyer, given enough time: for instance, artifact statues will eventually be deconstructed; artifact hatch covers never will.

Building destroyers will destroy nearly **all** types of buildings they can reach, whether or not they block their path - doors, floodgates, hatch covers, vertical/horizontal bars, floor/wall grates, statues, workshops, and even furniture are vulnerable. The only buildings that will be spared by a building destroyer are wells, bridges, roads, traps (including levers and track stops), animal traps, chains, cages, stockpiles, upright weapons, and any buildings submerged in 4/7 or deeper liquid (even if they're innate swimmers). They can destroy most furniture and buildings from a lower z-level when a valid path exists to that furniture, though locked hatches and closed grates are safe as long as no alternative paths exist. Building destroyers will path to and destroy even opened (or stuck open) doors, hatches, floodgates, or vertical bars. They will cause damage to any attached mechanisms during building destruction, sometimes leading to the unlinking of furniture to a lever before the furniture in question is fully destroyed.

## Destroying from underneath

Building destroyers cannot destroy buildings unless they can path to the building on the z-level of the building. This means that building destroyers **cannot** destroy, for instance, a forbidden hatch above them (note that non-forbidden, i.e. passable, hatches are vulnerable!) or a magma forge from the magma underneath it **unless** a clear alternate path to the building exists. If such a path exists, they do not have to follow it; they can destroy the building from the z-level below while standing on a ramp or stairs that leads up to the building's z-level.

Consider the following diagrams, as viewed from the side:

[TABLE]

[TABLE]

[TABLE]

[TABLE]

[TABLE]

This was tested with trolls in an entrance-way accessed by both lever-controlled floodgates and a manually locked door. Ramps led up to the floodgates and the door. When both were closed, the trolls showed no interest. When the door was unlocked, a troll began to destroy it. When the door was locked again, the troll went away. When the floodgates were opened, a troll returned and destroyed the locked door from the ramp outside, while the open floodgates were also apparently being destroyed from the ramps by other trolls. This may be related to the bug in which dwarves appear to be building diagonally as long as they can access the spot orthogonally. It is unknown whether this applies to an open path extending through the full length of a fortress, rather than just a few steps away through open floodgates.

## Annoying Variety: level 1

When the value is **1**, the creature will go after statues, windows (glass or gem), archery targets, slabs, wooden doors, and wooden hatches. They can't destroy homes during world gen as (semi)megabeasts.

**\[BUILDINGDESTROYER:1\] creatures:**

- Cave crocodile
- Giant cave spider
- Giant desert scorpion
- Giant olm
- Giant cave toad

## Dangerous Fun Variety: level 2

When the value is **2** the creature will actively seek out buildings and destroy them. They can also destroy buildings during world-gen with this tag. Megabeasts rely on this token for their pathing when attacking your fort. Constructions (walls, staircase, floors, etc.) are still safe, since they're processed the same way natural terrain is for most situations.

The simplest way to keep building destroyer 2's from targets is with walls or channels. A drawbridge will act like a constructed wall *(if up)* or floor *(if down)*, blocking building destroyer 2's without that danger of being destroyed.

Tame animals still carry their building destroyer tokens, and have been observed to occasionally topple a statue.

**\[BUILDINGDESTROYER:2\] creatures:**

- Amethyst man
- Blind cave ogre
- Bronze colossus
- Cave dragon
- Cyclops
- Dragon
- Ettin
- Experiment
- Fire man
- Gabbro man
- Giant
- Hydra
- Iron man
- Magma man
- Minotaur
- Mud man
- Ogre
- Sasquatch
- Troll
- Voracious cave crawler
- Yeti
- All forgotten beasts, titans, and demons
- Werebeasts (in werebeast form only)

Level 2 building destroyers can destroy chairs, beds, tables, coffins, non-empty farm plots, furnaces, trade depots, shops, doors, floodgates, chests, weapon racks, armor stands, workshops, cabinets, statues, glass windows, gem windows, siege engines, archery targets, your embark wagon, screw pumps, unfinished constructions, floor hatches, wall/floor grates, wall/floor bars, gear assemblies, horizontal/vertical axles, water wheels, and windmills.

See the Modding guide for more information on creature tokens.

## Capture

Considering a good part of the building destroyers are useful to capture, and that most of them are not trapavoid, you can easily trap them with the right arrangement of cage traps, furniture and walls.

See Trap design for more information on this subject.

## Undead

All undead building destroyers are level 1 (except if they are undead versions of level 2 destroyers), and they also gain the ability to destroy wooden supports, which generally ends poorly for the creature.

Due to the way undeath is classified, "non-living" creatures such as magma men, bronze colossuses, and inorganic forgotten beasts/titans are also considered to be undead.

## Bugs

- Building destroyers can, and will, destroy buildings even if there's one tile of empty space between them and the building. In fact, they cannot destroy immediately adjacent buildings, and they can become stuck if they start destroying the building while adjacent. This can be a result of a fight, for instance when a Forgotten Beast kills the last defender while standing in such a spot, then it won't move to a better suiting position and will stand idling, unless killed or distracted.
