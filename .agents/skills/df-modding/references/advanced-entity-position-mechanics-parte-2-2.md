# Advanced entity position mechanics (parte 2/2)

- The succeedable position can be appointed by another \[SITE\] \[AS_NEEDED\] position that has just been created and filled.
- The succeedable (site or civ) position is \[APPOINTED_BY\] the \[LAND_HOLDER\] position, which has just been created due to site elevation. This typically resolves when the diplomat leaves the map, at which point the landholder position becomes active.
- If all other requirements are met, premature succession can occur immediately after unpausing following embark, for positions with \[REQUIRES_POPULATION:7\].

#### Non-working (triggers)

Premature succession does **not** occur in the following cases:

- An \[AS_NEEDED\] succeedable position slot is manually created by the player while its succeeding position is already filled. \[AS_NEEDED\] positions must always be appointed after creation.
- The succeeding position is filled after the succeedable position becomes available. The moment of creation is the decisive trigger; filling the source position later is too late.
- The succeedable position can be appointed by another site or civ position with a fixed number of slots that has just been appointed. In this case, the succeedable position is just available for appointment itself, nothing more
- Any situation occurring during world generation.
- The succeeding position is \[REPLACED_BY\] the succeedable position. In this case, replacement removes the unit from the source position first, leaving no holder available for the succession mechanism to use.
- The position is \[APPOINTED_BY\] a civ-level position, that just became a citizen of your fortress. It must be noted that those civ-level positions were active all that time and the succeedable position could be appointed even before. The monarchs arrival does not trigger premature succession
- A \[SQUAD\]-position cannot inherit another \[SQUAD\]-position. This also means that premature succession will not work in this case.

# Losing a position

A unit can lose a position when:

- It dies
- It succeeds another position, even if it has nothing to do with the previous position.
- It is assigned to another SQUAD-holding position
- It is convicted of a crime.
- Another unit is ELECTED for the position
- It is convinced by an adventurer to give up its position, or is overthrown in a coup.
- Its position becomes replaced
- Another unit is appointed by the player, or the position is left vacant.
- It has assumed another position (of the same entity), as this always leaves the previous position vacant.

Note: A unit does not lose a position when the unit leaves the group (entity). Neither will a unit lose a position, if the corresponding entity is considered to be dead.

# Embarkment

Two types of positions are automatically filled by embark.

- Positions without \[APPOINTED_BY\] or \[ELECTED\] (assumable). All these positions, even with a NUMBER higher than 1, are all filled with one to three dwarves. Contrary to assumption, this doesn't take into account any limitations. REJECTED_CLASS, ALLOWED_CLASS, REJECTED_CREATURE, ALLOWED_CREATURE and GENDER are applied, but without the normal spread you may expect with assumptions. Also it doesn't look at \[SUCCESSION\] and \[SQUAD\] limitations.
- Positions that are elected are filled-in by the normal election rules.

Positions that have a defined appointer are never initially filled at embark.

All positions that don't have \[REQUIRES_POPULATION\] or with a \[REQUIRES_POPULATION\] of 7 or lower, will be available at embark.

# Land Holders

A Landholder is a **special civ-level noble** who gets a certain piece of land to hold, when that land is elevated to a certain level, determined by the \[LAND_HOLDER\] tag, and by the landholder triggers in the game's settings. In vanilla, these are the baron, the count and the duke.

A unit gaining the landholder position does not migrate to that specific named land. In world-gen, they stay just where they are, probably at the capital. In fortress mode, you can suggest a citizen for the role. So for the time being that works.

Succession is then a real issue. If you use BY_HEIR, its solved when that landholder has children living at your site. But when its not the case, the title just goes to anyone randomly. Succession BY_POSITION works, but only in the civ-chain, and there's no way to guarantee a civ-holder is at your site at that time. Even with 'automatic spread' positions, it goes to one of them randomly.

## Functioning of the regular landholder chain

The distinct difference between a landholder and a regular civ-level noble, is that a landholder may gain the position of landholder "of (sitename)" They are then seen as ruler of a particular site.

For a land_holder position to function as such, it has a few requirements:

- NUMBER:AS_NEEDED
- The first landholder-number of 1 is defined.
- No SITE (so civ) tag in that position.
- REPLACED_BY the next level landholder

If a landholder is defined with differentiating properties, it will function like a regular noble. A higher-up landholder that lacks the required tokens or connections will then not be used in elevation.

