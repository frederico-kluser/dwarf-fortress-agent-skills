# Demon

> Fonte: [Demon](https://dwarffortresswiki.org/index.php/Demon) — Dwarf Fortress Wiki (GFDL/MIT)

**Demons** are procedurally-generated creatures who inhabit the Underworld. These immense, malicious and formidably powerful beasts are among the most powerful enemies in the game in both fortress mode and adventurer mode. They are not available to be spawned in the object testing arena.

## Overview

Demons inhabit the Underworld. They are randomly generated at worldgen, creating unique fun for every player. Examples of possible demons include giant centipedes made of ash that hunger for blood, eyeless mosquitoes that spit toxins, and emaciated fruitbats with giant clicking mandibles. The number of different types of demon created during world generation is closely related to world size, and it can be directly controlled with advanced world generation – a world generated with "" set to in advanced world generation will not have any demons in it.

All demons share certain traits. They are supernatural, fanciful, evil-aligned creatures represented by an ampersand with a randomized color. They are all able to swim in and breathe water and magma, and destroy buildings. Furthermore, they are immune to traps, pain, fear, nausea, stunning, exertion, dizziness, fevers, fire, any sort of poison, and have fixed body temperature, thus are unaffected by extremes of heat and cold (even if made of materials that would suggest otherwise). Roughly half possess extravision. They are very large (size 10,000,000, smaller than a megabeast, but larger than a giant and 167 times the size of a dwarf). They don't require sleep, food, or drink. All non-unique demons start out at Accomplished skill level in the following combat skills: wrestling, biting, striking, kicking, fighting, archery, dodging, and observing. Unique demons start out at Grand Master in the same skills. All unique demons, and roughly a half of non-unique ones, possess intelligence ([`[CAN_LEARN]`](Creature_token#CAN_LEARN "[CAN_LEARN]") + [`[CAN_SPEAK]`](Creature_token#CAN_SPEAK "[CAN_SPEAK]")), so demons you face may well have developed their skills to a higher level than they began with; however, their skills cannot rust to a lower level. The initial wave spawns exactly one frame after you open the Underworld; the amount spawned can range from 10 to over 100. Demons inhabiting the Underworld spawn in groups of 1-5 individuals. The size of their population, specified as 5-10 in the raws, appears to be irrelevant, as the game makes all inhabitants of the Underworld spawn in limitless numbers. As long as the Underworld is unsealed, demons will continue to wander in from the edges of the map indefinitely, due to having populations that are (functionally) infinite.

Demons receive large bonuses to every physical attribute except agility, and to the mental attributes of focus and willpower (also analytical ability, memory, linguistic ability, and social awareness, but those are less relevant). Many, but not all demons, are capable of flight. They may possess a wide variety of special attacks, including webbing, firebreath, poisonous appendages, toxic spittle or poison breath. Inorganic or zombie demons are especially difficult to kill; they can be killed by bisection, decapitation, or pulping via blunt weapons (inorganic blobs can only be killed in this manner), but this is far beyond the capacities of an ordinary dwarf.

Demons of each species can be all genderless, all male or all female, or have both male and female castes. The latter can breed if given enough time. All demons are born adults, and immediately reach their full size after being born. They have a pet value of 2000☼, but cannot be tamed, and you are rather unlikely to capture one. If you have deactivated compressed saves, the raws for a given world's demons (as well as forgotten beasts, titans, werebeasts, etc.) can be found in the world.dat of its save folder. Blob/inorganic demons tend to be genderless and non-sapient, but more research is required on this.

Due to their somewhat spoilery nature – new players are unlikely to know they exist, creating much surprise when they inevitably dig too deep – veteran *Dwarf Fortress* players tend to hide the existence of demons by giving them nicknames, the most famous being **Hidden Fun Stuff** and **clowns**, with the Underworld being their "circus". Unique demons (see below), by extension, are usually referred to as the **ringleaders**.

Dwarves may like a species of demon for their *horrifying features*, their *rhythmic undulations* or their *bloated appearance*.

## Their interaction with the world

Certain types of demons, those described as "being twisted into humanoid form" and marked with instead of in world.dat, will occasionally escape the underworld. This happens by the aid of a deity matching that particular demon's sphere through a ritual conducted with an artifact slab. Once they are in the mortal world, they will gain rule over a goblin civilization – each goblin faction in the world will be led by a unique demon, and attempting to create a world without demons in it through advanced world generation will lead to goblins being locked away in the underworld until a dwarf civilization digs too deep. As noted in legends mode, these demons will occasionally make journeys to the depths of the world and tame the creatures that dwell in them – most specifically, species with the token – going from giant rats to voracious cave crawlers and cave dragons. Presumably, this is how goblin civilizations gain access to these creatures to use them in sieges.

Demons may also arise when a dwarven civilization digs too deep in worldgen – the dwarves have a chance to fight them off, but, most of the time, the fortress will be taken over by goblins under a demonic ruler.

Found within the goblins' dark fortresses are demonic spires made of slade, whose lowermost levels lead directly into the Underworld. They will also create slade vaults, whose treasure is guarded by incredibly powerful and dangerous angels. If you can manage to fight off those freakishly strong beings (don't expect to by the way), you can find in the vault's centre the slab that contains the demon's true name. Learning this name allows your adventurer to either banish it back to the Underworld or bind it to your servitude. Although you will have a next to unkillable super soldier on your side if you opt for the latter, it's more of a bragging-rights reward, if anything – getting past the angels already requires pretty much being a god among men.

 banish.png\|Banishing a demon back to the Underworld  compel service.png\|Compelling service from demon

