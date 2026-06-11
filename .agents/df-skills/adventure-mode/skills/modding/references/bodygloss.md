# Bodygloss

> Fonte: [Bodygloss](https://dwarffortresswiki.org/index.php/Bodygloss) — Dwarf Fortress Wiki (GFDL/MIT)

A **bodygloss** is a token in the raw body tokens and creature tokens which performs a simple word substitution on the creature's body parts. For instance, if a creature makes use of the "\[BODYGLOSS:PAW\]" token, then a hypothetical body part called "second right foot" would be renamed "second right paw".

It is important to distinguish the body token and creature token versions. The body token variant is defined anywhere in an "OBJECT:BODY" file and has the following syntax: *\[BODYGLOSS:id:singular:replacement:plural:replacements\]*

Note that this is a simple string replacement for all body parts—replacing "ear" will also replace the middle of "h**ear**t".

To make use of this token, the creature token variant is included beneath a creature definition (in an "OBJECT:CREATURE" file) and has the following syntax: *\[BODYGLOSS:id\]* Then, it will perform the word substitution defined by the bodygloss in the body tokens file; any occurrence of the words *singular* and *plural* in any body part will be replaced with the words *replacement* and *replacements*, respectively.

The default list of bodyglosses included in unmodded *Dwarf Fortress* is as follows, as taken from body_default.txt:

`[BODYGLOSS:PAW:foot:paw:feet:paws]`\
`[BODYGLOSS:MAW:mouth:maw:mouths:maws]`\
`[BODYGLOSS:CLAW_HAND:hand:claw:hands:claws]`\
`[BODYGLOSS:CLAW_FOOT:foot:claw:feet:claws]`\
`[BODYGLOSS:HOOF:foot:hoof:feet:hooves]`\
`[BODYGLOSS:TRUNK:body:trunk:bodies:trunks]`\
`[BODYGLOSS:BRANCH_ARM:arm:branch:arms:branches]`\
`[BODYGLOSS:LEG_STUMP:leg:stump:legs:stumps]`\
`[BODYGLOSS:ROOTS_FOOT:foot:roots:feet:roots]`\
`[BODYGLOSS:INSECT_UPPERBODY:upper body:thorax:upper bodies:thoraxes]`\
`[BODYGLOSS:INSECT_LOWERBODY:lower body:abdomen:lower bodies:abdomens]`

The following bodyglosses are used exclusively by randomly-generated creatures - titans, forgotten beasts, and demons:

`[BODYGLOSS:RCP_GLOSS_HOOF:foot:hoof:feet:hooves]`\
`[BODYGLOSS:RCP_GLOSS_PAW:foot:paw:feet:paws]`
