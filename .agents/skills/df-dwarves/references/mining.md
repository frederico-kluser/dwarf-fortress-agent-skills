# Mining

> Fonte: [Mining](https://dwarffortresswiki.org/index.php/Mining) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

|                                         |
|-----------------------------------------|
| **Mining**                              |
| Skills used |
| Miner                                   |
| Tasks                                   |
| Dig / Remove construction               |

A designated area being mined.

**Mining** is an essential part of building a fort in *Dwarf Fortress*. There are several reasons you might want to mine, such as searching for various stone types, ores and gems, or simply to create the basic tunnels and rooms in your fort. Mining refers to either the skill that performs mining, the labor associated with it, or simply the task or job of performing said labor. Military dwarves equipped with picks will use mining as their "weapon skill." Mining through softer materials such as sand or soil is much faster than mining through stone.

There are several types of jobs associated with this skill:

- **Digging** removes the section of the wall while preserving both the ceiling (which is the floor of the level above) and the floor.
- **Channeling** removes the section of the wall, the floor, and if possible places a ramp one level below.
- **Ramps** replaces the section with a ramp, also removing the tile and floor one level above.
- **Stairs** carves out upward and/or downward stairs.
- **Remove Construction** removes a construction, ie. a built wall, stair, floor, etc.
- **Remove Stairs/Ramp** removes a dug-out stairs or ramp.

Mining can only be done in pre-existing stone or soil. NOTE: Constructed walls, stairs or ramps are not dug and instead must be removed using the 'Remove Construction' option (mx). This uses the mining skill to be completed, regardless of the material the construction is made from.

When discovering a unique stone, gem or ore, the game will display an annoucement that looks like the following:\
You have struck saltpeter!

## Understanding digging

Side view of various mining tasks.\
Gray/black areas represent un-mined rock, cyan/black represents mined-out areas. Solid green represents existing floor "tiles", cyan represents mined-out floor tiles. Up stairs, down stairs, and ramps are red, blue, and mustard (yellow) respectively.\
In each of the 9 "digging" scenarios, the dwarf miner is shown as having completed the command(s) listed in that figure, moving from left to right. Each individual command is separated by a comma ",". (The "x2" notation indicates that the command is completed twice.) The dwarf has completed those commands in the order they are listed. For example, in the bottom right figure: "Down stairs, up/down stairs, up stairs, mine x2" is five separate commands.

Each layer in the three-dimensional *Dwarf Fortress* map consists of two parts: a wall-part, and a floor-part. Mining a tunnel removes the wall-part but leaves the floor-part in place. Channeling removes the floor-part as well, leaving open space above, and if a wall-part exists below, it becomes an upward ramp. Digging an upward ramp removes the wall-part of the designated tile and both parts of the tile above it. Up stairs only modify the wall-part of the designated tile (and are unusable without Down stairs in the tile above), the Down stairs designation will remove the wall-part of the tile (if present) and place a stair connection in the floor-part of the designated tile. Up/down stairs modify both parts of the designated tile (but remain unusable until the tile above/below has the proper stair connection).

## Making a dwarf a miner

1.  Go to the y labor menu, then work details tab
2.  Select the "Miners" work detail on the left side of the screen
3.  Find the dwarf you would like to make a miner, and click the rightmost box, a green check mark should appear
4.  If you would like this dwarf to *only* mine, and ignore all other labors (they will still eat, sleep, take breaks, etc. ) you can toggle the dwarf's "Specialize" button (the hammer and lock icon) to be red.

To start mining, a miner requires an available pick. A dwarf's agility and mining skill affect how quickly they mine, as does pick material and quality, and even a difficulty setting.

Giving a dwarf the miner work detail will disable the "wood cutter" and "hunter" work details, as those labors all involve the usage of different tools.

## Designating the area to be mined

1.  Press m to bring up the digging orders menu.
2.  Highlight the requested action by pressing:
    - m for mining
    - u for channeling
    - r for an upward ramp
    - t for stairs, set a start and an end point in a different elevation to determine if it leads upwards or downwards
3.  (Optional) Set the priority by pressing n to open the advanced options, and clicking a number to set the priority. Tiles with first/lowest numbered priority value will be mined first.
4.  Draw a rectangle using the mouse. An area should now be highlighted, indicating the area to be mined. The opposite corner can also be placed on a different z-level with c/e, designating areas across z-levels for mining.

## Mineral production (profit!)

When the wall-part is removed from a stone tile, there is a 25% chance that a single stone (also known as a boulder) will be left behind. Minerals which are found in veins have a 33% chance of leaving ore, and minerals found in small clusters (or individual tiles) have a 100% chance of leaving a stone or rough gem behind. Finally, any "deep" material (i.e. adamantine or slade) has a 100% chance of leaving a usable stone (though the latter is normally undiggable). Mining skill only influences the amount of time it takes to mine each tile; it does not affect drop rate.

Carving a channel down or ramp up needs special care to provide the full 25%/33%/100% mineral production: in the case that both the bottom tile (where the new ramp up is) and the top tile (new open-space above the newly carved ramp) are both dug out together as part of the same designation, there is only a single chance of mineral production, even though two tiles had their wall-part removed, effectively halving the mineral production chance to 12.5%/16.5%/50% in that case. But if special care is taken to ensure the top open-space tile is dug out first before carving the ramp below it, the full chance from both tiles can be achieved.

The stoneworker's workshop can create four blocks from each boulder, so on average you can create one stone block for each tile of stone mined. Each ore stone also produces 4 metal bars at a smelter, so, on average, you will produce 1⅓ bars of the basic metal\* for every tile of ore mined, or 4/ for small clusters of rare ore.

(\* Two ores, tetrahedrite or galena, have a chance to produce additional bars of silver as well as producing the 4 bars of their basic metal (copper and lead, respectively). As a footnote, while iron ores produce 4 bars of iron, and that is all the metal required for 1 bar of steel, steel production additionally consumes 1 flux stone and 1 bar of fuel per single bar of steel produced.)

When tunnels are dug in soil, nothing is left from the material, there is no soil equivalent of a "stone" to be further used. The floor-part will remain (if it wasn't channeled), and is suitable for farming, or, if the right kind of soil, for sand or clay collection.

After pressing m and opening the advanced n options menu, you can set the designation type to switch between designating all materials (v), designating just g gems, designating just gems and o ores, or designating ore/gem clusters or veins to be mined automatically with V. Switching the designation type to automining will allow you to quickly assign mining tasks to entire veins.

## Training mining

Dwarves gain mining experience for each tile mined, be it stone, ore, gem, or soil. Soil is mined extremely quickly and is one of the fastest ways to train miners. Since the skill of mining also is used in combat, a dwarf with mining enabled that is carrying a pick will increase their mining skill through combat drills. This process is much faster than learning by digging through stone, but not nearly as fast as learning by digging through soil.

The fastest way to train mining is to first dig out upstairs, then remove the upstairs. Removing upstairs (even rock ones) is extremely quick and still provides mining experience.

## Mining warm and damp stone

Wet tiles that should not be dug.

When designating any digging operation, warm and damp tiles will flash, indicating magma or water in adjacent tiles. Miners can dig these safely, provided there is an escape route. (*"Safely"* here implies only the short term survival of the digging dwarf, your fortress may well be flooded as a result, even many levels above the digging level, *eventually* killing your dwarf.)

Channeling and ramping designations involve two operations, and your dwarf will be submerged in the fluid when done. Unskilled swimmers can reach an exit ramp out of water if near enough, but magma will certainly cost your miner's life (the flow from either can knock dwarves off ledges, or, naturally, flood the fortress.)

Wall tiles *above* magma will flash "warm", and designations will be cancelled even if an entirely safe tunnel is being dug. This is rather annoying when carving out rooms above the magma sea, although there is a way around it. Designating a channel two levels above the magma will mine out the warm wall immediately above the magma, and the designation won't be cancelled because it's not in the area of the warm stone.

## How to cancel a mining operation

If you placed a designated area for mining but want to cancel the mining (for example if you approached damp stone) open the eraser tool with x and select an area you want to cancel.

## Rampless channels

To create a channel with no ramps, you have to mine out the area underneath the channel first, or manually designate the ramps created for removal afterwards mx. If you wish for these channels to be completely inaccessible from the outside, channel out the access-point (downward staircase). Another (more complicated) way of removing any access to the moat is to replace the dug out ramps with constructed ones and creating a cave-in with constructed floors. Rampless channels are an effective substitute for walls against melee enemies that cannot fly, and they can be dug out far faster than a wall can be built. However, channels offer no defense against archers or dragonbreath.

When digging ramps upwards, watch out for loose stone or other items that might be on the floor above, as falling objects can injure the unfortunate miner.

## See also

- Map tiles – Different types of walled, floor and open spaces.
- Caverns – Large underground tunnel systems.
- Exploratory mining – Mining focused on finding valuable stone.
- Soil – A list of soil types.
- Stone – A list of different types of stones and ores left behind from mining.
- Smoothing – Increase fortress value and dwarf happiness by improving the quality of your rough-stone mineshafts.

|  |
|----|
| "Mining" in other / Languages / Dwarven / : / avuz / Elven / : / cèthutha / Goblin / : / ngogngo / Human / : / bora |
