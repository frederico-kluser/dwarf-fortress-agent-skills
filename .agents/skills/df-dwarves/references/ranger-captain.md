# Ranger captain

> Fonte: [Ranger captain](https://dwarffortresswiki.org/index.php/Ranger_captain) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

!!UNKNOWN!!  · xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

Ranger Captain

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

None

Function

Leads a unit of / elven / rangers, serving unknown military function.

The **ranger captain** is a noble position used by elves, appointed and commanded by the princess. It is presumably intended as an equivalent to captains or lieutenants, leading a squad of 10 rangers. In addition to this, ranger captains have "attack enemies" and "patrol territory" as responsibilities, but their exact effects are unclear. They are not appointed in civilization creation, because their Position_token NUMBER is not fixed, it is AS_NEEDED. This means that they are only then created when they are needed, and those circumstanses are very rare.

       [POSITION:RANGER_CAPTAIN]
            [NAME:ranger captain:ranger captains]
            [NUMBER:AS_NEEDED]
            [SQUAD:10:ranger:rangers]
            [RESPONSIBILITY:ATTACK_ENEMIES]
            [RESPONSIBILITY:PATROL_TERRITORY]
            [APPOINTED_BY:GENERAL]
            [PRECEDENCE:200]
            [DO_NOT_CULL]
            [DUTY_BOUND]
