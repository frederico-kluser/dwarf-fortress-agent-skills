# Sloth bear man

> Fonte: [Sloth bear man](https://dwarffortresswiki.org/index.php/Sloth_bear_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes sloth bear men for their large floppy ears.**
- **Biome**
- **Any Tropical Forest**
- **Variations**
- **Sloth bear - Sloth bear man - Giant sloth bear**
- **Attributes**
- **Alignment:** Savage
- **Steals food · Steals drink · Learns · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 8,500 cm 3
- **Mid:** 42,500 cm 3
- **Max:** 85,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 60-80
- **Cannot be butchered ( Value multiplier ×2)**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A person with the head and claws of a sloth bear.*

**Sloth bear men** are animal people versions of the sloth bear who can be found in savage tropical forests. They spawn in groups of 1-5 individuals and are generally content to keep to themselves, but may fight back if provoked. In terms of size, they are a little larger than the average human. They also possess the [`[CURIOUSBEAST_GUZZLER]`](/index.php/Creature_token#CURIOUSBEAST_GUZZLER "Creature token") creature token, which means that they will wander towards exposed stockpiles of alcohol and drink it. Be careful, they can drink entire barrels in an instant!

Like other savage animal people, they can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves like sloth bear men for their *large floppy ears*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\

Certain powerful human nobles take great offense at engravings depicting them as sloth bear men.

|  |
|----|
| "Sloth bear man" in other / Languages / Dwarven / : / gäzot uvel udos / Elven / : / timeba atha onino / Goblin / : / ongo ron ngorûg / Human / : / thruque rorec abo |

    [CREATURE:SLOTH_BEAR_MAN]
        [COPY_TAGS_FROM:BEAR_SLOTH]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:sloth bear man:sloth bear men:sloth bear man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:sloth bear woman:sloth bear women:sloth bear woman]
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
        [NAME:sloth bear man:sloth bear men:sloth bear man]
        [DESCRIPTION:A person with the head and claws of a sloth bear.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:5]
        [MAXAGE:60:80]
        [CREATURE_TILE:'B']
        [COLOR:0:0:1]
        [GO_TO_TAG:USE_TISSUE_TEMPLATE:NAIL:NAIL_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:FINGER:NAIL:FRONT]
