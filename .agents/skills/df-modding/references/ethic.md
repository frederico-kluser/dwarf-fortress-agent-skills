# Ethic

> Fonte: [Ethic](https://dwarffortresswiki.org/index.php/Ethic) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

!!UNKNOWN!!  · xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

\

**Ethic** tags are used in the entity raw files to determine how different civilizations feel about various issues. Relationships between civilizations are based on their ethic responses in relation to each other; similar ethics result in friendship, while conflicting ethics result in animosity. Strongly conflicting ethics often trigger wars during world generation. (In practice, this generally causes elves to declare war on everybody else over killing plants and making trophies, and everybody else to declare war on the elves over the devouring of sapient beings.)

Some ethics also affect fortress mode features, such as justice, or trading. In adventurer mode, ethics can affect the level of conflict (lethal, or no quarter). During world generation, ethics also affect how the entity treats its kills, such as devouring them or making trophies out of them.

## Example

In the raw files for entities, ethics appear as follows:

    [ETHIC:LYING:PERSONAL_MATTER]

This means that the entity will treat lying as a personal matter - more technically, the value of its LYING ethic is set to PERSONAL_MATTER.

## Ethic types

|  |  |
|----|----|
| Token | Extra Information |
|  ASSAULT | The result of a tantrumming citizen attacking another in fortress mode. Other effects unknown. |
|  EAT_SAPIENT_KILL | This determines if members of the civilization will sometimes devour defeated enemy combatants. |
|  EAT_SAPIENT_OTHER | This includes whether or not a civilization is willing to butcher other sapients. Note that any sapient creature that dies on site will never be butchered by citizens in fortress mode, and if butchered in adventure mode the products are inedible and unusable. However, this works for offsite behaviors (caravans will deliver products made from sentients, etc.) Also note that if an item doesn't actually come from a sapient creature that died on site (i.e: it was generated as part of a caravan or site) it is usable and edible regardless of ethics. |
|  KILL_ANIMAL | A response of JUSTIFIED_IF_EXTREME_REASON, JUSTIFIED_IF_SELF_DEFENSE, or anything from MISGUIDED to UNTHINKABLE (see below) causes the entity to refuse animal products in trade — namely, materials with \[IMPLIES_ANIMAL_KILL\]. Animal products sold by caravans will be marked as "grown", which means kosher for their ethics, for example grown leather. |
|  KILL_ENEMY | If REQUIRED, all lethal combat with an enemy who is an enemy of the whole entity will put the creature in no quarter mode. |
|  KILL_ENTITY_MEMBER | If REQUIRED, all lethal combat with an enemy in the same entity will put the creature in no quarter mode. Determines whether and how often entity members will be murdered. |
|  KILL_NEUTRAL | If REQUIRED, all lethal combat with an enemy who is neutral with the entity will put the creature in no quarter mode, and the creature will also demand that strangers identify themselves; it will also greatly increase war aggression in worldgen. |
|  KILL_PLANT | This includes a civilization's position towards wood — any response from MISGUIDED to UNTHINKABLE (see below) causes the entity to refuse wooden objects (except for "grown" wooden objects) in trade, and also prohibits them from bringing caravan wagons. Caravans will sell grown wood objects (if the civ has WOOD_PREF) and even grown non-wood objects, that elves refuse to buy (if the civ uses misc processed wood products). |
|  LYING | Giving false witness reports?\[Verify\] |
|  MAKE_TROPHY_ANIMAL | This determines whether animal kills will lead to characters with trophies. Historical figures can arrive at your fortress with leather, horn, ivory, tooth, hair, bone or nail jewellery from slain non-sapients, and fortress citizens may put on crafts made from their kills as well. |
|  MAKE_TROPHY_SAME_RACE | This determines whether kills of one's own race will lead to characters with trophies. Historical figures can arrive at your fortress with leather, tooth, hair, bone or nail jewellery from their race. Example: a goblin with a -goblin tooth ring-. |
|  MAKE_TROPHY_SAPIENT | This determines whether kills of other sapients will lead to characters with trophies - as previously, but regarding other races, including INTELLIGENT. |
|  OATH_BREAKING | The result of a citizen violating noble mandates in fortress mode. Other effects unknown. |
|  SLAVERY | Civilization will enslave defeated enemies and bring them back to their site. Also affects whether you may trade caged sapient beings to merchants. Aside from diplomacy, higher/lower values don't seem to affect anything beyond if a civilization is willing to take slaves at all.\[Verify\] |
|  THEFT | This determines whether the civilization will try to steal goods and how it will respond when stolen from.\[Verify\] |
|  TORTURE_ANIMALS | Determines if the civilization will kill all animals of the conquered site, or preserve them for further use. |
|  TORTURE_AS_EXAMPLE | Civilization will sometimes execute non-combatants after defeating enemy defenders. |
|  TORTURE_FOR_FUN |  |
|  TORTURE_FOR_INFORMATION |  |
|  TREASON | Protects position-holders from being murdered like everyone else – the reason that demon overlords of goblins manage to live for centuries, despite goblins' regard of killing each other as being a personal matter. |
|  TRESPASSING | Ignoring burrow restrictions\[Verify\] |
|  VANDALISM | The result of a tantruming citizen breaking furniture in fortress mode. Other effects unknown. |

## Ethic values

As used internally (see below), roughly in order of acceptability:

|  |  |  |
|----|----|----|
| Num | Token |  |
| 0 |  NOT_APPLICABLE |  |
| 1 |  ACCEPTABLE |  |
| 2 |  PERSONAL_MATTER |  |
| 3 |  JUSTIFIED_IF_NO_REPERCUSSIONS |  |
| 4 |  JUSTIFIED_IF_GOOD_REASON |  |
| 5 |  JUSTIFIED_IF_EXTREME_REASON |  |
| 6 |  JUSTIFIED_IF_SELF_DEFENSE |  |
| 7 |  ONLY_IF_SANCTIONED |  |
| 8 |  MISGUIDED |  |
| 9 |  SHUN |  |
| 10 |  APPALLING |  |
| 11 |  PUNISH_REPRIMAND |  |
| 12 |  PUNISH_SERIOUS | Will result in either a beating or a month in prison. See: Justice#Punishments |
| 13 |  PUNISH_EXILE | Mentioning in history: "...after being exiled following a criminal conviction." |
| 14 |  PUNISH_CAPITAL | Will result in either 8 months in prison or 50 hammerstrikes. See: Justice#Punishments |
| 15 |  UNTHINKABLE |  |
| 16 |  REQUIRED |  |

\

## Ethic value numbers in relation to each other

The following table describes how entities respond to other cultures, with the observer on the vertical axis and their target on the horizontal axis. If an entity's accumulated animosity towards another passes a certain threshold (determined by the ruler's personality) then it will run a risk-assessment check. If passed, this will lead to a declaration of war.

