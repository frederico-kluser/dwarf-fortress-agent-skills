# Skill

> Fonte: [Skill](https://dwarffortresswiki.org/index.php/Skill) — Dwarf Fortress Wiki (GFDL/MIT)

*See also: Combat skill*

**Skills** are used by dwarves and other creatures to accomplish almost every task in the game. Higher levels of a skill allow a dwarf to accomplish the respective task more quickly and/or more effectively. Whenever a skill is used, experience is gained for that skill, allowing the dwarf to progress to higher skill levels. Creatures aside from dwarves may also possess skills that match what species they are (e.g. cats and monkeys having legendary skill in climbing).

If a dwarf does not use a skill for a prolonged period of time, the skill will be labeled "rusty." If the rusty skill continues to remain unused, it will eventually be labeled "very rusty," or "V rusty" in-game. Skills remaining at 'very rusty' for prolonged periods of time will gradually suffer permanent experience loss. It is not possible to know in-game whether a given skill has suffered level loss, but any utility capable of reading exact XP levels will show a skill with a lost level as being at 100% of the XP required to take it to the next skill level. See Rust below for more details.

To determine what skills a dwarf has, hover over and click them, that will bring you to their "Overview" menu. From there you can see and access the "Skills" tab; "Labor," "Combat," and "Social" being the main three types of skills used by Dwarves. "Other Skills" regards all skills outside the main types, skills like swimming and instrument use. Finally, "Knowledge" is used in the knowledge system.

## Skill level names

The names of skill levels are as follows, in order of the experience required to achieve them:

[TABLE]

## Skills in use

`Skills are never referred to in-game by "level number", but for all practical purposes, that is how they are treated by the game. "Dabbling" is not functionally a level, with "Novice" being level 1, and "Legendary" being any level 15 and up. `

All skills take (400 + 100 \* the new level) experience points to gain a level, meaning Novice takes 500 experience points, and reaching Legendary from Grand Master takes 1900 experience points, or 18000 total experience.

Many skills can gain practical levels beyond level 15, or "Legendary". Farming, plant gathering, and fishing use an older formula for calculating yields which effectively caps the skill level at "Legendary+5", but most other crafting skills use the following formula to determine the quality of the resulting item:

1.  Find the effective skill level (i.e. Novice=1, Legendary=15), *uncapped*, with status penalties applied (see below)
2.  Roll for item quality "points": `rand(0..10) + rand(0..(level * 5) / 2) + rand(0..(level * 5) / 2)` (where `rand(0..N)` returns a number from 0 to N, inclusive)
3.  Add points for physical attributes: `(rand(0..phys_attr1) / 100) + (rand(0..phys_attr2) / 250) + (rand(0..phys_attr3) / 250)` (for whichever attributes are actually associated with the skill)
4.  Add points for mental attributes: `(rand(0..ment_attr1) / 100) + (rand(0..ment_attr2) / 250) + (rand(0..ment_attr3) / 250)` (see above)
5.  Adjust points based on focus (or lack thereof): `points = (points * current_focus) / undistracted_focus`
6.  Apply status penalties **again**, this time to the "points"
7.  If you have a Curse (or Blessing) with a Luck modifier, apply it to the points: `points = (points * luck_mul_percent) / 100`
8.  Add 10 points if the item being produced matches an Item preference on the maker
9.  Add 10 points if the item being produced matches a Material preference on the maker
10. Feed the points into the following formula:
    - 0-21 - base quality
    - 22-29 - Well-crafted
    - 30-34 - Fine
    - 35-44 - Superior
    - 45-54 - Exceptional
    - 55+ - 1/3 Masterwork, 2/3 Exceptional

A matching material or a matching item preference is each worth, on average, four skill levels. As both act as flat bonuses to base points, they are especially helpful for low-skill workers. Attributes are less impactful: to get a skill level's worth of bonus (on average), 500 points in a primary attribute or 1250 points in a secondary attribute are required. (This is roughly two or, respectively, five "tiers" of attribute description in the thoughts and preferences screen.)

Labors with or without quality often have a time period associated with them, and skill levels reduce this significantly. Legendary skill can eliminate all time required to do a job down to a single action, exponentially increasing productivity.

Combat skills can scale upwards to a functionally impossible-to-reach degree, meaning that simply reaching Legendary in a combat skill only means they've just started climbing the ranks of the legendary warriors of *Dwarf Fortress*. A Legendary +100 warrior will hit more regularly and deal more damage than a "mere" Legendary +10, although it takes nearly three-quarters of a million more experience points to get there.

## Skill penalties

Dwarves which are suffering from various status ailments will have all of their skill levels reduced, causing them to work slower and produce lower-quality goods where relevant. The latter is unimportant for non-quality tasks such as wood cutting or furnace operating, but you may want to delay construction of, say, platinum statues or steel breastplates, if the smith forging them is famished or hollow-eyed from lack of sleep. For instance, dwarves that aren't in a martial trance that have pain above a certain level get all their rolls halved.

Each of the following status ailments can impact a Dwarf's skills:

- Nausea - reduce by 50%¹
- Winded - reduce by 50%¹
- Stunned - reduce by 50%¹
- Dizzy - reduce by 50%¹
- Fever - reduce by 50%¹
- Blind - reduce by 75%¹
- Extreme Pain - reduce by 75%¹²
- Tired - reduce by 25%¹
- Over-Exert - reduce by 25% twice¹
- Exhausted - reduce by 25% three times¹
- Dehydrated - reduce by 50%
- Starving - reduce by 50%
- Very Drowsy - reduce by 50%
- Thirsty for Blood - reduce by 25% or 50%, depending on severity

¹ - Does not apply to dwarves who are Enraged, in a Martial Trance, or throwing a Tantrum

² - Does not apply to dwarves who are in a Strange Mood or are Insane

Notably, having multiple status ailments will result in **cumulative** penalties - for example, being both Stunned and Dizzy will cause all skill levels to drop by 75%.

## Professions

Skills are grouped under "professional" categories (shown below), each category represented by a specific color. In classic, the display color for a dwarf reflects its current profession, which is determined by their highest level (not experience) of their skills; in premium the colors of their name and clothing change. Professions do not affect skills or tasks in any way, professions are merely a reflection of the highest skill, and a loose way to differentiate dwarves with different types of skills. It is not perfect, but it can help when trying to spot a specific dwarf in a list or group.

So (and assuming it's their highest skill) your Miners names are always light gray, your Metal Workers are always dark gray, Masons (and Engravers) are always white, your Mechanics (and Siege Engineers and Pump Operators) are always red, and those waves of olive migrants are all "Farmers" of some stripe. This is not to say that a dwarf doesn't also have some other skill(s) from a different category, ones that may be just lower than their highest skill (which is determining the color for their current profession), so be sure to examine each new arrival - but that's their current best, and so their current color/profession.

A dwarf with no skill levels above dabbling is displayed as "peasant" as their listed "profession", falling in the teal "miscellaneous" category.

The one exception to this are some of your appointed noble positions, which are the magenta/purple of the Administrator category. Appointing a new noble will apply that magenta color to the new "noble" dwarf, regardless of their previous profession.

Professions can change as skills are increased. When a skill in a new category is raised to a higher level than any in other categories, creating a new "highest" status, the dwarf will change listed profession and display color accordingly. This change is accompanied by a minor announcement to that effect.

[TABLE]

## Skills, attributes and traits

- **Skills and attributes**:
  - .. are both trained by being used in activities they relate to.
  - .. both influence future success of these activities, like craft quality, work speed, combat survivability, accuracy and damage.
  - The dwarf's profession is determined by their highest-ranking skill group.
  - Crafting skills are increased by preferences, allowing the the dwarf to make items beyond their skill level.
  - The dwarf's highest moodable skill determines potential artifact types during a strange mood.

- **Traits**:
  - can be changed (at least beliefs change through arguments).
  - affect which social skills gain experience *(if the dwarf has X trait it will not gain experience in X skill)* at all.
  - give thoughts when performing certain activities.
  - influence choice of artifact materials.

To summarize, it goes like this:

`Thought  Attribute`\
`   ^          ,----------|                         |`\
`modifies   modifies    trains                   increases`\
`   | ,--------'          |                         |`\
`   | v                   v                         v`\
` Trait --influences--> Skill --increases--> Dwarf performance`\
`   |           ,---------|`\
` item        item        |`\
`material     type    determines`\
`   |  ,--------'         |`\
`   v  v                  v`\
`Artifact <--chosen-- Profession`\
`             dwarf`

Since the same skills can be used by various professions, and the same attributes are trained by various skills, this allows for cross-training.

As traits can limit learning some skills, which can be required by some Noble positions, the need arises to:

- avoid appointing a dwarf that will never learn a certain skill to a Noble position that uses it:
  - *appointing a straightforward dwarf as a broker will result in a consoler, non-flatterer, non-liar broker*.
- appoint a dwarf with a useful effect given by a trait to a profession that benefits from it:
  - *appointing an undisciplined dwarf to an important job will result in fun*.
  - ''appointing an angry dwarf to soldier will result in more enraged bonuses.

## Skill rust

Every skill has the following set of improvement and decay counters, which are caste specific:

(Default is )

`* % of improvement points you get (Default 100)`\
`* unused counter rate (Default 8)`\
`* rust counter rate (Default 16)`\
`* demotion counter rate (Default 16)`

The unused counter starts incrementing while a dwarf isn't using a skill. Once it reaches the cap, it will reset to zero, and the rust counter rate will increment by 1. This continues until the rust counter's cap is reached, and then the demotion counter is incremented by 1, and the rust counter is reset to zero. When the demotion counter finally reaches its cap, a 'layer' of rust is added to the skill, and the demotion counter is reset to zero.

The and descriptions which are appended to a skill within *Dwarf Fortress* are determined by the following conditions:

- Rusty: A skill level greater than 0 and less than 4, and the skill level \* 0.5 \<= the number of rust layers.
- Very Rusty: A skill level greater than or equal to 4, and the skill level \* 0.75 \<= the number of rust layers.

For example, a level 3 skill with 4 layers of rust: 3 \* 0.5 = 1.5 which is less than the 4 layers of rust, so it's a Rusty skill. A level 8 with 6 layers of rust: 8 \* 0.75 = 6 which is equal to the layers of rust, so it's a Very Rusty skill.

In testing, it appears that the layers of rust are limited to a maximum of 6. If the counters reach the maximum and it attempts to increase to a 7th layer of rust, all counters are stopped, and the 'Rusty' and 'V. Rusty' descriptions are erroneously removed from the skill descriptions within *Dwarf Fortress*.

## Performances

Randomly generated musical instruments and musical compositions are also considered skills and gain experience from use, though it is not clear how greater skill levels affect anything or if these performance-related skills rust.
