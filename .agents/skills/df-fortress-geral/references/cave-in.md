# Cave-in

> Fonte: [Cave-in](https://dwarffortresswiki.org/index.php/Cave-in) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

A section of the cavern has collapsed!

A cave-in from the floor above.

A **cave-in** is when walls, floors, and other terrain plummet downwards to lower Z-levels under the influence of gravity. A cave-in will occur if constructions or ground tiles are detached from all support (bridges and hatches do not provide support). Since it is only a placeholder, the system is highly unrealistic—you can hold up a giant megafortress by a slender pillar of soap. Toady One has stated he intends to implement more realistic cave-ins in future versions.

Cave-ins can be disabled in the settings.

## How cave-ins work

Any *disconnected* construction or section of rock or soil will cave in. The game checks for connections along the X, Y, and Z axes (that's left/right, up/down, and above/below). Any construction, even stairs (natural or constructed), and supports (naturally) provide support/connections. Tree trunks provide support on all axes. Up stairs will provide support for the z-level above even if there is no downstairs above, acting as an invisible floor. **Diagonal connections and bridges do not provide support.** Ramps will not provide support to the tile above them, but will act as a connection for the adjacent tiles on the same level.

Note that supports and fortifications, but **not** statues, create an invisible floor on the level above them. No dwarf can enter the invisible floor, but it will hold an area attached to the floor tiles in four directions alongside it or the constructed/natural wall above it.

## Results of a cave-in

### Falling terrain

- Any unsupported terrain crashes down through multiple floors and ramps, and stops only upon reaching a wall, up or up/down stair, a fortification, a multi-tile tree, or a support.
- Falling tiles do not stay connected in one mass; each falling column will fall as far as it can as described above.
- Falling natural floors, stairs and ramps will be destroyed, leaving behind a natural floor of the highest such terrain; natural stone walls pile up; and constructions deconstruct, leaving behind their building materials.
- Trees, shrubs and saplings that fall are obliterated. Falling grass of all types (including cave moss and floor fungus) gets turned into undifferentiated green "Grass".
- Anything falling into a fluid sinks to the bottom. Therefore, it is not a good idea to punch a skylight into your meeting area if you forgot that e.g. your gem pile was directly below and you had a magma tube three Z levels afterwards... you get the idea.
- Falling soil will change into the soil type at the layer it falls to, or the lowest type on the map if it falls into the stone layers.
- Aquifer tiles will continue producing water, and other tile properties will remain the same in the fallen terrain.

### Below the cave-in

- Any creature caught directly underneath (on the same tile underneath) a cave-in is killed, the only exception being Ghosts. To clarify, it will kill all non-ghost creatures between the tile below the initial tile caving in to its final resting point.
- Most plants under a cave-in are obliterated, but not multi-tile trees.
- Any item caught under a cave-in is destroyed completely, unless the item is a stone boulder (i.e. not including ice), a rough gem, a corpse (but not a severed body part), or an artifact.
- All buildings and most constructions under the falling area are destroyed, as are natural ramps and unsupported floors. Only walls, supports, up and up/down stairs, and fortifications (both mined and constructed) remain intact.
- Supported natural terrain will remain intact during the cave-in (terrain unsupported from below will collapse).
- Any fluid displaced by falling natural walls is not destroyed, but transported to directly on top of the fallen walls. This principle can be used to construct magma pistons.
- Any mined minerals or stone in the area directly under the cave-in will be forced out from under the cave-in (or even up a few z-levels too, if the cave-in falls a long distance).
- Dropping rock layers on top of a cavern-soil floor will remove the soil; irrigation will be required to resume tree farming.

### Above the cave-in

- Buildings above the cave-in will deconstruct if they are no longer supported.
- Anything standing on the area that caves in falls and may get away with being stunned. The fall victim has a chance of being unable to walk away, somewhat proportional to the distance fallen but not set in stone. ~~No~~ Pun intended.

### Other effects

- A large amount of dust is generated, as pictured to the right. Any creature caught by the dust from the collapse is knocked unconscious and can be thrown a few tiles even up z-levels, which may cause them to fall off, say, a narrow bridge fifty z-levels above the ground, or can mash them into a fine paste against the wall. Dwarves will receive an unhappy thought from choking on dust clouds (which won't matter if they're dead).
- Magma mist will be generated in all tiles of magma that were in the path of the cave-in.
- Any terrain that is rendered unsupported by the cave-in will cause a subsequent cave-in.

## Avoiding cave-ins

Do not make unconnected sections of rock.

Actually, you're quite unlikely to cause cave-ins unless you are actively trying to cause them. In which case, you'd be wondering how to avoid cave-ins that *cause damage* to your folks. That's simple: Add a support under the stone mass, and link it to a distant lever. When you're done, hide everyone, pull the lever and watch the fireworks. If you're feeling lazier, use statues to keep dwarves off the wrong squares. Provided they move directly away from the cave-in area, the dust may not catch them - and they don't blunder off edges and die unless the dust catches them.

One of the more common accidental cave-ins results when you're taking out the floor in a checker-pattern (dwarves channeling may sometimes tend to make this mistake) and the area below isn't supported, resulting in a situation like the diagram below:

    Floor -1
    ▒▒▒▒▒▒
    ▒    ▒
    ▒ X +▒ <-- The X is a floor tile. It's not attached, so it will fall down.
    ▒  +>▒
    ▒    ▒
    ▒▒▒▒▒▒

    Floor -2
    ▒▒▒▒▒▒
    ▒....▒
    ▒...▒▒ <-- Causing this area to receive a cave-in flow and knocking out any dwarves in its reach.
    ▒...<▒
    ▒....▒
    ▒▒▒▒▒▒

Another thing to watch out for is if you want to dig away a hill above ground, to make room for your fancy overground fort. You may dig away the hill on one level, and then have a huge platform of "floor" on the z-level above that falls on your miner if they get disconnected from the ground. Easy thing to miss the first time you do it. To avoid this, channel *from the surface downwards*, which doesn't remove anything that isn't supported - though you might still mine out something that was supporting a floor you *weren't* mining, so be careful. Miners also don't check that there's nobody standing on the floor that will shortly cease to exist - meaning that several miners channelling floors in the same area are a danger to each other. So you should allow only one dwarf to mine out floors in an area at a time.

## Using cave-ins

Intentional cave-ins serve several purposes:

- **Terraforming**
  The natural floor tiles will preserve their type after falling several z-levels. It's a good way of moving the sand and clay tiles deeper, closer to the magma furnaces. A controlled cave-in of upper soil layers will help make an underground pasture field. Moving a whole layer of soil floor tiles along with the supporting soil layer will make it possible to create an underground orchard. Over time, tree saplings specific to the surface biome will start growing on this caved-in soil. The supporting layer must remain unmined to allow the growth of roots.
- **Defense** / **Cavern Control**
  Use cave-ins to block off the edges of cavern lakes. Combined with walls higher up (and ordinary constructions for non-flooded map edges), a cavern can (with great effort) be rendered completely safe from all intruding vermin1. This can also be used to completely drain a cavern lake for subsequent tree farming.
- **Death**
  Since a cave-in kills all creatures instantly, it can provide a convenient or amusing way to off a group of creatures. This is also one of the most effective ways of dealing with titans and forgotten beasts with dangerous syndromes, especially airborne contaminants (deadly dust/vapors) and poisonous blood. For certain randomly generated creatures, they may be so indestructible that a cave-in is the *only* way to kill them. Also, it's a great way to "mercifully" deliver an "injured" dwarf from the "wretched" fate of lying in a bed all by himself.
- **Removal of floor tiles**
  Causing a cave-in will destroy non-reinforced (no wall or support underneath) floor tiles directly underneath the falling terrain – this is a good way to hollow out a large area. All that's left to do is a little bit of cleanup on the edges, but look at all the channeling you saved yourself!
- **Breaking through multiple aquifer levels**
  Showcase with two levels: User:Rhenaya/HowtoDualAquifer
- **Trapping \[TRAPAVOID\] creatures:**
  Since the dust from a cave-in can knock creatures unconscious, and any unconscious creature triggers a trap (including your dwarves and other friendly creatures), combine a cave-in with nearby cage traps for the capture. Note that this is only useful for kobolds and gremlins, as all other creatures which avoid traps are also immune to being knocked unconscious.
- **Moving water/magma faster than pump stacks**
  Main article: Magma piston

### Caving in the top level/terrain from inside

You can cause terrain above you to cave in without going outside by first mining up stairs below the "borderline" you want to channel, channel the tiles above them, and removing the stairs afterwards. The tiles above the up stairs can be mined from below while standing on the stair, so you don't have to go outside. Ramps would also work for that alone, but the ramps would allow enemies to enter, whereas the up-stairs alone do not allow passage to above as there is no corresponding down-stair above them.

1Not literal vermin; those won't be blocked.

## Bugs

- Layer material can change when collapsing soil layers.Bug:1206
- Forest fires cause constant collapses.Bug:6829
- Rarely, a cave-in may happen right at the start of the game. This can have several effects depending on where it happens, including releasing underground tree spores.
- Cave-ins can occur randomly if you dig out an area of surface containing trees, creating lots of fun.Bug:9479
