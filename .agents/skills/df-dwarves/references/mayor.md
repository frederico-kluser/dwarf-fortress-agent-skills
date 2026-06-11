# Mayor

> Fonte: [Mayor](https://dwarffortresswiki.org/index.php/Mayor) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

Mayor

Room requirements
 

Office
Decent Office

Quarters
Decent Quarters

Dining room
Decent Dining Room

Tomb
None

Furniture requirements

Chests
2

Cabinets
1

Weapon racks
1

Armor stands
1

Other

Mandates
1

Demands
2

Arrival conditions

50 population / Elected

Function

Meet with foreign dignitaries / Talk with unhappy citizens

The **mayor** is a noble whose job it is to speak with unhappy citizens, and (until a baron is appointed) entertain foreign diplomats. They are automatically elected from the most social dwarf, most likely the expedition leader, once the population reaches 50. A new mayor may be elected from time to time as your dwarves' social skills change.

## Mayoral nobility

A dwarven mayor conducting a "meeting" with some goblin "liaisons".

A mayor or expedition leader is required to appoint other nobles. Should your leader suffer an unfortunate accident, you will have to wait for a new leader to be elected before appointing nobles.

Mayors are classy individuals, who require certain living standards in their rooms and furniture. They may demand certain types of furniture in their rooms and will get unhappy if you don't comply. They can mandate the production of certain goods, and receive a happy thought if you comply. If the mandated items are not produced in time, the mayor will receive an unhappy thought and will order the punishment of whoever they consider responsible. Likewise, they can prohibit the export of certain goods instead of mandating their construction, resulting in dwarves being punished for trade violations.

Mayors are not replaced by barons, dukes, counts or monarchs; if one of these nobles arrives, or if a citizen of your fortress is promoted to one of these positions, the mayor will still issue mandates and require quarters.

## Mayoral elections

If you don't have a mayor, then the first election will be triggered at the beginning of any season when you have 50 or more dwarves (including children). Also, if you have have 50 dwarves and no mayor, *any* change in the nobles' screen (including selecting "leave vacant") will trigger an election *immediately*. (This can be used to "force" an election if one is not triggered normally.)

Once you have a mayor, elections take place at exactly 4:00 PM on the 17th day of summer (specifically, 20000 season-ticks after the beginning of that season). Mayors elected in summer serve for that one year duration, but can be re-elected at that time.

When an election happens, it's usually the dwarf with the highest social skills who gets elected. In previous versions children had nothing to do but socialize, and did, therefore, gain lots of social skill, which carries over when a child becomes an adult at age 18, and so an 18-year-old mayor was not a rare sight. But in the current version, children prefer playing over socializing, and thus will only rarely become a mayor (with the possible exceptions of migrant children who already had high social skill on arrival, and of unhappy children constantly complaining).

The mayor doesn't actually need to be a dwarf, any citizen can be elected - however, dwarves currently on a mission, or otherwise absent from the fortress, cannot. Prime candidates for mayor include vampires (who tend to have high social skills if they have been around for a long time), tamed gremlins, and other non-working citizens of your fortress, since they cannot be put to work either and have nothing to do but socialize and gain experience in all\* relevant social skills.

*(\* Not all dwarves can learn all 10 social skills. Depending on their personality values and personality facets, they may be unable to earn experience one or more; for example, liar is relatively uncommon. If dwarves arrive at your fortress with scores in a skill they do not qualify to learn, that skill will rust away from lack of new experience; this includes your starting dwarves. The lack of such skills does not prevent them from being elected, but does put them at a disadvantage, both during an election and then, if elected, in handling some of their mayoral duties.)*

### Preferred candidates

There are, perhaps, three main criteria which separate "good" candidates from less desirable ones.

The first is their current role in the fortress, the current skills and services that they provide, be those artistic, industrial or military. If you're going to war, you don't want your one armorsmith to constantly leave the forge to hold meetings with whiny dwarves and children. Similarly with outstanding military candidates - a mayor can't console anyone while they are at war. Likewise, a distant miner won't dig effectively if constantly walking back and forth to hold a meeting. And so forth - this is personal preference, but it can make a big difference if exactly the "wrong" profession suddenly has new demands placed upon them.

The second is their fitness for the job itself. As mentioned above, a vampire could be elected; there are uses in a fortress for a Vampire (properly isolated), and you don't want to have to choose between your Mayor draining dwarves or being isolated from their duties in consoling unhappy citizens. A simple handicap or physical injury may prevent effective meetings. Or just a lack of some of the social skills, precluding some of the mayoral functions - harder to console unhappy citizens if you're just too cruel to qualify for the Consoler skill.

But the most significant factor in (un)desirability might be mandates, which are temporary mayoral decrees for mandatory production of specific items, or bans on export of same via trade. Ignoring or overlooking a mandate results in dwarven justice, a potentially fatal outcome, and then all the fallout from that victim's bereaved friends - no thank you. Such mandated items are drawn directly from the preferences of the mayor, and so are predictable. While it may be not overly burdensome to (not) produce figurines, or flood gates, or bucklers for a while, it may be an entirely different matter for beds, or goblets, or breastplates, or coffins for the dead. Material preferences (e.g. a type of stone, metal, gem, wood, animal, food/drink, etc.) have no bearing on mandates.

The "best" candidate then is a dwarf that has no *item preferences* at all, which is uncommon but not too rare - perhaps(?) one in fifteen or twenty or so. No item preferences means no mandates - and that's better for everyone. Just hope that dwarf has solid social skills, or at least a potential for such (see previous).

### Preparing a candidate

If an undesirable dwarf is elected, it is far from impossible to "groom" a different dwarf to win the next election.

Elections are based on the Conversational/Social skills of all candidates, with the dwarf with higher social skills winning; but there are limited options for arranging for targeted extra experience in social skills. The simplest is to remove all labors/tasks from the chosen dwarf, and let them socialize in a central meeting area full time, season after season - all (possible) skills will increase, slowly but surely. The other side of this coin would be to keep all undesirable candidates away from social interaction as much as possible - keep them busy in workshops or far-away mines, or (better) enroll them in full-time military training. If the player decides to do mass-trading (with as many trade transactions as possible), the broker will earn significant additional social skill experience due to the high skill gain per trade transaction. This is the best reliable way to try to influence that a certain dwarf will gain the social skills to (eventually) become (and stay!) mayor.

Of course, the brute force method is the ever-popular unfortunate accident, but that requires *every* other better-qualified dwarf to meet such an end, which could rapidly thin out otherwise useful citizens. Less extreme would be to send all such contenders off map on a quick mission just before election time each year, or year round (especially in the case of the Mayor themself, to prevent any experience gain) if your other residents can survive without the emotional support of meeting with the now-absent mayor.

\

       [POSITION:MAYOR]
            [NAME:mayor:mayors]
            [SITE]
            [NUMBER:1]
            [RESPONSIBILITY:MEET_WORKERS]
            [RESPONSIBILITY:RECEIVE_DIPLOMATS]
            [RESPONSIBILITY:MILITARY_GOALS]
            [REQUIRES_POPULATION:50]
            [RULES_FROM_LOCATION]
            [ELECTED]
            [PRECEDENCE:60]
            [FLASHES]
            [BRAG_ON_KILL]
            [CHAT_WORTHY]
            [DO_NOT_CULL]
            [KILL_QUEST]
            [COLOR:5:0:0]
            [ACCOUNT_EXEMPT]
            [DUTY_BOUND]
            [DEMAND_MAX:2]
            [MANDATE_MAX:1]
            [REQUIRED_BOXES:2]
            [REQUIRED_CABINETS:1]
            [REQUIRED_RACKS:1]
            [REQUIRED_STANDS:1]
            [REQUIRED_OFFICE:500]
            [REQUIRED_BEDROOM:500]
            [REQUIRED_DINING:500]
