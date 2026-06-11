# Skill

> Fonte: [Skill](https://dwarffortresswiki.org/index.php/Skill) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*See also: Combat skill*

**Skills** are used by some dwarves and other creatures to accomplish almost every task in the game. Higher levels of a skill allow a dwarf to accomplish the respective task more quickly and/or more effectively. Whenever a skill is used, experience is gained for that skill, allowing the dwarf to progress to higher skill levels. Skills can also be taught in a demonstration, either through a guildhall or military training. Some species of creatures are born with natural skills (e.g. cats and monkeys having legendary skill in climbing).

If a dwarf does not use a skill for a prolonged period of time, the skill will be labeled "rusty." If the rusty skill continues to remain unused, it will eventually be labeled "very rusty," or "V rusty" in-game. Skills remaining at 'very rusty' for (*even more*) prolonged periods of time will gradually suffer permanent experience loss. It is not possible to know in-game whether a given skill has suffered level loss, but any utility capable of reading exact XP levels will show a skill with a lost level as being at 100% of the XP required to take it to the next skill level - see Rust below for more details.

To determine what skills a dwarf has, hover over and click them, which brings you to the dwarf's "Overview" menu. From there, you can see and access the "Skills" tab; "Labor," "Combat," and "Social" being the main three types of skills used by dwarves. "Other Skills" regards all skills outside the main types, like swimming and instrument use. Finally, "Knowledge" is used in the knowledge system.

## Skill level names

The names of skill levels are as follows, in order of the experience required to achieve them:

|  |  |  |
|----|----|----|
| Rank | Skill Name | Notes |
| 0 | Not | (No skill) |
| 0 | Dabbling | This level isn't displayed on the "prepare for journey carefully" screen. |
| 1 | Novice |  |
| 2 | Adequate |  |
| 3 | Competent |  |
| 4 | Skilled |  |
| 5 | Proficient | Maximum possible starting skill level for dwarves while "preparing for journey carefully". |
| 6 | Talented |  |
| 7 | Adept |  |
| 8 | Expert |  |
| 9 | Professional |  |
| 10 | Accomplished |  |
| 11 | Great | Characters with this level of a specified weapon mastery (including wrestling) or higher are elite. |
| 12 | Master |  |
| 13 | High Master |  |
| 14 | Grand Master | Maximum possible skill for any creature in the object testing arena. |
| 15+ | Legendary |  |

## Skills in use

Blinking legendary dwarves.

Skills are never referred to in-game by "level number", but for all practical purposes, that is how they are treated by the game. "Dabbling" is not functionally a level, with "Novice" being level 1, and "Legendary" being any level from 15 and up.

All skills take (400 + 100 \* the new level) experience points to gain a level, meaning Novice takes 500 experience points, and reaching Legendary from Grand Master takes 1900 experience points, or 18000 total experience.

Many skills can gain practical levels beyond level 15, or "Legendary". Farming, plant gathering, and fishing use an older formula for calculating yields which effectively caps the skill level at "Legendary+10", but most other crafting skills use the following formula to determine the quality of the resulting item:

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

For custom reactions, the roll for item quality points can be altered. `[``SKILL_ROLL_RANGE``:11:5]` is the default behavior, where 11 is the size of the flat `rand(0..10)` roll (a d11-1 roll), and 5 is the factor for the level rolls.

A matching material or a matching item preference is each worth, on average, four skill levels. As both act as flat bonuses to base points, they are especially helpful for low-skill workers. Attributes are less impactful: to get a skill level's worth of bonus (on average), 500 points in a primary attribute or 1250 points in a secondary attribute are required. (This is roughly two or, respectively, five "tiers" of attribute description in the thoughts and preferences screen.)

Labors with or without quality often have a time period associated with them, and skill levels reduce this significantly. Legendary skill can eliminate all time required to do a job down to a single action, exponentially increasing productivity.

Combat skills can scale upwards to a functionally impossible-to-reach degree, meaning that simply reaching Legendary in a combat skill only means they've just started climbing the ranks of the legendary warriors of *Dwarf Fortress*. A Legendary +100 warrior will hit more regularly and deal more damage than a "mere" Legendary +10, although it takes nearly three-quarters of a million more experience points to get there.

### Legacy-style skill checks

As mentioned above, farming, plant gathering, and fishing use an older algorithm for converting skill level to a number in 0-5 range. For these three skills, the result is used to determine item *quantity* instead of quality -- directly for fishing and gathering, and with some adjustments in the case of farming. This check does not appear to be affected by focus or attributes.

The algorithm is as follows:

- Start with 0.
- With a (skill in 5) chance, add 1. (Always at Proficient or above.)
- With a (skill in 10) chance, add 1. (Always at Accomplished or above.)
- With a (skill in 15) chance, add 1. (Always at Legendary.)
- With a (skill in 20) chance, add 1. (Always at Legendary+5 or above.)
- With a (skill in 25) chance, add 1 *one-third of the time*. (Thus the skill is capped at Legendary+10 for this purpose.)

The result is the amount of fish or gathered shrubs or a factor for crop yield.

## Skill penalties

Dwarves which are suffering from various status ailments will have all of their skill levels reduced, causing them to work slower and produce lower-quality goods where relevant. The latter is unimportant for non-quality tasks such as wood cutting or furnace operating, but you may want to delay construction of, say, platinum statues or steel breastplates, if the smith forging them is famished or hollow-eyed from lack of sleep. For instance, dwarves that aren't in a martial trance that have pain above a certain level get all their rolls halved.

Each of the following status ailments can impact a Dwarf's skills:

- Nausea - reduce by 50%1
- Winded - reduce by 50%1
- Stunned - reduce by 50%1
- Dizzy - reduce by 50%1
- Fever - reduce by 50%1
- Blind - reduce by 75%1
- Extreme Pain - reduce by 75%12
- Tired - reduce by 25%1
- Over-Exert - reduce by 25% twice1
- Exhausted - reduce by 25% three times1
- Dehydrated - reduce by 50%
- Starving - reduce by 50%
- Very Drowsy - reduce by 50%
- Thirsty for Blood - reduce by 25% or 50%, depending on severity

1 - Does not apply to dwarves who are Enraged, in a Martial Trance, or throwing a Tantrum

2 - Does not apply to dwarves who are in a Strange Mood or are Insane (not that they're going to perform skill rolls in the first place)

Notably, having multiple status ailments will result in **compounded** penalties - for example, being both Stunned and Dizzy will cause all skill levels to drop by 75%.

## Professions

Skills are grouped under "professional" categories (shown below), each category represented by a specific color. In classic, the display color for a dwarf reflects its current profession (unless the option to display clothing dyes is enabled), which is determined by their highest level (not experience) of their skills; in premium the colors of their name and clothing change. Professions do not affect skills or tasks in any way, professions are merely a reflection of the highest skill, and a loose way to differentiate dwarves with different types of skills. It is not perfect, but it can help when trying to spot a specific dwarf in a list or group.

So (and assuming it's their highest skill) your Miners names are always light gray, your Metal Workers are always dark gray, Masons (and Engravers) are always white, your Mechanics (and Siege Engineers and Pump Operators) are always red, and those waves of olive migrants are all "Farmers" of some stripe. This is not to say that a dwarf doesn't also have some other skill(s) from a different category, ones that may be just lower than their highest skill (which is determining the color for their current profession), so be sure to examine each new arrival - but that's their current best, and so their current color/profession.

A dwarf with no skill levels above dabbling is displayed as "peasant" as their listed "profession", falling in the teal "miscellaneous" category.

The one exception to this are some of your appointed noble positions, which are the magenta/purple of the Administrator category. Appointing a new noble will apply that magenta color to the new "noble" dwarf, regardless of their previous profession.

Professions can change as skills are increased. When a skill in a new category is raised to a higher level than any in other categories, creating a new "highest" status, the dwarf will change listed profession and display color accordingly. This change is accompanied by a minor announcement to that effect.

|  |  |  |  |  |
|----|----|----|----|----|
| Miner / Miner / R / Woodworker / Bowyer / Q / Carpenter / Q / Wood cutter / R / Stoneworker / Engraver / Q / Stonecutter / R / Stone carver / Q / Mason / Q / Ranger / Ambusher / Animal caretaker / Animal dissector / R / Animal trainer / Trapper / Q / Doctor / Bone doctor / Crutch-walker / Diagnostician / Surgeon / Suturer / Wound dresser | Farmer / Beekeeper / Q / Brewer / R / Butcher / R / Cheese maker / R / Cook / Q / Dyer / Q / Gelder / Planter / O / Herbalist / O / Lye maker / R / Milker / R / Miller / R / Potash maker / R / Presser / R / Shearer / R / Soaper / R / Spinner / R / Tanner / R / Thresher / R / Wood burner / R / Fishery worker / Fish cleaner / R / Fish dissector / R / Fisherdwarf / O / Metalsmith / Armorsmith / Q / Furnace operator / R / Metal crafter / Q / Blacksmith / Q / Weaponsmith / Q | Jeweler / Gem cutter / Q / Gem setter / Q / Craftsdwarf / Bookbinder / Q / Bone carver / Q / Clothier / Q / Glassmaker / Q / Glazer / Q / Leatherworker / Q / Papermaker / Q / Potter / Q / Stone crafter / Q / Strand extractor / R / Wax worker / Q / Weaver / Q / Wood crafter / Q / Engineer / Mechanic / Q / Pump operator / R / Siege engineer / Q / Siege operator / Other Jobs / Knapper / Administrator / Appraiser / Organizer / Record keeper | Military / Archer / Armor user / Axeman / Biter / Blowgunner / Bowman / Crossbowman / Dodger / Discipline / Fighter / Hammerman / Kicker / Knife user / Lasher / Maceman / Military tactics / Misc. object user / Pikeman / Shield user / Spearman / Striker / Swordsman / Thrower / Wrestler / Broker / Comedian / Conversationalist / Flatterer / Intimidator / Judge of intent / Liar / Negotiator / Persuader | Miscellaneous / Climber / Concentration / Consoler / Leader / Observer / Pacifier / Reader / Rider / Schemer / Student / Swimmer / Teacher / Tracker / Performance / Dancer / Singer / Musician / Poet / Speaker / Keyboardist / Stringed instrumentalist / Wind instrumentalist / Percussionist / Scholar / Critical thinker / Logician / Mathematician / Astronomer / Chemist / Geographer / Optics engineer / Fluid engineer / Wordsmith / Writer / Unused / Balance / Coordination / Druid / Skill 1 / Skill 2 / Skill 3 / Skill 4 / Skill 5 / Skill 6 / Skill 7 / Skill 8 / Skill 9 / Skill 10 |

Q Predominantly affects the quality of items produced O Predominantly affects the number of items produced (output) R Predominantly affects the rate at which items are produced, or at which the skill is undertaken

## Skills, attributes and facets

- **Skills and attributes**:
  - .. are both trained by being used in activities they relate to.
  - .. both influence future success of these activities, like craft quality, work speed, combat survivability, accuracy and damage.
  - The dwarf's profession is determined by their highest-ranking skill group.
  - Crafting skills are increased by preferences, allowing the dwarf to make items beyond their skill level.
  - The dwarf's highest moodable skill determines potential artifact types during a strange mood.

- **Facets**:
  - can be changed (at least beliefs change through arguments).
  - affect which social skills gain experience *(if the dwarf has X facet it will not gain experience in X skill)* at all.
  - give thoughts when performing certain activities.
  - influence the choice of artifact materials.

To summarize, it goes like this:

    Thought  Attribute
       ^          ,----------|                         |
    modifies   modifies    trains                   increases
       | ,--------'          |                         |
       | v                   v                         v
     Facet --influences--> Skill --increases--> Dwarf performance
       |           ,---------|
     item        item        |
    material     type    determines
       |  ,--------'         |
       v  v                  v
    Artifact <--chosen-- Profession
                 dwarf

Since the same skills can be used by various professions, and the same attributes are trained by various skills, this allows for cross-training.

As facets can limit learning some skills, which can be required by some Noble positions, the need arises to:

- avoid appointing a dwarf that will never learn a certain skill to a Noble position that uses it:
  - *appointing a straightforward\[Verify\] dwarf as a broker will result in a consoler, non-flatterer, non-liar broker*.
- appoint a dwarf with a useful effect given by a facet to a profession that benefits from it:
  - *appointing an undisciplined\[Verify\] dwarf to an important job will result in fun*.
  - *appointing an angry dwarf to be a soldier will result in more enraged bonuses.*

## Skill rust

Every skill has the following set of improvement and decay counters, which are caste specific:

[`[SKILL_RATE]`](/index.php/Creature_token#SKILL_RATE "Creature token") (Default is `[``SKILL_RATE``:100:8:16:16]`)

- % of improvement points you get (Default 100)
- unused counter cap (Default 8)
- rust counter cap (Default 16)
- demotion counter cap (Default 16)

Once per day, each skill's "unused" counter increments by 1, and if it reaches the cap (without the skill ever being used), it resets to zero and increments the rust counter. Once the rust counter reaches its cap, it resets to zero, adds a "layer" of rust to the skill (to a maximum of 6), and increments the demotion counter. When the demotion counter reaches its cap, it resets to zero and the skill level is *permanently* reduced by 1 (and must be re-earned). With the default numbers, it takes about 4 and a half months before rust sets in, 2 years and 3 months before rust maxes out, and 6 years before actual skill levels begin to decay.

The Rusty and V.Rusty descriptions which are appended to a skill within *Dwarf Fortress* are determined by the following conditions:

- Rusty: A skill level greater than 0, and the number of rust layers is at least 50% of the original skill level.
- Very Rusty: A skill level greater than or equal to 4, and the number of rust layers is at least 75% of the original skill level.

Since a skill can never gain more than 6 levels of rust, only skills between "Skilled" and "Expert" can ever show as "V. Rusty", and only skills at "Master" or lower can ever show as "Rusty" - higher level skills will silently accumulate rust until they are eventually demoted below "High Master", then the rust will become visible.

Whenever experience is gained, the skill's "unused" counter is reset to zero, its "rust" and "demotion" counters are *decremented* by 1, and one or more levels of rust are removed depending on the amount of experience gained:

- 50% of the gained experience points (rounded down, plus 1) are lost
- 10% of the *lost* experience points (rounded down, plus 1) are spent toward removing *levels* of rust
- If it was enough to remove *more* rust than was accumulated, then the experience penalty is set to 10 points per remaining rust level, minus 10

For example, when a dwarf who has 6 levels of rust completes a job that normally would grant 30 points of experience, 16 of those points (50% of 30, plus 1) are lost (leaving 14 points of actual skill gained) and 2 levels of rust (10% of 16, rounded down, plus 1) are removed. If the skill only has 1 level of rust, a single job would work it away without losing any experience.

## Performances

Randomly generated musical instruments and musical compositions are also considered skills and gain experience from use, though it is not clear how greater skill levels affect anything or if these performance-related skills rust.