If a fortress meets the trigger for a new LAND_HOLDER tier when a caravan leaves, then the next time the outpost liaison or equivalent arrives, they will offer to make you an official colony, which will allow you to select all positions for that LAND_HOLDER level. Each time they appear, the outpost liaison will only promote your fortress one tier up the LAND_HOLDER track.

The landholder's LAND_NAME is not required for the functioning of this system. If omitted, messages will be shown with a more generic text.

## Appointment

This mechanism differs from the regular methods of position management. It ignores all regular appointment- and election rules, so it more or less functions like automatic assignment. A landholder is, in vanilla, appointed by the monarch. Changing this doesn't seem to do anything. If they are appointed by a site-position, a not-yet-existing civ-position, or not appointed at all: the system keeps working as usual.

A landholder can appoint civ-positions and site positions. This works as expected: the positions only are appointed then when that landholder becomes available on civ-level or when he arrives at that site for site-level positions.

If your rank of landholder is the first of its rank in the realm, and is the sole appointer of some civ-position, then immediately as it gains the title, it will appoint the empty civ-slots. This may happen on your site, but the frequency and certainty is hard to determine.

## Succession

Succession rules are applied to some extent:

- In world-gen it works according to succession rules, and site-positions can be used here. This means that a site position or a civ-position can inherit a landholder position, and vice versa.
- In fortress mode, once a landholder has been appointed, it then can inherit civ-level positions, and vice versa. This means that your baron can become king.
- Succession rules do not apply within the \[LAND_HOLDER\] chain; a count will not inherit a baron's land. This is because succession does not work well with the AS_NEEDED token.
- Premature succession works in fortress mode with landholders. If a unit gets a landholder's position and that landholder is the appointer of an as yet empty position, which is defined as succeeding from a third one, then the succession is immediately applied. The landholder themselves can even be the successor of a newly created position.
- A landholder's position is, in fortress mode, not successionable by a site-position or vice versa

### Impossibilities for succession by a site-position

It would be very beneficial if the landholder can be succeeded by a \[SITE\]-position. So far, the following tests have not lead to positive results:

- making landholder and site-position both non-\[DUTY_BOUND\]
- make the site-position be \[APPOINTED_BY\] the landholder and/or the monarch
- give landholder and site-position \[REJECTED_CREATURE\]
- Let the monarch live at your site when succession could happen.
- Let the site-position be \[REPLACED_BY\] the landholder.

If the vanilla \[SUCCESSION:BY_HEIR\]-tag is omitted, a seemingly random unit somewhere in the realm is assigned this position.

## Nomination

The player is able to nominate a unit to become the LAND_HOLDER, but this only works with units of \[LAND_HOLDER\] level 1. The player can select all units, only limited by the PRECEDENCE of the current units' positions.

A unit that has a position with a PRECEDENCE lower or equal to that of the landholder's position, cannot be selected. This means that a baron (or count) from another site or the monarch cannot be selected, because their precedence is lower or equal.

The GENDER token does not work here: also units with the wrong gender (sorry) can be selected.

## Levels

In mods, up to 10 levels of LAND_HOLDER may be defined.

If a landholder is replaced by a wrong landholder number (1 replaced by 3), then the number 3 is still correctly attached to the settlement.

If the current landholder has the highest available landholder number, then the next elevation will not happen - the diplomat will not elevate your fortress to a higher position, even if that position might be REPLACED_BY a lower landholder.

These chains do work:

- 1 -\> 2a - \> 2b -\> 3
- 1 -\> 3 -\> 2 -\> 4

These chains do not work:

- 2 -\> 3 (need to start at 1)
- 1 -\> 4 -\> 2 -\> 3 (stops after 4 as the highest)
- 1a -\> 2, 1b -\> 2 (only 1a and 2 work, 1b is not used)

## Moving landholders

It may happen that a land-holder no longer lives at the site which they are the landholder of, specifically when the current landholder dies, leaving the title to an heir living somewhere else.

To prevent this from happening, you can make their succession from heir and make sure that their kids live at your site. Or, you can make their position succeeded by another civ position, and make it so that this civ position is somehow available on your site. But if multiple of these positions exist, it cannot be guaranteed that a citizen of your fortress will inherit the title.

In world gen, a landholder lacking the DUTY_BOUND-token will also move to the site they like, according to legends mode.

## Replacement by a generic civ-position

