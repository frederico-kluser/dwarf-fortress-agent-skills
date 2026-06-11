# Penguin man

> Fonte: [Penguin man](https://dwarffortresswiki.org/index.php/Penguin_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes penguin men for their waddling gait.**
- **Biome**
- **Arctic Ocean**
- **Variations**
- **Penguin - Penguin man - Giant penguin**
- **Attributes**
- **Alignment:** Savage
- **Learns · Egglaying · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 1,110 cm 3
- **Mid:** 18,500 cm 3
- **Max:** 37,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A humanoid with the head, feet, and feathers of a penguin.*

**Penguin men** are humanoid versions of the common penguin and a species of unremarkable animal people, found in savage arctic oceans. They are only a little over half the size of an adult dwarf, and as such are unlikely to pose a threat to a civilian's life.

Like other savage animal people, penguin men may occasionally join civilizations, becoming full-fledged citizens who may appear in your fortress as visitors or be playable in adventurer mode.

Some dwarves like penguin men for their *coloration*, their *waddling gait*, and their *way of flying through the water*.

Penguin man from the game *Stellaris*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
It has been rumored that one penguin man has been seen in a tuxedo, wearing a top hat and an umbrella. Rumor has it that he lives in the sewers, with a bunch of clowns and many penguins. He is the nemesis of a certain bat man.

Penguin men tend to show an aversion to windows (gem or glass) and apples.

    [CREATURE:PENGUIN MAN]
        [COPY_TAGS_FROM:BIRD_PENGUIN]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_TAG:BODY]
        [CV_REMOVE_TAG:BODY]
        [CV_ADD_TAG:BODY:HUMANOID_NECK:2EYES:2LUNGS:HEART:GUTS:ORGANS:GIZZARD:HUMANOID_JOINTS:THROAT:NECK:SPINE:BRAIN:SKULL:4FINGERS:4TOES:BEAK:TONGUE:RIBCAGE]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:penguin man:penguin men:penguin man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:penguin woman:penguin women:penguin woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:KICK_ATTACK]
        [APPLY_CREATURE_VARIATION:TALON_SCRATCH_ATTACK]
        [APPLY_CREATURE_VARIATION:BEAK_BITE_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:750:600:439:1900:2900] 20 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:penguin man:penguin men:penguin man]
        [DESCRIPTION:A humanoid with the head, feet, and feathers of a penguin.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:5:10]
        [MAXAGE:60:80]
        [CREATURE_TILE:'p']
        [COLOR:7:0:1]
