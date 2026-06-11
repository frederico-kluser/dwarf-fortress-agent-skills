# Militia commander

> Fonte: [Militia commander](https://dwarffortresswiki.org/index.php/Militia_commander) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

Militia Commander

Room requirements
 

Office
None

Quarters
None

Dining room
None

Tomb
None

Furniture requirements

Chests
None

Cabinets
None

Weapon racks
None

Armor stands
None

Other

Mandates
None

Demands
None

Arrival conditions

Appointed on / nobles screen / or / military interface / .

Function

Leads the local / military / of your fortress.

The **militia commander** is an appointed noble who serves as the senior leader in the military command hierarchy of your fortress. They can be assigned at any point (from either the n nobles screen or the q squad screen), and have no room requirements. The militia commander is only surpassed by the general in terms of military rank among dwarves who may inhabit a playable fortress.

The militia commander administrates your armies, and the position is necessary to expand your militia with new squads and to assign militia captains to serve as squad leaders. If desired, they can act as a militia captain to lead a squad of their own, though this is not necessary. Their role is primarily a figurehead and grants no bonuses unless personally participating in military activities. As such, they can be completely unskilled in combat skills; in fact, many fortresses avoid assigning a useful military dwarf to the role. However, if their squad is created and activated, they participate in the training, venture with them on missions and serve the same as any other squad leader.

Some skills have been reported to aid the role of the militia commander, though none are mandatory for that position. Organizer speeds up the time to organize training sessions. Military tactics is used when squads are sent into missions\[Verify\], and shows up as a "relevant skill" when assigning the role in the nobles screen. Ambusher skill is also useful for raids where dwarves will attempt to avoid detection.\[Verify\]

       [POSITION:MILITIA_COMMANDER]
            [NAME:militia commander:militia commanders]
            [SITE]
            [NUMBER:1]
            [SQUAD:10:militia-dwarf:militia-dwarves]
            [APPOINTED_BY:EXPEDITION_LEADER]
            [APPOINTED_BY:MAYOR]
            [RESPONSIBILITY:MILITARY_STRATEGY]
            [COMMANDER:MILITIA_CAPTAIN:ALL]
            [PRECEDENCE:120]
            [DO_NOT_CULL]
            [DUTY_BOUND]
