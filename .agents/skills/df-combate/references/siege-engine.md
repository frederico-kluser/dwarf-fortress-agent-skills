# Siege engine

> Fonte: [Siege engine](https://dwarffortresswiki.org/index.php/Siege_engine) — Dwarf Fortress Wiki (GFDL/MIT)

A **siege engine** in *Dwarf Fortress* is half building, half heavy weapon, and includes both the **catapult** and the **ballista**. Both are capable of launching hazardous projectiles at a tremendous range (more than a screen-width, around 80 to 100 tiles for a catapult and between 130 and 200 tiles for a ballista). A ballista arrow can kill or injure each creature in its path indiscriminate of friend or foe, but a stone launched from a catapult cannot harm dwarves or tamed animals.

Unlike what the name may imply, siege engines are only deployed defensively, and no siege will use them against you (although the use of siege engines against your fort is planned for future versions).

Siege engines can be made to face in any of the four cardinal directions, but they cannot be moved after placement. They can, however, be rotated, or deconstructed back into their 3 parts (with -), to be moved elsewhere. Both the construction of siege equipment and the engine itself require a dwarf with the "Siege engineering" labor designated, which uses the "Siege engineer" skill.

The player determines when (or if) each engine is actively firing or not; when active, a single engine is crewed by a single siege operator.

Ballistae require specially-made ammo – ballista arrows, made from wooden logs at the siege workshop (and optionally tipped with metal ballista arrowheads that have been made at a forge by a weaponsmith). Catapults use simple stone as ammunition. Catapults respect economic stone restrictions and cannot fire clay at all.

## Building Siege Engines

\-

In order to build a siege engine, you first need to produce (at least) three catapult or ballista parts in the siege workshop; catapults are made from any 3 **catapult parts**, and ballistae are made from any 3 **ballista parts**. All parts are made from any type of wood at the siege workshop. Beyond that, "parts" are generic - there are no particular "sub-types" of parts beyond the distinction between those for the two different engine types. The quality of the parts determines the overall rate of fire (and maybe accuracy) of the engine - the best are made with 3 masterwork parts. This won't make up for an untrained siege operator, but every little bit helps. Siege engine parts are stored in Furniture stockpiles.

Once you have the parts, you may then build the respective siege engine like any other building, selecting the parts that you wish to construct that particular engine with. It is not known whether the skill of the dwarf assembling the siege engine has any effect, but the quality of the parts certainly has: siege engines put together from masterwork parts have a much higher rate of fire.

The assembled siege engine is, effectively, a 3x3 building. It cannot be moved about, other than by taking it down and re-assembling it at the new site. Siege engines do not impede movement, though, so you don't have to worry about building them in a corridor.

## Using Siege Engines (simple)

will let you change the orientation, whether the siege engine is pointing north / south / east / west. This takes effect immediately, it does not require a dwarf to come and turn the engine.

toggles the current status between:

- Not In Use: Dwarves with the Siege operator job will reload unloaded engines and leave them unattended.
- Prepare to Fire: Siege operators will load the engine and remain stationed for further commands.
- Fire at Will: Siege operators will fire and load normally.

Once an engine is given orders to fire (or prepare to), a dwarf with the siege operating labor designated will respond and report to the engine. The dwarf(s) will (re-)load any siege engine that is not currently loaded; there's no way to prevent this short of disabling the labor on all dwarves or forbidding every piece of ammo (or otherwise blocking a path to it, perhaps by locking doors or using a burrow.)

Ammo is destroyed upon landing, unless it falls a z-level, and then it falls harmlessly. (See below.)

`########`\
`CCC..._#`\
`CCC..._#`\
`CCC..._#`\
`########`

The channel at the end of this firing range preserves the stone. For catapults there is usually so much spare stone that this is not necessary, but it could be used for fast stone transport, or simply to set up a self-contained training area. A similar effect can sometimes be observed when firing a catapult over bumpy ground outside.

The design can be further improved by using a drawbridge rather than a wall, this way when the drawbridge is raised it acts like a wall deflecting the stone into the channel below. In the case of an attack on your fortress the drawbridge can be lowered allowing the catapult to fire.

`#####################`\
`CCC..._¦.............`\
`CCC..._¦.............`\
`CCC..._¦.............`\
`#####################`

Drawbridge raised deflecting stones into channel.

`#####################`\
`CCC...[].............`\
`CCC...[].............`\
`CCC...[].............`\
`#####################`

Drawbridge lowered allowing catapult to shoot down the corridor.

Since catapults will never hurt your dwarves, you can easily take the above designs and face the catapults towards each other with channels behind them.

`######################`\
`#_CCC............CCC_#`\
`#_CCC............CCC_#`\
`#_CCC............CCC_#`\
`#########....#########`

This is obviously only for training purposes, but the point is efficiency. As each catapult fires, it "gives" stones to the engine across from it. This is entirely self contained, as your operators will continuously recycle the same ammunition, practically playing "catch" with the stones they are training with. Stones will always be available directly behind each operator, however dorfs some dwarves are incredibly stupid. They will tend to pick the last MINED stone for loading (like masons and crafters), so its best to burrow them into the range. Even then, the idiots will sometimes cross the range and pick up stones from the far end.

## Special considerations

- Both catapults and ballistae have narrow fields of fire – they will only shoot at creatures directly "in front" of them, and so cannot target anything off at an angle. They can be turned 90 degrees, but that often will not solve the problem. Unskilled operators have trouble aiming perfectly straight, and their shots will randomly veer off to either side, resulting in a field of fire roughly 19 degrees across. Highly skilled operators fire their shots perfectly straight, restricting their field of fire to a straight line facing directly north/south/east/west.
- Both catapults and ballistae aim and fire only along one z-level. While ammo from both may drop down z-levels, they do no damage to creatures there. This also means that no "head room" is necessary – ammo only flies out, never up.
- Catapults have a minimum range – at least 30 tiles.
- Catapults can and will fire over any creatures between them and their target.
- Ballistae fire over prone creatures without hitting them.
- Neither are affected by fortifications.
- Siege operators are civilians and, as such, will run in fear if enemy units come too close to them. "Too close" varies somewhat, but may be as far as 10 tiles.
- Siege operators cannot "aim" sideways - they always try to fire perfectly straight, but if they're unskilled there's a chance that the shot will "go wild" and veer off to either side by a random amount. In the case of catapults, however, these "wild" shots will actually calculate their arc height based on whatever enemy units are present off to that side (rather than based on what would've been directly ahead).

As for the actual amount of variance, siege engines aim at a location exactly 60 tiles away and up to 10 tiles to either side (if the shot is "unskilled"), which works out to a 19 degree spread (9.5 degrees to each side). The game generates 3 random numbers from 0 to 14 and checks if any of them are less than the unit's effective Siege Operator skill level (where Dabbling is 0 and Legendary is 15, and status ailments such as Nausea/Winded/Stunned/Fever/etc. can each reduce the level by as much as 50%) to see if the sideways drift should be eliminated. This works out to the following probabilities:

Dabbling - 0% Novice - 18.7% Adequate - 34.9% Competent - 48.8% Skilled - 60.6% Proficient - 70.4% Talented - 78.4% Adept - 84.8% Expert - 89.8% Professional - 93.6% Accomplished - 96.3% Great - 98.1% Master - 99.2% High Master - 99.76% Grand Master - 99.97% Legendary - 100%

### Safety Warning

**Ballistae can and will kill anything in their path!** Ballista arrows may hit any units in any square that the head passes through. They are moderately dangerous weapons, and should never be used with friendlies anywhere in their cone of fire, including the space the ballista arrowhead occupies when loaded on the engine. Always designate a restricted traffic area for a lot of tiles along the firing arc and keep dwarves out of the area or, better, wall off anything in front of them with fortifications to prevent all friendly traffic, or both. The shots appear to travel until they hit a wall or fly off the screen; the maximum range is about 150 tiles for an ordinary ballista. If the bolt passes through any part of a tree, the tree will disappear, presumably reduced to toothpicks.

Surprisingly, catapults are relatively safe. Catapult operators will target enemies (and wild animals) if there are any in their field of fire. If not, they will loose the shot in a high arc (not requiring additional z-levels, though) that misses everything until it lands. It is perfectly safe to operate a catapult in the cave: just point it at a nearby wall of solid rock. A nice side effect is that this will, in due time, clear the whole area of stone.

Using catapults to shoot into the open may provide some meat: as said above, the operators will target animals if there are any. However, elephants don't take nicely if you slay some of them. You also have a slight risk of killing your own dwarves or caravan escorts if they happen to be hunting the selfsame animal (and hence are close to it).

**"Fire at Will" does *not* mean there has to be anything to shoot at!** The siege engine will simply continue to be loaded and fired, simply launching ammo (stone or arrows) downrange with no (visible) target if given this command. This can be good against unseen ambushes, or if you wish to move stone across a map, but not if you are worried about depleting an ammo stockpile.

## Using Siege Engines (advanced)

### Placement

Siege engines can almost only shoot at targets right in front of them on the same Z-level. The target may deviate only slightly, as the field of fire is about 10-20 degrees wide. Because of the huge blind spots, it is advisable to prepare the position so that the enemy will be channeled through the field of fire.

Siege operators are civilians! They may cease firing and run if the enemy comes too close, which is around 20 tiles. You should therefore place the engines behind a moat or a wall of fortifications that will keep the enemy at a safe distance, or shield access to their location in some other fashion.

Siege engines can shoot through fortifications, just like any other projectile weapon. As fortifications appear to provide some protection against incoming bolts and arrows, it's usually a good idea to protect the siege engine in that way. The siege engine can shoot through any tile thickness of fortification. Fortifications further on in the path of the shot will not hinder it either.

### Skill and Quality

The quality of the siege engine parts affects the engine's reload time (and possibly accuracy). It is not known whether the siege engine itself also can be of a certain quality. The quality and material of the ammunition (in case of ballista arrows) affects the damage and possibly accuracy as well.

The only way of obtaining high-quality siege engine parts is to have them made by a trained engineer; the only way to train an engineer is to make parts or ammunition. Assembling and disassembling siege engines does not train the siege engineer skill. Dwarves will occasionally produce masterpieces long before reaching Legendary skill level, but be prepared to waste hundreds of logs until you have three masterpiece parts. Bringing an engineer to Proficient level (the highest you could buy when starting a new fortress) will take about 120 logs. Becoming Legendary requires 600 logs.

The operator skill affects reload time and accuracy. It will take a whole month for an unskilled dwarf to load a catapult; a Legendary operator with nearby ammo will get several shots at a running enemy.

Operators are best trained by firing into a nearby pit (to conserve ammo and ensure that it remains near the engine). It is recommended to have multiple skilled operators for each engine, since, as civilians, they cannot be compelled into action if they've decided to take a rest. Dwarves that have increased their strength statistic load engines much more rapidly than others, making them good candidates for operator duty (experienced operators can be cross-trained for strength). You should start training early: it can take one year for an operator to become Proficient, and two more years until he finally reaches Legendary level; by then he will have spent 300 rounds.

Loading ballista arrows seems to be much faster than loading catapults, probably due to the much lighter weight of the projectile.

An alternative approach is cross-training any highly skilled dwarves who aren't doing anything useful at the moment. With a couple levels each in strength and agility, a free siege engine, and an ample supply of ammunition nearby, a dwarf can become a Legendary siege operator within a few seasons at most, giving more flexibility in defense and several more levels for the fortunate dwarf. Rotating legendary miners out to siege-operation and then to stone-hauling duties sets up an efficient cycle.

### In Battle

Catapults are generally less effective in battle situations than ballistae. The launched rocks will often glance off mail armor, making them poorly suited for killing even goblins; they are also very inaccurate. Their ammo is easily replenished, making them ideal for target practice and very cheap to make and use.

Ballista arrows tipped with softer materials (such as wood) can glance off ordinary clothes, making the choice of arrowhead significant. However, the arrows may hit multiple targets in a single launch. This makes ballistae many times more efficient than catapults, which fire in an arc that hits only a few tiles per shot and is nearly useless against anything larger than smaller, poorly-armored foes. Ballista arrows fired through too many successive targets will be lost or destroyed; the limit seems to be roughly 5-6 goblin-sized targets hit before the arrow is lost. Adding a channel to the end of the arrow's trajectory will allow expensive bolts to be recovered after the attackers are dealt with.

A siege engine you want to use for actual defense shouldn't be set to fire at will, as this likely means that it's not loaded and ready at the time you actually need it. You should train your operators on other pieces. You might train your operators on a set of catapults and defend your fortress with a set of ballistae.

When the time comes, switch off all training engines and set all of the ones you'll be using to prepare to fire so the operators will be on-station; if some of them are currently not loaded, designate them to be disassembled so to prevent your operators from loading the training weapons instead of firing the real ones. Alternatively, use civilian alert levels with burrow restrictions, and just make sure the training catapults are not within any allowed burrow.

Remember, operators are civilians. They do not care that the fortress is at stake: hunger, thirst, sleep and breaks will always come first. It's wise to train more operators than you have engines, and disable all other work for them in times of need. The most effective way to ensure that your operators won't run off is to lock them in with the siege engine during the moment of truth.

### Ballista battery

If you place ballistae close enough together, you can completely cover a two or three tile wide corridor. Because siege engines are 3x3, they need to be staggered, so each one fires through the edge of the one ahead of it. This can be dangerous for your operators. To minimize risk, place fortifications to keep dwarves from wandering too far, and have only one entrance to the ballista room. There is still some risk that dwarves might wander into the line of fire, even with no reason to do so.

**Three tile-wide corridor** (battery room 5 tiles wide)

`                                ╔═══`\
`══════════════════════════╦══╦══╝▐▀\`\
`Entrance++++++++++++▼     ╬  ╬▐▀\◄═«  (~ammo~)`\
`Entrance++++++++++++▼     ╬▐▀\◄═«▐▄/`\
`Entrance++++++++++++▼     ╬◄═«▐▄/ (~ammo~)`\
`══════════════════════════╣▐▄/ (~ammo~)`\
`                          ╚═════════`

:\*`＋` - floor

:\*`═` - wall

:\*`▼` - ramp (down)

:\*`·` - channel (aka "empty space" on this level)

:\*`╬` - fortification

Due to the rare wild shot, the staggering should always be from one side to the other, and not put one ballista far ahead of the one it overlaps, as this may increase friendly-fire accidents.

Ammo storage can be on the same level, or via stairs or ramps on another z-level. Expand the room as desired for more storage. Also note that ballista arrows are stored in furniture stockpiles, not ammo stockpiles.

An alternate strategy could be to place a floodgate or retracting bridge in the center of the 3x3 hallway, and activate it during times of crisis so that the Goblins are forced to fight in two separate 1x1 corridors rather than a single 3x3 corridor. If the corridors are further lined with spike traps and weapon traps, this combined defense can assure your dwarves that any attempts to assault your base will be very, very bloody.

A drawbridge can be combined with the channeled area to provide a practice area, as discussed above. The channels would be accessible from the battery area via a staircase, keeping the dwarves below/behind the lines of fire at all times.

## Catapults as stone movers

When a catapult throws a stone, that stone is destroyed upon landing, unless it falls a z-level, where it lands harmlessly. That means that if you can arrange it so ammo hits a wall (or door, or raised bridge), and there is empty space immediately under that, the stone arrives at that point. If the ammo reaches its maximum range, again, it falls harmlessly. Even with a single, no-quality catapult and an untrained crew, this is massively faster than hauling stone by hand. Ammo that hits stairs is destroyed, even if it can fall a z-level. Stones falling one z-level onto a floor with empty space under it will also be destroyed, make sure there is a wall under the tile where the ammo ultimately lands on.

## Gatling Catapults

This involves a catapult, a garbage dump activity zone, and a legendary siege operator. Set up your catapult where you'd like it to be used, then place a garbage dump zone in the middle of the catapult and dump a sufficient number of stones there. Reclaim the ammo using -- (making sure that you don't have any stone stockpiles that permit the stone you used) and you're good to go. With a sufficiently strong/agile siege operator (and a lack of distractions), you can easily manage 2-3 stones flying at once per catapult.

## Bugs

- Siege projectiles are surprisingly non-lethal
- Liaisons/children do not avoid standing in front of a firing ballista

------------------------------------------------------------------------

**See Also:**

:\*Defense design

:\*Army corps of engineers "Army corps of engineers")
