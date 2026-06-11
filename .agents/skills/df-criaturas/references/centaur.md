# Centaur

> Fonte: [Centaur](https://dwarffortresswiki.org/index.php/Centaur) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **C**
- **Urist likes centaurs for their strength.**
- **Biome**
- **None**
- **Attributes**
- **Fanciful**
- **Cannot be tamed**
- **Age**
- **Adult at:** Birth
- **Max age:** Immortal
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Centaurs** are fanciful creatures which are merely the stuff of legends. They do not actually exist, appearing only in engravings as the fancy of artists. A female centaur is known as a *centauress*.

Some dwarves like centaurs for their *strength*.

## The "Centaur" Problem

*"We've got the "centaur" problem, or whatever, where I wanna take any piece of anything, and slap it onto something else... That has complications in terms of the materials, and the body parts, and that kind of thing that need to be worked out."* - Toady One, Dwarf Fortress Talk \#28 \[38:26\]\
\
Procedurally generating centaurs has been discussed since the days of *Dwarf Fortress's* predecessor, *Slaves to Armok*. Combining two creature objects, such as a human with the lower body of a horse, and respecting the raw files and body structure of each component is a consideration that the nonexistent nature of the centaur and the other fanciful hybrid creatures allude to.

Though creatures like merpeople and satyrs are conceptually hybrids, they are singular, manual implementations, rather than a system that can generate any number of chimeric beings based on combining existing creatures. Experiments are generated from an independent random creature profile rather than being based on their input creature.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\

Some trolls like centaurs for their milk.

Admired for its *strength*.

## See Also

- Chimera
- Griffon

    [CREATURE:CENTAUR]
        [NAME:centaur:centaurs:centaur]
        [CREATURE_TILE:'C'][COLOR:6:0:0]
        [FANCIFUL]
        [DOES_NOT_EXIST]
        [PREFSTRING:strength]
        [ALL_ACTIVE]
        [CASTE:FEMALE]
            [CASTE_NAME:centauress:centauresses:centauress]
            [FEMALE]
        [CASTE:MALE]
            [CASTE_NAME:centaur:centaurs:centaur]
            [MALE]
