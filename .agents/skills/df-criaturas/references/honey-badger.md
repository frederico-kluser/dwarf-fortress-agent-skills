# Honey badger

> Fonte: [Honey badger](https://dwarffortresswiki.org/index.php/Honey_badger) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes honey badgers for their tenacity.**
- **Biome**
- **Any Tropical Forest Tropical Shrubland Tropical Savanna Tropical Grassland Any Tropical Wetland Any Desert**
- **Variations**
- **Honey badger - Honey badger man - Giant honey badger**
- **Attributes**
- **Steals food**
- **Tamed Attributes**
- **Pet value:** 25
- **Not hunting/war trainable**
- **Size**
- **Birth:** 900 cm 3
- **Mid:** 7,000 cm 3
- **Max:** 14,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 15-25
- **Butchering returns**
- **Food items**
- **Meat:** 7-12
- **Fat:** 7-12
- **Brain:** 0-1
- **Lungs:** 0-2
- **Intestines:** 1
- **Liver:** 0-1
- **Tripe:** 0-1
- **Raw materials**
- **Bones:** 4-10
- **Skull:** 1
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A small mammal known to defend itself ferociously in combat, often fighting off multiple animals many times its size.*

**Honey badgers** are small creatures found in a variety of biomes, from tropical forests to deserts. Compared to common badgers, honey badgers are nearly identical in terms of behavior; they are just as prone to rage, randomly attacking other creatures in their vicinity for no reason, including passing dwarves. They are solitary, unlike the common badger who appears in large clusters, but honey badgers possess the distinction of being food thieves. As such, make sure to keep them out of your stockpiles. They possess noticeable sexual dimorphism, with their males being significantly larger than females, though they're still smaller than normal badgers. A newborn honey badger is called a *cub*.

Honey badgers can be captured in cage traps and trained into cheap exotic pets. Being food thieves, a food stockpile surrounded by traps can be used as bait to capture them. They give equivalent returns to a normal badger when butchered, but appear much less often in comparison. An enraged honey badger can serve as a distraction against intruders, but don't expect it to survive a fight against anything bigger than itself.

Some dwarves like honey badgers for their *fearlessness* and their *tenacity*.

Admired for their *fearlessness*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\

They have a reputation among players for attacking random dwarves at the most inopportune moments, such as knocking fisherdwarves into rivers or dwarves working at high elevations off mountains, usually leading to their death from drowning or typical falling complications. Here are a few interesting facts about Honey Badgers from a renowned expert.

- "Nothing can stop the Honey Badger when it's hungry."
- "It's pretty bad ass."
- "They have no regard for any other animal whatsoever."
- "Honey Badger don't give a shit, it just takes what it wants."
- "The Honey Badgers are just crazy."

    1 kph

    [CREATURE:HONEY BADGER]
        [DESCRIPTION:A small mammal known to defend itself ferociously in combat, often fighting off multiple animals many times its size.]
        [NAME:honey badger:honey badgers:honey badger]
        [CASTE_NAME:honey badger:honey badgers:honey badger]
        [CHILD:1][GENERAL_CHILD_NAME:honey badger cub:honey badger cubs]
        [CREATURE_TILE:'b'][COLOR:7:0:1]
        [CREATURE_CLASS:MAMMAL]
        [NATURAL]
        [PETVALUE:25]
        [PET_EXOTIC]
        [LARGE_ROAMING]
        [POPULATION_NUMBER:10:20]
        [CLUSTER_NUMBER:1:1]
        [BIOME:ANY_TROPICAL_FOREST]
        [BIOME:SHRUBLAND_TROPICAL]
        [BIOME:SAVANNA_TROPICAL]
        [BIOME:GRASSLAND_TROPICAL]
        [BIOME:ANY_TROPICAL_WETLAND]
        [BIOME:ANY_DESERT]
        [BONECARN]
        [PRONE_TO_RAGE:10]
        [CURIOUSBEAST_EATER]
        [GRASSTRAMPLE:0]
        [PREFSTRING:tenacity]
        [PREFSTRING:fearlessness]
        [BODY:QUADRUPED_NECK:TAIL:2EYES:2EARS:NOSE:2LUNGS:HEART:GUTS:ORGANS:THROAT:NECK:SPINE:BRAIN:SKULL:5TOES_FQ_REG:5TOES_RQ_REG:MOUTH:TONGUE:GENERIC_TEETH_WITH_LARGE_EYE_TEETH:RIBCAGE]
        [BODYGLOSS:PAW]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
        [BODY_DETAIL_PLAN:VERTEBRATE_TISSUE_LAYERS:SKIN:FAT:MUSCLE:BONE:CARTILAGE]
        [BODY_DETAIL_PLAN:BODY_HAIR_TISSUE_LAYERS:HAIR]
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
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:15:25]
        [ATTACK:BITE:CHILD_BODYPART_GROUP:BY_CATEGORY:HEAD:BY_CATEGORY:TOOTH]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:bite:bites]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_CANLATCH]
        [ATTACK:SCRATCH:CHILD_TISSUE_LAYER_GROUP:BY_TYPE:STANCE:BY_CATEGORY:ALL:NAIL]
            [ATTACK_SKILL:GRASP_STRIKE]
            [ATTACK_VERB:scratch:scratches]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:SECOND]
        [ALL_ACTIVE]
        [HOMEOTHERM:10067]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [SWIMS_INNATE]
        [MUNDANE]
        [CASTE:FEMALE]
            [FEMALE]
            [BODY_SIZE:0:0:900]
            [BODY_SIZE:1:0:4500]
            [BODY_SIZE:2:0:9000]
        [CASTE:MALE]
            [MALE]
            [SET_BP_GROUP:BY_TYPE:LOWERBODY][BP_ADD_TYPE:GELDABLE]
            [BODY_SIZE:0:0:900]
            [BODY_SIZE:1:0:7000]
            [BODY_SIZE:2:0:14000]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:BODY_UPPER:HAIR]
             [PLUS_TL_GROUP:BY_CATEGORY:BODY_LOWER:HAIR]
             [PLUS_TL_GROUP:BY_CATEGORY:TAIL:HAIR]
             [PLUS_TL_GROUP:BY_CATEGORY:HEAD:HAIR]
             [PLUS_TL_GROUP:BY_CATEGORY:EAR:HAIR]
                [TL_COLOR_MODIFIER:WHITE:1]
                    [TLCM_NOUN:hair:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:LEG_FRONT:HAIR]
             [PLUS_TL_GROUP:BY_CATEGORY:LEG_REAR:HAIR]
             [PLUS_TL_GROUP:BY_CATEGORY:FOOT_FRONT:HAIR]
             [PLUS_TL_GROUP:BY_CATEGORY:FOOT_REAR:HAIR]
             [PLUS_TL_GROUP:BY_CATEGORY:TOE:HAIR]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:legs:PLURAL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
        [TL_COLOR_MODIFIER:BROWN:1:BURNT_UMBER:1:CINNAMON:1:COPPER:1:DARK_BROWN:1:DARK_PEACH:1:DARK_TAN:1:ECRU:1:PALE_BROWN:1:PALE_CHESTNUT:1:PALE_PINK:1:PEACH:1:PINK:1:RAW_UMBER:1:SEPIA:1:TAN:1:TAUPE_PALE:1:TAUPE_SANDY:1]
                    [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:IRIS_EYE_BROWN:1]
                    [TLCM_NOUN:eyes:PLURAL]
