# Tiger man

> Fonte: [Tiger man](https://dwarffortresswiki.org/index.php/Tiger_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes tiger men for their stripes, of course.**
- **Biome**
- **Any Tropical Forest Tropical Shrubland Tropical Freshwater Swamp Tropical Saltwater Swamp Mangrove Swamp**
- **Variations**
- **Tiger - Tiger man - Giant tiger**
- **Attributes**
- **Alignment:** Savage
- **Learns · War animals · Hunting animals · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 14,750 cm 3
- **Mid:** 65,555.555555556 cm 3
- **Max:** 147,500 cm 3
- **Age**
- **Adult at:** 3
- **Max age:** 60-80
- **Cannot be butchered ( Value multiplier ×3)**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*An orange striped person with the head of a tiger.*

**Tiger men** are animal people versions of the common tiger, often inhabiting savage tropical forests and coastal/wetland areas. They are large, predatory carnivores that can present a significant threat to an unarmed dwarf, as they are over twice the size of the average human.

Like other savage animal people, they can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves prefer tiger men for their *stripes, of course*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\

## Tamed tiger men

In previous versions, elven merchants used to sometimes bring tamed (enslaved?) tiger men to trade. As they could not work, they had plenty of time to improve their social skills and could even become the mayor of a fortress. This was due to the combination of the Tiger Man's \[PET\] and \[CAN_LEARN\] tags; however, since the first one was removed in version 40.05, this no longer happens.

## Behavior

Tiger men prefer to consume meals made from flour, Dwarven sugar and milk when possible. Particularly tough, agile and strong tiger men may become brokers for this food combination, urging caravans arriving to your fortress to purchase it while profusely claiming it is *great*.

Some tiger men will form close bonds with blonde, mischievous dwarven children. The child will often own a red-colored ~~minecart~~ wagon, and have a fierce grudge with a brunette child of the opposite gender in your fort.

Other tiger men are capable building destroyers and tend to wreak havoc if they enter the elven home of a corresponding sloth bear man. Inexperienced tiger men readily consume honey from sloth bear men's stockpiles of glazed «+earthenware jugs+» despite their innate negative preference for it, leading to a negative thought. Some dwarves like tiger men for their *tail-bouncing propagation*.

A distinct lineage of tiger men may achieve legendary maceman skill, specifically with masterwork wooden or iron maces, demonstrating an uncanny ability to propel small bone toys across vast pastures into designated refuse pits with exceptional accuracy. These tiger men often develop a strong preference for tunics dyed with redroot dye during these striking displays. Despite their high focus skill, these tiger men are notorious for triggering berserk rages in their spouses. Following a failed liar check, the aforementioned iron mace might unexpectedly be wielded by the spouse, prompting the tiger man to make a hasty exit from their opulent throne room using a steel minecart. Their erratic handling of these minecarts often derails them into iron floodgates resulting in water surges, or colliding with fungiwood trees. Separately, fortress sheriffs have, on occasion, discovered these same tiger men in inappropriate stunned or unconscious statuses while nominally in command of the aforementioned steel minecart. Such incidents invariable lead to swift but light sentences, often a temporary suspension of their booze rations.

Furthermore, some tiger men develop an almost pathological need for public attention, often attempting to obsessively amass a large collection of other, lesser felines, always in poorly constructed cages near their lairs. These tiger men always exhibit a preference for unusually styled lion leather caps and garishly dyed cave spider silk cloaks, and have been known to frequently perform surprisingly popular, if discordant, ballads detailing their numerous grievances, often against certain leopard women with a higher animal training skill level than them. On occasion, such a tiger man might launch a spectacularly ill-advised campaign for mayor, only to find their ambitions severely curtailed by the captain of the guard following successful interrogations about murder plots (attempted by dispatching poorly-trained gorilla men to cause mayhem) and the suspicious use of low-value meat stockpiles.

*Art by AlsaresLynx*

    [CREATURE:TIGER_MAN]
        [COPY_TAGS_FROM:TIGER]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:tiger man:tiger men:tiger man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:tiger woman:tiger women:tiger woman]
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
        [NAME:tiger man:tiger men:tiger man]
        [DESCRIPTION:An orange striped person with the head of a tiger.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:5]
        [MAXAGE:60:80]
        [CREATURE_TILE:'T']
        [COLOR:6:0:1]
        [GO_TO_TAG:USE_TISSUE_TEMPLATE:CLAW:CLAW_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:FINGER:CLAW:FRONT]
