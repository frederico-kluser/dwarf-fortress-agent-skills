# Water

> Fonte: [Water](https://dwarffortresswiki.org/index.php/Water) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Water** is a fluid found all over the world. It flows from mountain springs, forming the world's oceans, lakes, rivers, and brooks, falling as rain and snow, and freezes into ice. Water is home to a variety of aquatic creatures. Many creatures can swim in deep water, but air-breathing creatures that are submerged in water can drown in it. Water comes in two varieties: **freshwater**, which makes up almost all inland water, and **saltwater**, which fills the seas. Some brooks and murky pools can be saltwater, even if the fortress site is partially mountainous. - it is not known if this is a bug. To tell the difference, attempt to set up a drinking zone including some of the water in question - if there are zero tiles of water source available, the water is saltwater. Mud is a contaminant, which is created any time water covers an area. Any tiles that contain mud may be used for farming.

Water normally will be displayed with a blue tile. You can toggle depth indicators (a white number reflecting the current water level on a given tile) by pressing f or clicking on the Display Water Levels button to the left of the minimap. Water can also take on other colors indicating contaminants, such as **blood**, **ichor**, or **goo**.

Dark-colored water symbols indicate the water is one Z-level below the camera level. Water has 7 depth levels per tile, with 1 being the equivalent of a shallow puddle, and 7 filling the tile completely. Dwarves can safely walk through water up to a depth of 3 - at depth 4 or higher, they will cancel jobs due to "Dangerous terrain" and begin to gain swimming experience. At depth 7, any dwarf that does not have sufficient swimming skill will drown.

Interestingly, water can slow falls - that is, with deep enough water and short enough falls, if the water is deep enough relative to the height of the fall, creatures can be less injured, or even completely uninjured (from a 4-level drop to a 3-level deep pool, for example).

Objects made of wood, including logs, do not float in water; they sink to the bottom like all other objects. Things that enter or fall into water will make visible splashes and ripples.

## Processes

### Evaporation

Roughly 4×4 tiles of a river.

A partially flooded fortress. ASCII mode.

In the normal underground temperature of 10015 °U , evaporation occurs when water or magma is at a depth of 1/7. The exact rate of evaporation is unknown, but it is affected by temperature and surrounding liquids - a single 1/7 water tile will evaporate faster than a large recently-flooded area, or a 1/7 water tile by a river, for example.

At high temperatures (usually found in scorching climates), water can evaporate at greater depths -- even at 7/7. This is generally accompanied by the grass drying out and turning yellow. Such evaporation can be prevented by flooring over water tiles to make them Inside.

Water or magma at 1/7 depth will not evaporate if it is on top of 7/7 depth liquid.

### Freezing and thawing

Many environments get cold enough for water to freeze in winter. When this happens, any water that is Above Ground will freeze into ice. However, water a single tile away that is in an underground tunnel will not freeze.

When water freezes or thaws, it does so *instantly*; therefore, any creature swimming in water when it freezes will ~~die~~ have fun, and anything standing on a frozen pond when it thaws will fall into it and drown if it cannot swim. (Note: This is also true in adventurer mode, so keep an eye on the temperature if you plan to cross a river!) When ice walls thaw, they always leave a 7/7 water tile, even if the tile had less than 7/7 when the ice formed.

Mining ice can produce chunks of ice. Taking these chunks into a stone layer will cause them to eventually melt, turning them into "water" items (much like those hauled in buckets) which can't be used for anything.Bug:360

Caving in an ice wall into a stone layer will cause it to instantly melt into water (provided it does not become exposed to the outdoors), which can be used to get water near the surface in a glacier biome without having to use a pump stack to pump water up from a cavern pool.

If you constructed a well or a floor grate right over the top of some water and it freezes, the item will be deconstructed to its original parts, but some may fall into the water.

#### Freezing point

The freezing point of water, 10000 °U , is an important, if not *the* most important, temperature in *Dwarf Fortress*. Below this point, water freezes into ice, and above this point, ice will melt into water. A biome that never dips below this temperature will make obtaining ice next to impossible, and a biome that never rises above this temperature will require underground storage, magma, or an alternative heating method to obtain liquid water.

Although it is most commonly known as the freezing point of water, 10000 °U is also the freezing points of standard blood, ichor, goo, slime, pus, milk, egg white, and egg yolk. Nether-caps are naturally constantly at this temperature, but will cause neither water to freeze nor ice to melt. The temperature also acts as the condensation point of cave floater gas, at which it becomes cave floater juice. As a result of these dependencies, many creatures will die if they cannot keep their internal body temperature above the freezing point of water.

Below this point, many machine components, including screw pumps, windmills, and minecart rollers will not work, instead displaying "Frozen here". In colder environments, these machines must either be kept indoors or heated with nearby fire or magma.

## Lakes and rivers

### Lakes

During world generation, the world will create lakes. Lakes are large bodies of still water (for an embark tile at least). They usually have rivers coming to-and-from the lake, giving and exporting water to the lake. Take note, however when embarking with even a partial part of the river on your embark tile, for there have been accounts of the lake being higher than your embark wagon, therefore flooding half of the embark tile. It is unknown whether or not this is a bug, but due to the circumstantial evidence, it most likely is. for more information on lakes, see lake.

### Rivers

Rivers are bodies of water created during world-gen, that will flow from their starting point, all the way to either a lake, or the ocean. Rivers can be extremely useful when you embark beside one, however, most rivers have at least a light aquifer on their tile, therefore making it difficult to settle there. Rivers can be used in many ways to help your fort, but if used improperly, will cause mayhem. for more information concerning rivers, see river.

## Properties

### Depth

Water (as well as magma) can be one of seven different depths. You can find out how deep water is by mousing over the tile containing the water or by turning on f numeric fluid depth with a button next to the minimap, or in the settings menu under the *Game* tab.

Water depth ranges from 0-7, where 0 is no water and 7 is maximum depth. Note that water depth is *per Z-level* (or z-index); that is, if a tile is at depth 7/7, it means that the water *on that level* is at maximum depth, not that the water extends down 7 Z-levels. A lake three Z-levels deep, with each level having 7/7 depth, can be thought of as having 21 levels of depth.

Looking at water lower than the depth of its surface can reveal things that are swimming around or have fallen into it.

|  |  |
|----|----|
| Depth | Description |
| 0 | No water present. |
| 1 | Water may evaporate. No effect on dwarven jobs. |
| 2 | Knee-deep. Dwarves will suspend build orders if an affected tile has 2/7 or more water. |
| 3 | Waist-deep. Water at this depth or lower will cause suffocation in aquatic creatures. |
| 4 | Dangerous terrain. Movement trains swimming. Dwarves will not path through water at 4/7 or higher. Minimum height to make an ice wall when frozen. |
| 5 | Head height. Minecarts will skip over fluids at this level. |
| 6 | Over a dwarf's head, but even non-swimmers can tread water at this height for a time. Minecarts will collect fluids at this level. |
| 7 | Risk of drowning. Can have water on floorless tile above. Fortifications no longer provide a barrier to creature movement.Bug:3327 |

### Sourced water

Water that comes from aquifers, as well as any water source that extends from the edge of the map (rivers, brooks, oceans, and some lakes) is considered to be **sourced water**. Any sourced water is an endless supply of water that can never run dry, although it can freeze for part or all of the year in colder biomes. Murky pools, although not 'sourced water' as described here, also slowly generate water during rain storms. This can make it possible for a murky pool to replenish itself even when it has been completely drained.

When using sourced water you should strongly consider installing floodgates, and be aware of how pressure works, or you could easily end up flooding your fortress and having a lot more fun than anticipated.

## Flow

Cut tree logs falling into water, creating splashes and ripples.

Water and magma are both fluids which are constantly trying to **flow** into adjacent tiles until they have filled all available space or until they run out of fluid. Fluids technically move in 9 directions: down, and to the sides. Fluids cannot move diagonally up or down. Fluids at a depth of 1/7 no longer attempt to move unless they can move down. Fluids under pressure can appear to travel upward until the pressure equalizes, though in reality they are moving downward and/or sideways relative to their source. The higher the temperature in the environment, the faster water will flow.

When water falls onto a tile that is already full, the game will always attempt to move it into a non-full tile on the same Z-level that can be legally reached (i.e. without going through a wall or other obstruction), even if it has to "teleport" the incoming fluid a long distance to do so. Only when all available tiles are full will incoming water "pile up" on top. This behavior can be exploited to move water long distances very quickly (see "Getting rid of unwanted water" below).

If the flow is strong enough, it can move objects such as dwarves, pets, stones, weapons, or corpses.

Fluids in *Dwarf Fortress* act like a fairly thick, viscous material. This makes it possible to do highly implausible things like pump out a dry hole in the middle of a river or ocean.

## Contamination

Water can be contaminated in different ways, both natural and artificial. This contamination can have a negative effect on the water's quality, and can even harm dwarves that ingest it.

### Salt water

Dwarves cannot use salt water directly; while healthy dwarves will usually prefer to drink booze, wounded dwarves can only be given water to drink, so if you have only salt water on your map, it is helpful to desalinate it.

To check to see if water is salty, use the z menu and place a water source zone to see how the game shows the pond/pool. If the "Water Source: \#" is 0, then the source is salty. If not, then your dwarves will drink it.

A screw pump or a U-bend made of stairs can be used to desalinate water. Dwarves will drink water from a well over salt water, give it to sick dwarves and use it to clean wounds. Even if you do not designate the well as a water source (which is unnecessary anyway), the dwarves will still use it.

### Stagnant water

Water taken from a murky pool or wetlands biome will be stagnant, just as water taken from near the ocean will be salty. Dwarves get an unhappy thought if they have to drink stagnant water, and a patient whose wound is cleaned with stagnant water will have an increased risk of infection. Stagnant water can be purified by the same means as salt water. Also, if clean water (or even salt water) flows into stagnant water, it will convert it to fresh water.[\[1\]](/index.php/v0.34:Release_information/0.34.09 "v0.34:Release information/0.34.09") Note that water that spawns on the map (such as the output of a screw pump or a dumped bucket) in a tile orthogonally adjacent to a tile of stagnant water, will itself spawn as stagnant water.

The game will describe stagnant water as stagnant if it was in a bucket or flask/waterskin, and looking at standing or flowing water with k will indicate whether or not it is stagnant.

### Water laced with mud

If a water source is only one Z-level deep and its floor is covered by "a pile of mud" (like most underground pools), then any water taken from it will be "water laced with mud". Drinking water laced with mud will give your dwarves an unhappy thought. It might also cause infection if used to clean a wound, similarly to stagnant water.

Unlike stagnant water, merely moving the water with flow or gravity, or keeping a level of water higher than one Z-level will take care of the problem, since it only occurs if the water source tile contains "a pile of mud", and water coming into contact with a clean floor only creates "a dusting of mud".

### Contaminants

Water can be tainted by contaminants - it is considered tainted when the specific tile in question has more than a dusting/spattering directly on it. Water can be tainted by a contaminated creature going through it, by flowing over dirty items or terrain, directly spilling contaminant into a tile, or by placing LIQUID_MISC items straight into water. Water can wash contaminants into walls, but walls will not spread contaminants to water.

If a creature walks through contaminated water without shoes, they'll come into contact with contaminants therein\[Verify\], transferring any contact syndromes. However, water contaminants obtained on creatures as a result of this process will not be considered tainted.

Water items - such as in buckets when withdrawing water from a well - will always describe what contaminant they're tainted by. However, emptying out the buckets will not produce the contaminant. Additionally, stagnant and salt are special types of contaminants that change the description of liquid water itself.

A dwarf that drinks the contaminated water will be affected by the contaminant if it has ingestion or contact syndrome, and contaminated water is always considered dirty, giving an unhappy thought to the dwarf.

Contaminants that get into water currently can do very strange things. A pool of blood that gets covered by water will be pushed out of the water as the water flows, creating more pools of blood at the edge of the water. Overflowing a large reservoir that contains contaminants of blood will generate a large amount of blood very quickly. This behavior is thought to be ~~the will of Armok~~ a bug.\[Verify\]

## Getting rid of unwanted water

Water will flow off the edge of the map endlessly, which is one way to get rid of large amounts of water (evaporation works better with small amounts). Underground, there are at least two ways to accomplish this. One is to channel your excess water into a dry cavern that is open to the map edge, as the water will flow out (depending on slopes, original water level and such). Be careful if you dump the water into an underground lake, as such lakes have some sort of equilibrium built into them, and your excess water may cause them to flood. The other, probably easier method, is to mine to the map edge (since you cannot mine the map edge itself, just up to it), then smooth the edge and then carve fortifications into it. Water will flow through the fortifications and off the edge of the map. Make sure your exit flow is equal to or, for safety, greater than your input.

Draining lakes and oceans from underneath can be a finicky task, but there's a bit of dwarven magic for it: build a retractable bridge on the level beneath the sea bottom, with ramps directly underneath it. Link this to a lever to control the flow as you desire. Now evacuate the dwarves and wall off the area above the bridge. Then, with the bridge in place, designate ramps around the bridge leading up - breaking through to the sea bottom. Now how can the dwarves dig these squares out? Yep, from beneath the bridge. In this way, they get the water flow started without ever getting their feet wet. This is a great way to set up channels one square in from the map edge near a water source, so that you can properly wall off the baddies from getting into the fort.

**NOTE: This technique no longer works. Attempt at your own risk.** If you simply need to tap a single tile of the bottom of a lake/ocean there is a simple ~~and completely foolproof~~ way to do it; dig a tunnel under the lake, and place a door at the very end of the tunnel. Now order the dwarf to dig an upward ramp at the end of the corridor (the upward ramp will pierce the bottom of the lake), he will do so while standing in the door tile and once he finishes digging he will take a step back and the door will automatically close preventing water from following the miner. The final step is to connect a lever to the door and pull the lever to open the door. Done right, this method allows piercing even the deepest lakes without risk to the miner and also provides a way of blocking the flow in future.

Due to the way the game handles water flow, making your drainage vertical rather than horizontal whenever possible will drain water much more quickly and efficiently. IE: A tunnel one tile wide and two Z-levels deep will drain water considerably faster than a 2 tile wide tunnel on a single Z-level.

Dwarves, especially babies, have an almost-supernatural talent for finding ways to get washed down drains. Putting grates or floor bars over any drainage holes, no matter how unlikely they seem, will reduce tantrums by grieving parents.

Liquid of life. or more commonly in Dwarf Fortress: liquid of !!FUN!!

|  |
|----|
| "Water" in other / Languages / Dwarven / : / arel / Elven / : / alu / Goblin / : / esp / Human / : / thomo |

    [MATERIAL:WATER] - reconstructed from data extracted from memory
        [STATE_COLOR:ALL_SOLID:WHITE]
        [STATE_NAME_ADJ:ALL_SOLID:ice]
        [STATE_COLOR:LIQUID:CLEAR]
        [STATE_NAME_ADJ:LIQUID:water]
        [STATE_COLOR:GAS:CLEAR]
        [STATE_NAME_ADJ:GAS:steam]
        [STATE_NAME_ADJ:SOLID_POWDER:snow]
        [STATE_NAME_ADJ:SOLID_PASTE:slush]
        [BASIC_COLOR:1:0]
        [BUILD_COLOR:3:0:0]
        [TILE_COLOR:7:7:1]
        [SPEC_HEAT:4181]
        [MELTING_POINT:10000]
        [BOILING_POINT:10180]
        [SOLID_DENSITY:920]
        [LIQUID_DENSITY:1000]
        [EVAPORATES]
