# Moon snail man

> Fonte: [Moon snail man](https://dwarffortresswiki.org/index.php/Moon_snail_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes moon snail men for their predatory nature.**
- **Biome**
- **Temperate Ocean**
- **Variations**
- **Moon snail - Moon snail man - Giant moon snail**
- **Attributes**
- **Alignment:** Savage
- **Aquatic · Learns · Shell · Humanoid**
- **Cannot be tamed**
- **Size**
- **Max:** 35,100 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A colorful person with the head and shell of a moon snail.*

**Moon snail men** are animal people variants of the common moon snail, who can inhabit savage temperate oceans. They spawn in groups of 1-3 individuals and are generally content to keep to themselves, and may not encounter your fortress at all due to being purely aquatic. In terms of size, they are a little over half the weight of the average dwarf.

Like other non-amphibious, aquatic animal people, moon snail men cannot currently join civilizations or appear as visitors and they are not playable in adventurer mode.

Some dwarves like moon snail men for their *predatory nature* and their *striking coloration*.

Not a very fast runner.\
*Art by McAzar*

|  |
|----|
| "Moon snail man" in other / Languages / Dwarven / : / ïlon nasod udos / Elven / : / anaye limi onino / Goblin / : / zusla snuslû ngorûg / Human / : / oku copgur abo |

    [CREATURE:MOON_SNAIL_MAN]
        [COPY_TAGS_FROM:MOON_SNAIL]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:moon snail man:moon snail men:moon snail man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:moon snail woman:moon snail women:moon snail woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:KICK_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:moon snail man:moon snail men:moon snail man]
        [DESCRIPTION:A colorful person with the head and shell of a moon snail.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:3]
        [MAXAGE:60:80]
        [CREATURE_TILE:'s']
        [COLOR:4:0:1]
