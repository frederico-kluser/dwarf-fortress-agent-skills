# Embark profiles.txt

> Fonte: [Embark profiles.txt](https://dwarffortresswiki.org/index.php/Embark_profiles.txt) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

!!UNKNOWN!!  · xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

|                                                    |
|----------------------------------------------------|
| File |
| prefs                                              |
| embark_profiles.txt                                |

*See Starting build for detailed information on planning an embark.*

*See Embark profile repository for a collection of embark profiles.*

The **embark_profiles.txt** file contains any embark profiles (or starting builds) you have created. It is found in the `prefs/` folder, the location of that depends on the portable mode setting, but the file only exists once you've saved a profile. Most of these can be transferred between minor versions (e.g. v0.34.10 to v0.34.11), but you need to remember to do so.

## Format

Each profile begins with a \[PROFILE\] tag, followed by a \[TITLE:*name*\] tag.

### Skills

Skills are identified by their skill token. The syntax for skills is:

    [SKILL:#:skill name:level]

where \# is the dwarf (1-7), "skill name" is the skill, and "level" is the number representing how skilled the dwarf is.

Note that skills are capped at Proficient (5), and this is checked by the game on embark, so it's not possible to start with legendary dwarves. There are other ways to do this (see Cheating or User:Vjek for more information).

### Items

Items are identified by their material and item tokens, the same format as reactions:

    [ITEM:quantity:(material token):(item token)]

For examples, see reaction, item token, material token, or DFHack createitem.

Be aware that profiles cannot add any items that the player's civilization does not have access to. If an embark profile specifies an iron anvil, but the host nation has not discovered iron, then the anvil will not get included. This specific issue can be worked around by specifying a more expensive steel anvil (which is always available). For lumber, tunnel tube wood is also always available and (as of DF v0.44) is the lightest wood that is so.

### Pets

    [PET:quantity:creature name:caste:age]

- "Creature" is the creature ID found in the raws (e.g. CAT for cats).
- "Caste" is the caste ID, which can also be found in the raws. Most creatures have MALE and FEMALE castes.
- "Age" can be either STANDARD (for adults) or CHILD (for children).

## Obtaining new profiles

- See Embark profile repository for a collection of embark profiles.
- The Masterwork mod includes a set of embark profiles as well.
