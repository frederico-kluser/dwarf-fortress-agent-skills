# Need

> Fonte: [Need](https://dwarffortresswiki.org/index.php/Need) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

Status screen.

**Needs** affect a creature's focus - needs that are unmet for long enough will increasingly damage the creature's **focus**, while sufficiently well-satisfied needs will improve it. Better focus leads to better results from work--essentially, a boost to all skills. Distraction is the opposite--an unfocused dwarf may become sloppy in their work, making worse crafts or failing a block during combat.

The need system replaces the generalized on break feature of previous versions. Dwarves will sometimes perform jobs that satisfy their personal needs, instead of working for the betterment of the fortress. These personal-fulfillment jobs generally come in two varieties: low-priority (indicated by green text, e.g. Listen to Poetry), or high-priority (magenta text with an exclamation point, e.g. Pray to Lorsïth!). Low-priority jobs may be cancelled to undertake a fortress job. High-priority jobs will not be cancelled for fortress jobs.

## Focus

*Overall, Urist is unfocused by unmet needs.*

Focus affects a dwarf's ability to perform. A dwarf with high focus will work faster and produce better results, while a distracted dwarf will take longer to do everything poorly. Focus is separate and independent of overall mood; a dwarf can be happy even with largely-unmet needs, or unhappy yet focused. However, prolonged insufficiency in meeting needs is a cause for both low focus and bad thoughts. Thus, focus can, with prudence, be used to predict future mood developments.

Focus represents the percentage of the combined totals of met over unmet need values. The ratio of 1:1 (100%) represents a neutral state.

Focus statuses:

|  |  |
|----|----|
| Very focused | 140% and higher |
| Quite focused | 120-139% |
| Focused | 101-119% |
| Untroubled | 100% |
| Unfocused | 81-99% |
| Distracted | 61-80% |
| Badly distracted | 60% and lower |

A highly-focused dwarf can receive an effective skill boost of up to 50%; a badly distracted dwarf can receive an effective skill penalty of up to 50%.[1]

\

## Diversity

*She is unfocused by a lack of trouble-making.*

An individual creature's set of needs and their weights (levels) are affected by personality facets. For instance, a dwarf that values romance will be unfocused "after being unable to make romance", while a dwarf that personally values nature will be unfettered "after seeing animals". Unreligious dwarves will have no need to pray or meditate; dubious and casual worshippers will have low or medium level needs to pray; committed believers will have high level need; and dwarves following multiple deities will have a separate prayer need, with separate level for each of their deities. Proposed weights per need level are 1, 2, 5, and 10.

As expected, high-level needs hold a much larger sway in a dwarf's overall focus than low-level needs. For example, "immoderation" controls the need for alcohol; dwarves, thus, are more likely to have a need for alcohol than humans (but most of the time won't have a very strong one). A small percentage have no need for alcohol at all, though they'll still slow down without it, due to dwarves' alcohol dependence.

Needs are shown in the "Needs" sub-tab of the "Personality" tab of a creature's character sheet, which can be accessed by clicking on the creature or from the creature tabs by clicking  next to the creature in one of the sub-tabs of the "creatures" tab..

Degree of fulfillment:

|  |  |
|----|----|
| Descriptor | Range |
| Unfettered | 400 to 300 |
| Level-headed | 299 to 200 |
| Untroubled | 199 to 100 |
| Not distracted | 99 to -999 |
| Unfocused | -1,000 to -9,999 |
| Distracted | -10,000 to -99,999 |
| Badly distracted | -100,000 and below |

When a need is satisfied, its value is refreshed to maximum (400), regardless of previous value. There is no minimum to how Badly distracted a need can get. A deeper negative value won't further reduce total focus, which is based on a ratio of all needs' focus rating.

\
In the absence of needs rated as "Badly distracted" the focus score is expressed as the ratio of:

    [6     * number of Unfettered scores +
     5 1/3 * number of Level-headed scores +
     4 2/3 * number of Untroubled scores +
     4     * number of Not distracted scores +
     3 1/3 * number of Unfocused scores +
     2 2/3 * number of Distracted scores] / (4 * number of scores total)

where the numerator is rounded down to a whole number.

It is currently unknown how "Badly distracted" needs contribute to focus, pending further science, but it is likely that they contribute 2 points each to the numerator.

## Fortress actions per need