Escaped demons can also take over human civilizations by impersonating deities and having humans worship them. As with conventional lords, you can encounter them as normal in adventure mode – they won't be hostile to you and will behave as any other member of the civilization they rule. They can also arrive as non-hostile diplomats from human civilizations in fortress mode. Depending on the type of demon, this can be mildly amusing, or inadvertently deadly to your fort or adventurer.

In fortress mode, goblin law-giver demons may arrive as part of a goblin siege and are most of the time very dangerous.

Demons can (and, in most cases, will) spread sphere-aligned evil from sites they control. Nightmare or darkness demons will spread regions filled with bogeymen, death demons will spread reanimating evil regions, and so on. The evil-spreading can be reversed if the demon is slain or their site conquered or razed (e.g. through a raid.)

Depending on their spheres, demons may also be granted abilities similar to those of necromancers. Death demons are able to create experiments and raise corpses and intelligent undead, though they do not raise corpses in world gen because they would be hostile to the goblins they rule. Nightmare demons may be able to summon nightmares and bogeymen.

## Demon generation

Although the exact algorithm used to produce demons is unknown, something of the algorithm can be gathered from the string dump and analysis of demons. When generating a demon, the game begins by picking a creature from a predefined list, which is fixed and includes creatures not found in vanilla DF (such as anteater, ankylosaurid) and more general shapes (blob, quadruped, and humanoid). It is granted spheres, with a preference for "negative" spheres like misery, death, and torture. If inorganic, a material will be chosen, either one of the hardcoded ones (such as salt, ash, ice, or vomit), flames, or a randomly chosen raw-defined inorganic (any type of stone, soil, gem, metal, or other, such as gypsum plaster). If organic, it will get some sort of randomly-colored covering (such as feathers or hair) and/or have some feature (such as its eyes, nose or skin) removed. It will be granted a few "extra" features, like a tail, a trunk, or a shell, and a flavorful descriptor (such as "it knows and intones the names of all it encounters"). It may get some sort of special attack (such as a poisonous sting, toxic breath, fire breath). It will finally be given a name consisting of an adjective and a noun. The adjective will be based on the creature's color, its material (such as "inferno" or "snow"), what animal it's shaped like, or a descriptor (such as "winged", "three-eyed" or "skinless"), and the noun chosen from the following list: demon, devil, fiend, brute, monster, spirit, ghost, banshee, haunt, phantom, specter, or wraith.

## Strategy

Of all of the challenges facing a player, defeating a demon horde is probably the most difficult, unless you are using certain trap schemes – and even then, you will need to take special precautions.

### Containment

Containment is the simplest strategy for dealing with demons. A simple constructed wall will block any demon. Because of their building destroyer status, demons cannot be contained via locked doors. However, indestructible artifact-quality portals can stop them, as can some bridges. As building destroyers can only destroy objects on the same z-level, a floor grate or forbidden hatch cover on a staircase/channel will also block movement. It may be difficult to lure demons away from artifact furniture, should the area need to be accessed to reset a trap. If using bridges, be aware that any raising bridge that lands on a demon will deconstruct, and that demons can easily have internal temperatures greatly exceeding the melting points of steel or iron, leading to deconstruction as they pass over them. Because of their vast numbers, containment is an important part of any attempt to defeat them – fighting two groups of 25 demons is much easier than fighting one group of 50.

One particular gentleman, AussieGuy on the Bay12 forums, has found an ingenious method for disposing of an entire demonic invasion at once: a stupid dwarven trick known as "the dwarven checkerboard".(Source)

