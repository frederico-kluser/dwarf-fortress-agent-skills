# Wolverine man

> Fonte: [Wolverine man](https://dwarffortresswiki.org/index.php/Wolverine_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes wolverine men for their tenacity.**
- **Biome**
- **Taiga Mountain**
- **Variations**
- **Wolverine - Wolverine man - Giant wolverine**
- **Attributes**
- **Alignment:** Savage
- **Learns · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 4,500 cm 3
- **Mid:** 22,500 cm 3
- **Max:** 45,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A person with the head and tail of a wolverine.*

**Wolverine men** are animal people variants of the common wolverine who can be found in savage mountains and taigas. They spawn in groups of 1-5 individuals and are generally content to keep to themselves, though like the common animal, they are prone to rage and may randomly flip off, attacking any creature unfortunate enough to be in their general vicinity. In terms of size, they are over half the weight of the average dwarf.

Like other savage animal people, wolverine men can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves like wolverine men for their *tenacity*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
The chief factor limiting a wolverine man's effectiveness in combat is his savage and uncivilized refusal to wear armor.

To that end, an experiment was conducted on a captured wolverine man, wherein a team of dwarven scientists stitched adamantine threads directly onto his skeleton. Only the wolverine man's amazing recuperative abilities allowed him to survive the procedure (especially considering the state of dwarven health care); despite suffering from amnesia, the specimen nevertheless proved X-traordinary on the battlefield, capable of enduring single combat with such monstrosities as a cyclops wearing a ☼rose quartz visor☼ and an osmium colossus - both of which he later befriended.

After enjoying a largely successful career against foes such as a sabretooth tigerman and a soil-based forgotten beast masquerading as an island, the subject was ultimately incapacitated by Magngebzo, an elderly goblin sorcerer capable of manipulating magnetic fields.

*Art by Devilingo*

    [CREATURE:WOLVERINE_MAN]
        [COPY_TAGS_FROM:WOLVERINE]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:wolverine man:wolverine men:wolverine man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:wolverine woman:wolverine women:wolverine woman]
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
        [NAME:wolverine man:wolverine men:wolverine man]
        [DESCRIPTION:A person with the head and tail of a wolverine.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:5]
        [MAXAGE:60:80]
        [CREATURE_TILE:'w']
        [COLOR:6:0:0]
        [GO_TO_TAG:USE_TISSUE_TEMPLATE:NAIL:NAIL_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:FINGER:NAIL:FRONT]
