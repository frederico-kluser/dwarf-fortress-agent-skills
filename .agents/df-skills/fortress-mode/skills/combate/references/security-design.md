# Security design

> Fonte: [Security design](https://dwarffortresswiki.org/index.php/Security_design) — Dwarf Fortress Wiki (GFDL/MIT)

''This page is one of several inter-related articles on the broader topic of defending your fortress and your dwarves. **Security design** focuses on how to turn the physical layout and architecture of a fort into a defensible whole. For a general overview of the threats that will challenge your fortress and things to consider when preparing a standard defense, see the **defense guide**. For complex traps that are not a minor/optional part of a larger defensive plan (but might be adapted or plugged into one), see **trap design**. For specific advice on how to get your soldiers prepared for any threat, see **military design**.

## Standard key

`  `**`Key:`**\
**`symbol tile`**\
`     -  Open space`\
` +   -  Constructed floor, or top of wall section from lower level`\
` `**`0`**`   -  Isolated wall section`\
`╔╦═╗`\
`╠╬═╣ -  Connected wall `\
`║║ ║`\
`╚╩═╝`\
` ╬   -  Fortifications`\
` X   -  Up/down ``stairs`\
`    -  Down stair`\
` ▲   -  Up ramp/slope`\
` ▼   -  Down ramp/slope`\
` .   -  natural ground`\
` ☺   -  dwarf`

## General suggestions

General designs include suggestions that can be "plugged in" to a part of any typical fortress, and/or can be modified to suit a number of purposes. At the most basic level, a retracting bridge over a central stairway can isolate the surface from your fortress. On the truly labor-intensive end, you can fully enclose areas of wilderness you wish to utilize in walls or behind moats with the only access being from within your base. Hostile creatures, even 'invisible' ones like ambushers, start at map edges and travel across the map (except for a bug which occasionally causes creatures to spawn in the interior of the map).

### Surface isolation

A bridge which can isolate your fortress from the surface at the pull of a lever is a very effective preliminary defense, and still serves as a backup plan when you add larger and more resource-intensive defenses. A raising bridge can be used if you dug your entrance into the side of a hill, or a retracting bridge over your central stairwell if you dug straight down from the surface. Retracting bridges have the advantage of being non-lethal to dwarves and animals (in the event of a lever-pulling mishap) but are a little more complicated to build.

### Meeting area as defense

Especially in the very early game, you can use a meeting zone to attract animals and idle dwarves to a given area. This makes a pretty poor defense in general, but it's not a bad way to create an alarm system against minor threats such as thieves and protect your stockpiles from pesky kea, at least until you have something better (which won't be hard). Remove the zone later, or it attracts idle dwarves and children. Note that until you designate something else, the site of your wagon (even once deconstructed) is a default meeting area.

### Guard Animals

Both thieves and ambushes are invisible until something detects them - a dwarf, a caravan, a wild creature, a domestic animal, anything. Once this happens (even if it was triggered by a wild groundhog on the far edge of the map), the game will pause with the appropriate announcement, forcing your attention to the situation - which is nice. Therefore, it's a common practice to use animals to act as alarm systems, by restraining or assigning them to a pasture in entryways.

There are some considerations to good placement of such animals. If you have a 1- or 2-tile-wide hall, one animal is enough. If you have a 3-tile-wide hallway, a single pastured animal placed in the middle is still sufficient, or you can restrain two animals, one at each side of the hall.

`══════════     R = restraint`\
`+++1R1++++     1 = area of animal 1`\
`+++bbb++++     2 = area of animal 2`\
`+++2R2++++     b = area of both`\
`══════════`

Either arrangement creates a thief-proof barrier against unannounced intrusion, as there is no combination of locations where an invisible enemy can sneak by without bumping into an animal. Caravans can pass over restraints and pastures and their contained creatures without a problem (however, do note that wagons will not appear on the map edge if a creature is blocking their intended location). Guard animals can also see hidden enemies one z-level below them, so long as there is no intervening floor, so if space is tight you can also place them above your entranceway.

Unless you're happy losing these animals on a regular basis, you should try to keep them alive.

:\* Put them around a corner or behind a U-bend, so archers cannot fire at them from a distance.

:\* Don't have them as your "first line of defense"; put them deeper in the entry, behind some traps.