In general, entities react much more strongly to actions that violate *their* taboos than to the outlawing of their customs in other civilisations. For example, Civ A finds slavery Acceptable, but Civ B considers it a Capital Offence.

- Civ A will consider Civ B most unreasonable (−5) for executing people over such a non-issue.
- Civ B will be shocked and disgusted (−15) that Civ A engages in such a debased activity.
- The end result is mutual negativity. However, Civ B is 3× *more* offended, and much more likely to go to war over the issue — assuming, of course, they think they have a chance of winning.

 
TARGET

Accept.
Personal
Reperc.
Good
Extreme
Self-Def.
Sanct.
Misguid.
Shun
Appall.
Reprim.
Serious
Exile
Capital
Unthink.
Req.

OBSERVER     
Acceptable
+1
+1
+1
0
0
0
0
−1
−2
−2
−2
−3
−5
−5
−2
+1

Personal
+1
+1
+1
0
0
0
0
−1
−2
−2
−2
−3
−5
−5
−2
+1

No Reperc.
+1
+1
+1
0
0
0
0
−1
−2
−2
−2
−3
−5
−5
−2
+1

Good Reas.
0
0
0
+2
+1
0
0
0
−1
−1
−1
−1
−1
−1
−1
0

Extreme Reas.
−1
−1
0
+1
+2
0
0
0
−1
−1
−1
−1
−1
−1
−1
−1

