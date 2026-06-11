# Shell

> Fonte: [Shell](https://dwarffortresswiki.org/index.php/Shell) — Dwarf Fortress Wiki (GFDL/MIT)

A **shell** is a hard external covering used by certain creatures for defense.

As obtaining shells implies killing the creature that created it (like mussels), elves stop trading with you if you offer any item crafted from shells.

## Acquiring shells

In most cases, they are acquired as part of your fishing industry: dwarves may catch shelled vermin critters such as turtles, oysters, and mussels, which produce a shell when processed at a fishery. These creatures will also leave behind their shells if left to rot long enough after being caught. They may also be obtained from butchering a few land animals, such as armadillos, desert tortoises, giant forms of many shell-bearing vermin, and, with luck, certain fun creatures.

Be aware that shells cannot easily be acquired via trading – any non-caged turtles, crustaceans, or shellfish purchased from traders have already been processed and had their shells removed. As a result, fortresses with no naturally occurring above ground fishing sites can struggle to acquire shells. This can cause problems if a shell-preferring moody dwarf requests shells as a material. To avoid the risk of dwarves attempting to make impossible artifacts, you can catch pond turtles by having fisherdwarves fish in an outdoor pond. As long as there is a population of pond turtles in the area, your fisherdwarves will eventually catch some, which can be shelled in a fishery. Alternatively, you may be able to capture or trade for tortoises, armadillos, or other **non-vermin** shell-bearing creatures for the purposes of animal husbandry. Procedurally-generated creatures that have shells will also provide a stack of shells when butchering - if this is your only source of shells, be sure to save them for strange moods.

Whichever process you use will likely take a significant amount of time, so make sure you do it *before* the strange mood strikes.

Also, be aware that, due to a bug, fishing will eventually cause an extinction of shell-bearing fish. This process can take years, or even decades, depending on how aggressively your fort fishes, but will always happen eventually. If your economy relies on trading shells and shell crafts, or you wish to have some for a strange mood, you should plan ahead for this eventuality.

## Uses

Shells can be worked by a dwarf with the bone carver skill. They can be used for many of the same purposes as bone, such as in making crafts, decorations, and cheap, lightweight, low-defense armor (leggings, gauntlets, and helms only). Notably, unlike bones, they cannot be used to produce bolts.

Shells can be stored in a refuse stockpile. Stored shells will decay over time due to vermin, but even a small fishing industry can produce many shells very quickly. As such, having a bone carver on hand to convert them to trade goods can be an effective way to generate wealth early on; even though shells have a low innate material value, quantity can win out over quality here. Also, shell armor is better than nothing and doesn't slow down your military like metal armor does – consider producing some early on if you can't immediately acquire metal armor.

## Modding

In previous versions, shells were frequently requested by moody dwarves, and difficult if not impossible to obtain. As of the current version, only dwarves with a preference for shells will demand them for artifacts. Shells are still hard to come by, though, so players occasionally mod the game to make sure their fortress will have shells available.

### Adding shells to existing creatures

The combination of the common requirement for shells during strange moods, the bug that causes shell-producing fish to be unavailable in many maps, and the inability to trade for shells may lead to unresolvable strange moods. It is possible to modify the raws to allow other creatures to produce shells, if the player is so inclined:

1.  In raw/objects/creature_domestic.txt, find "\[CREATURE:COW\]"
2.  Alter the \[BODY\] section to include ":SHELL" i.e., \[BODY:QUADRUPED_HOOF:TAIL:2EYES:SHELL:BRAIN...\]
3.  Add the \[USE_MATERIAL_TEMPLATE:SHELL:SHELL_TEMPLATE\] tag to the \[BODY_DETAIL_PLAN:STANDARD_MATERIALS\] section
4.  Add the \[USE_TISSUE_TEMPLATE:SHELL:SHELL_TEMPLATE\] tag to the \[BODY_DETAIL_PLAN:STANDARD_TISSUES\] section
5.  Add the \[BODY_DETAIL_PLAN:SHELL_POSITIONS\] tag to the creature
6.  If you wish to apply this change to a game in progress, remember to also alter the copy of creature_domestic.txt contained in your saves folder, as each game has its own copies of the raws.

Slaughtering a cow should now produce a "Stray Cow shell" usable by dwarves stuck in strange moods. Pay attention, that editing creature after creating world may cause later crashes when changing game's version. In fact, after porting the save to the modified version, the game will crash every time your dwarves try picking up the skeleton that previously had shell. It's **strongly** recommended to use the second way, as it doesn't add any new body part to creatures, but only adds a new way of using an already existing body part, which is much less crash provoking.

### Enabling other materials to be used in moods

If you don't want to add shells to existing creatures, you can enable other materials, like hooves or ivory, to be used in strange moods instead of shells. The only effect is that the materials will be available for moods, you won't be able to e.g. make shell crafts of them.

1.  In raw/objects/material_template_default.txt look up the material you want to enable, for example \[MATERIAL_TEMPLATE:HOOF_TEMPLATE\]
2.  Add the \[SHELL\] tag to the material
3.  If you wish to apply this change to a game in progress, remember to also alter the copy of material_template_default.txt contained in your saves folder. The change won't affect body parts that are already lying around, but will affect newly created body parts from butchered creatures.
