# Leopard man

> Fonte: [Leopard man](https://dwarffortresswiki.org/index.php/Leopard_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes leopard men for their spotted coats.**
- **Biome**
- **Any Tropical Badlands Rocky Wasteland Sand Desert**
- **Variations**
- **Leopard - Leopard man - Giant leopard**
- **Attributes**
- **Alignment:** Savage
- **Learns · War animals · Hunting animals · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 6,000 cm 3
- **Mid:** 30,000 cm 3
- **Max:** 60,000 cm 3
- **Age**
- **Adult at:** 3
- **Max age:** 60-80
- **Cannot be butchered ( Value multiplier ×3)**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A spotted person with the head and tail of a leopard.*

**Leopard men** are animal people variants of the common leopard who can be found in savage tropical regions and deserts. They spawn in groups of 1-5 individuals and are generally content to keep to themselves. In terms of size, they are the same weight as the average dwarf.

Like other savage animal people, they can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode. Leopard men are able to wear dwarf-sized armor and clothing, making it a good choice for adventurers of their species to start in a dwarven civilization.

Some dwarves like leopard men for their *spotted coats*.

Not as cartoony in-game. Nor friendly.\
*Art by Taski Guru*

|  |
|----|
| "Leopard man" in other / Languages / Dwarven / : / mingkil udos / Elven / : / icemì onino / Goblin / : / utol ngorûg / Human / : / upur abo |

    [CREATURE:LEOPARD_MAN]
        [COPY_TAGS_FROM:LEOPARD]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:leopard man:leopard men:leopard man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:leopard woman:leopard women:leopard woman]
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
        [NAME:leopard man:leopard men:leopard man]
        [DESCRIPTION:A spotted person with the head and tail of a leopard.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:5]
        [MAXAGE:60:80]
        [CREATURE_TILE:'l']
        [COLOR:6:0:1]
        [GO_TO_TAG:USE_TISSUE_TEMPLATE:CLAW:CLAW_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:FINGER:CLAW:FRONT]
