# Orientation

> Fonte: [Orientation](https://dwarffortresswiki.org/index.php/Orientation) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Orientation** mediates how intelligent creatures are romantically attracted to one another, which, along with characters' personalities and time spent together, may build to a romantically involved relationship or marriage. Such relationships do not need to be opposite-sex, same-sex marriages and love affairs can in fact happen, both in world-gen and gameplay, albeit more rarely than opposite-sex romance. Orientation is controlled by the [`[ORIENTATION]`](/index.php/Creature_token#ORIENTATION "Creature token") creature token, and defaults to 95% of all creatures being interested in heterosexual relationships.

## Mechanic

The orientation token takes 4 arguments: `[``ORIENTATION``::::]`. A one-time check is made for each creature to determine orientation, by "rolling a die" once for each sex, against the total of the three chances for that sex. Disinterested means that they will not form romantic relationships.

The orientation token is omitted from most creature definitions, and in its absence, the game uses some default settings:

- `[``ORIENTATION``:MALE:5:20:75]` and `[``ORIENTATION``:FEMALE:75:20:5]` for a caste which has the [`[FEMALE]`](/index.php/Creature_token#FEMALE "Creature token") token under it.
- `[``ORIENTATION``:MALE:75:20:5]` and `[``ORIENTATION``:FEMALE:5:20:75]` for a caste which has the [`[MALE]`](/index.php/Creature_token#MALE "Creature token") token under it.

This pair of default settings generates all populations as 71.2% strictly heterosexual, 23.8% bisexual, 3.8% aromantic/asexual, and 1.2% strictly homosexual; for animals, this in practice can be boiled down to 95% opposite-sex interested and 5% not, meaning there is a 9.75% chance that a breeding pair of only one male and one female will not breed properly (adding a second one of each reduces this to a 0.5% chance). Intelligent creatures require marriage to breed. If this behavior is undesirable, it can be changed with DFHack's \`set-orientation\` script.

## Modifying orientation

For more information about how modifying *Dwarf Fortress* files works, and specifically creature castes, see Modding#Creature_castes.

In order to correctly add a custom orientation to any creature, the [`[ORIENTATION]`](/index.php/Creature_token#ORIENTATION "Creature token") token with its 4 arguments must be placed beneath at least one of the [`[CASTE]`](/index.php/Creature_token#CASTE "Creature token") tokens of that creature. Each caste only needs *one* pair of orientation tokens to function correctly (and the game will only use one pair per caste). Any orientation change to that caste is effective immediately upon reloading a saved game, but as a given creature's orientation is determined at birth, only newly-generated creatures will be affected.

- Adding the tokens `[``ORIENTATION``:MALE:0:0:100]``[``ORIENTATION``:FEMALE:100:0:0]` beneath the [`[CASTE:FEMALE]`](/index.php/Creature_token#CASTE:FEMALE "Creature token") token and `[``ORIENTATION``:FEMALE:0:0:100]``[``ORIENTATION``:MALE:100:0:0]` beneath the [`[CASTE:MALE]`](/index.php/Creature_token#CASTE:MALE "Creature token") token would effectively make each caste (and if only those two castes exist, the whole creature) behave exclusively heterosexually with no interest whatsoever toward the same sex, like they did in old versions. Keep in mind that the chance of none of your dwarves being capable of marrying is, at most, 2.7%, and as of 0.47 there are out-of-wedlock children anyway, so it's actually 0.0125%. That this modification is required to have more children is a myth at best.
- To make the entire creature or just one caste of the creature exclusively homosexual, simply apply the [`[ORIENTATION]`](/index.php/Creature_token#ORIENTATION "Creature token") token paired with the desired commitment-possible chances to the matching sex. In effect, apply the heterosexual-only change in reverse.
- Adding `[``ORIENTATION``:MALE:0:0:100]``[``ORIENTATION``:FEMALE:0:0:100]` to *just one* caste would effectively make that caste behave bisexually, with every interest in partnering up with anyone. The other unmodified castes would still use their own orientation token setting, or the default if there was no [`[ORIENTATION]`](/index.php/Creature_token#ORIENTATION "Creature token") token. Changing the *ratio* within the tokens from 0:0:100 to *0:100:0* would result in mostly only lovers with rare marriages.
- Adding `[``ORIENTATION``:MALE:100:0:0]``[``ORIENTATION``:FEMALE:100:0:0]` to all castes would effectively make the creature behave asexually, with no interest in partnering up and having children (although non-hist fig populations will still marry and have children as normal, and may even arrive already-married with children as migrants). Gameplay-wise, if the player doesn't want their fortress involved with any children, it would be simpler just to edit the baby/child cap setting.

A small reminder: As stated on the creature token page regarding [`[ORIENTATION]`](/index.php/Creature_token#ORIENTATION "Creature token") the values used are just a ratio, and not an actual percentage. The numbers do not need to add up to any specific number; a setting of 750:200:50 will provide the same effect as 75:20:5 and a setting of 99:99:99 the same as 1:1:1.

## Adventure mode

Adventurers have a special "indeterminate" orientation which has no behavior, instead acting identically to asexuality or aromanticism (partially, because a [`[SLOW_LEARNER]`](/index.php/Creature_token#SLOW_LEARNER "Creature token") with that orientation does not count as sterile and will breed in Fortress mode), and thus cannot ever marry or have children in vanilla, even after retiring them to a site. This can be changed (*or indeed, fixed, as it might be*) with DFHack's `set-orientation` script, though you will have little control over the retired adventurer's partner choices, once they're off-map.
