# Orca

> Fonte: [Orca](https://dwarffortresswiki.org/index.php/Orca) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes orcas for their great jumps.**
- **Biome**
- **Any Ocean**
- **Variations**
- **Orca - Orca man - Giant orca**
- **Attributes**
- **Aquatic · Beaching**
- **Cannot be tamed**
- **Size**
- **Birth:** 180,000 cm 3
- **Mid:** 2,500,000 cm 3
- **Max:** 5,000,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 50-90
- **Butchering returns**
- **Food items**
- **Meat:** 148-223
- **Fat:** 28-34
- **Brain:** 12-14
- **Heart:** 6-7
- **Lungs:** 24-26
- **Intestines:** 38-39
- **Liver:** 12-14
- **Kidneys:** 14
- **Tripe:** 12-13
- **Sweetbread:** 7
- **Eyes:** 2
- **Spleen:** 7
- **Raw materials**
- **Bones:** 29
- **Skull:** 1
- **Teeth:** 1
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge ocean mammal. It is a vicious predator and can hunt in groups.*

**Orcas** are aquatic creatures found living in any ocean biome, appearing in groups of 3-9 individuals. They are among the largest mundane creatures in the ocean (losing only to the basking shark, whale shark and sperm whale), but are benign and will ignore dwarves even if they somehow get close to them. In the event an orca is forced to fight, it will defend itself with bites and tail slaps, which due to its massive size, can be particularly deadly. An infant orca is called an *orca calf*.

Being fully-sized creatures rather than vermin, the only way to fish orcas is to trap them on land, typically with the use of a drowning chamber, though they may occasionally beach themselves into your hands without any effort on your part. Due to their massive size, they provide a fantastic amount of returns when butchered, enough to feed a fortress for quite a while, especially when it's still growing.

Some dwarves like orcas for their *coloration* and their *great jumps* (even though in-game orcas are unable to jump at all).

Admired for their *great jumps*.

\

    1 kph

    Orcas were sponsored by the generous contributions of the Bay 12 community.

    [CREATURE:ORCA]
        [DESCRIPTION:A huge ocean mammal.  It is a vicious predator and can hunt in groups.]
        [NAME:orca:orcas:orca]
        [CASTE_NAME:orca:orcas:orca]
        [CHILD:1][GENERAL_CHILD_NAME:orca calf:orca calves]
        [CREATURE_TILE:'O'][COLOR:0:0:1]
        [CREATURE_CLASS:MAMMAL]
        [LARGE_ROAMING]
        [AQUATIC][UNDERSWIM][IMMOBILE_LAND][BEACH_FREQUENCY:10]
        [BENIGN][NATURAL]
        [PETVALUE:750]
        [BIOME:ANY_OCEAN]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:3:9]
        [PREFSTRING:coloration]
        [PREFSTRING:great jumps]
    [BODY:BASIC_2PARTBODY:BASIC_HEAD_NECK:SIDE_FLIPPERS:TAIL:2EYES:2LUNGS:HEART:GUTS:ORGANS:NECK:SPINE:BRAIN:SKULL:MOUTH:GENERIC_TEETH:RIBCAGE]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
            [REMOVE_MATERIAL:HAIR]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
            [REMOVE_TISSUE:HAIR]
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
        [BODY_SIZE:0:0:180000]
        [BODY_SIZE:4:0:2500000]
        [BODY_SIZE:10:0:5000000]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:50:90]
        [ATTACK:BITE:CHILD_BODYPART_GROUP:BY_CATEGORY:HEAD:BY_CATEGORY:TOOTH]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:bite:bites]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_CANLATCH]
        [ATTACK:SLAP:BODYPART:BY_CATEGORY:TAIL]
            [ATTACK_SKILL:STANCE_STRIKE]
            [ATTACK_VERB:slap:slaps]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PREPARE_AND_RECOVER:4:4]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_WITH]
            [ATTACK_FLAG_BAD_MULTIATTACK]
        [ALL_ACTIVE]
        [NO_DRINK]
        [HOMEOTHERM:10067]
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:900:528:352:176:1900:2900] 50 kph
        [SWIMS_INNATE]
        [CANNOT_JUMP]
        [MUNDANE]
        [CASTE:FEMALE]
            [FEMALE]
        [CASTE:MALE]
            [MALE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
                [TL_COLOR_MODIFIER:MOTTLED_BLACK_WHITE:1] should break up by part
                    [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
