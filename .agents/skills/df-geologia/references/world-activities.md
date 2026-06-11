# World activities

> Fonte: [World activities](https://dwarffortresswiki.org/index.php/World_activities) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

!!UNKNOWN!!  · xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

After world generation, game worlds continue to develop and advance while time passes in-game, simulating off-screen various activities in the world outside of the player's influence and without their direct input, referred to as "world activation".

World activation happens when you start a new fortress or adventure mode game, during the two weeks that pass in the calendar when you begin. Otherwise, it happens as time passes as you play at normal fortress/adventurer speed. You can play many games of fortress and/or adventure mode in the same world, each building up its history.

## Types of activities

Types of activities that are simulated during world activation:

### Succession

Historical figures can get married, have children, do their various jobs, and die: as can their children *ad nauseam*, as they are also historical figures.

The various positions of nobles will either be inherited by another historical figure, or assigned to a new historical figure by the parent civilization when the position is vacated or they have an unfortunate accident. Conflicts over succession and illegitimate site ownership can emerge, and armed usurpations and insurrections can take place.

### Site changes

A legendary sword being made a symbol during world generation

Existing NPC sites are conquered, liberated, defended, destroyed, reclaimed and new sites are created[1] while playing. Bandits will loot villages, armies will conquer cities, and forgotten beasts will ransack fortresses. Abandoned dwarven fortresses can be reclaimed later by the player.

As the player can do in fortress mode, during world generation and world activities), certain items can also be chosen as the symbol of a group's administrative position. These items were either, upon construction, an artifact, or were later - but prior to becoming a symbol - made into an artifact by naming the item (ie. to sanctify someone; the item having been that someone's favorite possession).

### Movement

Consequently, all kinds of creatures and groups travel around on the world map. However, others teleport. No, really.

The following groups teleport:

- Caravans
- Diplomats
- Migrants
- The various beasts

The rest physically travel on the map, including:

- Bandits
- Refugees
- Scholars
- Thieves
- Questers
- Religious professions such as prophets, monks or pilgrims
- Armies like siegers or other invaders

Screenshot showing Goblin civs prioritizing conquering the Elves down south above attacking the player fort (here highlighted with a yellow 'A' due to the rumour of artifacts.) ASCII mode.

Armies move around the map while playing for various reasons, including site invasion (not just to the player site), harassment, searching for work, reclamation of sites and more. As invaders need to actually travel the world map to get to your site, embarking close to a site of potential invaders increases the chances of an invasion. Other factors that influence the probability of an invasion are the "effective" population of said site\[Verify\], in other words, how many soldiers the site can spare to attack you. While a site may have a high population, it may be occupied with other, more important campaigns than the player's site.

The asterisks \* on the fast travel map in adventure mode are creatures and armies moving around on the world map.

### Non-player adventurers

Non-player adventurers will group up in parties and wander around, or adventure alone. They will also go on quests to retrieve artifacts in play, which they receive from historical figures that are in power, for example, a lord or noble from another site. For fortress mode, this manifests as visitors coming to your fort and requesting you hand over artifacts. If you say no to them, they may try to steal it from you, or outright attack your fort.

In adventurer mode, this is more subtle: non-player adventurers can be found who are looking for artifacts, and may compete with you when you are trying to get artifacts, if they happen to be looking for the same artifact. If you are holding the artifact they seek (even if you are hiding it in your backpack), they will try to mug you (like bandits) and may also attack you, follow you around, or vocally demand that you give them the artifact.

## Information

Greetings from the mountainhomes. Let's discuss our situation.

In an active fortress session, the player will get information about current events through the liaison. During the meeting, communication of this information is implied. The actual information will appear on the Civilization and World Info screen, under the "News and rumors" tab.

## Notes

- In older versions, any world activity stopped after world generation finished. This is no longer the case since v0.40.01 and the changing of this is what is usually referred to as "world activation". "Restarting" world generation is not planned.

- Currently, when new sites are founded during fortress mode by other civilizations, ie. forest retreats, hamlets/towns, dark pits or hillocks, then the civ_id (and cur_owner_id) is not set properly (for the created site), instead the civ_id is set to the id of the army, which founded the site (allthough it probably should use the field entity_id of the army_controller instead - terminology according to dfhack), which can potentially lead to problems. Also the cur_owner_id of a site is usually not updated, if another civilization takes over a site in fortress mode. Furthermore, in such cases, the flag "dead" (in the property "flags" of the entity) of the previous site government is not set to true. In such cases it can also happen, that a historical figure, who is created on-the-fly, to be the FORCED_ADMINISTRATOR is not associated with any entity (eg. not belonging to any group) at all (despite being the forced administrator of the new government) and the historical figure can - in that case - ie. lack skills (info.skills is nil for that particular historical figure). In case of a destroyed site getting reclaimed by any civilization then the cur_owner_id will still be set to -1 after successfully reclaiming a site (as destroying a site does set the cur_owner_id to -1). None of the above (except a forced administrator not associated with any group) can be seen without using tools like dfhack (ie. as legends and the game usually do not display these things, only the possible side-effects can be experienced in-game).
