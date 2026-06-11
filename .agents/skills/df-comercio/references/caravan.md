# Caravan

> Fonte: [Caravan](https://dwarffortresswiki.org/index.php/Caravan) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

**Caravans** facilitate the transfer of goods between sites. Merchant caravans from the Mountainhome and neighboring friendly civilizations will arrive throughout the year, looking to trade, and if you "make contact" with other civilizations by sending a raid to "demand tribute", those civilizations' sites might be convinced to send a caravan of their own afterwards, \*on top\* of tribute 'caravans' and even if your demand fails. This means you could have multiple caravans in the same season for a given race, possibly at the same time.

Merchant caravans use pack animals, and for the worthy, wagons, to carry their goods, accompanied by guards for protection. An arrival of a caravan will trigger an announcement message (at the bottom of your screen) informing you that a caravan has arrived. They will appear on the edge of the map and proceed to move towards the trade depot where they will unload their goods. If caravans are unable to find a path to your trade depot (or if you have not built a depot at all), they will bypass your site. They may also turn around if they become spooked by wildlife or corpses, ambushed by goblins or any other enemy forces, or if it takes too long to reach the trade depot (though that would require weeks of travel while on the map).

Caravans will embark on their journey between 30000 and 40000 ticks (25 to 33.33 days) after their arrival, whether they have succeeded in reaching the depot or not. The announcement that they will be leaving soon is issued about 4 days before the announcement that they have embarked on their journey (at which point they do start to load their wagons and pack animals). Note that if the caravan team or their animals are delayed and prevented from leaving, they will eventually go insane. Merchants and diplomats go insane if they are unable to reach the map edge within 25 days of having finished their business at your fortress; for diplomats, this is when they end the meeting and try to leave, and with merchants it's when they've finished packing everything up. Caravan guards on the other hand do not count, meaning after all caravan traders, pack animals and wagons have left the map safely, the caravan is considered to have safely left the fortress, whatever happens to the remaining caravan guards (which are then shown as friendly) does not matter (so detaining them, using them for live target practice or cannon-fodder/first line of defense against sieges is all possible, without later repercussions from the parent civ of the caravan the guards did protect).

A maximum of 100 items (not counting the contents of cages, bags, bins and barrels) will be loaded on a pack animal of an arriving caravan (on the other hand caravans leaving a trade depot can load many more items on a pack animal).

## Types of Caravans

### Trade

*Further: Trade*

Trading caravans are useful for getting supplies not available in the player's fortress area. A caravan from the mountainhome and various friendly civilization you are in contact with will visit the fortress on a yearly basis, linked to one season, which is spring for elves, summer for humans, and autumn for dwarves - no race trades in winter by default.

Caravans will only show up if that race considers the fortress site both accessible (as denoted on the embark screen) and "worth the effort" (as determined by the \[PROGRESS_TRIGGER\_\*\] tokens in the entity definition), with the exception of dwarves, who always arrive unless they are extinct.

Take note that pre-barony a maximum of 200 items (not counting the contents of cages, bags, bins and barrels) will be brought by any trade caravan, as the caravan will have a maximum of two pack animals, regardless of whether the caravan weight limit would allow for more items to be brought.

### Tribute

*Further: Mission#Tribute*

If your fortress performs a successful mission to "demand tribute", whether it be one-time or annual, that site will also send a caravan, once a year. They usually arrive at the start of a season, and that season can be specified by you (including Winter) at the time of the mission. No actual "trading" or broker is involved, they simply drop off the goods at your depot and then leave, without speaking to any of your dwarves. Tribute caravans tend to be relatively small, but they are guarded. You don't have any control over the content of the tribute - what they bring depends on the civilization's available materials, the site's size and tracked items, and so forth, and may range from excessively mundane (like a bunch of average quality clothing) to extremely useful (like exotic animals). Notably, tributes are one of the few ways to obtain evil animals tamed by goblins, such as beak dogs for instance.

As stated above, tributes are also one of the few ways to "contact" another civilization without triggering an outright war, and therefore ensure that it will send out regular caravans afterwards, \*on top\* of the tribute caravans it'll be sending and even if your tribute demand failed.

## Mechanic

### Movement & Access to Depot

Caravans appear to enter the map from a random direction, one which does not necessarily coincide with the relative direction of the originating civilization on the world map, and they may appear from different directions and z-levels each year. However, they will always arrive at a location with a wagon-navigable path to the Trade Depot when one is available. Site-bisecting features like rivers will limit them to appear on a specific side, if only one side has an accessible path to your depot. While caravan traders and pack animals may use stairs and cross traps in order to access your depot, wagons cannot do so, and will not spawn if a clear path without stairs or traps is not available.

Caravans can usually be restricted to show up in a specific spot on the map edge, but under some circumstances they will insist on showing up on one particular side of the map. In particular, if your fortress is bisected by a river, then caravans and migrants will only ever arrive at tiles which were *originally* accessible from your original embark wagons "Wagon (embark)") - even if you later build a bridge across to the other side, those edges will never be used.

