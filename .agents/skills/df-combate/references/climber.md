# Climber

> Fonte: [Climber](https://dwarffortresswiki.org/index.php/Climber) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

Skill: Climber

Association
 

Profession
None

Job Title
Climber

Labor
None

Tasks

None

Workshop

None

Attributes

Strength / Agility / Willpower / Endurance / Spatial Sense / Kinesthetic Sense

**Climber** is a skill which allows a creature to climb. Higher levels improve the chances of successfully stopping the "In flight" status (falling, jumping or being knocked back) by holding onto something and decrease the chance of losing hold when climbing. In fortress mode, dwarves will not climb over walls or trees as part of normal pathing from one job to another. However, they may attempt to climb if stuck in a location (for example, if they've dug themselves into an inescapable channel) or chased by an enemy.

Climbing requires at least one free body part with the [`[GRASP]`](/index.php/Body_token#GRASP "Body token") tag (usually a hand). If a creature has the [`[CANNOT_CLIMB]`](/index.php/Creature_token#CANNOT_CLIMB "Creature token") tag, then it cannot climb, even if it has free grasp parts. Some creatures such as cats and giant cave spiders have a [`[STANCE_CLIMBER]`](/index.php/Creature_token#STANCE_CLIMBER "Creature token") tag and use their [`[STANCE]`](/index.php/Body_token#STANCE "Body token") parts (legs) instead. Starting climbing is not possible while prone, but "In flight" and "In air" statuses override proneness.

To climb a surface, it must be able to be held from the side. Floors cannot be climbed, nor can surfaces, with the exception of tree branches, be held from beneath. Trees and 1 z-level tall cliffs and buildings are always safe to climb. Unskilled climbers will often lose hold when attempting to climb walls (not trees) while "In air" - at least 1 z-level above the floor.

Climbing speed does not depend on stats or skills, but is rather a type of gait. Some creatures (notably giant cave spiders) can climb as fast as they walk. Many kinds of animals are born with Legendary skill in climbing, these normally being either fliers, arboreal, or species found in caverns.

## Climbing surface

Climbing block walls (even at floor level) and attempting to stop one's flight by grabbing onto anything will improve climbing skill, regardless of success. Climbing trees, rough-hewn natural stone, soil, or constructions made of raw material is easiest and is worth 5 exp only when attempting to grab while flying. Climbing block walls is harder, but possible, and is worth 5 exp when climbing and 10 exp when attempting to grab while flying.

Climbing smoothed or engraved natural stone walls is impossible, but smoothed pillars can be climbed. [1]

Cast ice is easily climbed, even when 'straight' (smoothed) or carved into fortifications.

Climbing any protruding floor (or raised drawbridge) is impossible. [2]

## Climbing safety

Non-climbable walls are as easy as putting a floor jutting out on the side you don't want creatures climbing from.

|     |     |     |     |     |     |     |     |     |
|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| z   | \+  | 1   |     |     | \_  | \_  | \_  |     |
| z   | \+  | 0   |     | →   | g   | █   | \_  | \_  |

Goblins don't get in, dwarves don't get out. This works because you can't hold onto the "side" of a floor tile (or more technically, the air above it.) No tile may be held from the bottom, with the sole exception of tree branches.

Don't try to substitute overhanging walls or fortifications for the floors; they *can* be climbed from 1 level below!

|     |     |     |     |     |     |     |     |     |
|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| z   | \+  | 2   |     |     | →   | →   | ↘   |     |
| z   | \+  | 1   |     | ↗   | █   | \_  | █   | ↙   |
| z   | \+  | 0   |     | →   | ↖   | █   | →   | g   |

A two-tile overhanging wall, however, is a safe overhang:

|     |     |     |     |     |     |     |     |     |     |     |
|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| z   | \+  | 2   |     |     | \_  | \_  |     | \_  | \_  |     |
| z   | \+  | 1   |     |     | █   | █   | \_  | █   | █   |     |
| z   | \+  | 0   |     | →   | →   | g   | █   | \_  | \_  | \_  |

Any combination of floors/fortifications/walls works for the top, as long as they protrude out at least two tiles.

Safe minimalist fortifications:

|     |     |     |     |     |     |     |     |     |
|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| z   | \+  | 2   |     |     | \_  | \_  |     |     |
| z   | \+  | 1   |     |     | ╬   | \_  | \_  |     |
| z   | \+  | 0   |     | →   | →   | g   | █   | \_  |

The fortification acts as the 2nd overhanging tile. Note that the roof, above the lower floor tile, prevents archers from jumping off the wall and charging the enemy, and protects them from flying creatures.

Safe miminalist bars:

|     |     |     |     |     |     |     |     |     |
|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| z   | \+  | 2   |     |     |     |     |     |     |
| z   | \+  | 1   |     |     |     |     | ‼   | \_  |
| z   | \+  | 0   |     | →   | →   | g   | █   | \_  |

Because the bar is a building, it has no grabbable surface area on the side to lift one up by, though beware enemy archers.

Creatures cannot jump up z-levels. They *can* jump straight through fortifications while hanging on the side, although not necessarily will always.Bug:8160

Potentially unsafe:

|     |     |     |     |     |     |     |     |     |
|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| z   | \+  | 2   |     | \_  | \_  | \_  |     |     |
| z   | \+  | 1   |     | →   | ╬   | ↘   |     |     |
| z   | \+  | 0   |     | →   | ↖   | █   | →   | g   |

Lastly, always be wary of trees; it goes without saying that they are the enemy of dwarfkind. Trees can be used by invaders as siege towers to leap onto your walls, therefore it follows that a paved road around your walls, or digging out the z-level below the area, are effective ways of holding back the wooden menace.

## Adventure mode

Adventurers with a free, working grasp can climb by holding an adjacent wall (possibly offset by 1 z-level above or below) or tree branches 1 z-level above. This initiates the "Climbing" status, which allows you to move in any direction relative to the wall, including straight up and down with \ and \> or diagonally upwards and downwards with Shift-direction and Ctrl-direction, respectively. Any movement prompts for which surface and hold to climb to next; choosing a surface on a different z-level moves you to that z-level even if you did not input a diagonally upwards or downwards move. Adventurers cannot initiate climbing while on the ground (meaning you cannot prop yourself up against a wall in one final, daring stand), though you can initiate climbing while swimming.

When falling or "In flight", passing by a graspable surface opens a menu allowing you to attempt to stop your fall by latching on to the surface. Releasing the hold with h or going prone with s while climbing immediately removes the "Climbing" status, causing you to fall. Doing so 1 or 2 z-levels from the ground (or water) is typically safe, though much higher up can have serious consequences if you fail to grab something.

Climbing most walls and trees neither requires nor grants any skill in climbing. As noted above, the exceptions to this rule are climbing block walls, e.g. most walls of generated buildings, and attempting to stop your flight by grabbing on to any wall or tree. Accordingly, the quickest way to train climbing is to jump along a block wall while attempting to grab it, possibly using a macro.

## Bugs

- Dwarves climb trees and refuse to climb down until they die of thirst.Bug:9252Bug:11284 With timely intervention, they can be saved by cutting down the tree or building stairs alongside a branch.
- Adventurers can be mostly unable to climb if they woke up stunned.Bug:8543 Work around is to wait an hour after waking up stunned.
