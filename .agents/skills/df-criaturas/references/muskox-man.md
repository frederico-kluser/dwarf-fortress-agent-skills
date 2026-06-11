# Muskox man

> Fonte: [Muskox man](https://dwarffortresswiki.org/index.php/Muskox_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes muskox men for their strength.**
- **Biome**
- **Tundra Temperate Grassland**
- **Variations**
- **Muskox - Muskox man - Giant muskox**
- **Attributes**
- **Alignment:** Savage
- **Learns · Grazer · Horn · Horn · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 18,684.210526316 cm 3
- **Mid:** 74,736.842105263 cm 3
- **Max:** 177,500 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 60-80
- **Cannot be butchered ( Value multiplier ×2)**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A horned person with the head of a muskox.*

**Muskox men** are animal people versions of the common muskox, inhabiting savage tundras and temperate grasslands. They spawn in groups of 1-5 individuals and are generally content to keep to themselves, but will fight back if provoked. In terms of size, they are almost three times the size of the average dwarf.

Like other savage animal people, they can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves like muskox men for their *strength*.

For some reason, winters don't bother them.

    >[CREATURE:MUSKOX_MAN]
        [COPY_TAGS_FROM:MUSKOX]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:muskox man:muskox men:muskox man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:muskox woman:muskox women:muskox woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:HOOF_ATTACK]
        [APPLY_CREATURE_VARIATION:TOOTH_BITE_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:muskox man:muskox men:muskox man]
        [DESCRIPTION:A horned person with the head of a muskox.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:5]
        [MAXAGE:60:80]
        [CREATURE_TILE:'M']
        [COLOR:6:0:0]
