# Need

> Fonte: [Need](https://dwarffortresswiki.org/index.php/Need) — Dwarf Fortress Wiki (GFDL/MIT)

**Needs** affect a creature's focus - needs that are unmet for long enough will cause stress, become bad thoughts, and increasingly damage the creature's **focus**, while sufficiently well-satisfied needs will improve it.

The need system replaces the generalized on break feature of previous versions. Dwarves will sometimes perform jobs that satisfy their personal needs, instead of working for the betterment of the fortress. These personal-fulfilment jobs generally come in two varieties: low-priority (indicated by green text, e.g. ), or high-priority (magenta text with an exclamation point, e.g. ). Low-priority jobs may be cancelled to undertake a fortress job. High-priority jobs will not be cancelled for fortress jobs.

## Focus

*Overall, Urist is unfocused by unmet needs.*

Focus affects a dwarf's ability to perform. A dwarf with high focus will work faster and produce better results, while a distracted dwarf will take longer to do everything poorly. Focus is separate and independent of overall mood; a dwarf can be happy even with largely-unmet needs, or unhappy yet focused. However, prolonged insufficiency in meeting needs is a cause for both low focus and bad thoughts. Thus, Focus can, with prudence, be used to predict future mood developments.

Focus represents the percentage of the combined totals of met over unmet need values. The ratio of 1:1 (100%) represents a neutral state.

Focus statuses:

[TABLE]

A highly-focused dwarf can receive an effective-skill bonus of up to 50%; a badly distracted dwarf can receive an effective skill penalty of up to 50%.

## Diversity

*She is unfocused by a lack of trouble-making.*

An individual creature's set of needs and their weights (levels) are affected by personality traits. For instance, a dwarf that values romance will be unfocused "after being unable to make romance", while a dwarf that personally values nature will be unfettered "after seeing animals". Unreligious dwarves will have no need to pray or meditate; dubious and casual worshippers will have low or medium level needs to pray; committed believers will have high level need; and dwarves following multiple deities will have a separate prayer need, with separate level for each of their deities. Proposed weights per need level are 1, 2, 5, and 10.

As expected, high-level needs hold a much larger sway in a dwarf's overall focus than low-level needs. For example, immoderation controls the need for alcohol; dwarves, thus, are more likely to have a need for alcohol than humans (but most of the time won't have a very strong one). A small percentage have no need for alcohol at all, though they'll still slow down without it, due to dwarves' alcohol dependence.

Needs are shown in a dwarf's thoughts and preferences description page, which can be accessed by iewing that dwarf then , , or from the nit menu with iew, .

Degree of fulfillment:

[TABLE]

When a need is satisfied, its value is refreshed to maximum (400), regardless of previous value. There is no minimum to how a need can get. A deeper negative value won't further reduce total Focus, which is based on a ratio of all needs' Focus rating.

In the absence of needs rated as "Badly distracted" the focus score is expressed as the ratio of:

`[6     * number of Unfettered scores +`\
` 5 1/3 * number of Level-headed scores +`\
` 4 2/3 * number of Untroubled scores +`\
` 4     * number of Not distracted scores +`\
` 3 1/3 * number of Unfocused scores +`\
` 2 2/3 * number of Distracted scores] / (4 * number of scores total)`

where the numerator is rounded down to a whole number.

It is currently unknown how "Badly distracted" needs contribute to focus, pending further science, but it is likely that they contribute 2 points each to the numerator.

## Fortress actions per need (unconfirmed denoted by (?))

