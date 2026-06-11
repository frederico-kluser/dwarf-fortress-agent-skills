# Bobcat man

> Fonte: [Bobcat man](https://dwarffortresswiki.org/index.php/Bobcat_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes bobcat men for their short tails.**
- **Biome**
- **Any Forest Any Desert Tropical Freshwater Swamp Tropical Saltwater Swamp Temperate Freshwater Swamp Temperate Saltwater Swamp Mangrove Swamp Mountain**
- **Variations**
- **Bobcat - Bobcat man - Giant bobcat**
- **Attributes**
- **Alignment:** Savage
- **Learns · War animals · Hunting animals · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 3,900 cm 3
- **Mid:** 19,500 cm 3
- **Max:** 39,000 cm 3
- **Age**
- **Adult at:** 3
- **Max age:** 60-80
- **Cannot be butchered ( Value multiplier ×2)**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A person with the head and short tail of a bobcat.*

**Bobcat men** are humanoid versions of the common bobcat and a species of unremarkable animal people, found in a variety of savage biomes. They are a little over half the size of an adult dwarf and are unlikely to pose a threat to a fortress' inhabitants. While not as rare as their fully-animal cousins, bobcat men are also few in number, with only a maximum of 10 potentially existing in the fortress' surroundings.

Like other savage animal people, bobcat men may occasionally join civilizations, becoming full-fledged citizens who may appear in your fortress as visitors or be playable in adventurer mode.

Some dwarves like bobcat men for their *short tails*.

*Art by house longeye*

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Bobcat men will not raid your yarn stores, nor can they glide. They may occasionally make odd quips.

Some bobcat men are inexplicably drawn to the miner labor, showing a strange obsession with moving vast quantities of stone. These individuals possess a relentless urge to pilot heavy iron wheelbarrows and minecarts, adeptly using them to clear out channels and flatten terrain for new paved roads. Curiously, these bobcat men will absolutely refuse to haul any materials unless provided with pig tail tunics brighly dyed with tomato skin dye. They are also notorious for taking extended but regimented breaks at the tavern to consume dwarven ale while loudly complaining about the Architect's poorly planned blueprints.

A distinct caste of bobcat men with aggressively petition the Manager to undergo rigorous testing involving track stops and rollers. Those who pass are officially recognized as \*\*Minecart Certified\*\*. These certified bobcat men carry an air of overwhelming superiority, frequently boasting that their prestigious title makes them irresistibly attractive to all other animal men, unrivaled by any noble title or artifact wealth.

Nevertheless, bobcat men are infamous for their lack of urgency when cooperating with other labors. If a massive excavation project is momentarily halted because a single piece of microcline needs to be hauled away, the bobcat man will immediately develop the Drowsy status, curl up inside their assigned minecart, and go to sleep. They will only awaken once lesser creatures have finished all the grueling manual labor.

    [CREATURE:BOBCAT_MAN]
        [COPY_TAGS_FROM:BOBCAT]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:bobcat man:bobcat men:bobcat man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:bobcat woman:bobcat women:bobcat woman]
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
        [NAME:bobcat man:bobcat men:bobcat man]
        [DESCRIPTION:A person with the head and short tail of a bobcat.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:5]
        [MAXAGE:60:80]
        [CREATURE_TILE:'b']
        [COLOR:6:0:0]
        [GO_TO_TAG:USE_TISSUE_TEMPLATE:CLAW:CLAW_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:FINGER:CLAW:FRONT]
