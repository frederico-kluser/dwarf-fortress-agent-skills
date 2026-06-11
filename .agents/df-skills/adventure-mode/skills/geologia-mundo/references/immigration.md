# Immigration

> Fonte: [Immigration](https://dwarffortresswiki.org/index.php/Immigration) — Dwarf Fortress Wiki (GFDL/MIT)

*"Migration" redirects here. This article is about people migrating into your fortress, for the opposite see emigration.*

**Immigration** is the process of people from another site of your home civilization moving into your fortress. As the fortress prospers, migrants will be attracted in larger numbers, these will arrive in groups once per season. In the early seasons after establishing the outpost, a smaller migrant group of 2-10 arrives, followed by a large group in the low double digits in the second spring one year after embarking. A notification will be received upon arrival, the migrant group will spawn at the edge of the map and proceed to march into your fortress and to the nearest meeting hall.

Migrants come from all walks of life; from historical figures and skilled craftsdwarves, to unwashed refugees fleeing the horrors of the land. Each group will often include such things as children and domestic animals, including both pets and stray livestock - be prepared with adequate food, drink, and beds, among other things.

The player can also initiate immigration by requesting workers from their holdings, and by accepting petitions for residency from visitors from nearby civilizations. Note that the migrant population must be managed carefully, as if it's too low, there might not be enough people available to maintain the fortress and its defenses, and if it's too high, the fortress may not be able to support your population, leaving them to the mercy of hunger, marauding raiders, and worse. However, migration waves are generally a good thing — if you're prepared for them.

## Skills and labor preferences

Each migrant can arrive with a wide collection of often unrelated skills, far greater than possible with one of the starting 7 dwarves, and experience levels as high as Legendary. Any and all skills might be represented, including obscure military skills (like blowgunner), high levels of one or more social skills, crutch walker, concentration and others - it's even possible to have dwarves with skills that may not be obtainable in fortress mode, like tracking or pikedwarf "pikedwarf"). However, Immigrant skills are influenced by your fortress' needs — migrants with skills your fortress uses a lot, or that your fortress does not have at all, are more likely to show up at your gates. Important skills (mining, food production, and basic crafting, according to Toady) are weighed more heavily than other skills.^(Source MP3)

Migrants may also arrive with equipment matching their skills; for example, a miner migrant may bring a pick with them. Migrants may arrive with all labors except hauling, cleaning, recovering wounded, and caring for wounded disabled, depending on the settings one has entered into d_init.txt.

Some immigrants are historical figures. These immigrants come to your fortress with skills representing their history, or wounds that they have suffered during world generation. They may even be vampires or werebeasts.

## Limiting/preventing immigration

In v0.50.01 and above, the game tab under the settings menu lists a *"Population Cap"* setting which immediately prevents further immigration once at the desired number. This includes the two hardcoded migrant waves, but does not include babies. There is also a *"Strict Population Cap"* setting which prevents both immigration and babies when reached. Both can be violated by a few special cases, such as the arrival of a monarch. Keep in mind that adjusting the population caps do not adjust population requirements (such as 80 to get a king). Such requirements can be modified in the game's advanced difficulty settings for your fortress.

The number of migrants depends on the created wealth of your fortress and is affected by your dwarves' activities. Note that if your fortress should ever become a mountainhome, you will receive an additional migration wave with the promotion, regardless of your population cap. The number of migrants is affected by how far below the population cap your fortress is. If your fortress is one dwarf short of the cap, you will receive a single migrant (if any). Also note that population cap will not remove dwarves from an existing fortress but will prevent new ones from immigrating or being born.

It is worth noting that you need a certain minimum population size before any of your dwarves will experience strange moods.

To reiterate, the population cap is a (mostly) hard limit on the number of dwarves in your fortress. If you want a fortress with 50 dwarves, simply set the *"Population Cap"* and *"Strict Population Cap"* settings in the game tab to 50.

## Immigration mechanics

The date on which immigrants appear in a season is determined at the start of that season, but the number of immigrants and their skills are determined when the migrant wave arrives. Typically there are two migrant waves that will appear no matter what (referred to as hardcoded waves) in the first two seasons. There is never a migration in the first winter - literally not even a message.

After the first two hardcoded waves, migrants will not arrive until the fortress has accumulated enough wealth, which must be reported by visitors such as merchants. A trade does not have to happen.

Migrant skill levels seem to depend on the size of the home civilization; a difference will be noticed if you picked a dwarven civilization that was not well-established (few towns or none) compared to a well-established one.

The two hardcoded waves may not show up for a while if the fort does not start on the 15th day of Granite. Note that there may be various reasons for a hardcoded migrant wave to not show up at all, such as if it were blocked by a siege, or if it is not the first fort in the world.

In rare cases, your civilization may undergo a  civil war. If this is the case, no immigrants will join your fort after the two hardcoded waves.

### Migrant wave sizes

The first two migrant waves have a minimum size of 1, if a wave member has a relative in your group already, and a maximum size of 10. The size of these waves is unaffected by fortress wealth, danger, or even the extinction of their home civilization. Note that there may be various reasons for a hardcoded migrant wave to not show up, like if it was blocked by a siege or if it is not the first fort in the world. The third migrant wave and on are influenced by the created wealth of the fortress, with more wealth attracting more immigrants (more research is needed to determine specifics) - specifically, influenced by the fortress wealth as reported by the last outgoing dwarven caravan. Wealth created after the caravan leaves has no influence until the next year's caravan leaves. If the caravan fails to make it out, then the fortress' wealth is not reported. If the dwarven liaison makes it out, but the caravan does not, the liaison does not report on fortress wealth.

Imported wealth, caravan sales figures, absolute caravan profit and caravan profit margin either have no effect on migration numbers, or only have an effect by applying a percent modification to the numbers driven by created wealth. If a fortress manages to trade (not offer) away 100% of its created wealth, then no immigrants will come the next season. More research is needed to determine if the statistics have any influence on migration numbers.

One factor which is known to affect migrant wave size is the total size of your fortress's nits list (all 4 categories), which consists of dwarves, invaders, merchants, and animals which either died or currently live at your fortress. As this number increases, the maximum size of migrant waves will be reduced: starting at a local population of 1000, migrant wave sizes are limited to 10, and at subsequent levels of 1300, 1600, 1800, 2000, 2200, 2400, 2600, 2800, and 2900, the limit is decreased by 1, and once you reach a local population of 3000 you will cease to get migrants at all.

The game will cull unimportant dead units eventually, see `CULL_DEAD_UNITS_AT` in settings. DFHack also has the command `fix/dead-units` that can clear uninteresting (unnamed) dead units from the units list and allow migrants to arrive again.

The largest wave size reported to date is 77 ^([archive)

## Fortress Failure Migration

If a fortress is abandoned during unhappy, stark raving mad times, the citizens can migrate to your new fortress *still* stark raving mad (berserk possibly, further looking into required). Likewise, if your fortress happened to have any husks around when it was abandoned, some of them may also migrate to your new fortress.

## Deterring migrants

A different message for migrant arrivals will be triggered depending on your fortress' dangerousness & happiness. That number is not actually a death count, but some sort of composite "fear" value determined by adding up a bunch of sources and dividing them by various amounts. It is currently not exactly known what those sources are, but at least one of them is a death count. 0-9 is normal, 10+ is "danger" or "dangerous", and 50+ is "cursed death trap" or "tomb".

| Messages (Some migrants arrival) |
|----|
| ''Some migrants have arrived. |
| ''Some migrants have arrived, despite the danger. |
| ''Some migrants have arrived at this unhappy place. |
| ''Some migrants have arrived at this unhappy place, despite the danger. |
| ''Some migrants have arrived at this miserable place. |
| ''Some migrants have arrived at this miserable place, despite the danger. |
| ''Some migrants have decided to brave this terrifying place, knowing it may be their tomb. |
| ''Some migrants have decided to brave this terrifying unhappy place, knowing it may be their tomb. |
| ''Some migrants have decided to brave this terrifying place, knowing it may be their miserable tomb. |

| Messages (One migrant arrival)                                       |
|----------------------------------------------------------------------|
| ''A migrant has arrived at this miserable place, despite the danger. |
| ''A migrant has arrived at this miserable place.                     |
| ''A migrant has arrived at this unhappy place, despite the danger.   |
| ''A migrant has arrived at this unhappy place.                       |
| ''A migrant has arrived, despite the danger.                         |
| ''A migrant has decided to brave this terrifying miserable place.    |
| ''A migrant has decided to brave this terrifying place.              |
| ''A migrant has decided to brave this terrifying unhappy place.      |
|                                                                      |

| Messages (Migrant Refusal) |
|----|
| ''No one else even considered making the journey to this cursed death-trap. |
| ''No one else even considered making the journey to this cursed miserable death-trap. |
| ''No one else even considered making the journey to this cursed unhappy death-trap. |
| ''No one else even considered making the journey to this miserable hellhole. |
| ''No one even considered making the journey to such a cursed death-trap this season. |
| ''No one even considered making the journey to such a cursed miserable death-trap this season. |
| ''No one even considered making the journey to such a cursed unhappy death-trap this season. |
| ''No one even considered making the journey to such a miserable hellhole this season. |

| Messages (Migrants Refusal) |
|----|
| ''The fortress attracted no migrants this season. |
| ''Migrants refused to journey to such a dangerous and miserable fortress this season. |
| ''Migrants refused to journey to such a dangerous and unhappy fortress this season. |
| ''Migrants refused to journey to such a dangerous fortress this season. |
| ''Migrants refused to journey to this unhappy fortress this season. |
| ''Migrants were too nervous to make the journey this season to this miserable fortress. |
| ''Migrants were too nervous to make the journey this season to this unhappy fortress. |
| ''Migrants were too nervous to make the journey this season. |
| ''Migrants were too wary to make the journey this season. |
| ''Others refused to journey to this dangerous and miserable fortress. |
| ''Others refused to journey to this dangerous and unhappy fortress. |
| ''Others refused to journey to this dangerous fortress. |
| ''Others refused to journey to this unhappy fortress. |
| ''Others were too nervous to make the journey to this miserable fortress. |
| ''Others were too nervous to make the journey to this unhappy fortress. |
| ''Others were too nervous to make the journey. |
| ''Others were too wary to make the journey. |

## Expelling migrants

Undesirable migrants can be selected for "emigration" from their individual preferences screen. To do this: Select the dwarf through the citizen list, view their Preferences, and press e to Expel. You will be prompted to confirm, and they will leave the fortress.

## Adventure mode

In certain locations in adventure mode, you may come across a Migrating Group - for instance, near any recently abandoned fortress; choosing to travel to the group will allow you to talk to the members of the former fortress as they travel back to dwarven civilization.

## Bugs

Some migrants will be incorrectly listed as babies or children, when they are not in the expected age range for those categories. This will automatically fix itself when they have their next birthday.

If your fortress does not have a meeting hall, you might have a situation where a single migrant cannot find the fort and just stands at the edge of the map, not moving at all. You may notice that, even if more migrants are part of the wave, they cannot enter the map (and do not show up on the units screen) until this migrant moves out of the square, as all migrants in a single wave must enter the map through this square.

## The Migrant Tier List

When a migrant wave arrives, players should stop what they are doing and check the migrants' skills to see what they may offer to their fortress.

Here, migrants are sorted into tiers, ordered by usefulness to a mid-to-high-level fort. "Valuable" skills can be sorted into three categories: those that produce better-quality items, those that perform tasks faster or more efficiently, and those that simply *cannot* be done unskilled, such as medical tasks. Even within these categories, dwarves can be more or less valuable depending on how often their skills are needed, or how difficult it is to raise their skill.

Lists like this are always just a guide, though. When you get down to bare bedrock, the most valuable skill a dwarf can have is the one that your fortress needs the most. Even those dwarves who have no useful skills can still be useful: even very young children can haul items, any healthy adult can serve as a low-quality soldier, and every adult dwarf can train useful skills over time.

#### Valued Migrants (A)

Some skills are central to most fortresses, either by improving the quality of critical items or by providing irreplaceable services. These migrants can improve a fort simply by showing up. *Also known as "can I give them a mood, please?"*.

- Weaponsmiths: Speak softly, but carry a big stick. Well-made weapons are significantly more deadly than poorly-made ones, on top of being more valuable. Weapons are also a great way to increase the value of rooms (particularly for nobles, temples, or guildhalls), because you can use a weapon trap to stack up to ten of them in a single tile. Skilling up weaponsmithing is time-consuming and always requires weapons-grade metal and fuel (or magma), and weapon artifacts can be some of the most useful items in the game.

- Armorsmiths: You need quite a lot of armor for a military, so armorsmiths are almost as useful as weaponsmiths, and you generally want more of them. Weaponsmiths are still a bit more useful: armor isn't quite as quality-dependent as weapons are, it can't easily be turned into furniture except with display furniture (which can be erratic when it comes to contributing to room value and can't prevent artifacts from being stolen), and armor artifacts are just as likely to be something of limited usefulness, like a single boot or gauntlet.

- Soldiers: Who doesn’t need extra meat shields dwarfpower? If you don't have any good soldiers yet, a skilled combatant is not only useful on their own, but can also teach peasants which end of the spear goes where. Even if you do have a well-trained military, soldiers have an alarming tendency to die, so reservists are still useful.

- Planters: Skilled growers produce larger stacks of crops. This has a cascading positive effect, making your cooks and brewers more efficient, making your prepared meals more valuable, and cramming more food and drink into fewer barrels or large pots, which means less need for hauling and more-efficient use of stockpile space. While it's relatively easy to train growers on your own, skilled growers have a huge downstream effect on your whole fortress.

- Mechanics: High-quality mechanisms don't jam when used in weapon traps, and a lever is another way to stack many valuable items in a single tile to juice room value. If you somehow have an excess, mechanisms make great (if heavy) elf-friendly trade goods.

- Cooks: Will quickly boost your fortress's value, and dwarves just adore fine meals, keeping up morale.

#### Good Migrants (B)

Put these dwarves to work, they have much to contribute. *Also known as "stalwarts of the fort"*.

- Miners: Always helpful, unless your fortress is *very* well developed - a high mining skill can also be useful in combat.

- Carpenters: Like blacksmiths, but they use wood instead of metal. Only source of quality beds and some newer items, like display cases and musical instruments. Also, only leather shields are lighter than wood. Wooden trap components can also be useful as a trade good if other industries have not been developed yet.

- Masons: Most fortresses cannot afford to make every piece of furniture out of metal or wood - stone is the traditional dwarven option, though it is a bit lacking in value as a material.

- Stonecrafters: Making trade goods for the caravan out of stone is a great way to kick-start trade, since metal and wood are often needed elsewhere. And real dwarves drink out of ≡stone mugs≡, not glass goblets or wooden cups or whatever.

- Engravers: Engraving is not usually needed in a new fort but is a huge boost in value and good thoughts in a mature one. A good engraver can smooth and detail a large room in *minutes*, shooting its quality sky-high, while a novice might take hours. Novice engravers also can take quite a while to train.

- Brewers: Should be obvious. Alcohol does not have a quality level, but the increase in production speed skilled brewers provide is never unwelcome.

- Healthcare: Skilled medical dwarves are irreplaceable for trying to save that one beloved soldier.

- Furnace operators: While bars do not have quality levels, highly skilled furnace operators are essential for producing enough metal for your metal industry.

- Wood burners: Similarly, unless your map has coal or you zipline the 100+ z-levels to magma, your furnaces are going to need a lot of charcoal.

- Leatherworkers: Leather can craft certain items that cannot be created sensibly with any other material, such as backpacks, quivers, waterskins, and lightweight shields (for all) and armor (for Hunters). Unless, of course, you are using adamantine.

#### Niche Migrants (C)

These migrants can be useful, but usually only in very specific cases, or for only a few tasks - if your fortress is focusing in that area, they fit in the above category, but if not, then they are just as valuable as peasants (see next category). *Also known as "it ain't much, but it's honest work"*.

- Blacksmiths: These dwarves make metal (not just iron) furniture and other large products, including valuable metal statues, which can boost the value of rooms and improve morale-how else are you going to immortalize your militia's valiant battle against that ferocious forest titan?

- Metalcrafters: You may not want to fill the next caravan with \*silver mugs\* and other metal finished goods, but making ≡gold chains)≡ for your guard animals and exotic pets is pretty dwarfy.

- Weavers, Clothiers: the textile industry is needed to supply your fort with thread, cloth and clothes, producing essential bags and ropes, materials for bandages and suturing, and preventing bad thoughts from dwarves whose clothes rot off their bodies (and cannot be reliably replaced with what the caravans bring).

- Millers, Shearers, Threshers: none of these labors have quality levels, but the increase in production speed can be highly profitable for a flour or textile industry.

- Glassmakers, Potters, and Glazers: You've either got sand/clay (and care about it), or you don't. Glassmakers can produce a wide variety of products, such as crafts, furniture, large weapons for traps and screw pumps, out of glass, and these products are often worth much more than their stone/wood counterparts. Potters are less versatile, but can also make valuable products for a decently low manufacturing price. Glazers complement potters and are needed to make their pots airtight and waterproof, allowing for liquid storage, and a good glaze job can add a lot of value to a product. Note that glassmakers and potters require sand or clay (respectively), and in large quantities to be truly effective, but these resources are basically infinite on embarks that contain them.

- Gem cutters and Gem setters: They just do not produce as much value as you would expect unless the gem cutter is of a high enough skill level. Training gem cutters so they do not waste your rough valuable gems with poor cuts is also quite tedious. Even then, gems are only useful for moods, decorations, or as a trade good. As for gem setters, encrusting is notoriously finicky, since the item to be decorated cannot be specified. So your gem setter will probably end up slapping your Masterwork cabochon cut diamonds on a barrel, or something.

- Herbalists: Herbology can be a wonderful way to kick-start an above-ground farm, or at least keep your food and booze supply nice and varied. Even dwarves can get sick of drinking the same old mushroom wine.

- Beekeepers, Wax workers, and Pressers: Beekeeping is interesting, but it isn't possible in biomes that lack honey bees (and note that bumblebees cannot bee domesticated). If you do get a beekeeping business going, wax workers and pressers become viable as well, since they use the products of beekeeping in their labors; otherwise, they are basically useless.

- Hunters: They usually come with a good marksdwarf skill, but immediately go hunting as soon as they are able to, causing possible fun. They can be useful if managed properly, and are definitely entertaining to watch, but it may be advantageous to just rely on your military for hunting game, since squads can be controlled more finely than hunters and are probably less likely to get themselves injured in the process.

- Fisherdwarves, Fish cleaners: Fishing is a decent source of food, and it's a great source of the elusive shells if your site contains pond turtles, but it runs the risk of crocodile accidents and other perils. Or, if you are unlucky, you will get absolutely nothing. Fisherdwarves can also only catch vermin fish; larger sea creatures require drowning chambers or other tactics.

- Siege engineers and Siege operators: Would be useful, but siege engines are currently bugged, dealing much less damage than you would expect, and they're often extremely dangerous to your own citizens when they do work as intended.

- Bone carvers: Bone is neither valuable (unless the creature was a megabeast or was very exotic), nor does it fulfill a particular niche, but it is a rather common alternative to wood, especially for practice bolts for marksdwarves.

- Dyers: Skilled Dyers can add extra value to dyed cloth, as it does have a quality level, but unless your fort is dependent on its textile industry, when was the last time you dyed cloth?

- Butchers, Tanners, Gelders, Animal trainers: While these labors can be pivotal to a fort's usage of animals, you really won't need more than one of these dwarves unless your meat industry is truly booming, and very often one dwarf can cover multiple of these jobs.

- Potash makers, Lye makers, Soapers, Pump operators, Woodcutters, Milkers, Cheesemakers: The products of these labors do not have quality levels, so the only difference between an unskilled laborer and a highly skilled one is production speed, which is really only critical if said products are the backbone of your industry (and who specializes in *soapmaking*?). Note that many of these products cannot be sourced from caravans, which makes domestic production a necessity, but still is not something needed "full time", or even close.

- Woodcrafters: Not to be confused with carpenters, these dwarves mostly just make useless crap and musical instruments out of wood. Show the elves what we think of their wood!

- Bookbinders, Papermakers: It is often much easier just to obtain codexes and paper from the caravan and migrants instead of producing them yourself, since that industry takes a while to setup, while producing limited benefits.

- Strand extractors: Skilled strand extractors are quick, and unskilled strand extraction is *agonizingly* slow. They are only useful after raw adamantine has been discovered and mined, and the strands do not have quality levels.

#### Useless Migrants (F)

Yes, "F" - they are that bad. *Also known as either "free military conscripts" or "can I toss them in the volcano now, please?", depending*.

- Peasants are not *entirely* useless, they are more like blank slates. Peasants can be trained in a moodable skill to control the artifacts your fortress will produce, and they make perfectly good haulers or military trainees, if you just ignore those pointless peasant skills.

- Animal dissectors and fish dissectors: They make animal extracts, which currently are some of the most useless items in the game.

- Bowyers: Bowyers make crossbows out of wood and bone... that is all. Weaponsmiths can do everything bowyers can do, except better, because heavier metallic crossbows are superior as blunt weapons in close quarters.

- Trappers: These dwarves make animal traps, not cages, which can only be used to trap vermin, not large creatures. You are better off relying on cats instead if vermin are threatening your stockpiles. These migrants often also have the marksdwarf or animal trainer skill, so their true value may lie elsewhere, unless you are seeking to trap vermin for a pet.

- Administrators: By the time migrant waves start arriving, you should already have these positions covered and filled; there is little advantage to having more than one dwarf with these skills. (The sole exception may be a new lead dwarf without any "item" preferences, so they issue no mandates, to replace a less appropriate/desirable leader, if you are lucky enough to find the right skill set.) Also see unfortunate accident.

- Animal caretakers: Bugged but may become more useful when fixed.

- Children: Cannot perform any labors. At least you will have a peasant...in about 18 years.

### Other

- Monarchs and their entourages: Serving as a major endgame goal, inviting these members of dwarven society comes with its own requirements and caveats, requiring a large amount of investment, labor, and time. The player can choose to never pursue this goal if they wish.