If a landholder is replaced by an AS_NEEDED non-landholder civ-position, then this will work: the current landholder loses that title upon settlement-elevation and gains that civ-title. However, the civ-title lacks the landholder-property of being attached to the land. It will not show the name of the settlement alongside the position's name. So no "minister of Shovelmounts"

If a landholder is replaced by a general AS_NEEDED civ-position, that itself is also replaced by a generic AS_NEEDED civ-position, then firstly the elevation is executed and also the unit gains that new position. However, he immediately loses it, because an AS_NEEDED position that is replaced by another position can be filled initially, but units wont be able to hold that title.

## Landholder with fixed number

A landholder's position that has a fixed number will be created and filled directly when the civilisation is born, so this position slot is then not available for the regular landholder-mechanic and will also not be used. That landholder will thus not be attached to a settlement.

It doesn't matter if the landholder's position is connected to the regular landholder's-chain with the REPLACE_BY token.

## Responsibilities

When given a certain \[RESPONSIBILITY\], a landholder may function as a regular civ-level noble. If the position has \[TRADE\] or \[OUTPOST_NEGOTIATING\] responsibilities, then the landholder functions both as a diplomat and as an actual land holder. A landholder with the \[MILITARY_STRATEGY\] responsibility will travel around taming creatures in world-gen, according to legends mode.

Besides that, the responsibilities work the same as with any other on-site living position-holder, civ or otherwise.

# Military

## Squad management

In the vanilla game, the Squad interface only becomes available after a militia commander has been appointed. Until then, the window displays:You must appoint somebody first to create a squad.

What’s surprising is how this is determined internally. In the entity raw definition, **only the last two positions that include a \[SQUAD\] token are checked** to decide whether the interface is accessible at all. As a result, if your hierarchy defines commanders A through E, appointing **Commander D or E** unlocks squad formation, while appointing A–C does nothing.

In other words, squad availability is not tied to *having a militia commander*, but to *which specific positions happen to be last in the raw list*—a notably hacky implementation.

These 'last two' are always the last two **available positions.** So if they get \[REPLACED_BY\] or become available because of \[REQUIRES_POPULATION\], the game adapts to those.

## Squad assignment

Squads can be assigned, even if the leader position has no holder.

A specific unit can only have one position associated with a squad. If it gains another 'squad holding position', it is unassigned from the first one. This does not work with a 0-squad, so only 1+squads are taken into consideration. This technique can possibly be used to distribute all positions equally among all citizens. It does however not work with election and assumption.

If a civ-level position is associated with a squad and it gets a site-level squad-holding position assigned, it loses the current civ-position.

Squads can get really messed up, if you make the position (or multiple) either elected or not-elected and not-appointed, then this can cause the game to assign multiple squads to the same unit. Automatic assignment and election does not take squads into account, but the nobles screen does. This can cause the positions to be cleared as the game figures out that they have more than one position, and immediately get elected or assumed again.

Positions that cannot have a squad-position:

- A site- or civ-position with a \[SUCCESSION\] token cannot be appointed a squad-holding-position. The other way around, however, does work. For example, if a site-position with a \[SUCCESSION\]-token is appointed to a unit that has already a position with \[SQUAD\]. But when that squad position is assigned to another unit, it cannot be assigned back.
- A position with \[SUCCESSION\] can also not be assigned as a **member** of a squad.
- A squad-holding position with a formed squad cannot be appointed to another squad holding position.

If a position has at least one squad member, it cannot be left vacant. First, the squad has to be disbanded, then the position may be cleared.

## 0-squads

A 0-Squad is defined in a position as \[SQUAD:0:member:members\]. It does not seem to do anything useful as of now.

- It cannot be used to activate the military interface
- It does not restrict the assignment of \[SUCCESSION\] positions.
- Assigning this position does not clear any previously held squad position.
- The Leader and Tactician skill are not marked as relevant skills and are not taken into account in elections.
- It cannot be formed as a squad.

# Further testing

The following questions may need additional testing. Feel free to add or answer

- Everything regarding COMMANDING and army-structure
  - [1]
  - [2]
  - [3]
- Stuff about the monarch, its arrival and its entourage.

# Oddities (Bugs)

Almost everything on this page could be called an oddity. Because of their unexpected usability, some may also be referred to as “undocumented features.” Others, however, are simply odd and not particularly useful, yet I hesitate to call them “bugs.”

