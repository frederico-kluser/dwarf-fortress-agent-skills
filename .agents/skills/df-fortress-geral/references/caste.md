# Caste

> Fonte: [Caste](https://dwarffortresswiki.org/index.php/Caste) — Dwarf Fortress Wiki (GFDL/MIT)

A caste is a means of defining a sub-species within the broader creature definition. When a creature is spawned, they are made into a randomly determined caste of the creature, using either equal weighting (by default), or the tag. Castes were originally conceived mainly for male/female distinction, and in vanilla DF, mostly serve the purpose of making males and females differ from each other. Many of the game's graphics will reflect the details of a creature's body. Many of the game's creatures will have a unique sprite for both the male and female version.

Caste-level definitions of a creature may be (and, in the vanilla raws, often are) defined for all castes at once.

The entire skeleton (that is, the `BODY:` tag) and tissue structure of creatures are moddable on a caste level, which allows for creatures with radically different body types (such as a giant spider and a human) to share the same "species". In fact, virtually every creature-level token is apparently caste-level moddable. The only tags that are believed to buck this trend are the tag, which would create a race incapable of breeding with itself if used improperly by segregating males and females, the tag, and tag, presumably to prevent megabeasts from breeding. Also, the vermin-related tags are in the creature-level. This also means it is possible to make caste-level moddable, and then make, among other things, *male dwarves who are milkable*, thanks to the extreme power of the moddability of the raws.

Some bugs are possible through modding, such as creating "fractal bodies" by defining the tag in the creature level, and then creating a new caste-level definition of the creature. This generates duplicate body parts, which increase in number the further away they are from the Upper Body part, with six upper arms, eight lower arms, and ten hands. Please mod responsibly.

Selecting Castes

|  |  |
|----|----|
| `[CASTE:]` | defines a caste called \. Tags following this affect only this caste. |
| `[SELECT_CASTE:ALL]` | state the following tags affect all Castes |
| `[SELECT_CASTE:]` | ... |
| `[SELECT_ADDITIONAL_CASTE:]` | ... |
| `[SELECT_ADDITIONAL_CASTE:]` | , etc., is used to specify that tags affect a subset of Castes |
