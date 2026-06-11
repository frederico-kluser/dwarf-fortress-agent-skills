# Visitor

> Fonte: [Visitor](https://dwarffortresswiki.org/index.php/Visitor) — Dwarf Fortress Wiki (GFDL/MIT)

A **visitor** or **guest** is a person who comes to the site at random to drop by at a location, which includes taverns, libraries, and temples. Some may seek permanent employment. Initially, a fortress will receive only about three visitors for a given location. First guests will initially visit out of curiosity, and when they leave, they bring back word of what the place is like. If the location proves to be popular and not deadly, it will attract more visitors. "Visitors" do not include merchants, diplomats, wild animals, or invaders.

The arrival of a visitor is notified in the announcements. Visitors are listed in on the nit list and labeled as on the right side of their names, along with their current activity.

Visitors provide protection and social interactions for citizens. Visitors are also a source of rumors, which they bring and spread from site to site, including the player's fort. Several downsides to visitors include overcrowding, alcohol depletion, accidental conflicts with citizens, and FPS issues from the increased population. Players wanting to remain an isolated fortress should restrict locations to to prevent people from visiting them, and shouldn't reveal a cavern, as its discovery will bring monster slayers.

Visitor population cap is set to 100 by default, and can be modified in d_init.txt from `[VISITOR_CAP: ]`. If set to 0, visitors will not come at all. `[VISITOR_CAP]` does not count long-term residents.

## Behavior

A visitor's current activities, objectives, and type can be investigated by pressing and hovering over it. The visitor must first interact with the locals before the information can be shown. Generally, visitors wanting to petition for residency are described as "seeking work", and typically call for meetings as soon as they arrive, unless there is another meeting taking place. Visitors who came to "relax" will socialize and partake in performances in taverns. Visitors described as "ready to leave" means they are exiting the map.

Visitors do not need to eat, drink, or sleep, but they receive alcohol from tavern keepers. Inn rooms are used for long-term residents only.

Guests are initially friendly to citizens and other guests. Drunk or otherwise violence-oriented visitors — particularly goblins, due to their ethics — may start arguments which can escalate into potentially-lethal brawls, or even loyalty cascades. Visitors side with the attacking force of their own civilization. On the other hand, in non-player sites, visitors can be drafted as defenders against invading armies (including your own missions).

When visitors first arrive, they will head towards their desired location and do their respective activities, if possible. If there are no locations assigned that allow visitors, they locate a meeting hall or an active meeting area and remain there. They cannot do any activities in meeting halls or unassigned meeting areas, even socializing. If there are no available locations, meeting halls, or meeting areas, visitors will stand around and do nothing. Visitors finish their current activities first before relocating.

Their current activity can be viewed in the unit list next to . Visitors with either means they are leaving, have just finished an activity, or have no location available to do their activities. Visitors can wander into other locations, but do not do activities that they did not come for. For example, visitors coming to relax will only socialize at a tavern and do not do other activities such as reading books or praying. Visitors must become long-term residents in order to do other activities in different locations.

Visitors will try to leave after they complete all of their activities. If they cannot find a path to exit the map (due to say, a forbidden door) they seem to "panic", wandering around frantically looking for an exit. Visitors will also leave after being interrogated for a crime, though this doesn't stop you from re-interrogating them if you wish.

## Visitor types

### Diplomat

Foreign diplomats arrive to your fortress for a multitude of reasons. Once their meetings are done, they will linger around your locations, sometimes for many months until they finally decide to leave. They are often followed by a pair of bodyguards who will defend them if they are under threat.

### Mercenary

Mercenaries come to enlist in the military, or to relax at a tavern. They can petition for long-term residency, and once accepted, they can be added to any squad (note that they cannot be squad leaders) and will follow any order the squad receives.

### Monster slayer and beast hunter

Monster slayers and beast hunters seek wild creatures to kill, or just to relax at a tavern. Monster slayers start arriving after a cavern is revealed; there does not need to be an unrestricted/public location, such as a tavern - the discovery of a cavern is enough.

After they socialize at a tavern for a while, they will petition for long-term residency. If granted, they will go outdoors or deep below to slay beasts; if not, they will simply leave. They will not begin to slay beasts until they become a long-term resident, and there is a path to such a beast.

Monster slayers go down into the caverns alone to slay subterranean creatures. Beast hunters remain above-ground and hunt wild animals, similarly to hunters.. Neither can have any labor enabled, but they are another able (and expendable) body if something unpleasant gets to where they are.

### Performer

Performers, as their name suggests, visit taverns to perform for other guests and citizens. They tell stories, dance, make music, or recite poetry. They do not ask for anything in return for their performances. They may seek long-term work.

Groups of performers under a single name may arrive as a performance troupe, and when petitioning will apply as a group. Allowing the petition will allow all of its members. Troupes may be made up of several bards and poets. Attacking or killing one member of a troupe does not automatically turn the rest of the group hostile. Due to a bug, troupes may arrive completely naked .

### Scholar

Scholars come to study in a library, which includes reading books and discussing topics with other scholars. If writing materials are available, they may use them to write their own books. While visiting scholars can depart with one or more of the local books from the library, they can also leave books that they have carried or written, thus encouraging new content in the book collection.

### Traveler

Travelers have no special purposes, and most only come to relax. Some may seek sanctuary if they were liberated from a site during missions. Travelers who seek sanctuary will be able to petition even if there are no locations assigned that allow visitors.

### Warrior

Warriors frequently visit the tavern to relax. They come armed with weapons and armor, so it is ill-advised to fight them. Most warriors are traveling questers, seeking rumors and asking questions regarding the location of their target, which is usually a lost artifact. Otherwise, they come to provide specific services.

### Miscellaneous

Other types of visitors may come, such as prophets, monks, pilgrims, peddlers or petty criminals. They are for the most part identical to travelers, though sometimes (often times) they are agents assuming fake identities in order to scout your fortress for items of value (see the Secret Agents section below)

## Questers

Questers will visit your fortress as representatives of a foreign entity, usually looking to retrieve an artifact. They are usually warriors, i.e. mercenaries. They go through your tavern first to gather informations from chatting other patrons, then leave after they've learned what they want. If one of your dwarves can't hold their tongue and reveals the presence of an artifact they're looking for inside your fortress, they will usually make more pressing demands or even attempt to steal it. Visiting questers will leave after a while regardless of what they learn or how much they socialize.

## Secret agents

Agents will visit from hostile civilizations to spy. They assume cover identities and gather information concerning artifacts, then leave to report back to their civilization. Agents cannot be forced to reveal their true identities, but players can distinguish them from other visitors by closely inspecting their names, roles, and equipment. For example, an agent might arrive at your fort claiming to be called "Urist McBard" despite being an elf carrying only weapons and armor, with no bard skills whatsoever. Also, visitors with "names" appearing in quotation marks seems to be a reliable indicator that the individual is an agent using a false name.

Additionally, if you have any open or cold cases in the justice screen, you can interrogate them to attempt to determine whether they are, in fact, agents seeking to steal your artifacts or perform other nefarious deeds at your fort. If your interogations fail (because your Sheriff or Captain of the Guard has lower social skills than the interrogation subject), but you know the visitor is an agent, you can still convict them (falsely) of crimes and your Sheriff/Captain of the Guard (or other members of your Captain of Guard's militia squad) will attempt to arrest them.

Note that if the suspect is able to evade capture and is about to escape (but is still on your map) you can give them a nickname on their character page (for example, you might nickname them "KILL THIS THIEF"). This nickname will persist after they leave your map and will appear in their name the next time they visit your fortress.

## Petitioning

Visitors who wish to work or stay longer can petition to become *long-term residents*. After about two years, long-term residents can apply for citizenship, which makes them into full-fledged citizens.

### Long-term residency

Visitors can petition to stay for a long time. When visitors request for long-term residency, they attend a meeting with the mayor at the mayor's office. Once the meeting starts, the etition notice will flash on top of the screen. In the petition screen, their purpose to stay is displayed, and players can have the final say on whether they become a resident or not. Currently there are four reasons to stay: "eradicating monsters", "entertaining citizens and visitors", "soldiering", "study".

When accepted, visitors will be added to the citizens list in the units screen. Their needs, preferences, and thoughts will be visible as normal, but labors or occupations cannot be assigned to them. Soldiering visitors can be assigned to squads, but they cannot be appointed as Militia captains. Aside from doing their main activities, long-term residents eat, drink, sleep, perform other activities, and reside at the Tavern if rooms are available. Locations set to are allowed for long-term residents; locations set to , however, disallow long-term residents.

Having finished their requirement, visitors whose petitions were not accepted will leave immediately after the meeting, unless they came for additional reasons.

### Citizenship

Long-term residents can apply for citizenship after living in the fort for about two years. Accepting the application will allow labors and occupations assigned to them.

To assign them occupations, the fort-wide occupation they initially had when applying for long-term residency must be unassigned. View the new resident, then select their Labor tab, then their Locations sub-tab, and remove any Location assignments. After this, the new citizens will become available for other occupations.

## Bugs

- As of v50.05, AI pathing can sometimes cause visitors (along with caravans and their wagons) to become stuck waiting to enter the map, which can prevent some or all types of visitors from some or all civs from visiting, and even prevent some merchants from entering the map. This can be fixed through DFHack's \`\`fix/stuck-merchants\`\` command.
