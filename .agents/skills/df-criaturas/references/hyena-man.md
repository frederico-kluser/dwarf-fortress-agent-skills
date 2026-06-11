# Hyena man

> Fonte: [Hyena man](https://dwarffortresswiki.org/index.php/Hyena_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes hyena men for their coordinated hunting.**
- **Biome**
- **Tropical Savanna Tropical Grassland Tropical Shrubland**
- **Variations**
- **Hyena - Hyena man - Giant hyena**
- **Attributes**
- **Alignment:** Savage
- **Learns · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 6,500 cm 3
- **Mid:** 32,500 cm 3
- **Max:** 65,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 60-80
- **Cannot be butchered ( Value multiplier ×2)**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A person with the head and markings of a hyena.*

**Hyena men** are animal people variants of the common hyena, who can be found in savage tropical grasslands. They spawn in groups of 5-10 individuals and are generally content to keep to themselves, but will fight back if provoked. In terms of size, they are about as large as the average dwarf.

Like other savage animal people, they can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode. Hyena men are able to wear human-sized and dwarf-sized equipment, making them a rather good choice for adventurers.

Inversely, hyena men-sized clothes are able to fit most races in your fortress, making clothes production for every dwarf, goblin and human much easier.

Some dwarves like hyena men for their *distinctive laugh* and their *coordinated hunting*.

-

  Hyena men ("Gnolls") from DnD

    [CREATURE:HYENA_MAN]
        [COPY_TAGS_FROM:HYENA]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:hyena man:hyena men:hyena man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:hyena woman:hyena women:hyena woman]
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
        [NAME:hyena man:hyena men:hyena man]
        [DESCRIPTION:A person with the head and markings of a hyena.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:5:10]
        [MAXAGE:60:80]
        [CREATURE_TILE:'h']
        [COLOR:6:0:0]
        [GO_TO_TAG:USE_TISSUE_TEMPLATE:NAIL:NAIL_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:FINGER:NAIL:FRONT]
