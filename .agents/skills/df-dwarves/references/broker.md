# Broker

> Fonte: [Broker](https://dwarffortresswiki.org/index.php/Broker) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

Broker

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

Appointed on the / nobles screen / .

Function

Valuation of items at depot / Visibility of item / values / Display of fortress / wealth / on / status / popup / Reports / wealth / to attract / migrants

The **broker** is a useful noble with no demands or requirements. A broker has several duties in the running of an organized fortress.

After you appoint a broker with the appraiser skill through the n Noble screen, you can see fortress wealth and trade information in a status popup by hovering your mouse over your civilization name in the top left of the Fortress UI. (The exactness with which this can be seen is determined by the duties of the bookkeeper.) Your broker's appraiser skill is also used to determine whether to display item values, in general and in the trade depot. The broker is also the noble who will allow you to see exact room values when setting up guilds and temples. How much skill they have determines how exact a value you can see for the location.

If your designated broker is currently off-map on a mission, you will lose all specific values during that absence.

At the trade depot, you can specify that only the broker may trade with visiting caravans. The advantage of this is that the broker gains appraiser skill by opening the trade window for the first time, which allows the display of item values at the depot, and gains social skills by trading, which improves returns on your trading efforts. The disadvantage, however, is that convincing your broker to go to the trade depot in a timely manner can at times be frustratingly difficult. Once your broker has gained the appraiser skill and your fortress has plentiful trade goods, allowing other dwarves to trade will spread out the experience gains and ensure a prompt response. Your traders also use the judge of intent skill to see how merchants react to trade offers.

Human civilizations may send a head treasurer to discuss trade agreements for the next year with the broker. If the broker is off the map or otherwise unreachable, the diplomat will leave unhappy.

## Relevant skills

Of the social skills, those in bold change the effectiveness of a Broker (and are trained by trading), the others do not:

|  |  |  |  |
|----|----|----|----|
| **Judge of intent** | **Liar** | *Conversationalist* | **Intimidator** |
| **Appraiser** | **Comedian** | **Persuader** | *Pacifier* |
| **Negotiator** | **Flatterer** | *Consoler* |  |

When selecting a broker, all of the above skills will appear as relevant, but not all are. The skills in bold change the way that the merchants respond to your actions, eg. making a counter-offer or accepting an offer, while the profit margin is not yet green.

The first time you open the trade interface for each visiting caravan, the current Broker will gain Appraiser experience based on the number of items available for trade. For each individual trade you make, 50 points of experience are distributed between the broker's social skills, selected and weighted according to the "haggle" conversation type (see linked article for more details).

This means in normal play the skills used in trading will raise perhaps one or two skill levels through the years; to reach Legendary requires over a thousand successful trades. If you find yourself wanting such a broker, setting up a macro to trade individual worn-out clothes for individual food items (as well as coins, bolts, and anything in a stack) is the fastest method to train these skills. Note that, once Legendary, having such high social skills means your broker is very likely to be elected mayor as well.

    [POSITION:BROKER]
        [NAME:broker:brokers]
        [SITE]
        [NUMBER:1]
        [RESPONSIBILITY:TRADE]
        [APPOINTED_BY:EXPEDITION_LEADER]
        [APPOINTED_BY:MAYOR]
        [PRECEDENCE:170]
        [DO_NOT_CULL]
        [COLOR:5:0:0]
        [DUTY_BOUND]
