# Echidna

> Fonte: [Echidna](https://dwarffortresswiki.org/index.php/Echidna) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes echidnas for their spines.**
- **Biome**
- **Any Temperate Forest Temperate Shrubland Temperate Savanna Temperate Grassland Any Desert**
- **Variations**
- **Echidna - Echidna man - Giant echidna**
- **Attributes**
- **Egglaying**
- **Tamed Attributes**
- **Pet value:** 50
- **Not hunting/war trainable**
- **Size**
- **Birth:** 1 cm 3
- **Mid:** 5,000 cm 3
- **Max:** 10,000 cm 3
- **Food products**
- **Eggs:** 1
- **Age**
- **Adult at:** 1
- **Max age:** 10-20
- **Butchering returns**
- **Food items**
- **Meat:** 7
- **Fat:** 7
- **Brain:** 1
- **Lungs:** 2
- **Intestines:** 1
- **Liver:** 0-1
- **Tripe:** 0-1
- **Raw materials**
- **Bones:** 4
- **Skull:** 1
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A small spiny mammal with a long snout. It eats ants and termites and reproduces by laying eggs.*

**Echidnas** are small solitary creatures found in most temperate biomes and deserts. They are benign meanderers, fleeing from any dwarf who attempts to confront them and generally not standing any chance against even the most inexperienced of hunters. Their bodies are covered in spines (which don't actually hurt to touch), and when threatened, they curl into a ball to defend themselves. A baby echidna is called a *puggle*, who are notably born as tiny as ants.

Echidnas can be captured in cage traps and trained into exotic pets. As monotremes, they lay eggs to give birth and as such can be placed in a nest box, though they only lay a single egg at a time. In terms of butchering returns, they are only slightly better than cats, making them overall poor animals for a meat industry or egg production.

Some dwarves like echidnas for their *spines* and their *egg-laying*.

## Bugs

If a curled-up or retracted creature dies, and is then reanimated by a necromancer, it retains the effects of being curled-up, but can move and attack as normal. As a result, for example an undead echidna is invulnerable to destructionBug:11463. It combines well with a separate bug that allows curled-up undead to attackBug:10519.

As a result, the undead echidna may at the same time be curled-up (making it unkillable) and move/attack. The same problem also affects the echidna man, giant echidna, giant hedgehog, hedgehog man and Armadillo.

Modding the game and removing \[PREVENTS_PARENT_COLLAPSE\] from the spine body part of the affected animals will allow them to be pulped and killed while curled up. While it makes normal echidnas weaker, this is not a major problem, as echidnas are not supposed to be really hard to kill. This workaround may restore otherwise unplayable games.

It was also reported that in adventure mode "I was able to finally kill the zombie by lighting fires underneath him/around him then waiting for a long time; eventually he 'died in the heat.'"Bug:10519.

Admired for its *spines*.

    1 kph

    Echidnas were sponsored by the generous contributions of the Bay 12 community.

        Slade Newitt
        Strange guy

    [CREATURE:ECHIDNA]
        [DESCRIPTION:A small spiny mammal with a long snout.  It eats ants and termites and reproduces by laying eggs.]
        [NAME:echidna:echidnas:echidna]
        [CASTE_NAME:echidna:echidnas:echidna]
        [GENERAL_CHILD_NAME:puggle:puggles]
        [CREATURE_TILE:'e'][COLOR:6:0:0]
        [CREATURE_CLASS:MAMMAL]
        [PETVALUE:50]
        [PET_EXOTIC]
        [NATURAL]
        [BIOME:ANY_TEMPERATE_FOREST]
        [BIOME:SHRUBLAND_TEMPERATE]
        [BIOME:SAVANNA_TEMPERATE]
        [BIOME:GRASSLAND_TEMPERATE]
        [BIOME:ANY_DESERT]
        [LARGE_ROAMING]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:1:1]
        [BENIGN][MEANDERER]
        [PREFSTRING:spines]
        [PREFSTRING:egg-laying]
        [BODY:QUADRUPED_NECK:TAIL:2EYES:2EARS:NOSE:2LUNGS:HEART:GUTS:ORGANS:THROAT:NECK:SPINE:BRAIN:SKULL:4TOES_FQ_REG:5TOES_RQ_REG:MOUTH:RIBCAGE]
        [BODYGLOSS:PAW]
        [GRASSTRAMPLE:0]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
            [USE_MATERIAL_TEMPLATE:SPINE:NAIL_TEMPLATE]
                [STATE_NAME:ALL_SOLID:spine]
                [STATE_ADJ:ALL_SOLID:spine]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
            [USE_TISSUE_TEMPLATE:SPINE:SPINE_TEMPLATE]
            [SELECT_TISSUE:HAIR]
                [INSULATION:100]
        [BODY_DETAIL_PLAN:VERTEBRATE_TISSUE_LAYERS:SKIN:FAT:MUSCLE:BONE:CARTILAGE]
        [BODY_DETAIL_PLAN:LEATHERY_EGG_MATERIALS]
        [BODY_DETAIL_PLAN:BODY_HAIR_TISSUE_LAYERS:HAIR]
        [BODY_DETAIL_PLAN:BODY_SPINE_TISSUE_LAYERS:SPINE]
        [USE_MATERIAL_TEMPLATE:NAIL:NAIL_TEMPLATE]
        [USE_TISSUE_TEMPLATE:NAIL:NAIL_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:TOE:NAIL:FRONT]
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
        [BODY_SIZE:0:0:1]
        [BODY_SIZE:1:0:5000]
        [BODY_SIZE:2:0:10000]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:10:20]
        [ATTACK:SCRATCH:CHILD_TISSUE_LAYER_GROUP:BY_TYPE:STANCE:BY_CATEGORY:ALL:NAIL]
            [ATTACK_SKILL:GRASP_STRIKE]
            [ATTACK_VERB:scratch:scratches]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:MAIN]
        [RETRACT_INTO_BP:BY_CATEGORY:BODY_UPPER:roll into a ball:rolls into a ball:unroll:unrolls]
        [CHILD:1]
        [NOCTURNAL]
        [HOMEOTHERM:10067]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:3512:2634:1756:878:4900:6900] 10 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [SWIMS_INNATE]
        [MUNDANE]
        [CASTE:FEMALE]
            [FEMALE]
            [LAYS_EGGS]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGGSHELL:SOLID]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGG_WHITE:LIQUID]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGG_YOLK:LIQUID]
                [EGG_SIZE:1]
                [CLUTCH_SIZE:1:1]
        [CASTE:MALE]
            [MALE]
            undescended, not geldable
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:HAIR]
                [TL_COLOR_MODIFIER:TAN:1]
                    [TLCM_NOUN:hair:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
        [TL_COLOR_MODIFIER:BROWN:1:BURNT_UMBER:1:CINNAMON:1:COPPER:1:DARK_BROWN:1:DARK_PEACH:1:DARK_TAN:1:ECRU:1:PALE_BROWN:1:PALE_CHESTNUT:1:PALE_PINK:1:PEACH:1:PINK:1:RAW_UMBER:1:SEPIA:1:TAN:1:TAUPE_PALE:1:TAUPE_SANDY:1]
                    [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
