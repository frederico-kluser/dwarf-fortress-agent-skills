# Alligator man

> Fonte: [Alligator man](https://dwarffortresswiki.org/index.php/Alligator_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes alligator men for their strength.**
- **Biome**
- **Temperate Freshwater Swamp Temperate Freshwater Marsh Tropical Freshwater Swamp Tropical Freshwater Marsh Temperate Freshwater River Tropical Freshwater River Temperate Brackish River Tropical Brackish River**
- **Variations**
- **Alligator - Alligator man - Giant alligator**
- **Attributes**
- **Alignment:** Savage
- **Amphibious · Learns · Egglaying · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 35.25 cm 3
- **Mid:** 117,500 cm 3
- **Max:** 235,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 60-80
- **Cannot be butchered ( Value multiplier ×3)**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A person with the head and tail of an alligator.*

**Alligator men** are humanoid versions of the common alligator and a species of animal people, found in savage swamps and rivers. They are nearly 4 times bigger than dwarves when adults and spawn in groups of 1-3 individuals, and as such make potentially dangerous opponents to the average unarmed civilian. Approach them with caution.

Like other savage animal people, alligator men may occasionally join civilizations, becoming full-fledged citizens who may appear in your fortress as visitors or be playable in adventurer mode. Due to being based on the raw files of the normal animal, they lack the ability to jump.

Some dwarves like alligator men for their *strength*.

Fearless and "cold-blooded".

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\

Be wary around alligator women, for they are known for biting the legs of careless dwarves in taverns.

There have been instances of "big-lipped" alligator men appearing out of nowhere and causing confusion and/or laughter, before quickly leaving.

Some visitors may enjoy alligator men as performers in taverns, but care should be taken due to heavy rivalry between them and hare men, especially when deciding the bassist of a four-animal person band.

Batmen are said to be frequently antagonized by Crocodile men, mostly by humans. No dwarf has ever seen a Crocodile man, the misattribution can most likely be chalked up to classic human stupidity.

    [CREATURE:ALLIGATOR_MAN]
        [COPY_TAGS_FROM:ALLIGATOR]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:alligator man:alligator men:alligator man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:alligator woman:alligator women:alligator woman]
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
        [NAME:alligator man:alligator men:alligator man]
        [DESCRIPTION:A person with the head and tail of an alligator.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:3]
        [MAXAGE:60:80]
        [CREATURE_TILE:'A']
        [COLOR:2:0:0]
        [GO_TO_TAG:USE_TISSUE_TEMPLATE:CLAW:CLAW_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:FINGER:CLAW:FRONT]