|  |  |  |  |
|----|----|----|----|
| Positive | Negative | Related Value or Facet | Job |
| spending time with people | being away from people | GREGARIOUSNESS | Socialize |
| drinking | being kept from alcohol | IMMODERATION, SELF-CONTROL | Drink alcohol |
| communing with \[deity\] / meditation | being unable to pray (to \[deity\]) |  | Pray/meditate in a temple |
| staying occupied | being unoccupied | HARD_WORK, ACTIVITY_LEVEL | (assumedly a sufficient amount of fortress tasks\*) |
| doing something creative | doing nothing creative | ART_INCLINED | Create or perform any artistic work |
| doing something exciting | leading an unexciting life | EXCITEMENT_SEEKING | Varied; including at least being in danger or catching a live vermin; can be satisfied by sparring |
| learning something | not learning anything | KNOWLEDGE, CURIOUS | Gain a rank in any skill, learn a new subject from written content. Learn something from watching a guild demonstration. |
| being with family | being away from family | FAMILY | Socialize with close family members. Note that this need *can* currently be assigned to dwarves without families. |
| being with friends | being away from friends | FRIENDSHIP | Socialize with friends. Any social interaction (which involves talking, ie. intellectual discussion, sharing personal insight or just talking, but not getting into an argument) between friends is enough as is making a new friend. |
| hearing eloquent speech | being unable to hear eloquent speech | ELOQUENCE | Hear or recite poetry |
| upholding tradition | being away from traditions | TRADITION | Talk with champion (Perform any improvisational form? Religious rites? Justice served?). Can be satisfied by partaking in some performances in a tavern. |
| self-examination | a lack of introspection | INTROSPECTION | read anything, compose song or poetry (automatically self-indulgent), sharing a personal insight (random social activity, which can happen also outside a meeting area) |
| making merry | being unable to make merry | MERRIMENT, HUMOR | Watching or partaking in any performance (dance, poetry, music) |
| practicing a craft | being unable to practice a craft | CRAFTMANSHIP | Craft any item |
| practicing a martial art | being unable to practice a martial art | MARTIAL_PROWESS | Gain a rank in any combat skill |
| practicing a skill | being unable to practice a skill | SKILL | Use any skill (?); definitly satisfied by gaining a rank in any skill. |
| taking it easy | being unable to take it easy | LEISURE_TIME | (assumedly spending a sufficient time idle or self-fulfilling?); ie. satisfied by watching any performance in a tavern (ie. listening to story) |
| making romance | being unable to make romance | ROMANCE, LOVE PROPENSITY | *interacting* with spouse/partner/lover or getting caught up in a new romance (gaining new lover) |
| seeing animals | being away from animals | NATURE | Animal must also see the dwarf.\* |
| seeing a great beast | being away from great beasts | EXCITEMENT_SEEKING, NATURE, CURIOSITY | Uncertain, possibly encounter LARGE_ROAMING? |
| acquiring something | being unable to acquire something | GREED, COMMERCE | Acquire any trinket (happens automatically when performing a "Store item in stockpile", "Store item in bin" or "Bring item to depot" job on an eligible trade good, note that this includes clothing, but items claimed via pick-up equipment jobs do not satisfy this need), but some dwarfs are picky and might not want any of your normal trinkets (in that case check the dwarf preferences and get/make some of the dwarfs preferred items (finished goods), preferable with some of the dwarfs favored materials and then make sure, that that dwarf will haul it). |
| eating a good meal | a lack of decent meals | IMMODERATION | Eating a preferred food (or a preferred alcohol cooked into a meal), or a meal worth over 20☼. |
| fighting | being unable to fight | VIOLENT | Partake in a fight or any combat or any sparring session. |
| causing trouble | a lack of trouble-making | HARMONY, DISCORD | Fight or Argue |
| arguing | being unable to argue | FRIENDLINESS | Argue |
| being extravagant | being unable to be extravagant | IMMODESTY | Wear any item with a quality modifier |
| wandering | being unable to wander | NATURE, ACTIVITY LEVEL | Complete a Fish, Return kill (hunt) or Gather plants job; complete a mission |
| helping somebody | being unable to help anybody | ALTRUISM, SACRIFICE | Bring water or food to patient/prisoner/animal\*; bring wounded units to rest; leading demonstration; being yelled at by unhappy citizens (for relevant nobles). Note: Give water tasks seem to be automatically created, if a dwarf gets thirsty, when already going to bed or on the way to get something to eat, or if a dwarf has already taken a job (ie. mining job), where the dwarf needs a long time to complete the job (ie. reach the digging destination and perform the digging job), and becomes thirsty on the way. And a give water task does not get deleted until completed (with the possible exceptions that the dwarf is no longer on-site or dead). |
| thinking abstractly | a lack of abstract thinking | ABSTRACT_INCLINED | Read or write any written content, or compose music or a poem. Playing make-believe. Having an intellectual discussion (social activity). Watch a (guild) demonstration. (Using Architect skill does not satisfy this need.) |
| admiring art | being unable to admire art | ARTWORK | Exposure to artful furniture, artistic crafts, or engravings. Watching certain performances. |

(\* See also animal caretaker)

