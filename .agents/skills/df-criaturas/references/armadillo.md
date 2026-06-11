# Armadillo

> Fonte: [Armadillo](https://dwarffortresswiki.org/index.php/Armadillo) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes armadillos for their thick, bony armor plates.**
- **Biome**
- **Tropical Savanna Tropical Grassland Tropical Shrubland Any Tropical Forest**
- **Variations**
- **Armadillo - Armadillo man - Giant armadillo**
- **Attributes**
- **Shell**
- **Tamed Attributes**
- **Pet value:** 20
- **Not hunting/war trainable**
- **Size**
- **Birth:** 750 cm 3
- **Mid:** 3,750 cm 3
- **Max:** 7,500 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 10-15
- **Butchering returns**
- **Food items**
- **Meat:** 7
- **Fat:** 7
- **Intestines:** 1
- **Raw materials**
- **Bones:** 4
- **Skull:** 1
- **Shell:** 1
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A small mammal with a leathery hide. It can roll into a ball to escape predators.*

**Armadillos** are small, solitary animals who inhabit most tropical biomes. A bit larger than your average cat, they're benign meanderers who do little but wander around aimlessly. When threatened, an armadillo can and will curl up into a ball; in this state, they will neither move nor attack, making them similar to a giant tortoise that has retracted into its shell. Male armadillos are called *boars*, while females are *sows* and infants are *pups*.

Armadillos can be captured in cage traps and trained into low-value exotic pets. They don't provide much food or bones when butchered due to their fairly small size, but do provide you with a shell that can be used by your bone carvers.

Some dwarves like armadillos for their *thick, bony armor plates*.

Admired for its *thick, bony armor plates.*

    1 kph, NO DATA

    Armadillos were sponsored by the generous contributions of the Bay 12 community.

        Andrew Quatch Kasurak likes Kipling's hedge-tortoise for its spherically armoured wit
        Courtesy of caknuck
        Jeremy Diamond
        Enkufka

    [CREATURE:ARMADILLO]
        [DESCRIPTION:A small mammal with a leathery hide.  It can roll into a ball to escape predators.]
        [NAME:armadillo:armadillos:armadillo]
        [CHILD:1][GENERAL_CHILD_NAME:armadillo pup:armadillo pups]
        [CREATURE_TILE:'a'][COLOR:7:0:0]
        [CREATURE_CLASS:MAMMAL]
        [PETVALUE:20]
        [PET_EXOTIC]
        [PREFSTRING:thick, bony armor plates]
        [GRASSTRAMPLE:0]
        [VISION_ARC:50:310]
        [LARGE_ROAMING]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:1:1]
        [BIOME:SAVANNA_TROPICAL]
        [BIOME:GRASSLAND_TROPICAL]
        [BIOME:SHRUBLAND_TROPICAL]
        [BIOME:ANY_TROPICAL_FOREST]
        [BENIGN][MEANDERER][NATURAL]
        [BODY:QUADRUPED_NECK:TAIL:2EYES:2EARS:NOSE:2LUNGS:HEART:GUTS:ORGANS:THROAT:NECK:SPINE:BRAIN:SKULL:MOUTH:TONGUE:GENERIC_TEETH:RIBCAGE:SHELL]
        [BODYGLOSS:PAW]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
            [USE_MATERIAL_TEMPLATE:SHELL:SHELL_TEMPLATE]
                [STATE_COLOR:ALL:MOTTLED_GRAY_PINK]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
            [USE_TISSUE_TEMPLATE:SHELL:SHELL_TEMPLATE]
        [BODY_DETAIL_PLAN:VERTEBRATE_TISSUE_LAYERS:SKIN:FAT:MUSCLE:BONE:CARTILAGE]
        [BODY_DETAIL_PLAN:BODY_HAIR_TISSUE_LAYERS:HAIR]
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
        [BODY_SIZE:0:0:750]
        [BODY_SIZE:1:0:3750]
        [BODY_SIZE:2:0:7500]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:10:15]
        [ATTACK:BITE:CHILD_BODYPART_GROUP:BY_CATEGORY:HEAD:BY_CATEGORY:TOOTH]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:bite:bites]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_CANLATCH]
        [RETRACT_INTO_BP:BY_CATEGORY:SHELL:roll into a ball:rolls into a ball:unroll:unrolls]
        [NOCTURNAL]
        [CREPUSCULAR]
        [HOMEOTHERM:10067]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:549:366:183:1900:2900] 48 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [SWIMS_INNATE]
        [MUNDANE]
        [CASTE:FEMALE]
            [CASTE_NAME:armadillo sow:armadillo sows:armadillo sow]
            [FEMALE]
            [MULTIPLE_LITTER_RARE]
        [CASTE:MALE]
            [CASTE_NAME:armadillo boar:armadillo boars:armadillo boar]
            [MALE]
            [SET_BP_GROUP:BY_TYPE:LOWERBODY][BP_ADD_TYPE:GELDABLE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:HAIR]
                [TL_COLOR_MODIFIER:BROWN:1]
                    [TLCM_NOUN:hair:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
                [TL_COLOR_MODIFIER:MOTTLED_GRAY_PINK:1]
                    [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:IRIS_EYE_BROWN:1]
                    [TLCM_NOUN:eyes:PLURAL]
