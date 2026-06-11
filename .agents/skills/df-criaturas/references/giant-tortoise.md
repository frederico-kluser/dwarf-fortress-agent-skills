# Giant tortoise

> Fonte: [Giant tortoise](https://dwarffortresswiki.org/index.php/Giant_tortoise) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant tortoises for their great size.**
- **Biome**
- **Tropical Shrubland Tropical Savanna**
- **Variations**
- **Giant tortoise - Giant tortoise man - Gigantic tortoise**
- **Attributes**
- **Shell · Egglaying**
- **Tamed Attributes**
- **Pet value:** 50
- **Not hunting/war trainable**
- **Size**
- **Birth:** 80 cm 3
- **Mid:** 150,000 cm 3
- **Max:** 300,000 cm 3
- **Food products**
- **Eggs:** 5-10
- **Age**
- **Adult at:** 1
- **Max age:** 100-200
- **Butchering returns**
- **Food items**
- **Meat:** 15
- **Fat:** 13
- **Brain:** 1
- **Heart:** 1
- **Lungs:** 2
- **Intestines:** 1
- **Liver:** 1
- **Kidneys:** 2
- **Tripe:** 1
- **Sweetbread:** 1
- **Spleen:** 1
- **Raw materials**
- **Bones:** 19
- **Skull:** 1
- **Shell:** 1
- **Skin:** Scales

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A medium-sized reptile with a large shell. It can retreat into its shell to escape predators.*

**Giant tortoises** are animals who live in tropical savannas and shrublands. They appear in groups of 5-10 in tropical areas, and can live up to 200 years. When fully grown, male giant tortoises are roughly as large as a common donkey, and twice the size of female giant tortoises. All giant tortoises are equally slow, moving at less than a third of the default speed.

Tortoises are extremely benign, and will nearly always react to threats by retracting into their shells, rather than fighting. Because of this, they nearly never frighten worker dwarves, and since they do not move when in their shell, you can freely build a cage trap directly underneath a tortoise in their shell. They will remain in their shell if tamed this way, which may pose a problem when it is time to train them in a zone. When retracted into their shells, they are impervious to unarmed attacks (from dwarves who are not Mighty) and also wooden bolts, making them excellent training dummies for the Observer skill and Archery.

Giant tortoises can be trained and kept as low-value pets, farmed for eggs, or bred for a meat industry. With 5-10 eggs in a clutch, they are poor for egg production, but for the meat industry, they are born in larger numbers than most larger creatures. They produce a moderate amount of meat without tying up your pastureland, and their shells can prove valuable for fulfilling strange mood requests. With their long lifespan, you can keep them around even when retiring a fortress for decades. Note, however, that giant tortoises require five years to reach full adult size.

Interestingly, only males seem to produce nose cartilage when butchered (which currently has no real use, and there are far better ways to determine gender). The "giant" is part of the creature's real name, with their savage counterparts being known as gigantic tortoises instead.

Some dwarves like giant tortoises for their *great size*.

Admired for its *great size*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Strangely, many humans mistake giant tortoises for dogs, and will often make sure to etch their observation into the ground.

    1 kph

    Giant tortoises were sponsored by the generous contributions of the Bay 12 community.

        Zai
        AlarionZakath
        Ves - They were so edible.

    [CREATURE:GIANT TORTOISE]
        [DESCRIPTION:A medium-sized reptile with a large shell.  It can retreat into its shell to escape predators.]
        [NAME:giant tortoise:giant tortoises:giant tortoise]
        [CASTE_NAME:giant tortoise:giant tortoises:giant tortoise]
        [CHILD:1][GENERAL_CHILD_NAME:giant tortoise hatchling:giant tortoise hatchlings]
        [CREATURE_TILE:'T'][COLOR:6:0:0]
        [PETVALUE:50]
        [BENIGN][NATURAL][PET_EXOTIC]
        [BIOME:SHRUBLAND_TROPICAL]
        [BIOME:SAVANNA_TROPICAL]
        [LARGE_ROAMING]
        [POPULATION_NUMBER:10:30]
        [CLUSTER_NUMBER:5:10]
        [PREFSTRING:great size]
        [BODY:QUADRUPED_NECK:TAIL:2EYES:NOSE:2LUNGS:HEART:GUTS:ORGANS:THROAT:NECK:SPINE:BRAIN:SKULL:MOUTH:TONGUE:RIBCAGE:SHELL]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
            [REMOVE_MATERIAL:SKIN]
            [REMOVE_MATERIAL:LEATHER]
            [REMOVE_MATERIAL:PARCHMENT]
            [REMOVE_MATERIAL:HAIR]
            [USE_MATERIAL_TEMPLATE:SCALE:SCALE_TEMPLATE]
            [USE_MATERIAL_TEMPLATE:SHELL:SHELL_TEMPLATE]
                [STATE_COLOR:ALL:ECRU]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
            [REMOVE_TISSUE:SKIN]
            [REMOVE_TISSUE:HAIR]
            [USE_TISSUE_TEMPLATE:SCALE:SCALE_TEMPLATE]
            [USE_TISSUE_TEMPLATE:SHELL:SHELL_TEMPLATE]
        [BODY_DETAIL_PLAN:VERTEBRATE_TISSUE_LAYERS:SCALE:FAT:MUSCLE:BONE:CARTILAGE]
        [BODY_DETAIL_PLAN:LEATHERY_EGG_MATERIALS]
        [SELECT_TISSUE_LAYER:HEART:BY_CATEGORY:HEART]
         [PLUS_TISSUE_LAYER:SCALE:BY_CATEGORY:THROAT]
            [TL_MAJOR_ARTERIES]
        [BODY_DETAIL_PLAN:STANDARD_HEAD_POSITIONS]
        [BODY_DETAIL_PLAN:SHELL_POSITIONS]
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
        [MAXAGE:100:200]
        [ATTACK:BITE:BODYPART:BY_CATEGORY:MOUTH]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:bite:bites]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_CANLATCH]
        [RETRACT_INTO_BP:BY_CATEGORY:SHELL:retract into
     shell:retracts into
     shell:come out of
     shell:comes out of
     shell]
        [DIURNAL]
        [APPLY_CREATURE_VARIATION:STANDARD_WALK_CRAWL_GAITS:4732:4026:3327:1097:5922:7567] 8 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [SWIMS_INNATE]
        [CANNOT_JUMP]
        [MUNDANE]
        [CASTE:FEMALE]
            [FEMALE]
            [BODY_SIZE:0:0:80]
            [BODY_SIZE:2:0:75000]
            [BODY_SIZE:5:0:150000]
            [LAYS_EGGS]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGGSHELL:SOLID]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGG_WHITE:LIQUID]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGG_YOLK:LIQUID]
                [EGG_SIZE:82]
                [CLUTCH_SIZE:5:10] 10-25?  large numbers not supported
        [CASTE:MALE]
            [MALE]
            [BODY_SIZE:0:0:80]
            [BODY_SIZE:2:0:150000]
            [BODY_SIZE:5:0:300000]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SCALE]
                [TL_COLOR_MODIFIER:ECRU:1]
                    [TLCM_NOUN:scales:PLURAL]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