| Positive | Negative | Related Belief or Facet | Job |
|----|----|----|----|
| spending time with people | being away from people | GREGARIOUSNESS | Socialize. |
| drinking | being kept from alcohol | IMMODERATION, SELF-CONTROL | Drink alcohol. |
| communing with \[deity\] / meditation | being unable to pray (to \[deity\]) |  | Pray/meditate in a Temple |
| staying occupied | being unoccupied | HARD_WORK, ACTIVITY_LEVEL | (assumedly a sufficient amount of fortress tasks\*) |
| doing something creative | doing nothing creative | ARTWORK | Create or perform any artistic work. |
| doing something exciting | leading an unexciting life | EXCITEMENT_SEEKING | Varied; including at least being in danger or catching live vermin, perform at a tavern or temple. |
| learning something | not learning anything | KNOWLEDGE, CURIOUS | Gain a rank in any Skill, learn a new subject from written content, watch a skill demonstration at a guildhall, watch a martial demonstration at a training area. |
| being with family | being away from family | FAMILY | (Socialize with close family members?), gain a sibling, have or sire a child. |
| being with friends | being away from friends | FRIENDSHIP | (Socialize with friends?) |
| hearing eloquent speech | being unable to hear eloquent speech | ELOQUENCE | Hear or recite poetry. |
| upholding tradition | being away from traditions | TRADITION | (Perform any improvisational form?), deliver dwarven justice |
| self-examination | a lack of introspection | INTROSPECTION | Read anything, compose song or poetry (automatically self-indulgent) |
| making merry | being unable to make merry | MERRIMENT, HUMOR | Be delighted after witnessing a performance. |
| practicing a craft | being unable to practice a craft | CRAFTMANSHIP | Craft or improve any item. This includes all actions enabled by the "labour-\>crafts" menu (without strand extraction?), items created from masonry, carpentry, jewelry and smithing, a meal cooked, a drink brewed. A mechanic creates a craft only when making a mechanism, an engraver only when engraving a slab. A furnace operator creates a craft when making pearlash. |
| practicing a martial art | being unable to practice a martial art | MARTIAL_PROWESS | Gain a rank in any combat skill, spar at a training area (individual practice or martial demonstrations do not count). |
| practicing a skill | being unable to practice a skill | SKILL | (Use relevant skill?) |
| taking it easy | being unable to take it easy | LEISURE_TIME | (Spend time idle or fulfilling personal desires?), be treated at a hospital. |
| making romance | being unable to make romance | ROMANCE, LOVE PROPENSITY | *Interact* with spouse/partner. |
| seeing animals | being away from animals | NATURE | Animal must also see the dwarf.\* |
| seeing a great beast | being away from great beasts | EXCITEMENT_SEEKING, NATURE, CURIOSITY | (Uncertain, possibly encounter LARGE_ROAMING?) |
| acquiring something | being unable to acquire something | GREED, COMMERCE | Acquire any trinket (happens automatically when performing a "Store item in stockpile" job on an eligible trade good) |
| eating a good meal | a lack of decent meals | IMMODERATION | Eating a preferred food (or a preferred alcohol cooked into a meal), or a sufficiently valuable meal. |
| fighting | being unable to fight | VIOLENT | Partake in a fight or any combat. |
| causing trouble | a lack of trouble-making | HARMONY, DISCORD | Fight or argue with another. |
| arguing | being unable to argue | FRIENDLINESS | Argue with another individual. |
| being extravagant | being unable to be extravagant | IMMODESTY | Wear any item with a quality modifier, create a masterwork or artifact. |
| wandering | being unable to wander | NATURE, ACTIVITY LEVEL | Complete a fishing, hunting, or plant gathering job. |
| helping somebody | being unable to help anybody | ALTRUISM, SACRIFICE | Bring water or food to patient/prisoner/animal\*; bring wounded units to rest; leading demonstration; being yelled at by unhappy citizens (for relevant nobles.) |
| thinking abstractly | a lack of abstract thinking | ABSTRACT_INCLINED | Read or write any written content, or compose music or a poem. Playing make-believe. (Using Architect skill does not satisfy this need.) |
| admiring art | being unable to admire art | ARTWORK | Be exposed to artful furniture, artistic crafts, or engravings. Watch certain performances. |

(\* See also animal caretaker)

Satisfying any need will usually result in a good thought and a decrease in stress. (If the dwarf has extremely low cheer they may feel NOT ANYTHING).

## Adventurer actions per need

