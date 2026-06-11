# Ethic

> Fonte: [Ethic](https://dwarffortresswiki.org/index.php/Ethic) — Dwarf Fortress Wiki (GFDL/MIT)

**Ethic** tags are used in the entity raw files to determine how different civilizations feel about various issues. Relationships between civilizations are based on their ethic responses in relation to each other; similar ethics result in friendship, while conflicting ethics result in animosity. Strongly conflicting ethics often trigger wars during world generation. (In practice, this generally causes elves to declare war on everybody else over killing plants and making trophies, and everybody else to declare war on the elves over the devouring of sapient beings.)

Some ethics also affect fortress mode features, such as justice, or trading. In adventurer mode, ethics can affect the level of conflict (lethal, or no quarter). During world generation, ethics also affect how the entity treats its kills, such as devouring them or making trophies out of them.

## Example

In the raw files for entities, ethics appear as follows:

`[ETHIC:LYING:PERSONAL_MATTER]`

This means that the entity will treat lying as a personal matter - more technically, the value of its LYING ethic is set to PERSONAL_MATTER.

## Ethic types

[TABLE]

## Ethic values

As used internally (see below), roughly in order of acceptability:

[TABLE]

## Ethic value numbers in relation to each other

The following table describes how entities respond to other cultures, with the observer on the vertical axis and their target on the horizontal axis. If an entity's accumulated animosity towards another passes a certain threshold (determined by the ruler's personality) then it will run a risk-assessment check. If passed, this will lead to a declaration of war.

In general, entities react much more strongly to actions that violate *their* taboos than to the outlawing of their customs in other civilisations. For example, Civ A finds slavery Acceptable, but Civ B considers it a Capital Offence.

- Civ A will consider Civ B most unreasonable (−5) for executing people over such a non-issue.
- Civ B will be shocked and disgusted (−15) that Civ A engages in such a debased activity.
- The end result is mutual negativity. However, Civ B is 3× *more* offended, and much more likely to go to war over the issue — assuming, of course, they think they have a chance of winning.

[TABLE]

All above info was collected and interpreted from the data given by Toady himself at 1.

## Ethics of vanilla civilizations

Animal people currently have the same ethics as kobolds.

[TABLE]
