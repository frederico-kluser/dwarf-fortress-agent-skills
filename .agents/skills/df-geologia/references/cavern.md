# Cavern

> Fonte: [Cavern](https://dwarffortresswiki.org/index.php/Cavern) — Dwarf Fortress Wiki (GFDL/MIT)

*Not to be confused with Cave.*

**Caverns** are *huge* natural underground tunnel systems, inhabited by strange and dangerous creatures. They go up, down, left, right, and just about anywhere else. Vanilla worlds provide three cavern layers. Number, size and z-position can be altered in the world generation parameters.

The caverns will usually have open map edges, allowing all sorts of creatures to migrate into and from them. By exploring the caverns in adventure mode it is possible to travel large distances below the surface - the caverns effectively connect all sites that access them.

Upon reclaiming a fort, all mud in the caverns is removed.

*In subterranean biomes, Chasm, water, and lava mean land, water (pool), and magma (pipes) respectively.*

## Geography

The top of the first cavern usually resides about 10-11 z-levels below the surface. Each cavern layer spans multiple z-levels. Beneath the third layer lies the magma sea.

If you hit caverns too often, then you can create a custom world with a higher number for 'Z Levels Above Layer 1' - Levels of stone above the first cavern layer. Making this higher will guarantee at least this many levels to build your fortress, but will have no impact on how many z-levels thick the surface layer is. Also, the top of a cavern may be higher than the rest of a cavern, so in practice there will be more levels than this.

Generating worlds using the ISLAND template tends to produce much deeper caverns (hundreds of z-levels down) than those with the REGION template, where only 50-60 z levels will separate the surface from the Underworld.

### Lakes and Pools

Usually, most cavern layers are filled with water to a certain degree. This can range from a few pools (similar to, but distinct from murky pools) at the bottom level to the whole layer being submerged, forming a gigantic underground sea, including fish and possibly camps of olm men and other fun aquatic creatures. If a body of water in a cavern connects to the map edge, creatures native to subterranean/underground biomes, that can swim, are able to spawn there, which maybe be considered a danger or a benefit.

The average amount of water cavern layers feature depends on your world generation settings, specifically

`   [CAVERN_LAYER_WATER_MIN:0]`

`   [CAVERN_LAYER_WATER_MAX:100]`

### Features

Exploring the underground world, you may find a variety of special geographical features. When your dwarves discover a feature, an announcement window will let you know of it.

**Deep pits:** Deep pits are... deep pits that connect one cavern level to the next. They have a fixed shape: The top z-level, where the pit meets the next cavern level, is un-muddied rough rock floor where the normal open space of the deep pit, and the random rock spires of the cavern collide.

If your map has an unseen cave-in at the beginning of embark, the caverns may have a deep pit somewhere. This occurs because some stone in the cavern above the deep pit is unsupported and falls down. This may be a bug.

**Magma pools:** Despite the name, magma pools are not actual pools, but tubes extending up from the magma sea. Their shape is fixed and their presence random. A magma tube might extend all the way to the top cavern, or merely a few z-levels. Magma pools can be distinguished from the magma sea even if they are only a single Z-level high due to two important features: they will always be walled by obsidian as opposed to the standard stone of the layer and, more importantly, will (very slowly) refill to their top if any magma is drained.

**Passages:** Passages are natural tunnels connecting two layers by ramps and short, twisted tunnel sections. The announcement window will let you know you've found a downward passage even if you happen to discover it from the bottom.

## Wildlife

A number of vermin and creatures can only be found in subterranean biomes, at certain cavern levels. Cavern creatures seem to follow different rules from above-ground creatures - their population numbers are usually far more than their raws imply, and alignment plays no role in whether they can be found in the map or not. Good creatures like the gorlak, evil creatures like the troll and savage creatures like the giant cave spider can be found in any cavern, regardless of the actual surroundings.

Forgotten beasts are a special type of procedurally-generated megabeast found only in caverns, and may invade your map from any of the three cavern levels.

### Creatures

[TABLE]

¹ Subterranean animal people may occasionally launch ambushes into a fortress from any of the cavern levels.

² Forgotten beasts are a special type of invader who serve as subterranean megabeasts.

### Vermin

[TABLE]

## Vegetation

Any cavern layer without a pool of water will have only muddy dense floor fungus, and no plants or trees except blood thorns.

Removing a layer will cause the layer above to randomly pick from trees that the now-removed layer could have handled and that the layer above can handle.

### Shrubs

[TABLE]

### Trees

[TABLE]

### Grasses

[TABLE]

## Dangers

Though digging down can be tempting, coupled with the fact that caverns can provide some helpful resources, there are many, many dangerous fun animals in a cavern. This includes giant cave spiders, giant olms, trolls and cave crocodiles, but even the seemingly harmless ones can provide great fun.

Cavern level one is as good as things get, and the following levels will only be worse. If you can't stand level one, you won't be able to stand level two or three. Flying creatures can ruin your day provide some fun if your main stairwell leads directly into the cavern (the bottom of up-down/down stairs can be passed by flying creatures). Also, any cavern of sufficient size will be inhabited by giant cave spiders, which can be both a benefit and a hazard.

Opening the caverns will make it possible for your fortress to be attacked by forgotten beasts, which range in lethality from "not much" to "nigh unkillable". One thing you really have to watch out for is having your main stairwell lead into a cavern. It doesn't have to be so walking creatures can get in, but just so there's an open hole. Any hostile creature sitting under your open stairway will spook any dwarves trying to use it, causing a flood of job cancellation messages as they keep trying to reach their destination. When this happens, it can lead to all your dwarves starving themselves to death. Only build stairs on the side, preferably with a hatch.

And of course, digging too deep will lead the player to encounter certain overwhelmingly fun things.

## Benefits

Caverns provide ever-regenerating resources in the form of underground forests, animals to hunt, and fish. On breaching a cavern layer, a variety of ores and gems lining its walls will be revealed. The cavern floors are always muddied, providing soil to a variety of underground plants. Also, underground caverns and the water they provide can be used in constructions and traps. In places like glaciers, caverns will provide the only source of water and farmable land. Throwing your prisoners into a damp hellhole filled with ravaging beasts is a nice addition, too. Additionally, creating a world without caverns will result in no subterranean plants, plant products (plump helmets/spawn/wine etc.) or fish available on embark. However this is a moot point, as without mods, dwarven civilizations only use indoor farming, and so will never form. Worldgen will stall without a usable dwarven civilization.

Once an underground cavern has been discovered, shrubs and trees will spontaneously grow on any subterranean soil or muddied rock on every embark site that accesses the cavern. This means that if you find a cavern in one embark site and embark in another site accessing the same cavern, plants will start growing there even before you discover the branch of the cavern that lies under the site. This allows you to construct underground tree farms and avoid sending dwarves to the surface to harvest wood, or just to get wood in environments without above-ground forests.

As walls can be built right up to the map edge below ground, it is possible to prevent land creatures from spawning by turning all the spawn points into walls. A single level of wall is sufficient to halt most non-fliers, who will appear on the wall and be unable to get down into the cavern itself. Creatures with the ability to climb or jump, however, tend to eventually figure out a way down, so prepare for these accordingly. Fliers can be stopped only by building walls up to the ceiling, and swimmers can't be prevented from spawning without obsidianising the water tiles on the map edge. The next best thing is to block off access, which can be achieved by dropping a layer of natural stone wall into the water.

NOTE: walls come with floors above them, which means that creatures may still spawn on top of the wall and interrupt jobs, or not spawn where you want them to (if you are trying to wall off most entrances and leave a few designated entrances with cage traps). So fortifications without floors on top of them should be built instead to seal an entrance from ground creatures. Also avoid completely walling off all ground creatures with only 1 floor of walls; the game will spawn flying creatures if ground creatures cannot be spawned.

### Creatures

Cage traps placed in the caverns can capture wild animals to potentially tame. As with above-ground creatures, subterranean groups of creatures are limited to one group at a time. Many of the more interesting creatures appear in groups of one and have small populations, so you'll have to clear out a lot of bugbats and crundles before being able to grab every giant cave spider or jabberer your site can produce.

These small populations may result in all spawned individuals being of the same sex, making breeding programs impossible even for creatures that have the necessary tags. Adding the \[CHILD:1\] to a creature is a relatively easy mod, but sex changes require the application of a transformational syndrome, and possibly changing the creature from an egg-layer to a live-birther.

## When should I start exploring?

One standard approach is to wait until you have a working military. The first cavern usually has few hazardous monsters, apart from the occasional giant olm or toad and giant cave spiders, but just one giant bat can destroy an early fort, and uninvited guests will wander in sooner or later. The subsequent caverns will become increasingly fun, so don't dig too deep without making adequate preparation. A decent military should be able to handle the cavern fauna, assuming they're not busy dealing with surface invaders.

Alternatively, you might want to breach the caverns as early as possible, then wall off the entrance. Doing so has several benefits: it will allow you to plan your fortress layout around the underground features, release the spores necessary for an underground tree farm, prevent a calamitous discovery later when powerful enemies lie in wait, and minimize the amount of time invested if the caverns prove unsuitable. You can of course continue to explore a cavern without a military, but you will likely get a bunch of dwarves killed.

Another alternative approach is to breach the caverns on a separate tunnel from your main fortress, so that beasts found inside have to path through the surface to reach your citizens, much in the way regular wild animals and invaders have to. Watch out for automatically created 'collect silk' jobs though, since dwarves assigned to them will be all the more in danger.

Not all parts of a cavern are immediately visible; a good portion of a cavern is revealed once you breach it, but other parts remain hidden until your dwarves explore them. Since you often don't know what you'll find in a cavern, they can be exciting places, but also very dangerous fun.

## Methods of exploration

*This section covers methods to explore already-discovered caverns; if you're having trouble finding the caverns, check Exploratory mining for tips.*

There are many different methods of exploring, some less fun than others.

**Military squads**: You can order your squads into the cavern with move orders. This way you can have dwarves manually explore the cavern by foot. The caverns are dangerous and unpredictable; well equipped dwarves will live longer. The quad:ttack:ist command will help you find and kill enemy creatures which may be located on many different z-levels inside the cavern.

Note that creatures may wander into the cavern from the edges, so, if you want to start collecting silk, gems, ore and the other valuable loot in a cavern, and you want to do so safely, you should first kill or capture the creatures in the cavern, then wall off the edges to keep new creatures from wandering in. Note that, if you want to keep flying creatures out, your walls will need to cover the edge of the cavern from the floor to the ceiling. If you'd still like to fight or capture wandering creatures, but don't want them killing your workers, you can leave some room for creatures to get in, and build doors or cages as necessary.

**Monster slayers**: Once you've discovered a cavern, if your world's population and history is large enough, a steady stream of wandering monster slayers will come to your fort, petitioning you for the right to live there and kill the awful horrors that live beneath your feet. While it's best not to rely on them to actually keep your fort safe from deep trouble, they actually do a pretty solid job of mapping out your caverns for you. Just be sure to keep cage traps and sane armed guards at whatever access route you choose to leave open so your slayers can reach their tasty slayables.

**Lone woodcutter**: Most cavern creatures are not faster than a normal dwarf, so it may be safer to send out a civilian woodcutter to cut 1 tree at where you want to explore. Unlike exploring with an early unarmed military team that will suicide against jabberers, a woodcutter will actually run away when confronted by hostile creatures. Cavern creatures also tend to give up the chase after a while, provided you can dodge the few hits they rarely get in if they catch up (not a problem if your explorer has moderate dodging skill).

**Fortifications**: as dwarves can see through fortifications, you can carve out a fortification near the edge of the explored area to safely discover more of the cavern. This prevents wildlife and megabeasts from entering your fort, as an added benefit. This method does not work for exploring the magma layers - or rather, it *does* work, but for a very, very brief time during which there is much fun.

**Digging and walling**: Instead of smoothing a wall and then carving a fortification, it can be quicker to just dig out the wall and then blocking off the opening with a constructed wall. The disadvantage over the fortification method is that if any dangerous creatures are lurking unseen near edge of the explored area they might get to your dwarf before the wall can be put up.

**Digging from above**: The only method that works in the magma layers, this method requires you to dig a hole from above the caverns into the cavern. It is advisable to seal the hole afterwards if you wish to prevent flying or magma creatures from entering your fort.

**Autonomous Dwarven Cavern Rover**: Pit an animal into the cavern through an access tunnel above the cavern floor, walling it up afterward if you wish. The animal will wander the cavern, revealing more of it, and possibly stumble across things you would prefer your dwarves not encounter unaware. If the animal is tame, its movement can be somewhat controlled by creating a meeting zone in the place you would like it to move to.

**Suicide mission**: Ideal for exploring the bottom of a deep pit or magma pool. Knock a dwarf or animal into the pit, and they will rapidly plummet. Despite being unconscious, they will report everything they see for as long as they are alive. Nobles, cats and vampires make excellent geonauts.

**Separate tunnels**: Digging exploration tunnels from within your fortress will result in a direct path from the caverns to your fortress- this can result in enormous volumes of fun. Players seeking to avoid fun may instead choose to start their exploration tunnels from elsewhere on the surface, outside the fortress. This guarantees that any threats released through exploration must pass through the same entrance utilized by surface threats, such as goblins or elephants, before they can access the fortress.

This method works in conjunction with the "Digging from above" method. Placing the tunnels as close as possible to the edges of the map will reduce obstruction to the fortress. The Dwarf Fortress Wiki assumes no liability for any potential damage to lesser surface races resulting from the release of subterranean monsters directly into the surface world.

## Adventure mode

You can enter a cavern with an adventurer and explore it. Ways to enter them include caves, dwarven fortresses that connect to tunnels, starting in Mountain halls, and goblin dark pits that have pits that can be climbed down. You can also encounter downward passages or deep pits that connect the different cavern levels.

The dangers are obvious; Nasty creatures, pitfalls, etc. You also have to watch out because you can't fast-travel underground, unless you are in a generated tunnel, and you can only start fast travel on those if you are not in a mountain tile or hostile site. That means no easy healing, so you have to be very careful. Make sure you stock up on food, water and (if you use it) ammunition before you head in, though, as caverns are quite massive and it can be difficult to find your way back. Worse, there are tribes of animal men underground, and unlike in the good old days they'll attack on sight. If you're lucky, you'll find a gremlin or other non-hostile intelligent wildlife, and those can potentially be recruited. Since you can't fast-travel, you have to rely on sleeping to heal, which can be dangerous due to the nature of caverns. You're on your own against whatever shows up, unless you brought or find allies. Escaping from the caverns by the same route used as an entrance can be very difficult, though if you manage to reach a cavern area immediately underneath a town you will be able to fast-travel to the surface.

If you discover the underground caves in Adventure mode, then retire and start a fortress, the fortress will grow subterranean plants as if a passage to the underground had already been opened on that map.

## Caravan and embark item availability

Embarkation and dwarven caravans will only provide resources available in the first cavern level. Since purring maggots don't appear in the first cavern level, unlike in 40d, you can't buy dwarven cheese or dwarven milk . A workaround is to edit the global raw files to make purring maggots appear on level one or be ALWAYS_PRESENT as pets of dwarven civilization, generate a new world, then edit the raws of the new world to change the maggots back to normal before embark.
