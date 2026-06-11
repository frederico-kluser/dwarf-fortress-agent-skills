# Toad man

> Fonte: [Toad man](https://dwarffortresswiki.org/index.php/Toad_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes toad men for their beauty.**
- **Biome**
- **Any Lake**
- **Variations**
- **Toad - Toad man - Giant toad**
- **Attributes**
- **Alignment:** Savage
- **Amphibious · Learns · Humanoid**
- **Cannot be tamed**
- **Size**
- **Max:** 35,100 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A dark green man with the distinct head of a toad.*

**Toad men** are humanoid versions of the common toad and a species of unremarkable animal people, spawning naturally in savage lakes.

They are a bit over half the size of dwarves when adults and spawn in groups of 1-5 individuals, posing no threat to dwarves unless provoked. Like other savage animal people, toad men can occasionally join civilizations, becoming full-fledged citizens who could appear in your fortress as visitors, or historical figures, or be playable in adventurer mode.

Some dwarves like toad men for their *beauty*.

Ready to hop into action.\
*Art by Rhys Harvey*

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\

They are also known to spend their time programming obscure ASCII video games.

The absence of toad men has formed much speculation amongst civilizations. The most notable one involves a group of three intergalactic toad men who leap from planet to planet to defeat a "dark queen", whom had kidnapped all of the other toad men of the world.

Toad men have also been reported to occupy dams, and these specific toad men seem to be followed around by rain. However, this does not make them harder to slay.

Embarking dwarves and merchant caravans should beware, as toad men have been known to steal and crash unattended wagons.

|  |
|----|
| "Toad man" in other / Languages / Dwarven / : / nod udos / Elven / : / imadu onino / Goblin / : / ngusnog ngorûg / Human / : / budok abo |

    [CREATURE:TOAD_MAN]
        [COPY_TAGS_FROM:TOAD]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:toad man:toad men:toad man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:toad woman:toad women:toad woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:KICK_ATTACK]
        [APPLY_CREATURE_VARIATION:MOUTH_BITE_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:toad man:toad men:toad man]
        [DESCRIPTION:A dark green man with the distinct head of a toad.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:5]
        [MAXAGE:60:80]
        [CREATURE_TILE:'t']
        [COLOR:2:0:0]
