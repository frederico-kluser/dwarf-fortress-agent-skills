# Gravity

> Fonte: [Gravity](https://dwarffortresswiki.org/index.php/Gravity) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*"The bigger they are, the harder they fall."*

**Gravity** in *Dwarf Fortress* shares similarities to the real world, but has some key differences. Items, creatures and fluids will descend under gravity, moving to a lower z-level in the right circumstances. Lighter-than-air gases (such as miasma and steam) will ascend z-levels. While this mimics the real world, the biggest key differences are listed below:

- In a cave-in, terrain collapses to the lowest point instantly, however items, creatures and buildings fall more slowly (over multiple ticks).
- Buildings in a cave-in will instantly deconstruct before they fall, and the resulting items will then fall separately.
- Liquids such as water and magma will realistically flow downward, as well as spread itself. The two liquids even flow at separate speeds, matching the viscosity of them in real life. Screw pumps can transfer the liquids upward, and can flow through metal bars. Constructions such as floodgates and hatches can impede their flow.
- Items and creatures that are thrown, shot, cut off and sent flying, knocked back or generally expected to travel in a parabolic arc will tend to do so (within the limitations of the game tiles); one notable exception is for siege engines, which currently launch projectiles in a flat trajectory. When the projectile reaches the limit of its range or hits an obstacle, it stops moving forward completely and falls down vertically, at a fixed speed of 6 steps per z-level, without accelerating.
- Creatures and items accelerate while falling. Water falls at a semi-random rate, taking between 5 and 20 ticks to fall a single z-level.
- Creatures that fall into water decelerate, generally suffering less overall damage upon impact with the bottom. Drowning while stunned, however, is still a concern.
- The density of the material in the landing zone can have a significant effect on the outcome of a fall. Light materials like featherwood reduce the risk of serious injury, while dense materials like platinum increase it. Falling damage below 0.2 tiles/step speed is simulated by being hit by a size 7290 blunt object with 100000 contact area[1].
- Creatures that are dropped onto a standing creature's head will generally suffer little damage regardless of how many z-levels they fell. The unfortunate creature who broke their fall may suffer significant damage, however.
- The value of *g* in DF for a falling dwarf is .032075 ± .000015 Z-levels/tick^2 based on drops of 59 z-levels done on v0.34.10. More recent tests on v0.42.0X show this value appears to have stayed constant. The value of *g* is the same for inanimate objects and may be the same for liquids. The latter needs testing.
- Falling entities observe the (mostly-hard) speed limit of terminal velocity, 270000 distance units per tick. Since a tile is 50% higher than it is wide, that translates to a maximum free-fall speed of 1.8 z-levels/step. Both creatures and objects are subject to this limitation. It should take 56 steps and 52 z-levels to reach this speed. Presumably, a 200-z fall is no different in effect from an exact 52-z one, since the falling object's or creature's velocity will not increase past this point.

In general, falls of 1-2 z-levels are unlikely to cause significant damage to your dwarves, and goblins have been seen to fall more than four with only light bruising and stunning. Large falls (30+ z-levels) will tend to cause the hapless victim to explode upon impact. The minimum drop with 100% mortality appears to be around 25 z-levels.[2]

On the other hand, falling items and creatures can cause grave injury to any creature they fall upon, even when falling a single z-level.Bug:5945 A falling giant cave spider web can easily break the neck of your master weaver, while worn clothing is liable to maim or kill anyone below. Refuse dumping may therefore be weaponized - just take care that your own dwarves do not mistakenly pummel one another with falling stones.
