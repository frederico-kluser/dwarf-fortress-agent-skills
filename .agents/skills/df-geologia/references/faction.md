# Faction

> Fonte: [Faction](https://dwarffortresswiki.org/index.php/Faction) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Factions** govern how creatures will react in each others' presence - the world is full of dangers for your unfortunate dwarves, and it seems that nearly everything is trying to kill them; fortunately, said dangers are also hostile to each other most of the time. Confrontations between such opposed factions happen in both fortress and adventurer mode; the wise player will see to it that they weaken each other instead of ganging up against one's fort or adventurer.

In the object testing arena, each creature created can be tied to a faction (referred to in-game as a "side"). Creatures will be friendly to other creatures within their faction, and will be hostile to any other creature. There are a total of 9999 factions, and an "independent" option which is hostile to all other creatures.

## Faction relative hostility

The table below shows the behavior of different factions when confronted:

|  |  |  |  |  |  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|----|----|----|----|----|
|  | **Dwarves** | **Elves** | **Humans** | **Goblins** | **Kobolds** | **Necromancers** | **Undead** | **Wildlife** | **Cave civs**2 | **(Semi-)Megabeasts** | **HFS** | **Werebeasts**3 |
| **Dwarves** | Friendly | Friendly1 | Friendly1 | Hostile1 | Hostile | Hostile | Hostile | Hostile | Hostile | Hostile | Hostile | Hostile |
| **Elves** | Friendly1 | Friendly | Friendly1 | Hostile1 | Hostile | Hostile | Hostile | Friendly | Hostile | Hostile | Hostile | Hostile |
| **Humans** | Friendly1 | Friendly1 | Friendly | Hostile1 | Hostile | Hostile | Hostile | Hostile | Hostile | Hostile | Hostile4 | Hostile |
| **Goblins** | Hostile1 | Hostile1 | Hostile1 | Friendly | Hostile | Hostile | Hostile | Hostile | Hostile | Hostile | Hostile4 | Hostile |
| **Kobolds** | Hostile | Hostile | Hostile | Hostile | Hostile | Hostile | Hostile | Hostile | Hostile | Hostile | Hostile | Hostile |
| **Necromancers** | Hostile | Hostile | Hostile | Hostile | Hostile | Hostile | Friendly | Hostile | Hostile | Hostile | Hostile | Hostile |
| **Undead** | Hostile | Hostile | Hostile | Hostile | Hostile | Friendly | Friendly | Hostile | Hostile | Hostile | Hostile | Hostile |
| **Wildlife** | Hostile | Friendly | Hostile | Hostile | Hostile | Hostile | Hostile | Variable5 | Hostile | Hostile | Hostile | Hostile |
| **Cave civs** | Hostile | Hostile | Hostile | Hostile | Hostile | Hostile | Hostile | Hostile | Friendly | Hostile | Hostile | Hostile |
| **(Semi-)Megabeasts** | Hostile | Hostile | Hostile | Hostile | Hostile | Hostile | Hostile | Hostile | Hostile | Friendly | Hostile | Hostile |
| **HFS** | Hostile | Hostile | Hostile | Hostile | Hostile | Hostile | Hostile | Hostile | Hostile | Hostile | Friendly | Hostile |
| **Werebeasts** | Hostile | Hostile | Hostile | Hostile | Hostile | Hostile | Hostile | Hostile | Hostile | Hostile | Hostile | Variable3 |

1Advanced civilizations are subject to the mechanisms of diplomacy and may routinely go to war or conclude peace treaties depending on worldgen and according to each civilization's ethics. On the one hand, war against elves or humans is not that uncommon; on the other hand, goblins will almost always be hostile toward everyone else.

2Cave civilizations are always hostile toward adventurers and they are usually hostile toward your dwarves. They often become friendly when confronted with a megabeast. Note that this behavior does not apply to most animal people, who are simply treated as wildlife.

3Werebeasts will switch factions from whatever civilization they belong to under their normal form to a special, species-dependent faction on the full moon. Different species of werebeasts will be hostile to each other.

4A HFS denizen often takes control of a goblin civilization, and sometimes becomes the ruler of a human civilization by posing as their god. Other HFS denizens are typically hostile.

5\[LARGE_PREDATOR\]s will attack anything significantly smaller than themselves. In most other cases, wildlife will flee from non-\[BENIGN\] wildlife. Two \[BENIGN\] wild animals will ignore each other.

## Entities and civilizations

There are four entity 'factions' that can be created in *Dwarf Fortress*, although vanilla only uses three of them. These factions are determined by the presence or absence of the Entity token#BABYSNATCHER or Entity token#ITEM_THIEF tags, so the four factions can be called the Civilized (with neither tag), the Babysnatchers, the Item Thieves, and the Babysnatching Item Thieves (which do not exist in vanilla DF). Members of the same faction will trade with you in fort mode, and members of all other factions may invade you. This is separate from civs at war, which is determined by having opposing ethics. (A civilization from an opposite faction which is \*also\* at war with you will simply siege you even more.)

Generally, civilization relationships override whatever loyalty a creature may have to begin with. Therefore:

- Conquered and otherwise incorporated populations from a foreign civ will always be loyal to that civ, both in fortress and adventure mode, \*except\* in the case of insurrections and nothing else.

- Foreign creatures kidnapped by goblins and raised by them will be loyal to their goblin civ and hostile against non-goblin civs, including your fort. This also includes their descendants, which means some goblin civs can be potentially *depleted* of goblins, but still send sieges (composed of humans, dwarves, elves, etc.) and ambushes to your fort.

- More amusingly, foreign creatures occupying a noble position in a civ for whatever reason (e.g. demons that have impersonated a god to take control of human civs, demon law-givers ruling goblin civs, or necromancer kings) will behave the same way any other civ member would toward your dwarves or adventurer. Hence the ludicrous possibilities for a demon to visit your fortress as a diplomat (or join you in your adventures) or a friendly necromancer inadvertently wreaking havoc on your fortress by raising corpses whenever they can.

Some caveats: sapient creatures without the ability to communicate will always be hostile, even if they technically would be considered the same faction. They will also wage endless wars, since they lack the ability to form treaties. This includes creatures without CAN_SPEAK (or INTELLIGENT, which is functionally CAN_LEARN and CAN_SPEAK combined). Creatures with UTTERANCES cannot communicate with other civs, however, if they have both UTTERANCES and CAN_SPEAK, they will be able to communicate. For instance: kobolds are unable to speak besides in utterances and are thus at war with everyone else - note that if you start as a kobold in adventure mode when they are available, you will be unable to speak to anyone, and other kobolds will attack you on sight because they won't be able to talk to you either.

Civilizations with the \[KILL_NEUTRAL:REQUIRED\] ethics (goblins in vanilla DF) will be hostile toward members of foreign civs. If you encounter goblins in Adventure mode, they will usually request that you "identify yourself". A common workaround if you are not from their civilization (which you usually aren't) is to assume a false identity so that they believe you are one of their own (remember that due to conquests, kidnappings, etc. multi-racial civilizations are the norm and being from another race wouldn't be considered suspicious).

## Undead and night creatures

The loyalty of undead and night creatures depends on whether they have a soul or not. Creatures with souls, even undead, will retain the existing loyalty links they had when they got 'transformed', with possible alterations or a more nefarious agenda of their own. For instance, necromancers, night trolls, mummies, etc. break off from civilizations and form separate entities with their own set of loyalties. This means they can and will conflict with one another (e.g. if they encounter each other while siegeing your fortress). Soulless undead (zombies and thralls), on the other hand, are hostile to every living creature (night creatures such as vampires are considered [`[NOT_LIVING]`](/index.php/Creature_token#NOT_LIVING "Creature token"), even if they do die), due to their [`[OPPOSED_TO_LIFE]`](/index.php/Creature_token#OPPOSED_TO_LIFE "Creature token") tag, which overrides all other relationships.

Vampires, despite their blood-sucking murder sprees, will still be loyal to their parent civ, including your fortress. In fortress mode, you can take advantage of their neutrality toward undead, ordering them to kill necromancers when facing a siege; a vampire can and will path toward a necromancer unhindered and usually beat them to death. You can also order vampires to kill zombies one by one as they won't react unless attacked. In adventure mode, when they are not exposed, they will behave as any member of a civ. Occasionally, they will be accompanied by cultists who will have formed a separate group gathered around their 'immortality worship': if you confront the vampire, they will turn against you.

Werebeasts are a notable exception: although nominally a night creature, they do not count as undead. Werebeasts are hostile toward each other (and everyone else) except if they belong to the same were-species (baby werebeasts are generally neutral with everyone).

Intelligent undead are creatures raised by necromancers to serve as their lieutenants. They retain their soul and aren't opposed to life but their loyalty will shift to that of the necromancer in worldgen. In fortress mode, intelligent undead raised by necromancers from your civilization are considered citizens if they were citizens when they died, and may be hostile (or just 'friendly' and mill around doing nothing) if they were invaders when they died. Intelligent undead raised by your adventurer will retain their loyalty links, so if you're the one that slew them in the first place, they will remember it and attack you on sight. A workaround is to destroy their soul by first raising them as regular undead, slay them, then raise them as intelligent undead - their soul will be a blank slate with no preexisting conflicting loyalties.

In adventure mode, should you learn the secrets of life and death or become a night creature yourself, all zombies will become neutral to you, letting you seize the opportunity to make short work of their squishy and unarmed masters. Undead you raise will follow you as if they were companions; however, they will **all** turn neutral if you purposely attack one of them. Generally speaking, there seems to be a worldwide solidarity among night creatures, and if your parent entity does not have beef with any of them, becoming a night creature will allow you to just chat with various necromancers or mummies, take quests from them, and take them as companions.

Occasionally, some creatures (either nightmare-aligned demons or necromancers who have somehow received secrets from a death deity that's also nightmare-aligned) will summon bogeymen and nightmares while attacking your fortress. These will usually be friendly.

## Levels of conflict

In adventure mode, while all hostile nonsapient beings are No Quarter by default (because they do not understand the concept of surrender), sapient creatures that are capable of speech (that means creatures with both \[CAN_LEARN\] and \[CAN_SPEAK\], or \[INTELLIGENT\]) can be talked out of a Lethal fight, either by surrendering to them or making them yield. A notable exception is creatures from civilizations with the \[KILL_NEUTRAL:REQUIRED\] or \[KILL_ENEMY:REQUIRED\] ethics, which are always No-Quarter with neutral and enemies, respectively. Non-lethal and below types of fighting (often happening at a tavern or as the result of a spat due to differing values or other grudges) can also be easily de-escalated. This makes conflicts with other hostile sapient beings much easier to manage.

In fortress mode, invaders and your dwarves are No Quarter toward each other (the only exception is elven or human diplomats offering peace treaties). Brawls may also happen at your tavern if non-dwarves drink more alcohol than their livers can handle, but these don't escalate into full blown war, although they do result in sometimes lethal injuries.

## Bandits and criminals

Bandits are entities consisting of groups harassing towns (including your fortress) from camps in the countryside, and they are hostile toward civilization members. If you don't want them to be hostile to your adventurer, you should start the game as an outsider with no link to existing entities, or assume the identity of one. Bandits may lay (small-scale) siege to you in fortress mode, and are often given as quest targets in adventure mode. However, as they effectively own sites (camps, with a boss acting as the lord) it means you can try and de-escalate any level of conflict you may have with them, talk to the boss, and join them as a lieutenant, and take quests from them, effectively shifting your loyalty.

Criminal organizations, on the other hand, dwell in a town's dungeons, and although they take part in various schemes, they are not nominally hostile toward anyone (apart from the occasional insult or spitting). Their members have links with existing groups in the town, and killing some of them as part of a quest may not be taken well by the citizenry.

## Insurrections

Several civilizations may lay claim to a single site. When a site belonging to a civilization gets occupied by another, there is a chance for the site's inhabitants to revolt, treating their current parent civ as enemies (and their former civ as friendly). This shift of loyalty often translates into a bunch of fights erupting out of nowhere in adventure mode.

## Intelligent wildlife

Random non-civilized intelligent beings (gorlaks, gremlins, animal people) are hostile (as wildlife would be) in fortress mode. In adventure mode, their behavior depends on their alignment - evil-aligned ones like trolls or ogres will attack you, while neutral and good-aligned ones like animal people or gorlaks can start conversations with you. (A notable exception is *civilized* animal people found in caves, that are hostile toward adventurers unlike previous versions.) They won't have much to say if they are not part of a civilization, though. Gremlins are special as they can be tamed in fortress mode, which means they are able to become pet citizens, which, in turn, triggers all sorts of weirdness.

Benign wildlife isn't really hostile in that they generally flee conflict if able, but they *will* put up a fight if cornered.

## Tamed enemies

In fortress mode, *any* creature that's been labelled as an enemy of your civilization *will* be hostile toward your fortress, no matter what. Creatures become enemies of your civilization by either killing a member of your civilization (e.g. one of your dwarves, but even pets qualify) or by belonging to an enemy civilization or otherwise hostile entity in the first place. In practice, this means that the following creatures will always be hostile, *despite* their tameable status:

- Megabeasts (rocs, hydras, dragons are the tameable megabeasts)
- Enemy mounts brought in a siege
- Wildlife creatures that have killed one of your dwarves or pets. Most often, they acquire a name for this feat.

You may cage and attempt to train these creatures, raise their training level, and sure enough, this will yield experience for your trainers, and raise civilization-level knowledge about the animals. But you should *never* set them free inside your fortress, as they will munch on your dwarves *and* trigger a loyalty cascade in the process. See below for specific cases.

Interestingly, the offspring of such creatures do *not* count as enemies of your civilization. This means you may attempt a breeding program between enemies of the same species, or an enemy and a wild counterpart that's presumably easier to handle. In practice, this leads to extremely disturbing situations where a mother either massacres her offspring as soon as she gives birth, or said offspring overwhelm her as soon as they come out of her. Note that this only ever happens if the species does not lay eggs - enemies do not use your nest boxes (and, if they are building destroyers, will simply demolish them) if you provide them with some.

## Miscellaneous

Megabeasts and semi-megabeasts are neutral toward each other, but will try to kill everything else they can find - whether it be in worldgen, adventurer mode or fortress mode. Forgotten beasts and titans are hostile to everyone, including other forgotten beasts and titans.

Berserk dwarves are hostile to everyone, including each other. Visitors side with their parent civ if it goes to war with you. Demons that didn't escape from the Underworld are hostile to every non-demon, and angels are hostile to every non-angel. This, obviously, does not apply to demons your adventurer has bound into servitude, nor does it apply to demons who rule (human or goblin) civilizations.

If for some reason a demon is given a nobility title, they will turn neutral to creatures from the same faction. If they are given a religious title, they will slaughter everyone with a different religion. Bestowing nobility titles can be a way to turn normally hostile creatures like night trolls or even bogeymen into becoming friendly to the parent civ the nobility relates to.

## Loyalty cascade

|  |
|----|
| "Faction" in other / Languages / Dwarven / : / uzlir / Elven / : / anoni / Goblin / : / osmrur / Human / : / ozo |

Loyalty cascades are the result of entity members attacking each other. The conflict will escalate into a full civil war (hence Toady One referring to it as the "civil war bug") and won't resolve until one side of the conflict is wiped out. Loyalty cascades can be triggered in both fortress and adventure mode.

### Attacking merchants from your mountainhome

If you order your military to kill merchants from your own civilization, a bizarre result of the way loyalty is handled makes the members of your military who attacked the traders become enemies of your civilization, but remain members of your fort's government (dwarves of this faction will henceforth be referred to as *separatists*). As enemies, they attack your other dwarves (*citizens*), but as members of the fort, they still follow orders. Allowing citizen militia-dwarves to attack the separatists will give them opposite loyalties of the separatists, (i.e. loyal to civ, not to fort), or *loyalists*, who do **not** follow orders. And then, if a separatist or loyalist kills a citizen, they become enemies of the civ **and** fort, making them *Renegades*, who are essentially complete enemies of the citizens.

### Attempting to tame enemy mounts

If you use cage traps against goblin sieges, you are likely to capture a few mounts from various species. You may assign them to your animal trainers and attempt to tame them, thus gaining a few facts about each specific species; but under no circumstances should you ever release them from their cages, as they are always considered enemies to your civilization and will wreak havoc as soon as they are free. Not only that, but they will trigger a similar loyalty cascade as soon as they attack your citizens, leading your fort to its demise through a never-ending civil war - as well as, for example, some copious jabberer-chomping. The best course of action is to keep re-training the mounts in their cages over and over again, thus facilitating future taming of their **wild** counterparts.

### Attacking a werebeast in dwarven form

If one of your dwarves turns into a werebeast and you send your military to kill them while shapeshifted, their failure to do so (and allowing the dwarf to revert to normal) may cause a loyalty cascade.

### Attacking a berserk citizen or werebeast in wereform

Dwarven military can no longer be relied upon to put an end to the rampages of citizens gone berserk or transformed into a beast. Fighting such a threat is treated as assaulting a citizen, and will cause *the defenders of your fort* to lose loyalty and be hunted down as traitors. Bug:7107 Seems partially fixed in 0.42\[Verify\].

### How to deal with loyalty cascades

To prevent the cascade from spreading, order the original separatists away from the fortress and let them fight amongst themselves. If the results are renegades, it is okay to allow other dwarves to kill them (by stationing them nearby). If the results are separatists/loyalists, then you will need to separate them somehow. Dwarves from these different "factions" will cancel jobs if they ever come across one another, each running away. This will likely lead to a massive number of job interruption announcements reading *Urist McDwarf cancels Eat: Interrupted by Farmer*

**NOTE:** Tame animals are loyal to civilizations and fortresses indefinitely due to a bug, so they can be used to kill off separatists/loyalists without repercussions.

As of 0.50, loyalty cascades should periodically end on their own[1]; separate your dwarves from each other until the fighting stops.

#### DFHack

For those who are using DFHack, the command fix/loyaltycascade can be used to immediately end most loyalty cascades.
