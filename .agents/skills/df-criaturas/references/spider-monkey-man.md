# Spider monkey man

> Fonte: [Spider monkey man](https://dwarffortresswiki.org/index.php/Spider_monkey_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes spider monkey men for their long limbs.**
- **Biome**
- **Tropical Moist Broadleaf Forest Tropical Dry Broadleaf Forest**
- **Variations**
- **Spider monkey - Spider monkey man - Giant spider monkey**
- **Attributes**
- **Alignment:** Savage
- **Learns · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 3,925 cm 3
- **Mid:** 19,625 cm 3
- **Max:** 39,250 cm 3
- **Age**
- **Adult at:** 3
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A long-limbed person with the head and tail of a spider monkey.*

**Spider monkey men** are an animal people variant of the rare spider monkey, living in tropical broadleaf forests, similarly to their precedents. They spawn in groups of 1-5 individuals and are generally content to keep to themselves. In terms of size, they are a little over half the weight of the average dwarf.

Like other savage animal people, they can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves like spider monkey men for their *long arms* and their *prehensile tails*.

|  |
|----|
| "Spider monkey man" in other / Languages / Dwarven / : / sethal vankåb udos / Elven / : / thepani rithé onino / Goblin / : / utes lam ngorûg / Human / : / azoc taksmo abo |

\

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Despite some claiming otherwise, no spider monkey men have been known to possess abilities reminiscent of actual spiders, nor have any human children ever been known to transform into one.

    [CREATURE:SPIDER_MONKEY_MAN]
        [COPY_TAGS_FROM:SPIDER_MONKEY]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:spider monkey man:spider monkey men:spider monkey man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:spider monkey woman:spider monkey women:spider monkey woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:KICK_ATTACK]
        [APPLY_CREATURE_VARIATION:NAIL_SCRATCH_ATTACK]
        [APPLY_CREATURE_VARIATION:TOOTH_BITE_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:spider monkey man:spider monkey men:spider monkey man]
        [DESCRIPTION:A long-limbed person with the head and tail of a spider monkey.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:5]
        [MAXAGE:60:80]
        [CREATURE_TILE:'m']
        [COLOR:0:0:1]
        [GO_TO_TAG:USE_TISSUE_TEMPLATE:NAIL:NAIL_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:FINGER:NAIL:FRONT]
