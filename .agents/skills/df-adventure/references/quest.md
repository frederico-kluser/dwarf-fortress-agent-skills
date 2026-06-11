# Quest

> Fonte: [Quest](https://dwarffortresswiki.org/index.php/Quest) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

"We gotta find someone's wooden crown in *THAT?!*\
*Art by Jonás López Moreno*

**Quests** can be completed by adventurers (and NPCs, who will actively seek out quest targets during both world generation and in play) to raise their reputation. Adventurers can start out in (or join) certain groups to be tasked with quests by the group's commander. Objectives can range from slaying monsters, to retrieving lost artifacts or children. Rumors help spread and circulate information relevant to quests.

## Quest log

\
The **quest log** menu displays everything known by the adventurer about the world, and is important for quests. Adventurers always start out with information about their local area, unless they began as outsiders - as they explore and discover new things, the log will actively fill up with new information.

Press Q to open the menu. The log can also be opened from the fast Travel screen. Pressing the green keys at the top of the screen navigates between nine tabs:

- e **Events**: Events that are happening or have happened in the past.
- a **Agreements**: The adventurer's existing and previous agreements with leaders and companions.
- p **People**: People, other historical figures, and their relationships to the adventurer.
- s **Sites**: Various sites around the world. Only sites that are shown on the map are listed.
- g **Groups**: Entities and their relationships to the adventurer. This includes civilizations, site governments, bandit gangs, etc.
- r **Regions**: Regions of the world. 'Additional information' will list the biomes the region possesses.
- b **Bestiary**: Creatures encountered by the adventurer, along with their descriptions, where to find them, and how many were slain.
- A **Artifacts**: Various known artifacts, their descriptions, and their last known whereabouts. Artifacts are only logged after their (rumored) whereabouts become known.
- i **Intrigue**: Criminal networks. Pressing Tab cycles through **Actors**, **Organizations**, and **Plots**.

On the right side of the screen is a list of names, which can be searched using the filter. On the left is either a navigable world map, or information of the highlighted name. The m key will alternate between the map and info.

On the map screen, navigate using the arrow keys or numpad. To pinpoint a known site, select the site's name and press z to center the cursor `O` to the site on the map. A green line will be drawn between the player's location `@` and the site. The line can be disabled with l. Press c to recenter the cursor back to the player's current location. Centering to a site in the same world tile with the player's location will cause the map to zoom into local view and display the player's position and the site tiles. Events, groups, regions, and creatures in the bestiary can also be centered on the map if their whereabouts are known.

The world map can contain unexplored areas that become visible once they are discovered. The initial uncovered range is dependent on the territorial extent of the character's starting civilization. Starting out as an outsider (no civ) will mean that the entire map, except for the starting area, will be hidden.

### Key bindings

|  |  |
|----|----|
| Key | Description |
| Q | Open quest log |
| Esc | Exit quest log |
| e | View events |
| a | View agreements |
| p | View people |
| s | View sites |
| g | View groups |
| r | View regions |
| b | View bestiary |
| A | View artifacts |
| i | View intrigue |
| m | Toggle map/info |
| z | Recenter on selected |
| c | Recenter on current location |
| l | Toggle line |
| f | Filter the list |
| +- \*/ | Select from list |
| 82467913↑↓←→ | Navigate the map |

## Commander

Commanders, or quest givers, are position holders that can assign orders to their subordinates (a squad). There are four positions known to give out quests: the captain of the guard, a lord/lady, and the leaders of bandit and outcast groups. With the exception of the captain of the guard, commanders flash on screen. Elven civilizations do not have quest givers. Adventurers automatically start off as subordinates, if the player selected the "hearthperson" occupation in the character creation screen.

Adventurers can join existing squads by speaking to a commander and selecting Ask to become a . Adventurers must have a reputable status as a killer, hero, or hunter before commanders will accept them.\[Verify\] Adventurers cannot join more than one squad; joining another will cause them to leave the old squad.

Attacking the commander will cause the standard hostile reaction, but it does not cancel the current agreement. If the commander dies in any way before the completion report can be given, the report can be given to the next person that takes up the position, which automatically happens after a while.

By claiming leadership over a site, characters can become a lord or lady and create their own squad of hearthpeople, but they cannot give out quest orders.

In order for a position to send out quests in adventure mode, it requires the tokens `[``RESPONSIBILITY``:LAW_ENFORCEMENT]` and a [`[SQUAD]`](/index.php/Position_token#SQUAD "Position token"). If the entity is using [`[SITE_VARIABLE_POSITIONS]`](/index.php/Entity_token#SITE_VARIABLE_POSITIONS "Entity token"), it needs to include the `LAW_ENFORCEMENT` responsibility to generate hearthpersons.

List of commanders

Civilization
Squad member
Commander
Location

Dwarven
Fortress guard
Captain of the guard
Fortress

Goblin
Hearthperson
Lord/Lady
Dark fortress, Dark pits

Human
Mead hall

Baron/Baroness
Keep

Varies1
Lieutenant
Bandit leader3
Camp, conquered site/structure

Human2
Outcast leader3
Catacombs, Dungeon, Sewers

1 Civilizations with [`[BANDITRY]`](/index.php/Entity_token#BANDITRY "Entity token"). By default, this includes humans, goblins, and kobolds.

2 Only human collections of outcasts have leaders.

3 Bandit and outcast leaders have unique titles (*chief*, *ringleader*, *warlord*, etc.).

## Process

### Receiving a quest

To receive a quest, talk to the commander and select Request duty or advice pertaining to service as a . The commander will assign an order, including additional information about the target. The details and status of the quest can be checked in the agreements log; quests are identifiable with Order:.

Players are not given the choice to choose a specific quest, nor can they request more than one quest at a time. The order cannot be cancelled and players are required to complete it before they are able to receive another quest. The status will turn from Not yet completed to Complete: report back once the objective is completed successfully.

Leaving the squad will remove any current orders from the agreements log, but it won't actually cancel the quest. The quest order reappears in the log after returning back to the squad, and players can still complete it per usual.

### Completing a quest

Once the quest is complete, report back to the commander and select: Give report pertaining to service as a . The quest will finish and its record will disappear from the agreements log. You can ask for a new quest afterwards.

Commanders can run out of quests, such that when asked for more, they say: You may enjoy these times of peace, but remain vigilant.

### Rewards

Any action committed in a quest will affect the character's reputation. Upon completion of a quest, the commander will automatically share the adventurer's incidents. To speed this process, adventurers can also spread rumors about themselves on their own. The easiest way to spread news is to talk to someone and choose:

Bring up specific incident or rumor

Pick an incident to tell to the person. Rumors can be filtered with specific keywords to help faster searches. For example, typing "`conflict`" or "`fight`" in the filter will only show combat events. By spreading rumors, news of acts will eventually spread throughout the land, and the character's reputation will slowly build up.

People with different personalities, values, and affiliations have varying responses towards certain actions. Reputation is based on an individual's or entity's personal view of your character.

Adventurers performing good and heroic deeds will eventually earn the title of a legendary hero. They will earn respect from others, and taverns will provide free or discounted services and accommodations as thanks. The more amazing the action is, the bigger the impact it will make to the reputation. Keep in mind that accumulated reputation, specifically heroism, can be ruined if the adventurer acts badly. For instance, if word manages to leak out about the character murdering an innocent peasant, the character will become an enemy of the people regardless of previous good deeds.

## Doing quests without a commander

### Temple Quest

You can take on a quest for a religious sect by speaking to one of its religious leaders (as in, a Priest or higher) (usually found at a temple; *though it seems to work even if they aren't at a temple.*) and selecting Offer Service from the conversation menu. The quest plays out much like a commander’s quest—except instead of military orders, the priest will send you on a divine errand to recover an artifact, usually a Primordial Remnant.

### Self-guided quest

*See also: Rumor*

Players can earn heroic reputation without a commander—perhaps the adventurer needs a worthy kill first, before becoming a hearthperson. Adventurers may already start off knowing a few potential opportunities, seen in the events log.

To learn about a potential target, talk to someone and select: Inquire about any troubles. The person will reply with a list of known troubles: choose a type of trouble from that list, and they'll respond with a specific incident of that type. For incidents involving objects or groups, the basic reply structure appears as:

- Trouble pertaining to a creature: (...) is in . Seek this place if you wish to confront . (...)
- Trouble pertaining to a group: (...) They have a called somewhere in .
- Trouble pertaining to an artifactv0.44.01
  - if the speaker wants it: I desire that be returned(...) Last I heard, .
  - if the speaker is part of a group that wants it: Speaking as a representative of , it is important that be returned(...) It should be brought to in . Last I heard, .
  - if another person wants it:  wants returned. Last I heard, .
  - if a group wants it:  of wants returned. Last I heard, .

You are then given the option to ask further questions about the information of the location and whereabouts. Once satisfied with the info, set forth on the objective.

## Finding quest locations and objects

Completing a quest requires searching for the location of the quest object, which can be difficult at first. If the location was already acquired from someone, open the Quest log and select the event or entity from the relevant list to find out where it is on the map. If the location is known, the "Recenter on current location" option will be available. Press z to recenter the cursor to the location of the quest object on the map. If the location is unknown, players can Ask for directions to a person.

### Whereabouts of a site

To find the location of a site on the map:

1.  In the 'Ask for directions' menu, select Ask for the whereabouts of .
2.  If they know the location, they will reply:

 is a to the . \[You received a detailed description.\]

The site will be listed in the quest log and become searchable on the world map. If they do not know the location, they will either state their lack of knowledge or advise to look for a more well-informed person nearby to ask - fellow travelers, as well as position/occupation holders (e.g. leaders, nobles, tavern keepers) are usually more knowledgeable about the goings-on of the world. People can also be asked to guide adventurers to a location, becoming temporary companions until arriving at the destination.

### Whereabouts of a creature

To find the site where a creature is located:

1.  In the 'Ask for directions' menu, select Ask for the whereabouts of .
2.  If they know the whereabouts, they will reply  is in .

Once at the site, to find the exact location of the creature (such as a hiding vampire), ask for whereabouts again to one of the locals. If the creature lives in a structure, they will say We are in . Search first in to the . Once at the correct structure, asking once more will give the response Must be right around here somewhere. In the current version, this is broken.Bug\[Verify\] When the precise location is unknown, they will instead say I'm not sure exactly where to look.

It can also be determined whether a creature is on the move or already dead by asking for its whereabouts. "On the move" means that the creature is not present in any site or structure and is currently wandering outside (or underground), possibly travelling between sites. By chance, targeted creatures can be encountered while travelling (they appear as `*` in the fast travel map). If the targeted creature is discovered to be already dead and the quest required killing the creature, then simply return to the commander; as its death counts as completion of the order. It is useful to remember that some creatures follow a day-night active cycle. For example, night trolls are nocturnal, so they usually remain in their lairs during the day and wander outside when night falls.

### Whereabouts of an artifact

\

## Types of quests

There are three types of quests that can be offered from the commander. Each quest and the type of target can affect different reputations. Commanders always present quests in this sequence: on-site drive off quests, all kill quests, off-site drive off quests, then trouble quests.

### Kill

A kill quest requires the character to search for and slay a particular beast. Quest targets include megabeasts, semi-megabeasts, titans, and forgotten beasts. Less powerful creatures include night trolls and vampires. Wild animals with [`[LARGE_PREDATOR]`](/index.php/Creature_token#LARGE_PREDATOR "Creature token") have a chance to start attacking civilizations and become kill quest targets as well. Kill quests raise the hero reputation, and the hunter reputation is also raised for slaying large predators. The difficulty of the quest critter affects the amount of reputation (e.g. defeating a dragon vs. a dingo).

Werebeasts are not one of the beasts that can be targeted, though there are strings that imply dialogue for werebeast quests.\[Verify\]

### Drive off

A drive off quest requires the character to rout an enemy/criminal group from a site. Targeted groups include outcasts, bandits, kobolds, necromancers, and warring civilizations. Drive off quests can raise the "hero" and "protector of the weak" reputation.

The quest implies chasing or leading the targeted members out of their location, but that is not necessary to complete the quest. It is also not required to attack or kill anyone to complete the quest, merely encountering the enemy (i.e., the enemy spots the player) then immediately returning back is usually sufficient to qualify as completion. No reputation will be acquired through this way, however, since the main source of reputation from this quest is from slaying the enemies.

Driving off necromancer groups or site governments from warring civilizations is impossible to complete.Bug:9995 Insurrections do not seem to be the solution.\[Verify\]

### Trouble

A trouble quest appears when the character's civilization is in "brewing trouble" with another civilization due to a dispute— which generally means war is near. The quest requires the character go to an opposing civ's site and "cause trouble" for the local residents. Quest givers will give directions to the nearest site controlled by the opposing civilization.

It is currently unknown what actions are required to complete this quest. Attacking, killing, murdering, robbing, harassing, and arguing with the inhabitants does not seem to work, nor does causing insurrections seem to be the solution. It is possible that trouble quests may be bugged.\[Verify\]

### Non-commander quests

These objectives are never ordered by commanders, but are included among the various troubles. Unique reputations can be attained by fulfilling these objectives - adventurers must seek for these quests on their own.

#### Artifact

An artifact quest involves the retrieval of an artifact for another person or group.v0.44.01 Artifact quests raise the "treasure hunter" reputation. There is also a sub-type artifact quest that involves returning books to a library; this sub-type quest raises the "protector of knowledge" reputation.

Artifacts can be properly given back to the owners by using the barter system, accessible by speaking to the owner and selecting Exchange, give, take, or show personal items. They can also be dropped or placed in the structure, but no reputation will be gained from this method.

Library quests work a little differently - when a book is shown to one of the scholars working for the library in the barter screen, they will request for the book to be donated to the library. Do *not* give a book to a scholar; it will register as being in the scholar's personal possession and not the library itself - drop or place a book inside the structure instead, and the book will automatically become part of that library. Donating original books provides more reputation than copies.\[Verify\]

Amusingly, players can take an artifact from a structure, leave and wait for a while, then come back to return the artifact and be praised for "finding" it for the owner, even having their adventurers gaining reputation from this method.

One can spread rumors about the specific deed by selecting the appropriate event in the incident/rumor menu. Filter keywords are *artifact* and the artifact's name/title.

- For regular artifact quests: Bring up your giving of to (in ) in
- For book quests: Bring up your placement of in in

#### Rescue

A rescue quest involves the retrieval of abducted children who were taken away by goblin snatchers and imprisoned at dark fortresses. Prisoners can be found under the central dark tower in prison cells. After greeting a prisoner, there is the option to save the prisoner. Saving lets them join the adventurer's party (the agreement is identified as "Rescue" in the agreements log). Rescue quests raise the "hero" reputation to legendary for the reunited prisoner and family only. The act of rescue is not recorded in the incident/rumor list, so this reputation cannot be shared to others.

Freed prisoners can be returned to their families, or get adopted by someone. To learn about the location of living family members, talk to the former prisoner and select Bring up the journey together. Former prisoners automatically conclude the rescue agreement when they see and reunite with their family members; or, to get someone to adopt a former prisoner, talk to the person and select Ask favor, place request, make demand or issue order, then select Ask listener to adopt . People with high family values (e.g. most dwarves) are more willing to adopt. More than one person can be taken in by a single adopter.

Warriors can be recruited to aid in the rescue of a prisoner; mention the abduction to a warrior (from the incident/rumor menu) to bring up the option: Ask listener to join you in a rescue. The agreement will end once the prisoner finds a home.

People can (unfortunately) suddenly become hostile to a prisoner after the prisoner has been reunited with their family – this includes the family members of the prisoner, themselves.Bug:9935 usually resulting in a loyalty cascade, and a rather tragic and short-lived reunion.

## See also

- Mission

|  |
|----|
| "Quest" in other / Languages / Dwarven / : / iseth / Elven / : / elabe / Goblin / : / osmod / Human / : / akul |
