# Announcement

> Fonte: [Announcement](https://dwarffortresswiki.org/index.php/Announcement) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **An example of a game-changing announcement, in ASCII mode.**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

List of announcements.

An **announcement** is a message displayed at the top left of the game screen used to indicate something important. Major announcements will pause gameplay and center the camera on the event in question, and game-changing ones will both do that and provide a framed message box presenting the event in question. The announcements list (N) lists all game announcements in dated order; some (but not all) can be zoomed to. (Announcements are not to be confused with reports, which detail combat results.)

When some major or important game-changing announcements occur, the following icon will appear, accompanied with a wooden ticking-like sound effect:\

## Controlling which announcements pause and recenter

You can control which types of announcements do and don't pause and/or recenter the game in the Announcements tab of Settings or by editing the `announcements.txt` file.

#### Announcement Settings

To change the behavior of announcements via the in game Settings, open Settings, select the Announcements tab. Then you'll need to find the setting of interest (announcements.txt wiki page may be able to help). You'll see the available options for each event includes, `Popup`, `Pause`, `Recenter`, and `Alert`. That's the functionality you're most likely to want to adjust. For example, if you want an Alert on the left side of the screen for combat strikes and wounds you would scroll down to 'Strike' and 'Wounds' and change the Alert column to 'Yes' - but don't get ambitious and change all the combat events to Alert, you'll regret it! (one at a time is recommended). More information on what each of these options do, including `Adv`, `Fort`, `Report`, and `Report (Active)` is available on the announcements.txt wiki page (and probably needs to become shared content between these two pages).

#### announcements.txt

To change the behavior of announcements via the `announcements.txt` file you'll need to adjust the `:options` for the particular event of interest. An announcement type containing ***:P*** will pause when that announcement type is made, and one containing ***:R*** will re-center when that announcement type is made. For example,

`[MIGRANT_ARRIVAL:A_D:D_D:P:R]`

means that the game will pause and recenter upon the announcement of migrants arriving. You could change it to

`[MIGRANT_ARRIVAL:A_D:D_D:R]`

to cause the game to recenter on the arriving migrants, but to not pause the game.

**Note:**

- `/init/announcements.txt` is for the **Default** settings
- `/prefs/announcements.txt` is for the **Current** settings

## Announcements

***Note:** Some of the icons may be incorrect. A question mark placeholder icon is in place of unknown icons. Please update them with the correct ones as soon as possible.*

Icon
Importance
Description

Minor announcements are the simplest and most common announcements, and will flicker through the announcements window very quickly. This is typically used for things that happen a lot in a well-developed fortress.

Minor
Job cancellation with a stated reason (building site submerged, item blocking site, dangerous terrain, needs rough picture jaspers, etc.), followed by a suspension notice if the job is furniture placement or building a construction. The standing orders menu (tab in y) allows you to filter job cancellation spam, between none, some, most, and all (default is some).

Minor
Standard changes in weather: "It has started raining," "The weather has cleared," or "A snow storm has arrived." Changes in the season.

Minor
Creatures and dwarves (and apparently ghosts as well) growing up and progressing from baby to child to adult. Animals jump straight from babies to adults. A dwarf cancelling a job with the reason of "Seeking infant." may also occur.

Minor
The creation of masterpieces. Can get quite annoying in mature fortresses, when the announcements will stack up the products of legendary dwarves.

Minor
A location and the surrounding areas have been made a county.

Minor
An artifact is not where it was last seen.

Minor
Something was stolen.

Minor
Something has escaped a cage.

Minor
A diplomat could not complete a meeting and left unhappy.

Minor
A masterpiece quality item has been lost or destroyed.

Minor
A new type of stone or ore has been found while digging.

Minor
Individuals are changing their status because they're in a squad.

Minor
Changes in profession, for both civilian and military dwarves. The start of every month is usually marked by rotations within your militia and thus a bevy of messages of this type.

Minor
A dwarf has begun hunting for animals.

Minor
When an animal is slaughtered, or a tame animal or dwarf is struck down within view of other dwarves.

Minor
When a creature is guzzling a fortress' alcohol.[Verify]

Minor
A scholar has discovered discourse on the nature of events.

Minor
An individual has lost their emotions.[Verify]

Minor
Animals giving birth.

Minor
A guest is visiting your fortress.

Minor
A messenger has returned with either success or failure with making contract with another settlement.

Minor
Two dwarves have gotten married.

Minor
Dwarves getting spooked by other creatures, and cancelling their jobs.

Minor
Combat is taking place, or someone has died in combat.

Minor
Sparring is taking place.

Minor
A workshop has been vandalized.

Minor
An agreement or mandate is active.

Minor
An animal has been caught in a trap.

Minor
An animal has broken free of an animal trap.

Minor
A trained creature going semi-wild (feral), the last stage before becoming wild again.

Minor
An animal has been adopted, or a cat has adopted a citizen.

Minor
A dwarf is in a martial trance.

Minor
Dwarves getting promoted and/or elected to a noble status. Such as baron, count or duke/duchess.

Minor
The raising of a ghost.

Minor
A citizen is undergoing a stressful breakdown.

Minor
Putting a citizen (and their associated ghost) to rest with a memorial slab or a coffin.

Minor
After one week, a dwarf or tame creature has been missing, or if a dwarf comes across a corpse.

Minor
A work order has been completed.

Minor
Dwarves growing attached to their weapons or armor.

Minor
A rumor has been passed on to your dwarves.

Minor
A creature is stung by a bee.

Minor
A citizen has become someone's student.

Major announcements are more important than minor announcements, and in addition to playing their message, the game may be paused and zoom to the location of the event. This is used for things that rarely happen, but aren't the most important. A wooden "ticking" sound effect is played for these announcement types.

Major
The arrival of a caravan. Best to get ready for thieves and ambushes as well.

Major
The arrival of the outpost liaison, although this always happens at the same time as the arrival of the dwarven caravan.

Major
The arrival of migrants.

Major
A new era has begun.

Major
Uncovering of a thief. End them quickly!

Major
Uncovering an ambush - very nasty if the dwarf in question is, for instance, just a poor old wood cutter out doing their job.

Major
Discovering a gremlin.

Major
Someone is caught sneaking around.

Major
A section of a cavern has collapsed. This is usually caused by improper digging.

Major
A dwarf entering a strange mood, claiming a workshop, setting to work, and either completing a legendary artifact or going insane in the attempt. (Each step gets its own announcement.)

Major
"We checked that stone for heat! What devilry is this?!" A single stream of flame will burst out in a random direction, setting someone on fire if it hits them. Only encountered in the deeper layers of the world.

Major
A dwarf has gone berserk. This can happen if the dwarf is undergoing a strange mood, and does not have the required materials to construct an artifact.

Major
A bogeyman transforms. Can be seen in the object testing arena.

Major
Someone has inherited a position.

Major
The arrival of the king or queen.

Major
A citizen in the military bestowed a name onto a shield or weapon.

Major
You have discovered an unusual volcanic wall studded with gems.

Major
The arrival of a semi-megabeast.

Major
The appearance of a creeping cloud in evil biomes.

Major
No available food is present. The ability to resolve this can depend on the surroundings around your fortress and what you already have.

Major
A deity is disturbed, and/or lays a curse.

Major
A monarch is satisfied with their position, but feels that there should be more development. We must dig deeper.

Warning: / Minor spoilers ahead / Game-changing / announcements are among the most important in the game. When these announcements occur, they pause the game, zoom to the location, / and / present a message box detailing the occurrence, in addition to repeating the message contained therein in the main feed after you close the box, for good measure. These are also reserved for incredibly rare, and potentially once-in-a-playthrough events.

Important
The creation of an artifact, whether from a strange mood or from a soldier bestowing a name upon his/her equipment.

Important
Discovering a cavern layer or the magma sea

Important
The arrival of a siege.

Important
Your fortress becomes the capital.

Important
The arrival of a megabeast, titan, forgotten beast, transformed werebeast, or an undead siege.

Important
The reveal of a demon, angel, artifacts, or fire in an Unusual volcanic wall

Important
Discovering a deep pit, magma pool, or downward passage in a cavern.

Important
Discovering adamantine - Praise the miners!

Important
Discovering the Underworld.

Important
An area has been founded, and is incorporated into your fortress' holdings.
