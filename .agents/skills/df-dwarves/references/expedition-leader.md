# Expedition leader

> Fonte: [Expedition leader](https://dwarffortresswiki.org/index.php/Expedition_leader) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

!!UNKNOWN!!  · xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

Expedition Leader

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

None

Function

Meet with foreign dignitaries / Talk with unhappy citizens

- *This page is about the administrative noble position within a fortress. For the skill, see Leader.*

The **expedition leader** is an administrative position automatically filled on embark. It is the job of this official to speak with, and console or simply hear the complaints of unhappy dwarves, and to entertain foreign diplomats. Once the population reaches 50, a mayor will be elected and the expedition leader position will be removed.

An expedition leader or mayor is required to appoint other administrators; they are also able to appoint replacements for elected positions, including their own, or remove current appointments, leaving the position empty. Should your leader suffer an unfortunate accident or be removed, you will have to wait for a new leader to be elected to be able to appoint any administrators; this can happen within a day. However, if the civilization is dead, the election will never happen and you will be unable to appoint a new leader or other officials.

There is a certain set of skills that are relevant for an expedition leader. There are also certain personality traits that influence whether experience is gained in the skill whatsoever. Furthermore, there are soul attributes that affect the skills and other skills that affect these same attributes (cross-training); the ones relevant for an expedition leader are as follows:

Skill (relevant for Expedition Leader)
Personality Trait (needed to gain Social Skill)
Attribute (affected by Social Skill)

Body
Soul

Social - Other
Consoler
Straightforwardness (Honesty)
> 39

Linguistic Ability

Empathy

Social Awareness

Pacifier
Cooperation (Compromising)
> 39

Linguistic Ability

Empathy

Social Awareness

Social - Broker
Comedian
Self-consciousness (Neurosis)

Agility
Creativity

Kinesthetic Sense

Linguistic Ability

Conversationalist
Friendliness (Reserved)
> 39

Linguistic Ability

Empathy

Social Awareness

Flatterer
Straightforwardness (Honesty)

Linguistic Ability

Empathy

Social Awareness

Liar

Creativity

Linguistic Ability

Social Awareness

Intimidator
Cooperation (Compromising)

Agility
Kinesthetic Sense

Linguistic Ability

Judge of intent

Intuition

Empathy

Social Awareness

Negotiator

Linguistic Ability

Empathy

Social Awareness

Persuader
Assertiveness (Leadership)
> 39

Linguistic Ability

Empathy

Social Awareness

The better match with the skills, traits and attributes in the table, the better an expedition leader the dwarf will be; try to avoid traits that halt experience gain for a relevant skill, otherwise time will be lost training a dwarf that will never get better at that skill.

## Bugs

- It has long been debated whether their being able to replace or remove elected positions including themselves is a bug.Bug:2512
- If the fortress population drops to 1 child or insane dwarf, can't appoint or elect nobles when migrants arrive.Bug:5299
- After passing the 50-dwarf-threshold, election for Mayor doesn't happen until any change is made to nobles screen.Bug:8514
- An empty expedition leader position cannot be refilled in a dead civilization and thus appointed positions also cannot be filled.Bug:11559

       [POSITION:EXPEDITION_LEADER]
            [NAME:expedition leader:expedition leaders]
            [SITE]
            [NUMBER:1]
            [REPLACED_BY:MAYOR]
            [RULES_FROM_LOCATION]
            [RESPONSIBILITY:MEET_WORKERS]
            [RESPONSIBILITY:RECEIVE_DIPLOMATS]
            [RESPONSIBILITY:MILITARY_GOALS]
            [PRECEDENCE:110]
            [DO_NOT_CULL]
            [ACCOUNT_EXEMPT]
            [DUTY_BOUND]
