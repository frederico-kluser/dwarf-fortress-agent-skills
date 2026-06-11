# Bookkeeper

> Fonte: [Bookkeeper](https://dwarffortresswiki.org/index.php/Bookkeeper) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

Bookkeeper

Room requirements
 

Office
Meager Office

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

Appointed on the / nobles screen / .

Function

Accurate accounting of / stocks / and / wealth / .

The **bookkeeper** is an appointed noble who updates the stocks and created wealth screens with more accurate information. The bookkeeper needs to work in an office to do this job. The bookkeeper uses the record keeper skill, which grants the clerk profession. Important stats for record keeper skill are Analytical Ability, Memory and Focus.

The desired level of accuracy can be set next to the bookkeeper position from n nobles screen by selecting one of the numbers 1 to 5. To increase above the lowest level of accuracy, the bookkeeper needs a meager office. They must work not only to attain an accuracy level, but also to maintain it. When first assigned, a bookkeeper spends a long time creating a full list of the stocks, but once done, it takes only a bit of time to maintain this level of detail (even at maximum quality), so most of Urist McBookkeeper's time can eventually be assigned somewhere else. If your designated bookkeeper refuses to use their assigned chair/office and simply will not do their job, double check that you have raised the "precision" level on the nobles screen.

*Note*: This precision level only affects the accuracy of the **count** of items, the accuracy of item and zone **values** are determined by the broker's appraiser skill.

Curiously, a bookkeeper does not require writing materials such as paper or scrolls to perform their job. Bookkeepers will be unable to do their jobs if they cannot grasp, though.

|  |
|----|
| "Bookkeeper" in other / Languages / Dwarven / : / thîkut-zuden / Elven / : / soya-sinu / Goblin / : / zosto-ol / Human / : / thothil-nushrat |

Artist rendering of a bookkeeper by Mechlin (post)

    [POSITION:BOOKKEEPER]
        [NAME:bookkeeper:bookkeepers]
        [SITE]
        [NUMBER:1]
        [RESPONSIBILITY:ACCOUNTING]
        [APPOINTED_BY:EXPEDITION_LEADER]
        [APPOINTED_BY:MAYOR]
        [PRECEDENCE:180]
        [DO_NOT_CULL]
        [COLOR:5:0:0]
        [DUTY_BOUND]
        [REQUIRED_OFFICE:1]
