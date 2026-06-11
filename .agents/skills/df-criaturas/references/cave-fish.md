# Cave fish

> Fonte: [Cave fish](https://dwarffortresswiki.org/index.php/Cave_fish) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes cave fish for their beauty.**
- **Biome**
- **Underground Depth: 1-2**
- **Variations**
- **Cave fish - Cave fish man**
- **Attributes**
- **Aquatic · Fishable**
- **Active Seasons**
- **Spring Summer Autumn Winter**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A small pale creature found in underground streams and ponds.*

**Cave fish** are a type of aquatic vermin only found in underground water sources, but they can be seen year-round, and are a ready source of food when cleaned at a fishery. Cave fish can be caught in any pool of water located within an appropriate cavern layer, whether or not it's connected to the map edge.

Some dwarves like cave fish for their *beauty*.

Admired for its *beauty*.

## Bugs

- Fisherdwarves will never give up fishing in underground pools, even when there's nothing to catch. Bug:1854

|  |
|----|
| "Cave fish" in other / Languages / Dwarven / : / äs tatlosh / Elven / : / garetho thaci / Goblin / : / omo otu / Human / : / ngethac amsir |

    [CREATURE:FISH_CAVE]
        [DESCRIPTION:A small pale creature found in underground streams and ponds.]
        [NAME:cave fish:cave fish:cave fish]
        [CASTE_NAME:cave fish:cave fish:cave fish]
        [CREATURE_TILE:224][COLOR:7:0:1]
        [VERMIN_FISH][VERMIN_GROUNDER][FISHITEM][IMMOBILE_LAND][VERMIN_NOTRAP]
        [AQUATIC][SMALL_REMAINS][UNDERSWIM]
        [NATURAL]
        [NOT_BUTCHERABLE]
        [BIOME:SUBTERRANEAN_WATER]
        [UNDERGROUND_DEPTH:1:2]
        [POPULATION_NUMBER:250:500]
        [PREFSTRING:beauty]
        [BODY:BASIC_2PARTBODY:BASIC_HEAD:SIDE_FINS:DORSAL_FIN:TAIL:HEART:GUTS:ORGANS:SPINE:BRAIN:SKULL:MOUTH:RIBCAGE]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
            [REMOVE_MATERIAL:HAIR]
            [REMOVE_MATERIAL:EYE]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
            [REMOVE_TISSUE:HAIR]
            [REMOVE_TISSUE:EYE]
        [BODY_DETAIL_PLAN:VERTEBRATE_TISSUE_LAYERS:SKIN:FAT:MUSCLE:BONE:CARTILAGE]
        [SELECT_TISSUE_LAYER:HEART:BY_CATEGORY:HEART]
         [PLUS_TISSUE_LAYER:SKIN:BY_CATEGORY:THROAT]
            [TL_MAJOR_ARTERIES]
        [BODY_DETAIL_PLAN:STANDARD_HEAD_POSITIONS]
        [BODY_DETAIL_PLAN:HUMANOID_RIBCAGE_POSITIONS]
        [USE_MATERIAL_TEMPLATE:SINEW:SINEW_TEMPLATE]
        [TENDONS:LOCAL_CREATURE_MAT:SINEW:200]
        [LIGAMENTS:LOCAL_CREATURE_MAT:SINEW:200]
        [HAS_NERVES]
        [USE_MATERIAL_TEMPLATE:BLOOD:BLOOD_TEMPLATE]
        [BLOOD:LOCAL_CREATURE_MAT:BLOOD:LIQUID]
        [CREATURE_CLASS:GENERAL_POISON]
        [GETS_WOUND_INFECTIONS]
        [GETS_INFECTIONS_FROM_ROT]
        [USE_MATERIAL_TEMPLATE:PUS:PUS_TEMPLATE]
        [PUS:LOCAL_CREATURE_MAT:PUS:LIQUID]
        [BODY_SIZE:0:0:1000]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:2:3]
        [ATTACK:BITE:BODYPART:BY_CATEGORY:MOUTH]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:bite:bites]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_CANLATCH]
        [HOMEOTHERM:10040]
        [ALL_ACTIVE]
        [NO_DRINK]
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:900:750:600:439:1900:2900] 20 kph
        [SWIMS_INNATE]
        [CANNOT_JUMP]
        [MUNDANE]
        [CASTE:FEMALE]
            [FEMALE]
        [CASTE:MALE]
            [MALE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
                [TL_COLOR_MODIFIER:WHITE:1]
                    [TLCM_NOUN:skin:SINGULAR]