:\* Put them inside, so flying creatures have to come down to their level to attack them.

:\* Use windows to protect your guard animal (note, however, that some intruders may not be detected if they are not forced to move directly adjacent to your animal).

:\* Consider using a pressure plate at the extreme entrance to seal off the hall further down and keep your guard animal(s) safe. Thieves won't trigger them, but the animals can deal with those - ambushes *will* trigger them, and you don't want them getting to your guard animals.

Remember that anything short of a megabeast is not a good match for an armoured opponent. While watching your tame grizzly bear or alligator tear a thief apart has an amusement value, watching the goblin maceman send them flying across the map, mangled and dying, has less.

Hunting animals have better observation (sight range) than their regular or war counterparts.

### Basic entryway

One of the more basic designs is a fortified wall surrounded by a moat. The moat should be a channel at least three tiles wide to keep anything from jumping across into your fort. Dig one additional tile on each side to prevent creatures from climbing out of the moat. You can flood the moat if you like, however doing so actually reduces its effectiveness. The next step is to build a wall around the inside of the moat (at least one tile from the edge). Add a layer of fortifications on top of the wall to deter climbers and allow your marksdwarves to fire on enemies outside.

`sideview `\
`        `\
`      #`

\_\_\_\_ \_▒\_ ░░░\_\_\_\_\_░░ \

### Defending the edge

You're not allowed to wall within five squares of the edge of the map... but this rule has more loopholes than the US federal income tax code. Until more versatile attackers emerge, it is not clear where effective play ends and exploit begins. *(Note: we disclaim any responsibility for damage involving harpies and skeletal giant eagles)*

- To start with, you can channel the ***second*** square from the edge. This will block the appearance of trade caravan wagons and prevent their movement along that edge of the map. Constructed track tiles (but not ramps) can also be used to block wagon movement.
- If there is only one wagon-accessible path to your Trade Depot, caravans will be forced to appear on that path. Limiting the caravan's options allows for better-prepared defenses along the caravan route.
- You can also build drawbridges all the way up to the edge. A long, skinny, raised bridge is effectively a wall; however, it looks the same whether it's open or closed.
- You can with some work use Obsidian casting to wall to the map edge

Train up diggers in soft soil and you can surround most of the map with a moat by the time the first migrants arrive. Be very, very wary of cave-ins, especially on highly sloped diagonal terrain - note that a downward ramp does not support adjacent floor tiles, and no tiles are supported diagonally.

Occasionally creatures have a strange habit of appearing well inside the map due to a bug. Additional defenses at these locations may be required. *\[Note: On one 6x7 map horses and other animals were also found to appear one embark unit (48 squares) left and up from the lower right corner, inside or atop the walls of a 5x5 doorless enclosure. Defend all leaks...\]*

#### Design considerations

