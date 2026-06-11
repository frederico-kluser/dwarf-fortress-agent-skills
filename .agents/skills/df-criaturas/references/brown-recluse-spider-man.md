# Brown recluse spider man

> Fonte: [Brown recluse spider man](https://dwarffortresswiki.org/index.php/Brown_recluse_spider_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes brown recluse spider men for their venomous bite.**
- **Biome**
- **Temperate Broadleaf Forest**
- **Variations**
- **Brown recluse spider - Brown recluse spider man - Giant brown recluse spider**
- **Attributes**
- **Alignment:** Savage
- **No Stun · No Pain · Learns · Webs · Syndrome · Humanoid**
- **Cannot be tamed**
- **Size**
- **Max:** 35,000.5 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A person with the head and arms of a brown recluse spider.*

**Brown recluse spider men** are humanoid versions of the common brown recluse spider and a species of animal people, found in savage temperate broadleaf forests. They are a little over half the size of an adult dwarf and appear in groups of 1-3 individuals. Their existence is marked by webs scattered across the surface, but the creatures themselves are uncommon to encounter.

They do not feel pain or fear, and have three pairs of arms and a moderately venomous bite that is usually deflected by clothes, but is quite effective at incapacitating animals with pain. Additionally, they cannot disturb or be caught in webs.

Like other savage animal people, brown recluse spider men may occasionally appear in your fortress as visitors, or even join civilizations, becoming full-fledged citizens.

Some dwarves like brown recluse spider men for their *venomous bite*.

### Adventure Mode

As adventurers, besides the advantages listed above, they have the advantages of no need for sleep, and their 6 arms allow them to equip up to five shields and a weapon if shield-user skill is selected at chargen. They can actually harvest webs and turn them into thread; an empty hand must be available to hold the web in order to convert it into thread.

The downsides include a non-standard and rather small body size, meaning most found armor will not be useful, and strength will be at a penalty. Additionally, brown recluse spider men are completely unable to swim or consume plant food (e.g. berries) due to being carnivorous.

Due to the way *Dwarf Fortress* names things, upon achieving superior base stats, these creatures become *superbrown* (e.g. having "superbrown recluse spider man strength").

Much smaller than pictured.

\

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
The nature of the animal person creature variation template means that they cannot, in fact, do whatever a spider can.

It is commonly assumed by uninformed dwarves that brown recluse spider men have the lower half of a spider. This is incorrect and illogical for animal people.

|  |
|----|
| "Brown recluse spider man" in other / Languages / Dwarven / : / neb orstist sethal udos / Elven / : / bideÿe éniri thepani onino / Goblin / : / urso ästspub utes ngorûg / Human / : / tasar zinga azoc abo |

    [CREATURE:BROWN_RECLUSE_SPIDER_MAN]
        [COPY_TAGS_FROM:SPIDER_BROWN_RECLUSE]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:STATE_NAME]
            [CVCT_TARGET:brown recluse spider]
            [CVCT_REPLACEMENT:brown recluse spider man]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:STATE_ADJ]
            [CVCT_TARGET:brown recluse spider]
            [CVCT_REPLACEMENT:brown recluse spider man]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:SYN_NAME]
            [CVCT_TARGET:brown recluse spider]
            [CVCT_REPLACEMENT:brown recluse spider man]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:SYN_IMMUNE_CREATURE]
            [CVCT_TARGET:SPIDER_BROWN_RECLUSE]
            [CVCT_REPLACEMENT:BROWN_RECLUSE_SPIDER_MAN]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:brown recluse spider man:brown recluse spider men:brown recluse spider man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:brown recluse spider woman:brown recluse spider women:brown recluse spider woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:KICK_ATTACK]
        [APPLY_CREATURE_VARIATION:MOUTH_BITE_VENOM_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:brown recluse spider man:brown recluse spider men:brown recluse spider man]
        [DESCRIPTION:A person with the head and arms of a brown recluse spider.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:3]
        [MAXAGE:60:80]
        [CREATURE_TILE:'s']
        [COLOR:6:0:0]
