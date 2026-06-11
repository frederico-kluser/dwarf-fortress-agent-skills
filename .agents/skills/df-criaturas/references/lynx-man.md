# Lynx man

> Fonte: [Lynx man](https://dwarffortresswiki.org/index.php/Lynx_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes lynx men for their ear tufts.**
- **Biome**
- **Taiga**
- **Variations**
- **Lynx - Lynx man - Giant lynx**
- **Attributes**
- **Alignment:** Savage
- **Learns · War animals · Hunting animals · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 4,750 cm 3
- **Mid:** 23,750 cm 3
- **Max:** 47,500 cm 3
- **Age**
- **Adult at:** 3
- **Max age:** 60-80
- **Cannot be butchered ( Value multiplier ×3)**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A person with the head and tail of a lynx.*

If Lynxes are rare among their climes (and trust me, they are), then the sapient **Lynx man** is even rarer. Found only within savage taiga biomes, the lynx man lives significantly longer than their non-sapient brethren, and rarely, they can join other civilizations like all the other animal people. Standing at 47,500 cm3, they're approximately 12,500 cm3 shorter than a dwarf, so they pose more of a threat than the average Lynx, but not much. However, like any of the other animal people, they can join other civilizations and are just as capable of becoming threats in their own right with enough dedication and adventuring.

Being exclusive only to savage Taiga biomes, only three can exist per region before being locally considered extinct. Unlike their animal brethren, they can't be butchered for parts either, severely limiting their usefulness. Arguably, they're more likely to be an annoying crimp on anybody's day than an actual legitimate threat, should you choose to embark on a savage taiga.

Some dwarves like lynx men for their *ear tufts*.

-

-

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
You better not let them enter your fortress if you don't want your nobles to get robbed and your dwarves to get addicted to skooma.

    [CREATURE:LYNX_MAN]
        [COPY_TAGS_FROM:LYNX]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:lynx man:lynx men:lynx man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:lynx woman:lynx women:lynx woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:KICK_ATTACK]
        [APPLY_CREATURE_VARIATION:CLAW_SCRATCH_ATTACK]
        [APPLY_CREATURE_VARIATION:TOOTH_BITE_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:lynx man:lynx men:lynx man]
        [DESCRIPTION:A person with the head and tail of a lynx.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:5]
        [MAXAGE:60:80]
        [CREATURE_TILE:'l']
        [COLOR:6:0:0]
        [GO_TO_TAG:USE_TISSUE_TEMPLATE:CLAW:CLAW_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:FINGER:CLAW:FRONT]
