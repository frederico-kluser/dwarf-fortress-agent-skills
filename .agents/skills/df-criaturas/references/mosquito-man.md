# Mosquito man

> Fonte: [Mosquito man](https://dwarffortresswiki.org/index.php/Mosquito_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes mosquito men for their ability to feast on blood.**
- **Biome**
- **Any land except Mountain , Glacier , Tundra Any Pool**
- **Variations**
- **Mosquito - Mosquito man - Giant mosquito**
- **Attributes**
- **Alignment:** Savage
- **Flying · Learns · Humanoid**
- **Cannot be tamed**
- **Size**
- **Max:** 35,000.5 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A person with the head and wings of a mosquito.*

**Mosquito men** are humanoid versions of the common mosquito and a species of unremarkable animal people, found in most non-freezing savage biomes. They are a little over half the size of dwarves when adults and spawn in groups of 1-3 individuals. They should pose no threat unless provoked. All mosquito men possess Legendary skill in climbing.

Like other savage animal people, mosquito men may occasionally join civilizations, becoming full-fledged citizens who may appear in your fortress as visitors or be playable in adventurer mode. They have 4 arms and 2 legs, allowing an adventurer to wield four items at once, though due to their small size, most weapons will need to be multigrasped with all four hands as to not receive a to-hit penalty. They can also fly, attack while flying and hover in place. Female mosquito people also have a special bite attack that draws a fair bit of blood from the target on hit, which can lead to them acquiring a different taste for blood.

Some dwarves like mosquito men for their *high-pitched buzz* and their *ability to feast on blood*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Also known as lawyers, these parasites can quickly bleed a fortress dry with lawsuits, court fees and general bloodsucking. This makes them ideal test subjects for dwarven science.

Curiously, mosquito men will occasionally visit your fort in caravans. However, they have only been observed to offer one human doctor, two human bandits, and one human wearing a steel mask with high physical attributes. While you have to buy the doctor, there is no charge for the other three.

Contrary to popular belief, mosquito men are quite small.

    [CREATURE:MOSQUITO_MAN]
        [COPY_TAGS_FROM:MOSQUITO]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:mosquito man:mosquito men:mosquito man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:mosquito woman:mosquito women:mosquito woman]
            [APPLY_CREATURE_VARIATION:PROBOSCIS_SUCK_ATTACK]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:KICK_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_FLYING_GAITS:900:750:600:439:1900:2900] 20 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [GO_TO_START]
        [NAME:mosquito man:mosquito men:mosquito man]
        [DESCRIPTION:A person with the head and wings of a mosquito.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:3]
        [MAXAGE:60:80]
        [CREATURE_TILE:'m']
        [COLOR:0:0:1]