- If a certain threshold is reached that makes an elected position electable, and the triggering event that initiates this evaluation is an assumption, then the resulting assumption works partially as an election. It referred to in the messages as an election and the \[REJECTED_CREATURE\]-token is not applied, like it is with assumptions.

# Examples

### The Founder

The founder is a single dwarf, appointed at embark. They will be the only one ever to have this position and are not replaceable. When they lose their position some way, the position will not be assumed by another dwarf.

    The Founder

    [POSITION:THE_FOUNDER]
        [NAME:the founder:founders]
        [NUMBER:1]
        [SITE]
        [ALLOWED_CREATURE:DWARF:ALL]        - will only be filled at embark, but not assumable later.
        [REJECTED_CREATURE:DWARF:ALL]       - will only be filled at embark, but not assumable later.
        [SUCCESSION:BY_POSITION:THE_FOUNDER]    - not unassignable, also cannot be assigned to a [SQUAD] position.
        [PRECEDENCE:200]
        Non APPOINTED_BY
        Non ELECTED
        Optional: Add responsibilities to make the game select a unit with certain skills.

### Marriage bar

Dwarven matrons are held in great honour. Upon marriage, a female dwarf is no longer expected to perform menial labour. All dwarven males hold this position by default, granting their spouses exemption from menial work.

The position becomes available with the arrival of the first migrants; otherwise, on embark, it would be assumed by females. Its succession rule is non-functional, but this prevents the player from unassigning the position. A squad size of 1 and the succession rules together prevent a unit from assuming the position more than once.

With precedence set to NONE, the position name is hidden, while LAND_NAME remains visible on the nobles screen. All married females receive the suffix “, Mrs.” and are marked as Nobles.

The practical usefulness of this position is debatable, but it serves as a clear demonstration of several mechanics.

    Mrs. Urist

    [POSITION:MRS_URIST]
        [NUMBER:300]
        [SITE]
        [ALLOWED_CREATURE:DWARF:MALE]
        Not APPOINTED_BY
        Not ELECTED
        [LAND_NAME:Dwarven male]
        [NAME:dwarven male:dwarven male]
        [PRECEDENCE:NONE]
        [SPOUSE_FEMALE:, Mrs.:spouses]
        [MENIAL_WORK_EXEMPTION_SPOUSE]
        [REQUIRES_POPULATION:8]
        [SUCCESSION:BY_POSITION:MONARCH]
        [SQUAD:1:member:members]

### The Archduke

The archduke is the leader of the civilization, but exists only from landholder 4-level. Until then, its position remains vacant. When a settlement is elevated to tier 4 (grand duke), the grand duke can appoint the ruler of the civilisation, the archduke. Because of 'Premature Succession', they themself inherit that position immediately, but only when in fortress mode. Its heir then becomes grand duke.

    The Archduke

     no POSITION:MONARCH or other PRECEDENCE:1

    [POSITION:THE_ARCHDUKE]
        [NAME:archduke:archdukes]
        [NAME_MALE:archduke:archdukes]
        [NAME_FEMALE:archduchess:archduchesses]
        [LAND_NAME:a archduchy]
        [NUMBER:1]
        [PRECEDENCE:1]
        [SUCCESSION:BY_POSITION:GRAND_DUKE]
        [APPOINTED_BY:GRAND_DUKE]
        (add additional monarch-stuff, like spouse name, demands etc.)

    [POSITION:GRAND_DUKE]
        [NAME:grand duke:grand dukes]
        [NAME_MALE:grand duke:grand dukes]
        [NAME_FEMALE:grand duchess:grand duchesses]
        [NUMBER:AS_NEEDED]
        [LAND_HOLDER:4]
        // Optional ...
        [PRECEDENCE:19]
        [LAND_NAME:a archduchy]
        [RESPONSIBILITY:LAW_MAKING]
        [RESPONSIBILITY:RECEIVE_DIPLOMATS]
        [SUCCESSION:BY_HEIR]
        [APPOINTED_BY:THE_ARCHDUKE]
        (add additional landholder-stuff)

    !!add to [POSITION:DUKE]
        [REPLACED_BY:GRAND_DUKE]


---
*Parte 2 de 2 de «Advanced entity position mechanics». Demais partes em arquivos `...-part-{1..2}.md` na mesma pasta. Fonte: https://dwarffortresswiki.org/index.php/Advanced_entity_position_mechanics*
