# Panda man

> Fonte: [Panda man](https://dwarffortresswiki.org/index.php/Panda_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes panda men for their big fluffy heads and bellies.**
- **Biome**
- **Any Temperate Forest**
- **Variations**
- **Panda - Panda man - Gigantic panda**
- **Attributes**
- **Alignment:** Savage
- **Learns · Grazer · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 115.38461538462 cm 3
- **Mid:** 50,000 cm 3
- **Max:** 100,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 60-80
- **Cannot be butchered ( Value multiplier ×2)**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A humanoid creature with the head and belly of a panda.*

**Panda men** are humanoid versions of the common panda and a species of animal people, found in savage temperate forests. They are nearly twice the size of dwarves when adults and spawn in groups of 5-10 individuals, though they are unlikely to pose any danger to your fortress unless provoked. Unlike their animal cousins, panda men aren't restricted to eating just bamboo, though they'll only appear in areas where bamboo grows.

Like other savage animal people, panda men may occasionally join civilizations, becoming full-fledged citizens who may appear in your fortress as visitors or be playable in adventurer mode.

Some dwarves like panda men for their *striking coloration*, their *big fluffy heads and bellies*, and their *lazy nature*.

\

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Panda men should be feared for their legendary kung fu, although even the Dragon warrior is not much of a match for a competent marksdwarf. They may also be seen joining forces with humans and goblins in wars against lightning-throwing kings and hordes of mantis men. These panda men often urge others to slow down, since life is to be savored.

Panda men also are proud cheesemakers, and refusing to eat their cheese has been known to make them throw a tantrum.

    1 kph

    [CREATURE:PANDA MAN]
        [COPY_TAGS_FROM:PANDA]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:TLCM_NOUN]
            [CVCT_TARGET:legs]
            [CVCT_REPLACEMENT:arms and legs]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_TAG:SET_TL_GROUP:BY_CATEGORY:LEG_FRONT:HAIR]
        [CV_REMOVE_TAG:SET_TL_GROUP:BY_CATEGORY:LEG_FRONT:HAIR]
        [CV_REMOVE_TAG:PLUS_TL_GROUP:BY_CATEGORY:LEG_REAR:HAIR]
        [CV_REMOVE_TAG:PLUS_TL_GROUP:BY_CATEGORY:FOOT_FRONT:HAIR]
        [CV_REMOVE_TAG:PLUS_TL_GROUP:BY_CATEGORY:FOOT_REAR:HAIR]
        [CV_ADD_TAG:SET_TL_GROUP:BY_CATEGORY:ARM_UPPER:HAIR]
        [CV_ADD_TAG:PLUS_TL_GROUP:BY_CATEGORY:ARM_LOWER:HAIR]
        [CV_ADD_TAG:PLUS_TL_GROUP:BY_CATEGORY:HAND:HAIR]
        [CV_ADD_TAG:PLUS_TL_GROUP:BY_CATEGORY:FINGER:HAIR]
        [CV_ADD_TAG:PLUS_TL_GROUP:BY_CATEGORY:LEG:HAIR]
        [CV_ADD_TAG:PLUS_TL_GROUP:BY_CATEGORY:FOOT:HAIR]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_TAG:TISSUE_LAYER:BY_CATEGORY:TOE:NAIL:FRONT]
        [TISSUE_LAYER:BY_CATEGORY:FINGER:NAIL:FRONT]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:panda man:panda men:panda man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:panda woman:panda women:panda woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:KICK_ATTACK]
        [APPLY_CREATURE_VARIATION:NAIL_SCRATCH_ATTACK]
        [APPLY_CREATURE_VARIATION:TOOTH_BITE_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:750:600:439:1900:2900] 20 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:panda man:panda men:panda man]
        [DESCRIPTION:A humanoid creature with the head and belly of a panda.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:5:10]
        [MAXAGE:60:80]
        [CREATURE_TILE:'P']
        [COLOR:7:0:1]