Also worth mentioning is the pathing behavior of the entire caravan. If one member of the caravan reaches an obstacle in their chosen path (i.e. a raised drawbridge that was lowered when they entered the map) the entire caravan will re-path, instead of encountering the obstacle one by one. This behavior can be useful when attempting to free "stuck" wagons - a trader on foot encountering a locked door will cause the stuck wagons to turn around and path to a different entrance/exit, if available.

### Destruction

If caravans are destroyed (intentionally or unintentionally), the items may remain for use. Caravans caught in a cave-in will flee as if they were attacked, but will leave all the items dropped by the caravan behind. Pack animals carrying items are affected just like a normal tamed mule and must be killed in the cave-in for them to drop items on the ground. It is however much more likely that the pack animals will only be stunned or rendered unconscious, and flee shortly after recovering from the hit.

While caravans can defend themselves, they don't like being ambushed. If a caravan becomes terrified by wildlife or horrified by corpses it will turn around and flee the map. Any event resulting in the death of any merchant or pack animal will also cause them to retreat and forget about trading with you for the season. Repeated caravan destruction (intentional or unintentional) will strain diplomatic relations and may result in a siege.

Ambushing or seizing a caravan and letting a survivor escape seems to have a more detrimental effect than simply annihilating the whole caravan. (Presumably because you've left a witness to report what happened.)

Overall, a given caravan visit can have a number of "problems" which will affect your relations with their civilization:

1.  "never seen again" - The entire caravan was destroyed and nobody left the map.
2.  "suffered hardships" - One or more merchants were killed, but some of them survived long enough to leave the map.
3.  "seized goods" - You seized goods from the caravan and they left.
4.  "offended" - You tried to trade wooden or animal items to the Elves.
5.  "missing goods" - The value of the caravan's goods when they left was less than what it was when they arrived (i.e. they had a net loss).

All of these will make the parent civilization unhappy, though some more than others. They take offence to both accidents and hostile acts - accidents just annoy them slightly less. In the case of elven merchants, they will take offence to your actions and bring fewer goods next year, do it too many times and they will declare war on you.

### Caravan Delay

If a caravan has arrived at your trade depot and is unable to leave for about two months after they finished packing up their goods, the merchants and animals will go insane. This can result in a bunch of merchants attacking your dwarves, or just standing around moping until they starve to death. It is not known for certain if this hurts diplomatic relations, but most likely it's the same as any case where the entire caravan fails to return home.

If you have locked the caravan into your fortress to hold out against a siege, it's a good idea to station a squad of soldiers near the trade depot in case the merchants go berserk. You may also want to make the depot a restricted area to encourage civilians to go around it. Alternatively, you can design the trade depot using drawbridges, so that it can be sealed off from the rest of the fortress during a siege.

If you want the merchants to leave safely, you can build four or more tunnels to each corner of the map, connected to your fortress only by drawbridges. As long as there is no other way to enter and exit your fortress, invaders and merchants will both go towards any tunnel that you activate. You can lock the merchants into the trade depot, and then open a tunnel entrance on one side of the map to make the invaders head towards that tunnel. When they get close to it, you can close it, and then open the entrance on the other side of the map, and let the merchants out of the depot. If your fortress and depot are in the middle of the map, this will give the merchants quite a head-start to get away.

Merchants can leave the map from any map edge-- including underground and aboveground map edges. If an unobstructed path through your fortress reaches a cavern edge, then blocking all overland paths will cause the merchants to depart underground. This can be useful, if you're suffering a prolonged siege; it can also be dangerous, if your underground regions are less secure than your surface. While it requires more preparation, an elevated bridge to a map edge can also allow merchants to depart in peace.

Caravan guards cannot be starved, dehydrated, or driven to insanity if prevented from leaving, their employers and animals can, however.

If a large amount of items are sold / offered to the caravan, it may take a while to load it all, especially if you chose to keep your precious bins and traded your items individually. Still even packing times of 43 days have so far shown no negative side effects (except dwarven guards and dwarven merchants having a thought about being kept from alcohol for too long).

## Bugs

- Caravans become terrified/horrified very easily, abandon their wagons, and flee. Bug:7185
- Wagons can occasionally become "stuck" on other wagons, walls, etc. Stuck wagons eventually deconstruct, leaving their merchandise behind. Bug:5687
- If a caravan attempts to leave in late Winter/early Spring, they may try to path over any large frozen body of water. If the water thaws while the caravan is on it, the caravan will become magically stuck in mid-air until either the water refreezes or a floor is built underneath it. At this point, if they are still alive, they will leave the map normally.
- When merchants leave with an animal, the merchants seem to be dragging their beast of burden instead of leading it. If the animal is incapacitated but not dead, the merchant will continue to walk at the same speed, dragging the unconscious beast.
- If a merchant's chosen map edge exit is guarded by a hostile creature (including those on a restraint), the merchant will wander back and forth repeatedly and eventually go insane rather than path to an alternate exit.
