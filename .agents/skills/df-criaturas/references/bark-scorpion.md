# Bark scorpion

> Fonte: [Bark scorpion](https://dwarffortresswiki.org/index.php/Bark_scorpion) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes bark scorpions for their stinging tail.**
- **Biome**
- **Any Desert Tropical Grassland Tropical Savanna Tropical Shrubland Tropical Coniferous Forest**
- **Variations**
- **Bark scorpion - Bark scorpion man - Giant bark scorpion**
- **Attributes**
- **Exotic pet · Extract · Hateable · Syndrome**
- **Pet value:** 0
- **Active Seasons**
- **Spring Summer Autumn Winter**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A tiny yellow bug. It has pincers and a stinging tail which can prove fatal.*

**Bark scorpions** are a species of hateable vermin found in deserts and a number of tropical biomes. They may sting dwarves, leading to pain but no long-term consequences. All members of the species possess Legendary skill in climbing.

Bark scorpions can be captured by trappers and turned into pets, but curiously have no pet value (making them be worth 0 dwarfbucks). An animal dissector can also make a vial of bark scorpion venom with a captured live scorpion.

Some dwarves like bark scorpions for their *pincers* and their *stinging tail*.

Admired for its *stinging tail*.

    1 kph

    Bark scorpions were sponsored by the generous contributions of the Bay 12 community.

        in fond memory of Ivan

    [CREATURE:BARK_SCORPION]
        [DESCRIPTION:A tiny yellow bug.  It has pincers and a stinging tail which can prove fatal.]
        [NAME:bark scorpion:bark scorpions:bark scorpion]
        [CASTE_NAME:bark scorpion:bark scorpions:bark scorpion]
        [CREATURE_TILE:249][COLOR:6:0:1]
        [CARNIVORE]
        [PET_EXOTIC]
        [PARALYZEIMMUNE]
        [NATURAL]
        [BIOME:ANY_DESERT]
        [BIOME:GRASSLAND_TROPICAL]
        [BIOME:SAVANNA_TROPICAL]
        [BIOME:SHRUBLAND_TROPICAL]
        [BIOME:FOREST_TROPICAL_CONIFER]
        [VERMIN_GROUNDER][VERMIN_HATEABLE]
        [POPULATION_NUMBER:250:500]
        [SMALL_REMAINS]
        [PREFSTRING:pincers]
        [PREFSTRING:stinging tail]
        [ALL_ACTIVE]
        [NO_SLEEP]
        [MUNDANE]
        [CANNOT_JUMP]
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [STANCE_CLIMBER][NATURAL_SKILL:CLIMBING:15]
        [NOT_BUTCHERABLE]
        [NOPAIN][EXTRAVISION][NOSTUN][NOFEAR]
        [NOBONES]
        [BODY:SPIDER:2EYES:HEART:GUTS:BRAIN:TAIL:TAIL_STINGER:UPPERBODY_PINCERS]
        [BODY_DETAIL_PLAN:CHITIN_MATERIALS]
        [BODY_DETAIL_PLAN:CHITIN_TISSUES]
        [USE_MATERIAL_TEMPLATE:VENOM:CREATURE_EXTRACT_TEMPLATE]
            [STATE_NAME:ALL_SOLID:frozen bark scorpion venom]
            [STATE_ADJ:ALL_SOLID:frozen bark scorpion venom]
            [STATE_NAME:LIQUID:bark scorpion venom]
            [STATE_ADJ:LIQUID:bark scorpion venom]
            [STATE_NAME:GAS:boiling bark scorpion venom]
            [STATE_ADJ:GAS:boiling bark scorpion venom]
            [PREFIX:NONE]
            [ENTERS_BLOOD]
            [SYNDROME]
                [SYN_NAME:bark scorpion sting]
                [SYN_AFFECTED_CLASS:GENERAL_POISON]
                [SYN_IMMUNE_CREATURE:BARK_SCORPION:ALL]
                [SYN_INJECTED]
                [CE_PAIN:SEV:75:PROB:100:RESISTABLE:SIZE_DILUTES:LOCALIZED:VASCULAR_ONLY:START:0:PEAK:10:END:2400]
        [EXTRACT:LOCAL_CREATURE_MAT:VENOM]
        [VERMIN_BITE:10:stung:LOCAL_CREATURE_MAT:VENOM:LIQUID]
        [BODY_DETAIL_PLAN:EXOSKELETON_TISSUE_LAYERS:CHITIN:FAT:MUSCLE]
        [BODY_DETAIL_PLAN:STANDARD_HEAD_POSITIONS]
        [USE_MATERIAL_TEMPLATE:SINEW:SINEW_TEMPLATE]
        [TENDONS:LOCAL_CREATURE_MAT:SINEW:200]
        [LIGAMENTS:LOCAL_CREATURE_MAT:SINEW:200]
        [HAS_NERVES]
        [USE_MATERIAL_TEMPLATE:ICHOR:ICHOR_TEMPLATE]
        [BLOOD:LOCAL_CREATURE_MAT:ICHOR:LIQUID]
        [CREATURE_CLASS:GENERAL_POISON]
        [GETS_WOUND_INFECTIONS]
        [GETS_INFECTIONS_FROM_ROT]
        [USE_MATERIAL_TEMPLATE:PUS:PUS_TEMPLATE]
        [PUS:LOCAL_CREATURE_MAT:PUS:LIQUID]
        [BODY_SIZE:0:0:3]
        [MAXAGE:2:10]
        [APPLY_CREATURE_VARIATION:TAIL_STING_VENOM_ATTACK]
        [APPLY_CREATURE_VARIATION:PINCER_ATTACK]
        [CASTE:FEMALE]
            [FEMALE]
        [CASTE:MALE]
            [MALE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:CHITIN]
                [TL_COLOR_MODIFIER:TAN:1]
                    [TLCM_NOUN:chitin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
