# Monarch

> Fonte: [Monarch](https://dwarffortresswiki.org/index.php/Monarch) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

|  |
|:--:|
|   This article or section contains **minor spoilers**. You may want to avoid reading it. |

Monarch

Room requirements
 

Office
Royal Throne Room

Quarters
Royal Bedroom

Dining room
Royal Dining Room

Tomb
Royal Mausoleum

Furniture requirements

Chests
10

Cabinets
5

Weapon racks
5

Armor stands
5

Other

Mandates
5

Demands
10

Arrival conditions

Fortress is a duchy capital and the / duke / duchess / is alive / Sufficient happiness / Metropolis / rank

Function

None

The **monarch** is the highest level noble, and also the noble of the highest precedence. Rather than being promoted from within, like the baron, count, and duke, the existing monarch arrives as an immigrant from the previous capital. However, one of your fortress residents may become monarch if the position is vacant, either by inheriting the title or after conducting "polite discussions with local rivals". A male monarch is known as a "king" and a female as a "queen". Either may arrive with a consort, as well as an entourage that can include the outpost liaison, general, elite military dwarves, and ordinary workers. Alliances can be sought with other settlements if a monarch is in your fortress.

To attract the existing monarch the fortress must be City rank, promoted to a duchy with the duke/duchess still alive, and reach a certain threshold of overall happiness. These requirements notably do not apply when one of your fortress residents is elevated to monarch.

With the presence of the monarch, a fortress becomes the capital of its civilization. As a result, it can no longer receive visits from a dwarven liaison (and so can no longer negotiate trade agreements with the dwarven caravans), nor can it give goods to dwarven caravans as offerings.

The monarch arrives at the same time as an immigration wave, but has an entirely separate entourage that can spawn from a different part of the map. The monarch's entourage includes a "royal guard" consisting of dwarves with Legendary +5 skill in a random weapon (but no skill in Fighter), Accomplished skill in Dodger, Shield User, and Armor User, and the "doesn't really care about anything anymore" trait. The monarch will arrive even if you have exceeded your population caps, though the entourage may be limited by the caps.

It may be that your monarch is an ancient vampire with thousands of kills to their name before arriving at your fortress. Some monarchs have been known to drop dead (*of regicide, perhaps*) as soon as they enter the map, especially in older worlds. Monarchs may also be of a different race, such as an elven king.

Random dwarves in dwarf fortress mode can become monarchs, if the current monarch dies, or if the position was vacant (common in dying civilizations). If the position no longer exists (i.e. the civilization is truly extinct) then no monarch will be appointed until the civilization is "resurrected" (by retiring a fortress, for example).

An adventurer can become a monarch; if they succeed in persuading the current one to yield, the monarch may then offer their position to the adventurer. (Whether they yield or offer may depend on their relative personalities and social skills.\[Verify\])

## Becoming a Mountainhome

|  |
|:--:|
|   This article or section contains **minor spoilers**. You may want to avoid reading it. |

By royal decree, avoiding the hidden fun stuff is no longer possible.

Once the monarch arrives and all room requirements are met, the player will be prompted to find "seven symbols not of this world" as well as to construct a "true throne". These symbols and the materials needed to build the "true throne" can be found inside an unusual volcanic wall (see for more details). Upon completion of this quest, you will be elevated from the Capital to the Mountainhome of your civilization, and it will be well-earned: this quest is fraught with danger that can end the entire fortress outright. The monarch's entourage of elite soldiers will make the challenges far more doable, but brute force can only take you so far. You'll have to think like a dwarf to stand a chance at seeing this to completion.

## In other civilizations

Elves also have a monarch position of sorts, but in terms of function and importance they're royalty in name only. The actual position at the top is the druid, capable of appointing the monarch position. Elves are notable only in that they have a defined princess (both their monarchs and the position under them are always female) position that can succeed a queen. However this doesn't actually replicate a hereditary monarchy, as princesses have to be replaced by the druid appointing a new one. Both serve various noble functions, with princesses having many of the same responsibilities as the dwarven general.

Humans and goblins, meanwhile, generate equivalent positions during worldgen. These tend to have names like "law-giver" or "master", and presumably have most of the functions and behavior dwarven monarchs do – without extracting the information from the world data, however, it can be difficult to tell. In the case of goblins, the position of master often starts off taken by something else entirely.

Artist rendering of a dwarf king by Mechlin (post)

## Bugs

The arrival of the Monarch is not necessarily an advantage for a fortress, as it comes with a significant risk of an accidental loyalty cascade.

If a dwarf goes berserk, or, during a tantrum, attacks a member of the Monarch's entourage, a loyalty cascade can be triggered. This can be particularly fun as the entourage can include several dwarves with high proficiency in military skills.

       [POSITION:MONARCH]
            [NAME_MALE:king:kings]
            [NAME_FEMALE:queen:queens]
            [NUMBER:1]
            [SPOUSE_MALE:king consort:kings consort]
            [SPOUSE_FEMALE:queen consort:queens consort]
            [SUCCESSION:BY_HEIR]
            [RESPONSIBILITY:LAW_MAKING]
            [RESPONSIBILITY:RECEIVE_DIPLOMATS]
            [RESPONSIBILITY:MILITARY_GOALS]
            [PRECEDENCE:1]
            [SPECIAL_BURIAL]
            [RULES_FROM_LOCATION]
            [MENIAL_WORK_EXEMPTION]
            [MENIAL_WORK_EXEMPTION_SPOUSE]
            [SLEEP_PRETENSION]
            [PUNISHMENT_EXEMPTION]
            [FLASHES]
            [BRAG_ON_KILL]
            [CHAT_WORTHY]
            [DO_NOT_CULL]
            [KILL_QUEST]
            [EXPORTED_IN_LEGENDS]
            [DETERMINES_COIN_DESIGN]
            [COLOR:5:0:1]
            [ACCOUNT_EXEMPT]
            [DUTY_BOUND]
            [DEMAND_MAX:10]
            [MANDATE_MAX:5]
            [REQUIRED_BOXES:10]
            [REQUIRED_CABINETS:5]
            [REQUIRED_RACKS:5]
            [REQUIRED_STANDS:5]
            [REQUIRED_OFFICE:10000]
            [REQUIRED_BEDROOM:10000]
            [REQUIRED_DINING:10000]
            [REQUIRED_TOMB:10000]