Self-Defence
−2
−2
−1
0
+1
+2
0
0
0
−1
−1
−1
−1
−1
−1
−2

Sanctioned
−2
−2
−1
0
+1
0
+2
0
0
−1
−1
−1
−1
−1
−1
−2

Misguided
−1
−1
0
0
0
0
0
+2
+1
+1
+1
0
0
−1
+1
−1

Shun
−1
−1
0
0
0
0
0
+1
+2
+1
+1
0
0
−1
+1
−1

Appalling
−5
−5
−3
−2
−1
−1
−2
+1
+1
+2
+1
+1
+1
0
+1
−5

Reprimand
−5
−5
−3
−2
−1
−1
−2
+1
+1
+1
+2
+1
+1
0
+1
−5

Serious
−10
−10
−7
−3
−2
−2
−3
0
+1
+1
0
+2
+1
+1
+1
−10

Exile
−10
−10
−7
−3
−2
−2
−3
0
+1
+1
0
+1
+2
+1
+1
−10

Capital
−15
−15
−10
−5
−3
−3
−5
0
0
+1
0
+1
+1
+2
+1
−15

Unthinkable
−15
−15
−10
−5
−3
−3
−5
0
+1
+1
0
+1
+1
+1
+2
−15

Required
+1
+1
+1
0
0
0
0
−1
−2
−2
−2
−3
−5
−5
−2
+1

All above info was collected and interpreted from the data given by Toady himself at [1].

## Ethics of vanilla civilizations

Animal people currently have the same ethics as kobolds.

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| Issue | Mountain / (dwarf) | Forest / (elf) | Plains / (human) | Evil / (goblin) | Skulking / (kobold) |
| Killing member of the same entity | Capital punishment | Justified with extreme reason | Justified with good reason | Personal matter | Exile |
| Killing neutral sapient | Only if sanctioned | Acceptable | Justified if no repercussions | Required | Required |
| Killing enemy | Acceptable | Acceptable | Acceptable | Required | Required |
| Killing animal | Acceptable | Justified in self-defence | Acceptable | Acceptable | Acceptable |
| Killing plant | Acceptable | Unthinkable | Acceptable | Acceptable | Acceptable |
| Torture as example | Unthinkable | Acceptable | Acceptable | Acceptable | Unthinkable |
| Torture for information | Unthinkable | Misguided | Acceptable | Acceptable | N/A |
| Torture for fun | Unthinkable | Unthinkable | Appalling | Acceptable | Acceptable |
| Torture of animals | Unthinkable | Unthinkable | Shunned | Acceptable | Unthinkable |
| Treason | Capital punishment | Exile | Capital punishment | Capital punishment | Unthinkable |
| Oathbreaking | Capital punishment | Exile | Capital punishment | Personal matter | N/A |
| Lying | Personal matter | Exile | Personal matter | Personal matter | N/A |
| Vandalism | Serious punishment | Reprimand | Serious punishment | Personal matter | N/A |
| Trespassing | Serious punishment | Reprimand | Serious punishment | Personal matter | N/A |
| Theft | Serious punishment | Reprimand | Serious punishment | Personal matter | N/A |
| Assault | Serious punishment | Exile | Serious punishment | Personal matter | Personal matter |
| Slavery | Capital punishment | Exile | Acceptable | Personal matter | Unthinkable |
| Eating sapients | Unthinkable | Unthinkable | Unthinkable | Personal matter | Unthinkable |
| Eating sapients (that have been killed in battle) | Unthinkable | Acceptable | Unthinkable | Personal matter | Unthinkable |
| Making a trophy from a corpse of the same race | Appalling | Unthinkable | Acceptable | Acceptable | Unthinkable |
| Making a trophy from a corpse of another sapient race | Shunned | Unthinkable | Acceptable | Acceptable | Unthinkable |
| Making a trophy from the corpse of an animal | Acceptable | Unthinkable | Acceptable | Acceptable | Unthinkable |