Satisfying any need will result in a good thought and a decrease in stress.

## Adventurer actions per need

|  |  |  |  |
|----|----|----|----|
| Positive | Negative | Related Value or Facet | Adventurer activity |
| spending time with people | being away from people | GREGARIOUSNESS | k Speak to anyone or reply to greeting. They don't have to be able to reply back. |
| drinking | being kept from alcohol | IMMODERATION, SELF-CONTROL | Drink alcohol |
| communing with \[deity\] / meditation | being unable to pray (to \[deity\]) |  | k Speak, Pray to or Begin a performance, Give a sermon |
| staying occupied | being unoccupied | HARD_WORK, ACTIVITY_LEVEL | Very wide variety of actions |
| doing something creative | doing nothing creative | ART_INCLINED | Perform or compose any work |
| doing something exciting | leading an unexciting life | EXCITEMENT_SEEKING | A wide variety of actions |
| learning something | not learning anything | KNOWLEDGE, CURIOUS | Gain a rank in any skill, learn a new subject from written content. |
| being with family | being away from family | FAMILY | Implemented, but inaccessible without modding. If your character has close family members, this need will be filled by spending time with them (seems to only apply to blood relations). However, there is currently no way to actually do this outside of mods. |
| being with friends | being away from friends | FRIENDSHIP | Unimplemented |
| hearing eloquent speech | being unable to hear eloquent speech | ELOQUENCE | Hear or recite poetry |
| upholding tradition | being away from traditions | TRADITION | Perform any improvisational form |
| self-examination | a lack of introspection | INTROSPECTION | read anything, compose song or poetry (automatically self-indulgent), craft a figurine of yourself |
| making merry | being unable to make merry | MERRIMENT, HUMOR | Recite any poem |
| practicing a craft | being unable to practice a craft | CRAFTMANSHIP | Craft an item (ie, Knapping, Bone Carving) |
| practicing a martial art | being unable to practice a martial art | MARTIAL_PROWESS | Gain a rank in any combat skill |
| practicing a skill | being unable to practice a skill | SKILL | Gain a rank in any skill |
| taking it easy | being unable to take it easy | LEISURE_TIME | Unknown (I fulfilled this need by going to sleep at a tavern, getting interrupted in the middle of the night by a giant alligator (which the bards killed by the time I went down the stairs) and performing with them for a while) |
| making romance | being unable to make romance | ROMANCE, LOVE PROPENSITY | Unimplemented |
| seeing animals | being away from animals | NATURE | Animal must also see you |
| seeing a great beast | being away from great beasts | EXCITEMENT_SEEKING, NATURE, CURIOSITY | Uncertain, possibly encounter LARGE_ROAMING?\[Verify\] |
| acquiring something | being unable to acquire something | GREED, COMMERCE | Acquire any item by trade or demand |
| eating a good meal | a lack of decent meals | IMMODERATION | Eating a sufficiently valuable meal. Foods with an item value of at least 4☼ count. |
| fighting | being unable to fight | VIOLENT | Engage in any combat of any lethality |
| causing trouble | a lack of trouble-making | HARMONY, DISCORD | Fight or Argue |
| arguing | being unable to argue | FRIENDLINESS | Get into any disagreement about values |
| being extravagant | being unable to be extravagant | IMMODESTY | Wear any item with a quality modifier on a body part - a waterskin will not work, as it can only be worn *in* another item of clothing |
| wandering | being unable to wander | NATURE, ACTIVITY LEVEL | Move to/from any site or region tile |
| helping somebody | being unable to help anybody | ALTRUISM, SACRIFICE | Reunite family members |
| thinking abstractly | a lack of abstract thinking | ABSTRACT_INCLINED | Read or write any written content, or compose music or a poem |
| admiring art | being unable to admire art | ARTWORK | Exposure to artistic crafts, examining adornments and coins |

Satisfying any need will usually result in a good thought and a mild decrease in stress. (If the dwarf has extremely low CHEER, they may "felt nothing after X").

Creatures with [`[NOEMOTION]`](/index.php/Creature_token#NOEMOTION "Creature token") cannot satisfy any need and will inevitably become 'distracted'. In unmodded games, this concerns only Intelligent undead.

## Adventure mode meta-strategy

Upon creating your adventurer, you may want to avoid having any of the non-fulfillable needs: romance, family, friends. Otherwise, you will suffer never-ending focus disadvantages. Some precaution is necessary in sacrifice/altruism -\> helping capability is not available as long as you're quite weak (fighting; companions), and maybe in martial prowess if you're not constantly fighting, and so increasing your stats. To fulfill your booze needs, you'll have to visit human towns' taverns or other dwarven fortresses quite often (and fill your extra water storage containers with ale from the barrels for on the road).
