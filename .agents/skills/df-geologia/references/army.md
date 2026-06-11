# Army

> Fonte: [Army](https://dwarffortresswiki.org/index.php/Army) — Dwarf Fortress Wiki (GFDL/MIT)

*About military activities in fortress mode, see Military.*

**Armies** are groups of people wandering the world with a specific purpose and direction. The word 'army' is used loosely here, as is the word 'group'; it simply represents the abstract data structures used by Toady One to keep track of moving people, and a 'group' can very well be one single person. Armies draw from existing populations (both abstract and historical figures) and can be encountered in the wild after world generation. Non-army entities always sit where they are, at their site of origin, and don't move after world generation.

The following groups are considered armies by the game:

- Your adventuring party (i.e. your adventurer and their companions)
- Non-player adventurers (i.e. questers) and agents
- Invading forces; this includes both offsite invaders and armies marching to siege you
- Squads sent offsite on a mission
- Bandit groups on a raid
- Refugee groups
- Migrant groups
- Caravans
- A necromancer's horde on patrol

On the other hand, other groups such as megabeasts and titans are not armies of their own, and always sit in their lair.

Every site can have its own army, and that army can potentially be sent out on missions. The civ itself can also have its own army, which is treated as a separate army. How armies are built depends on the noble positions.

Normally, nobles will be created based on their NUMBER; as long as a noble position can be appointed (either \[ELECTED\] or its \[APPOINTED_BY\] noble exists) that number of nobles will be created automatically. The exception to this is those with AS_NEEDED, which will never be created until an army is formed.

Missions are created by a noble with the \[MILITARY_GOALS\] position (defending a site from invasion is also considered a mission). When a mission is created, the noble will first decide how many troops it will send on that mission. This number is limited by the total population of the site.

These troops will be assigned to nobles with SQUAD tags. If there are not enough squads to handle all of the needed troops, nobles with the COMMANDER tag, who command positions with the \[NUMBER:AS_NEEDED\] tag, will start appointing subordinates. The "lowest ranked" noble that is still able to appoint new subordinates will have priority.

The \[COMMANDER:position:ALL\] tag states that a noble is the commander of the designated position. However, you can ALSO put a number here (this feature is not used in vanilla). For example, \[COMMANDER:position:10\]. This means that the commander can command a maximum of 10 nobles with the specified position. (ALL means they can appoint as many as they want.)

In vanilla DF, since the GENERAL has \[COMMANDER:LIEUTENANT:ALL\], and the LIEUTENANT has \[COMMANDER:CAPTAIN:ALL\], even though LIEUTENANT has \[NUMBER:AS_NEEDED\] there will almost never be more than one LIEUTENANT per civ: once there is one LIEUTENANT they can keep adding CAPTAINs until there are enough to manage the entire army, so no more LIEUTENANTs are needed. However, if, for instance, you limit the LIEUTENANT to only be able to command 10 CAPTAINs, if the mission requires an army larger than 100 soldiers the GENERAL will appoint a new LIEUTENANT.

This also means that if you limit the GENERAL to only be able to command 10 LIEUTENANTs, the civ's total army size will be limited to about 1000 soldiers. Using this, you can limit the size of a civ's army and make it weaker in war.