| Positive | Negative | Related Belief or Facet | Adventurer activity |
|----|----|----|----|
| spending time with people | being away from people | GREGARIOUSNESS | Spea to anyone or reply to greeting. They don't have to be able to reply back. |
| drinking | being kept from alcohol | IMMODERATION, SELF-CONTROL | Drink alcohol. |
| communing with \[deity\] / meditation | being unable to pray (to \[deity\]) |  | Spea, Pray to \ or begin a performance, give a sermon. |
| staying occupied | being unoccupied | HARD_WORK, ACTIVITY_LEVEL | Very wide variety of actions. |
| doing something creative | doing nothing creative | ARTWORK | Perform or compose any work. |
| doing something exciting | leading an unexciting life | EXCITEMENT_SEEKING | A wide variety of actions. |
| learning something | not learning anything | KNOWLEDGE, CURIOUS | Gain a rank in any Skill, learn a new subject from written content. |
| being with family | being away from family | FAMILY | Implemented, but inaccessible without modding. If your character has close family members, this need will be filled by spending time with them (seems to only apply to blood relations). However, there is currently no way to actually do this outside of mods. |
| being with friends | being away from friends | FRIENDSHIP | Unimplemented. |
| hearing eloquent speech | being unable to hear eloquent speech | ELOQUENCE | Hear or recite poetry. |
| upholding tradition | being away from traditions | TRADITION | Perform any improvisational form. |
| self-examination | a lack of introspection | INTROSPECTION | Read anything, compose song or poetry (automatically self-indulgent), craft a figurine of yourself. |
| making merry | being unable to make merry | MERRIMENT, HUMOR | Recite any poem. |
| practicing a craft | being unable to practice a craft | CRAFTMANSHIP | Craft an item via Knapping, Bone Carving, etc. |
| practicing a martial art | being unable to practice a martial art | MARTIAL_PROWESS | Gain a rank in any combat skill. |
| practicing a skill | being unable to practice a skill | SKILL | Use any skill. |
| taking it easy | being unable to take it easy | LEISURE_TIME | Unknown (Possibly engage in or witness a performance?) (I fulfilled this need by going to sleep at a tavern, getting interrupted in the middle of the night by a giant alligator (which the bards killed by the time I went down the stairs) and performing with them for a while.) |
| making romance | being unable to make romance | ROMANCE, LOVE PROPENSITY | Unimplemented. |
| seeing animals | being away from animals | NATURE | See an animal, animal must also see you. |
| seeing a great beast | being away from great beasts | EXCITEMENT_SEEKING, NATURE, CURIOSITY | Uncertain, possibly encounter LARGE_ROAMING? |
| acquiring something | being unable to acquire something | GREED, COMMERCE | Acquire any item by trade or demand. |
| eating a good meal | a lack of decent meals | IMMODERATION | Unknown. If the same as in Fortress mode, eating a preferred food, or a sufficiently valuable meal. |
| fighting | being unable to fight | VIOLENT | Engage in any combat, minor or major. |
| causing trouble | a lack of trouble-making | HARMONY, DISCORD | Fight or argue with another individual. |
| arguing | being unable to argue | FRIENDLINESS | Get into any disagreement about values. |
| being extravagant | being unable to be extravagant | IMMODESTY | Wear any item with a quality modifier on a body part - a waterskin will not work, as it can only be worn *in* another item of clothing. |
| wandering | being unable to wander | NATURE, ACTIVITY LEVEL | Move to/from any site or region tile. |
| helping somebody | being unable to help anybody | ALTRUISM, SACRIFICE | Reunite family members. |
| thinking abstractly | a lack of abstract thinking | ABSTRACT_INCLINED | Read or write any written content, compose music or a poem. |
| admiring art | being unable to admire art | ARTWORK | Expose yourself to artistic crafts, examine adornments and coins. |

Satisfying any need will result in a good thought and a decrease in stress.

Creatures with cannot satisfy any need and will inevitably become 'distracted'. In unmodded games, this concerns only Intelligent undead.

## Adventure mode meta-strategy

Upon creating your adventurer you may want to avoid having any of the non-fulfillable needs: romance, family, friends. Otherwise, you will suffer never-ending focus disadvantages. Immoderation too is only technically fulfillable for the itinerant adventurer, without a fortress's industry to reliably produce their preferred food.

Some precaution is necessary in sacrifice/altruism -\> helping capability is not available as long as you're quite weak (fighting; companions), and maybe in martial prowess if you're not constantly fighting and so increasing your stats. To fulfill your booze needs, you'll have to visit human towns' taverns or dwarven fortresses quite often (and fill your extra water storage containers with ale from the barrels for on the road).

\]\]