- The moat should be designed to prevent entry except by falling from both sides. (Otherwise inside and outside forces might be tempted to shake hands from adjacent squares.) Despite an abundance of giant corkscrews, grates, ballista bolts, etc., no one has ever invented the ladder, so this keeps anyone from entering or leaving the rest of the map.
- The moat should be dry, because sooner or later you will be tempted to let someone visit the edge to loot goblins or hunt varmints, and next thing you know your Legendary Weaponsmith who outpaces all your smelters will be whiling away his time carrying a leather thong to a stockpile when he runs into a groundhog and decides to react by jumping into the moat and holding his breath beneath the shallow waters until he drowns. (As always, the notice that he has drowned is the first you'll hear of it)
- The moat doesn't actually *need* to be adjacent to the edge of the map except when conserving valuable surface terrain (such as trees on a map that is mostly rock). It is easier to free trapped miners when they can dig further outward, and placing the moat on the sixth or further square in from the edge allows further modification with floodgates, walls, and doors. Any channeling permanently changes the dug-out tile to "Light Above Ground", which restricts these features from tiles near the edge even if floors are later constructed to close the space.
- Because migrants might turn up near wild animals or be followed closely by goblins, it is nice to wall off the last square in shorter segments. Each one or two segments are served by a separate lever bridge. This can be done by:
  - Natural barriers. The map edge is mostly continuous ramp, but occasionally a break appears on an uneven surface, by a river channel, etc.
  - Floors. Building a square of floor over a ramp at the map's edge makes the ramp unusable.
  - You can build drawbridges up to the edge and raise them. This will completely obstruct passage of almost every creature.
- Migrants, thieves, and sieges turn up all around the map, and can be allowed in by remote-controlled bridges. (Doors will not hold back building destroyers, and remote lever control is needed because other gates can be "taken by invaders" and become non-lockable.) Invaders can be allowed in by small groups and fought if desired, or preferably admitted into underground zigzags with a door waiting to be locked at the far end once they get close to it. If most of the invaders can be trapped inside such spaces, the remainder will stand and be wiped out completely without retreating.

### Simple 5x5 Archer's Tower

Build a tower specifically to post archers on, possibly away from your main defenses. This lets you open fire before the enemy approaches your gates. A pillbox can be attached to your walls, or separate, so that the only access is from tunnels below. These tunnels can stretch across the map, and only need be 1-tile big if no regular traffic is expected. Construct walls up to the second or third floor and then carve fortifications into them, so your dwarves can fire out. For extra usefulness, build a barracks, archery target, food stockpile, well and/or dining room in or near the tower. Add a door or hatch to lock them in.

When placing multiple towers, know that crossbows have a range of 20 tiles, so, depending on whether you want overlapping fire or not (and how intense/accurate), anywhere from maybe 15 to 38 tiles between the edge of the towers is recommended. Crossbows actually have their range *reduced* by extra height in DF, so all you need is 1 level up to keep enemy archers from using your fortifications against you, and you're set. (Channeling a defensive moat further out will also work, moving potential enemy archers even further away, but also moving non-missile targets that far as well.)

#### Siege engine turrets

If it's big enough, build a siege engine inside a pillbox. Since siege engines cannot fire at targets higher or lower than them, the device needs to be on the same z-level as any targets, but this could be across a large gap to a nearby plateau. Only a single tile of fortifications is needed to fire through the wall. Position the tower to fire where invaders tend to congregate.

You will want to guarantee that enemies do not approach the position and scare the civilian operators - this distance has been reported to be up to 20 tiles or so. Dig a moat, have some intervening valley or build some secondary fortifications to keep enemies at a distance. Unlike walls, fortifications on the same z-level do not block siege engine missiles, at any range. Unfortunately, if an enemy can walk up to them, fortifications will protect enemies from your archery fire (but not siege engine fire.)

*\[Note: Due to a number of outstanding bugs, siege engines are generally quite ineffective...\]*

### Control Room

Have one (large?) room (or several stacked on top of each other) for all defense-related levers, and central to idle dwarves - near your meeting areas and nobles quarters, with one or more halls or stairs leading to it for quick access. Connect a lever to all those doors and hatches as the first lever to be pulled in an emergency, and the respondent will lock themselves in for you, guaranteeing that they will then have nothing else to do but stay there and pull levers. This can, however, backfire when your chosen dwarf decides to go on break, take a nap, or throw a tantrum in the middle of a crisis.

It may also be an idea to have a second lever to at least one door, for emergency access. And possibly to add a stockpile of booze and food or a well for longer sieges.

### AI abuse

Taking advantage of the game's artificial intelligence and pathfinding is a whole article in itself. Try leaving a door un-forbidden during an attack. When the bad guys approach the door, forbid it, and the enemy will wander off. Unlock it again, and they turn around and head back towards the door again. You can get enemies to march back and forth over a set of traps this way, or lure them deep into a complex trap. This could be fully automated via pressure plates if you're feeling adventurous. (Even if you're a stickler for realism, you can justify this method as a way of letting Urist McRedshirt taunt the invaders into your hall-o-fun.)

### Bait animal

Restraining or pasturing a sacrificial animal just outside your walls, but within range of your marksdwarves and/or siege engines, can lure an enemy into attacking that while you cut them down. Make sure to place a pattern of some walls (or statues, see below) so enemy archers cannot simply shoot the creature from a safe distance.

##### Fortifications

Adding a ring of fortifications to help defend the animal against missile fire will keep melee troops away, but invite archers to come adjacent to the fortifications - and under your walls and crossbows. If you allow any path, the melee troops will try to follow it to the animal - be creative with that fact.

##### Traps

Surround the animal with traps to kill or capture approaching goblins.

Build a long, narrow, and twisty passage, accessible from the outside, possibly even unconnected to your fortress. Build as many simple traps as you like. Place a bait animal inside. Enemy attackers walk right in, and get torn apart by the traps. If any manage to make it to the end, and kill the useless animal, they're surrounded by traps, and no closer to your fortress.

If the animal is underground, you can build a tunnel above it, channel down, and mark the channel a pit/pond. That way, you can "reload" a new bait animal from the safety of your fortress. Note that this requires using a non-pet-passable door and that falls of more than a couple z-levels may injure your bait.

##### Distractions

Releasing a cage full of surplus animals will keep the enemy archers very busy. They may even be out of ammo when your wrestlers show up. This can be useful as an emergency measure since the animals need to be stored somewhere, anyway.

Alternatively, you can use remotely-actuated doors tied to a repeater: open providing a tempting target for enemy archers, then closed to block their arrows and protect the bait. Similarly, a captured necromancer can continually raise a few undead to give enemy archers easy targets to pincushion.

Minecart-riding dwarves can easily distract enemy archers--and if they are moving fast enough they'll be very difficult to hit. Getting your own archers to ride in the minecart, however, is quite a chore.

##### Vanishing act

Having a linked drawbridge that can open/shut (perhaps on both a lever to open and a nearby pressure plate to close), to lure the enemy in under your guns and then protect the animal when they get too close (for multiple uses.)

##### Vs. building destroyers

For building destroyers, spare furniture can serve the same purpose as bait animals. Building destroyers will hunt down and destroy structures, so carefully placing them can control their movements.

##### Trap chokepoints

Enemies can be herded by constructed features. If you have a particular zone covered by catapults and would like enemies to pass through it, strategically placed walls can make enemy pathfinding more favorable. A trap occupying a single tile in the middle of a barren plain is likely to never get triggered. However, if walls are placed in a cross-hair pattern around the trap, animals and invaders are much more likely to pass over it as they wander across the map. This can be a very useful trick when capturing wildlife with cage traps.

\ +++++║+++++ +++++║+++++ +++^^║^^+++ +++^^║^^+++ ═════^═════ +++^^║^^+++ +++^^║^^+++ +++++║+++++ +++++║+++++ \

##### Pathing slowdowns

If you're playing on a low-powered machine and you close up all entrances to your fortress during a siege, your game may grind to a halt and/or crash as the siegers continuously fail at pathfinding into your fortress. Bait animals may alleviate this.

##### Goblin loyalty is a beautiful thing.

Don't use cage traps as the front line of defense, as currently, a goblin squad will follow its leader indefinitely, and if its leader is caught in a cage the rest of the goblins will just stand there until they find something to do rather than exploring the lovely, pointy playground you've created.

On the other hand, this can be a fantastic way to train your siege operators, as the entire squad will valiantly stand guard at their leader's cage even in the face of overwhelming barrages of stone and metal, and unlike a bait animal neither the goblins nor your own attacks will kill their caged leader. Leave them alone long enough, and they'll eventually start killing their own deserters!

## Entrance designs

### Airlock defenses/buffer zone

Build two walls, each with a drawbridge. Build the trade depot in the buffer zone between them. Keep the outer bridge open, and the inner one closed. When the merchants appear, put crossbows on the walls to guard their approach. Once all the merchants are safely inside, close the outer bridge. Once there's no enemies left in the buffer zone, open the inner bridge so your civilians can start loading up the depot.

The airlock pattern can be useful even without putting the depot there. Let a few siegers in at a time, and crush them. Reset the traps, rest up the soldiers, and repeat.

### Siege Engines

*\[Note: Due to a number of outstanding bugs, siege engines are generally quite ineffective...\]*

One way to have siege engines (help) defend your fortress is:

**One ballista vs 3-wide hallway**

`══════════════════════════╦═════`\
`Entrance++++++++++++▼     ║▐▀\`\
`Entrance++++++++++++▼     ╬◄═«`\
`Entrance++++++++++++▼     ║▐▄/`\
`══════════════════════════╩═════`

Using this design you can (theoretically) cripple an army using a well timed volley. The hallway can be much longer than shown if you wish, as ballistae have extended ranges well over 100 tiles. The channeled area is necessary, as civilians (siege operators are "civilians") will run when enemies get within about 20-24 tiles of them, regardless of the actual path to that threat.

#### Ballista battery

Three (or more!) ballistae can be put into a "battery" if overlapped - one per tile-width of the hallway, with each ballista aiming down their row of tiles.

`                                ╔═══`\
`══════════════════════════╦══╦══╝▐▀\`\
`Entrance++++++++++++▼     ╬  ╬▐▀\◄═«  (~ammo~)`\
`Entrance++++++++++++▼     ╬▐▀\◄═«▐▄/`\
`Entrance++++++++++++▼     ╬◄═«▐▄/ (~ammo~)`\
`══════════════════════════╣▐▄/ (~ammo~)`\
`                          ╚═════════`

Be sure to use fortifications to prevent dwarves from wandering in front of the ballista to their deaths. If desired (and you have the mandwarfpower to spare), catapults may be put behind those, as they shoot safely *over* workers in front of them. Although less effective than ballistae, it's a little more firepower - and that can't be a bad thing.

For added flavour, channel out one or more tiles down the length of the 3-wide hallway and install retractable bridges. When invaders attack, retract the bridges, forcing them into paths that are only 1-tile wide.

Adding additional channels on either side of the hall will allow stray ammo to be recovered at a later time. Make sure to add locked doors, to prevent siege operators from walking down below enemy archers during a battle.

### Flooded entrance

Using a chamber as your entrance alongside a chamber full of water and some machinery you can flood or drain the entrance at will.

The basic premise requires two levers, two screw pumps and two gear assemblies. The amount of power required and the number of additional components needed to get the power to the screw pumps varies depending on distance/setup. One pump is placed to draw from chamber 1 and dump into chamber 2. The other is set in reverse. A gear assembly is placed next to each pump and connected to the main power system. Each gear is linked to a lever. Now at the flip of a switch you can submerge your entrance with water or magma for easy, secure defense against creatures that aren't amphibious or magma-dwelling, depending.

The picture above shows the design in action. The green pump is currently on while the red has been disconnected through the grey marked axle. The yellow X is just to mark that there is a channel under the axle.

An alternative that uses gravity rather than screw pumps (but works only if you have a volcano or surface river, a subterranean entrance chamber, and easy access to a cavern layer) is to dig a tunnel fitted with a floodgate or similar valve between a volcano or surface river and your entrance chamber. A second tunnel equipped with an appropriate valve mechanism allows the user to drain the chamber into a cavern layer. A grate can also be integrated into your drainage system to prevent the loss of valuable goblinite or similar remains.

### The "Reverse Battlement" design

Level Z+0 (ground): \

`  ...............`\
`F ═══════════════`\
`O .≥.g≥...g......`\
`R ..≤......g.....`\
`T ...g≤..g....... 

Level Z+1 (bridge):

`E      ║+++║     `\
`N +++++║+++║+++++`\
`T      ╬☺++║     `\
`R      ╬☺++║     `\
`A      ╬☺++║      

Note that in this diagram, the fortress interior is to the West, and the enemy forces come from the East. The marksdwarves on the bridge with the fortifications are one level above the goblins (or other attackers), who will pass under the bridge and charge on toward the west. As they move past the bridge they are targeted from behind (which is one level above) by the marksdwarves waiting in ambush. This allows the marksdwarves to face far fewer enemies at any one time, at least to begin with, and any dangerous enemy archers will remain close to the bridge, hopefully under the concentrated fire of your marksdwarves.

If you're feeling especially nasty, make the tunnel really long into the mountain and add a ballista battery (see above).

*(Adding ammo stockpiles, of your best quality bolts, to these stations will speed up reloading for longer sieges/battles. Even adding small, convenient food and alcohol stockpiles is not unheard of. Some designers place access to/from archery ranges very close to these stations, for faster deployment.)*

### Twisty maze

A maze of turns and blindspots patrolled by quality military can be a very formidable defense. Wide enough for wagons to pass though, but with no clear shots for any ranged weapons. Missile weapons do have a minimum range, so if a target is closer than that range, they will instead just charge to melee - and meet a dwarf with a much better melee skill. Downside to this is that you'd be mixing it up in melee all the time, but so long as you have at least 10 dwarves greeting the goblins as one coherent mass, you should win.

Variations on the twisty maze include:

- A wagon-wide twisty maze, and a not-so-twisty 1-tile wide hall o'traps, with a drawbridge that can force one or the other as the only path into your fortress.

- Making the side of the maze into fortifications, with a channel separating the fortifications from the actual floor of the maze, and having your archery targets on the other side of the fortifications so your marksdwarves can practice. When the goblins round the corner, they charge through a hail of crossbow bolts, and drop dead.

### Forced Detour

This particular design works well with plenty of archers, siege engines, and other ranged weaponry. A walled maze gives melee an advantage, but an open maze gives advantage to ranged attackers. \ ++++++++++++++++++Entrance ╔═╦════════════════0╞═╡0 \║+++║ ║+╬ + ╬+╬╬╬╬╬╬╬╬╬╬╬║+++║ ║+╬ + ╬☺++☺++☺++☺+\ The 3 tile wide lane is for traders, so if your trade depot is located before this set-up, cut it down to a 1 tile lane to slow down invaders more.

### Bridge Use

An example of bridge construction tactics to deal with vile forces of *any* size. (See picture).

- **Bridge 1** seals off the entire base
- **Bridge 2** forces everyone to take the long, winding, heavily trapped/defended path of death.
- **Bridge 3** seals the inside of the fortress

Clever triggering of the bridges allows you to break the hostile forces into smaller chunks to be trapped in the courtyard while being caught in traps and a crossfire of arrows from the fortifications around.

### Pulling it all together

Using ballistae, marksdwarves, bridges, traps, and guard animals in tandem brings up a few more considerations.

- Be careful about positioning your marksdwarves and ballistae opposite each other as an unlucky ballista bolt might injure a marksdwarf on the other side.
- Ballista are operated by Dwarf civilians. Therefore putting your ballista right next to the path the friendly neighbors use will cause your BallistaDwarfs to run off right as you want them to fire.
- Adding a stair back at the entrance of a trap hallway allows dwarves to access loot that falls; it also forces anything that dodges off the edge to walk the entire length again.
- Filling the walkway with traps is also highly recommended. Throwing random weapon traps around the map in high-traffic areas isn't a bad idea. Traps are cheap and effective, use them liberally.
- War animals are convenient for catching thieves. They also serve as bait. Don't place them where enemy archers can reach them easily, and keep them well out of range of the inevitable hailstorm of bolts.
- Bridges, and for non-building-destroyers, doors, can be used to control the movement of enemies.

`                                      Fortress`\
`                                       ║╞═╡║`\
`                                       ║D+D║ ╞═╡= Bridge`\
`                                       ║D+D║  D = War Dog (chained)`\
`                  ☺  ☺  ☺  ☺  ☺  ☺  ☺  ║+++║  ^ = Trap  c= cage trap`\
`                ╔╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╝+++╚╦══╗ `\
`/▀▌╔═══════════╦╝                       +++ ╬  ║ P= Gathering Pit`\
`»=►╬+++++++++++╬  ccc+^+^+^+^+^+^+^++++++++ ╬  ║    connected to`\
`\▄▌║+++++++++++╬  +                     +++ ╬ P║    Base next `\
`   ║+++++++++++╬  +                     +++ ╬  ║    z-level down`\
`/▀▌║+++++++++++╬  +                     +++ ╬  ║`\
`»=►╬+++++++++++╬  ccc+^+^+^+^+^+^+^++   +++ ╬  ║`\
`\▄▌║+++++++++++╬                    +   +++ ╬  ║`\
`   ║+++++++++++╬                    +   +++ ╬  ║`\
`/▀▌║+++++++++++╬                    +   +++ ╬  ║`\
`»=►╬+++++++++++╬  ccc+^+^+^+^+^+^+^++   +++ ╬  ║`\
`\▄▌║+++++++++++╬  +                     +++ ╬  ║`\
`   ║+++++++++++╬  +                     +++ ╬  ║`\
`/▀▌║+++++++++++╬  +                     ╞═╡ ╬  ║`\
`»=►╬+++++++++++╬  ccc+^+^+^+^+^+^+^++++++++ ╬  ║`\
`\▄▌╚═══════════╩╗                     +++++ ╬  ║`\
`                ║                    >+++++ ╬  ║`\
`                ╚════════════════════╗+++++╔╩══╝`\
`                                     ║╞═══╡║`\
`                                     Entrance`
