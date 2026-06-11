# Magma mist

> Fonte: [Magma mist](https://dwarffortresswiki.org/index.php/Magma_mist) — Dwarf Fortress Wiki (GFDL/MIT)

**Magma mist** is the !!Fun!! yellow mist created in three cases:

- when debris from a cave-in splashes into magma
- when a fast-moving item or creature skips across magma
- when you drop a sufficiently large item into magma

Unlike normal mist, magma mist is **not** created when magma falls down a Z-level. It sets fire to all non-fire-resistant creatures that share a tile with it.

Magma mist tends to be around longer than cave-in dust, and is created in quantities proportional to the thing dropped into the magma.

When it appears outdoors, it is called *lava* mist instead but is otherwise identical.

Magma mist is **not** to be confused with being "caught in a cloud of boiling magma", a bug involving messages displayed when caught in cave-in dust. This is not something to worry about.

## Preventative Measures

If you are a leaf-loving knife-ear being careful around magma, it isn't very likely that you'll run into magma mist at all, let alone have to worry about your dwarves breathing it in. The simplest thing you can do to prevent it is to watch out when dealing with mining above magma, or channeling above magma in particular.

If you plan on using a magma-based garbage disposal system, have sufficient z-levels between the dumping point and the magma/lava. Mass-dumping a whole siege's worth of corpses, body parts and assorted trash may generate magma mist clouds 3 z-levels high and wide, or higher. A single large corpse (e.g. a troll) is enough to cause a small magma mist cloud, potentially fatal if the magma's surface is just 1 z-level below the dumping point.

[TABLE]

[TABLE]

**Side View.** *Fun (left) and completely safe (right) magma garbage disposal points showing typical magma mist clouds after dumping a few corpses.*

## Weaponization

Magma mist can be used as an ignition device on various targets if you do not want to use magma itself and wait until it evaporates.

Channel a moat right next to your main fortress. Fill it with magma. Drop one (or several) large, unneeded items in the magma from a few higher Z-levels when an enemy walks on the path. It can also double as a waste disposal system.

Of course, since it sets targets on fire, be sure that it does not permit the burning target to reach your dwarves (or booze stockpile), and be sure that the invaders are not fire-immune (like a dragon or bronze colossus). Magma mist can cause the fat to melt off random body parts of creatures, producing between "Minor Melting" and "Moderate Melting". Potentially-fatal "Heavy bleeding" also ensues.

### Designs

Here is an example of a powerless minecart skipping magma mist generator.

This design has a tick cycle of 30 steps with 5/7 magma and 33 steps with 6/7 magma and a max delay of 6. Carts must not collide, or it'll fail. However, it's compact, and lot of mist is produced on the z-level above with multiple carts. This design requires metal minecarts because wooden minecarts are not heavy enough to make magma mist. The initial minecart input is at the bottom. The ramp accelerating to the left is needed due to the checkpoint effect, and the floor and empty space combination cause a small minecart jump.

|     |     |
|-----|-----|
| ╔   | ╗   |
| \+  | ▲   |
| .   | ║   |
| \+  | ▲   |
| ~   | ▲   |
| ▲   | ╝   |
|     | ║   |

**`Key:`**\
`  `**`╔ ╗ ║ ╝`**` = `**`Track`**\
`  `**`▲`**`       = `**`Track Ramp`**\
`  `**`↑ ← →`**`   = `**`Ramp acceleration direction`**\
`  `**`+`**`       = `**`Floor`**\
`  `**`.`**`       = `**`Empty Space`**\
`  `**`~`**`       = `**`Empty space with 5/7 or 6/7 magma below`**
