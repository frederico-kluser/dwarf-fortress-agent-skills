# Wild boar man

> Fonte: [Wild boar man](https://dwarffortresswiki.org/index.php/Wild_boar_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes wild boar men for their ferocious charges.**
- **Biome**
- **Any Savanna Any Grassland Any Shrubland Any Forest Any Wetland**
- **Variations**
- **Wild boar - Wild boar man - Giant wild boar**
- **Attributes**
- **Alignment:** Savage
- **Learns · Horn · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 7,500 cm 3
- **Mid:** 37,500 cm 3
- **Max:** 75,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A person with the head of a wild boar.*

**Wild boar men** are animal people versions of the common wild boar, who can be found in almost all savage biomes. They spawn in groups of 5-10 individuals and are generally content to keep to themselves, but may fight back if provoked by approaching civilians. In terms of size, they are slightly larger than the average human.

Like other savage animal people, they can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode. Wild boar men are among the few animal people capable of wearing human-sized armor while retaining the primary advantage most animal men have of being larger than humans.

Some dwarves like wild boar men for their *tusks* and their *ferocious charges*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
In the unseen enclaves of the Underworld, it has been rumored that zombie **wild boar men** spawn, all wielding ☼Golden short swords☼ but being oddly non-aggressive. If provoked, however, they are said to retaliate in packs.

Often snorts when laughing.\
*Art by plutus0519*

|  |
|----|
| "Wild boar man" in other / Languages / Dwarven / : / omrist dùstik udos / Elven / : / theÿise lebeyu onino / Goblin / : / muso oke ngorûg / Human / : / kozi stral abo |

    [CREATURE:WILD_BOAR_MAN]
        [COPY_TAGS_FROM:WILD_BOAR]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:wild boar man:wild boar men:wild boar man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:wild boar woman:wild boar women:wild boar woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:HOOF_ATTACK]
        [APPLY_CREATURE_VARIATION:NAIL_SCRATCH_ATTACK]
        [APPLY_CREATURE_VARIATION:TOOTH_BITE_ATTACK]
        [APPLY_CREATURE_VARIATION:TUSK_STAB_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:wild boar man:wild boar men:wild boar man]
        [DESCRIPTION:A person with the head of a wild boar.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:5:10]
        [MAXAGE:60:80]
        [CREATURE_TILE:'B']
        [COLOR:6:0:0]
        [GO_TO_TAG:BODY_DETAIL_PLAN:BODY_HAIR_TISSUE_LAYERS:HAIR]
        [APPLY_CREATURE_VARIATION:NAIL_MATERIALS]
        [GO_TO_TAG:USE_TISSUE_TEMPLATE:NAIL:NAIL_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:FINGER:NAIL:FRONT]
