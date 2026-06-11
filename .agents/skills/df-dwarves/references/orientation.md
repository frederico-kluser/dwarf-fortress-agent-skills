# Orientation

> Fonte: [Orientation](https://dwarffortresswiki.org/index.php/Orientation) — Dwarf Fortress Wiki (GFDL/MIT)

**Orientation** mediates how intelligent creatures are romantically attracted to one another, which, along with characters' personalities and time spent together, may build to a romantically involved relationship or marriage. Such relationships do not need to be opposite-sex, same-sex marriages can in fact happen, both in world-gen and gameplay, albeit more rarely than opposite-sex marriages. Orientation is controlled by the creature token, by default favouring heterosexuality as a majority.

## Mechanic

The orientation token takes 4 arguments: . A one-time check is made for each creature to determine orientation, by "rolling a die" once for each sex, against the total of the three chances for that sex. Disinterested means that they will not form romantic relationships; lover-possible and commitment-possible both allow marriages as of 0.47.05, and the actual difference between lover-possible and commitment-possible is unknown.

The orientation token is omitted from many of the nonsapient creature definitions, and in its absence the game uses some default settings:

- and for a caste which has the token under it.

- and for a caste which has the token under it.

It is believed that this pair of default settings generates **all** populations (including animals) as 71.2% strictly heterosexual, 23.8% bisexual, 3.8% aromantic/asexual, and 1.2% strictly homosexual.

Consequently although nonsapient creatures can't marry or even be "interested in commitment", they can still display a homosexual or asexual orientation, which prevents breeding. Since this cannot be easily checked in fortress mode, you just have to hope any creature pair you catch for your breeding program is actually compatible. This behavior can be removed using DFHack's fix-ster script.

## Modifying orientation

For more information about how modifying *Dwarf Fortress* files works, and specifically creature castes, see Modding#Creature_castes.

In order to correctly add a custom orientation to any creature, the token with its 4 arguments must be placed beneath at least one of the tokens of that creature. Each caste only needs *one* orientation token to function correctly (and the game will indeed only use one per caste). Any orientation change to that caste is then effective immediately upon reloading a saved game (if the save file raws were edited) or generating a new world (if the base game raws were edited). Any previously formed relationships in a currently running game world remain intact, however any new relationship interactions are informed by the new orientation settings for that creature caste.

- Adding the tokens beneath the token and beneath the token would effectively make each caste (and if only those two castes exist, the whole creature) behave exclusively heterosexually with no interest whatsoever toward the same sex, like they did in old versions. Keep in mind that the chance of none of your dwarves being capable of marrying is, at most, 2.7%, and as of 0.47 there are out-of-wedlock children anyway, so it's actually 0.0125%. That this modification is required to have more children is a myth at best.
- To make the entire creature or just one caste of the creature behave exclusively homosexually, simply apply the token paired with the desired commitment-possible chances to the matching . In effect, apply the heterosexual-only change in reverse.
- Adding to *just one* caste would effectively make that caste behave bisexually, with every interest in partnering up with anyone. The other unmodified castes would still use their own orientation token setting, or the default if there was no token. Changing the *ratio* within the tokens from 0:0:100 to *0:100:0* would result in mostly only lovers with rare marriages.
- Adding to all castes would effectively make the creature behave asexually, with no interest in partnering up and having children (although non-hist fig populations will still marry and have children as normal, and may even arrive already-married with children as migrants). Gameplay-wise, if the player doesn't want their fortress involved with any children, it would be simpler just to edit the baby/child cap.

A small reminder: As stated on the creature token page regarding the values used are just a ratio, and not an actual percentage. The numbers do not need to add up to any specific number; a setting of 750:200:50 will provide the same effect as 75:20:5 and a setting of 99:99:99 the same as 1:1:1.

## Adventure mode

Adventurers have a special "indeterminate" orientation which has no behavior, instead acting identically to asexuality (partially, because SLOW_LEARNER with that orientation does not count as sterile and will breed in fortmode), and thus cannot ever marry or have children in vanilla DF, even after retiring them to a site. This can be changed with DFHack's fix-ster script, though you will have little control over your retired adventurer's partner choices once they're off-map.
