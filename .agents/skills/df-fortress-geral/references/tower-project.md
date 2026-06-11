# Tower (project)

> Fonte: [Tower (project)](https://dwarffortresswiki.org/index.php/Tower_(project)) — Dwarf Fortress Wiki (GFDL/MIT)

*Not to be confused with necromancer's towers "necromancer's towers").*

A **tower** is any vertical structure consisting of multiple levels of a similar shape stacked on top of each other, often connected by stairs.

As a player construction, a large tower can serve the same role as a below-ground fortress, but without the drawbacks of cave adaptation: all of its tiles being Light Above Ground, so the dwarves will always be exposed to sunlight. However, it takes a large amount of resources (usually stone or wood) to construct a tower; while a source of clay or green glass can alleviate this, it is still much less efficient than carving out a fortress entirely beneath the earth.

Usually, a tower is built from constructed walls, floors, and stairs, although on some levels (such as those being used for the barracks) walls may be carved into or replaced by fortifications. With sufficient planning, a tower can also be cast from obsidian or, in an appropriate biome, ice.

### Construction

Getting "up" is not a problem - an up/down staircase can be built, one z-level at a time, just ordering the next level to be built on the previous, once that has actually been constructed. (You can't order constructions based on "future" construction.) There is an upper limit though, 15 z-levels above the highest point of land at your location. If in doubt, build a test staircase first.

And a dwarf can walk on top of a wall, which creates a walkable surface on the next level up. This is not *technically* a "floor", which is a specific construction, but can be walked upon just the same. (A floor blocks construction of a wall on that same level - one or the other, plan ahead!)

The problem can come when creating those walls. Because dwarves require an orthogonally adjacent tile to construct walls, creating a multi-z-level wall can be a logistical challenge. It is possible to use the floors provided by the lower level walls to construct the next level, though this requires staggering construction designations to build the walls farthest from an access point first. If you have an abundance of material (and plan to build floors on the inside anyway), you can use the implied floors from the walls below to construct an inner ring of floors, then use those floors to construct an outer ring of walls. Less resource-intensive temporary access can be provided by building one-tile-wide bridges as "scaffolds" around the interior.

Alternatively, staggering the tower walls can simplify construction:

`    z              z + 1           z + 2`

........... .╔═══════╗. +++++++++ ╔═════╗ .║.......║. +╔═════╗+ ╔\[#f00\]╝\[#\]+++++\[#f00\]╚\[#\]╗ .║.......║. +║ ║+ ║+ +║ .║.......║. +║ ║+ ║+ +║ .║...X...║. +║ X ║+ ║+ X +║ .║...O...║. +╚══\[#f00\]═\[#\]══╝+ ╚\[#f00\]╗\[#\]++\[#f00\]O\[#\]++\[#f00\]╔\[#\]╝ .╚══O.O══╝. +++++++++ ╚══╩══╝ ...........

` .  ground`\
` ═  wall`\
` X  stairs`\
` +  floor provided by wall below `\
` [#f00]═[#]  wall built last  `

This design lets you designate (almost) an entire level at a time using large swaths, allows multiple builders to work simultaneously without problems, uses fewer blocks and jobs, and requires no slow remove-construction jobs. It can be continued higher by alternating the top two levels.
