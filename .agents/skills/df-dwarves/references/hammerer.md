# Hammerer

> Fonte: [Hammerer](https://dwarffortresswiki.org/index.php/Hammerer) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

Hammerer

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

Appointed on the / nobles screen

Function

Justice / Executioner

The **hammerer** is a noble who serves as the executioner of your fortress, possessing no room or furniture requirements.

Normally, a dwarf that has committed a crime will be subject to justice at the hands of your sheriff (later, the captain of the guard), who will imprison the criminal in jail. However, if the crime is deemed particularly heinous, the hammerer will execute the criminal by using a chain to restrain them, and then, using a weapon that uses the Hammerman combat skill, will deliver 50 hammerstrikes; in most cases, a war hammer is used. While this typically results in the death of the criminal, it is possible for a particularly lucky and tough dwarf to survive the hammering, in which case they are released.

The hammerer is reserved for crimes considered "capital" according to dwarven ethics, which would be oathbreaking, treason, slavery and killing another member of your civilization - out of these, only the last one applies to fortress mode. Hammerers will also be responsible for (attempts at) dealing with discovered vampires. Hammerers are an ineffective way of killing vampires, however, as most non-military dwarves are not strong or skilled enough to kill one due to their enhanced toughness, leading them to free the vampire back into the fortress where it can murder innocents again.

If you are not willing to get your dwarves potentially killed by the justice force, it's better to simply not assign a hammerer at all. If you want a hammerer but would prefer to up the chances of dwarves surviving hammerstrikes, avoid letting them get their hands on a war hammer that's of high quality and made of some good metal like steel or silver, and give them something of poorer (or better) quality instead.

## Bugs

- In order for the hammerer to execute criminals, you must have an available chain in your jail - a cage cannot be used. If you have no available chains, the criminal's punishment will be automatically reduced to a beating.Bug:5172

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
There are multiple theories as to why the hammerer has such a huge role in dwarven politics. Experts claim that he serves no real purpose, as Armok usually finds a way to punish any delinquent even if no hammerer exists - magma, justice spiders or bridge mistakes usually lead to a criminal's ~~un~~timely demise. Hammerers do, however, present a sort of a calming factor on a typical fortress, and give any unhappy dwarf a simple, just, and brutal(ly effective) way to let off steam.

|  |
|----|
| "Hammerer" in other / Languages / Dwarven / : / ùnil / Elven / : / alara / Goblin / : / spar / Human / : / gibam |

       [POSITION:HAMMERER]
            [NAME:hammerer:hammerers]
            [SITE]
            [REQUIRES_MARKET]
            [NUMBER:1]
            [RESPONSIBILITY:EXECUTIONS]
                [EXECUTION_SKILL:HAMMER]
            [APPOINTED_BY:EXPEDITION_LEADER]
            [APPOINTED_BY:MAYOR]
            [PRECEDENCE:150]
            [DO_NOT_CULL]
            [COLOR:0:0:1]
            [DUTY_BOUND]
