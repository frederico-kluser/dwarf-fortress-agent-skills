# Leech

> Fonte: [Leech](https://dwarffortresswiki.org/index.php/Leech) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes leeches for their feeding habits.**
- **Biome**
- **Any Pool Any Lake**
- **Variations**
- **Leech - Leech man - Giant leech**
- **Attributes**
- **Exotic pet · Hateable**
- **Pet value:** 10
- **Active Seasons**
- **Spring Summer Autumn Winter**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A tiny, aquatic, worm-like creature that feeds on blood.*

**Leeches** are hateable vermin who can be found in pools and lakes. They will give unhappy thoughts to dwarves who absolutely detest leeches when they encounter them. Giant leeches, on the other hand, are likely to give dwarves unhappy *deaths*. They can't be captured in animal traps.

Some dwarves like leeches for their *feeding habits*.

Admired for its *feeding habits*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Little do dwarves know that the humble leech is actually the link between elves and nobles. The missing connection is the Leech man, although leech men are closer in the DNA line to nobles than elves.

|  |
|----|
| "Leech" in other / Languages / Dwarven / : / subol / Elven / : / awathi / Goblin / : / axson / Human / : / quigos |

    12 kph

    Leeches were sponsored by the generous contributions of the Bay 12 community.

        Footkerchief struggles in vain against the grip of the Leech's mouth.
        Karlito
        Baalak Nalzar-aung

    [CREATURE:LEECH]
        [DESCRIPTION:A tiny, aquatic, worm-like creature that feeds on blood.]
        [NAME:leech:leeches:leech]
        [CASTE_NAME:leech:leeches:leech]
        [CREATURE_TILE:'~'][COLOR:0:0:1]
        [PETVALUE:10]
        [VERMIN_SOIL]
        [FREQUENCY:100][VERMIN_HATEABLE]
        [SMALL_REMAINS][VERMIN_NOTRAP][NOBONES]
        [NATURAL][PET_EXOTIC]
        [NOT_BUTCHERABLE]
        [BIOME:ANY_POOL]
        [BIOME:ANY_LAKE]
        [APPLY_CREATURE_VARIATION:STANDARD_WALK_CRAWL_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [SWIMS_INNATE]
        [POPULATION_NUMBER:250:500]
        [PREFSTRING:feeding habits]
        [BODY:BASIC_1PARTBODY:BASIC_HEAD:HEART:GUTS:BRAIN:MOUTH]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
            [REMOVE_MATERIAL:HAIR]
            [REMOVE_MATERIAL:BONE]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
            [REMOVE_TISSUE:HAIR]
            [REMOVE_TISSUE:BONE]
        [BODY_DETAIL_PLAN:EXOSKELETON_TISSUE_LAYERS:SKIN:FAT:MUSCLE]
        [ATTACK:BITE:BODYPART:BY_CATEGORY:MOUTH]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:bite:bites]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_CANLATCH]
            [SPECIALATTACK_SUCK_BLOOD:25:50]
        [HAS_NERVES]
        [MUNDANE]
        [USE_MATERIAL_TEMPLATE:ICHOR:ICHOR_TEMPLATE]
        [BLOOD:LOCAL_CREATURE_MAT:ICHOR:LIQUID]
        [CREATURE_CLASS:GENERAL_POISON]
        [GETS_WOUND_INFECTIONS]
        [GETS_INFECTIONS_FROM_ROT]
        [USE_MATERIAL_TEMPLATE:PUS:PUS_TEMPLATE]
        [PUS:LOCAL_CREATURE_MAT:PUS:LIQUID]
        [BODY_SIZE:0:0:100]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [MAXAGE:5:10]
        [ALL_ACTIVE]
        [CANNOT_JUMP]
        [NO_SLEEP]
        [NO_DIZZINESS]
        [EXTRAVISION]
        [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
            [TL_COLOR_MODIFIER:BLACK:1]
                [TLCM_NOUN:skin:SINGULAR]