When using forbidden hatches to control flow of demons, note that some demons may be spawned with CANOPENDOORS to be not set, so once you unforbid the hatch, only the demons that can open doors will go through the door. The ones that can't open doors will remain behind the hatch, even if it is passable.

### Traps

Because all demons avoid traps, trapping demons can be very difficult – but not impossible. Demons become vulnerable to traps when they are webbed, so if you can find a way to get web onto your traps, the demons will be affected as any other creature (including your own dwarves!) would be.

Alternatively, advanced triggered traps may be used. Demons do not set off pressure plates, but if you can contain them, retracting upright spikes, casting them into obsidian, or caving a portion of mountain onto them are all effective. Any plan involving these kind of traps must involve both a way to bait the demons to where you want them and a way to keep the demons where you want them. Tame animals appear to work well as bait, but need to be replaced as they're killed. Bridges can be used to contain the demons, but be wary of the risks of deconstruction as described above.

Many traps need to be designed with the potential for extreme temperatures in mind. Obsidian trappers may find water used in the casting process boiling into steam before it contacts magma. Frequently, demons made of fire or steam explode on death, broiling nearby creatures and furniture. This effect can destroy upright spikes, leaving you with a trap chamber full of demons that you have no way to deal with. Demons do not destroy supports directly, but a hot enough demon may cause the destruction of nearby supports, just through heat damage. A clever dwarf might find a way to turn that to their advantage, if only such a thing as a clever dwarf existed.

### Ranged combat

Ranged combat sounds appealing, especially in the face of demons that explode with unimaginable heat upon death, but should be considered carefully. Most demons have vastly more powerful ranged attacks than marksdwarves have. Demons made of weak materials can be easily killed or dismembered by bolts, but inorganic demons composed of stronger stuff will only suffer chipped "bones".

Fortifications are appealing, as they can be dug directly into adamantine without ever exposing your fortress to a path to the demons. Even demons made out of steam cannot pass through a fortification unless it is submerged in 7/7 water or magma. Demons with syndrome attacks may attack through fortifications even without a path, although they appear to do so less frequently than if they have a path.

Still, should you contain a group of demons composed of weaker materials, marksdwarves can be very effective.

### Melee combat

Demons can be very frightening melee opponents, as each one alone is nearly the size of a megabeast, extremely fast, and has tremendous natural combat skills. That would be bad enough, but there tend to be pages of them rather than individuals. However, demons can still be defeated in melee combat.

Despite their powerful attacks, many demons are made up of very flimsy materials, such as salt, snow, steam, or filth. A strong punch can decapitate creatures like this. Some demons, however, can be made of much harder materials, and it can be very difficult to bring down a demon composed of minerals or armor-quality metal. Blunt weapons can be reasonably effective against weaker-material demons by severing limbs and body parts despite blunt status, but are not nearly as effective against demons as they are against earthly foes that suffer from pain and blood loss; without internal organs or blood loss, piercing weapons are relatively ineffective. Good slashing weapons can reliably take down demons of any material type.

The challenge of melee combat is how to deal with an enormous number of strong combatants while protecting against area-of-effect syndrome attacks and death explosions. Restraining visibility via a labyrinthine battleground is a good start. The area effects suggest meeting them with successive small waves of melee dwarves, but if the dwarves are too few, they'll be butchered by hundreds of angry demons before making a dent.

In all cases, your demon-fighting melee dwarves should be very well armed and armored (steel and adamantine) and Legendary in some, if not all, of the relevant combat skills.

### Clean-up

Unfortunately, once the wave of demons has been dealt with, it's not yet over. Syndrome-bearing dust and blood may litter the battlefield and your survivors, and can be very difficult to isolate and contain. Some dwarves may carry burning items back from their encounters with very hot demons. Survivors should all pass through a shallow pool of water to wash them and their equipment of anything dangerous and to douse any flames. Any path used for the fight is best abandoned and walled up. Demons will continue to enter the Underworld from its map edges, as wildlife do on the surface, but path differently from the initial wave, content to wander through the Underworld even should a simple unobstructed path exist into your fortress.

## Killed demons

Only unintelligent demons can be butchered in unmodded games, and butchering them yields products similar to those from forgotten beasts, including copious amounts of meat and bones, vividly-colored hair, feathers, scales or chitin, and shells, if the demon had one. All materials obtained from demons have a value multiplier of 1, and aren't appreciably better than their mundane counterparts.

Inorganic demons cannot be butchered, and after killing them you obtain only a massive demonic corpse to use in your stupid dwarf trick.

Little do demons know that though their claws and fire cannot pierce the adamantine sealing them away, a simple copper pick (or any other kind of pick, for that matter) can dig right through it with ease. Armok forbid these unholy creatures ever get their hands on one.
