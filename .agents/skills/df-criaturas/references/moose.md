# Moose

> Fonte: [Moose](https://dwarffortresswiki.org/index.php/Moose) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes moose for their broad antlers.**
- **Biome**
- **Taiga Any Temperate Forest**
- **Variations**
- **Moose - Moose man - Giant moose**
- **Attributes**
- **Grazer · Exotic mount · Horn · Horn**
- **Tamed Attributes**
- **Pet value:** 300
- **Not hunting/war trainable**
- **Size**
- **Birth:** 31,500 cm 3
- **Mid:** 262,500 cm 3
- **Max:** 525,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 15-25
- **Butchering returns**
- **Food items**
- **Meat:** 10-12
- **Fat:** 8
- **Brain:** 1
- **Heart:** 1
- **Lungs:** 2
- **Intestines:** 1-2
- **Liver:** 1
- **Kidneys:** 2
- **Tripe:** 1
- **Sweetbread:** 1
- **Eyes:** 0-2 *
- **Spleen:** 1
- **Raw materials**
- **Bones:** 14-16 *
- **Skull:** 1
- **Hooves:** 4
- **Horns:** 0-2 *
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A large mammal with great antlers and a large nose. It lives in temperate forests.*

**Moose** are large herbivorous animals who inhabit taigas and temperate forests, where they spawn one at a time. They are benign meanderers and generally avoid confrontation, and as such a dwarf hunter will typically emerge victorious when trying to hunt them. Moose possess significant sexual dimorphism, with males being over 1.5× larger than females and having access to a gore attack. Male moose are called *bull moose*, while females are *cow moose* and their newborns are *moose calves*.

Moose can be captured in cage traps and trained into fairly valuable exotic pets. Given their large size, they make prime targets for a meat industry and a good choice for a breeding program. The returns shown to the right are those of a male moose - a female will give less due to being smaller. Trained moose are grazers and therefore must be kept in a pasture in order to keep them fed and alive. Moose are exotic mounts, and may be seen being ridden by humans during sieges.

Some dwarves like moose for their *broad antlers* and their *large size*.

Admired for its *broad antlers*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\

The **Moose** is capable of bringing down the toughest adventurers and soldiers, with hooves that cave in skulls with frightening ease. This creature has been dubbed the Scourge of Canada by survivors of such horrific encounters.

Moose have also been known to bite female dwarves attempting to carve their initials into their flanks. Nó realli! She was Karving her initials on the mòòse with a sharpened stick given to her bÿ Betha, her brother-in-law, an Elven Stick Grower and star of manÿ Elven plaÿs, *The Hot Hands of an Elven Stick Grower*, *Shoots of Passion*, *The Huge Sprouts of Ave Forestnettle*.

We apologise for the fault in the D for Dwarf. Those responsible have been sacked. Mÿnd you, mòòse bites Kan be prettÿ nasti...

    5 kph

    Moose were sponsored by the generous contributions of the Bay 12 community.

        Silophant - "one of these once bit my sister"
        "Beware the room with a moose."
        A m°°se once bit my sister. / Mynd you, m°°se bites kan be pretty nasti...

    [CREATURE:MOOSE]
        [DESCRIPTION:A large mammal with great antlers and a large nose. It lives in temperate forests.]
        [NAME:moose:moose:moose]
        [CHILD:1][GENERAL_CHILD_NAME:moose calf:moose calves]
        [CREATURE_TILE:'M'][COLOR:6:0:0]
        [CREATURE_CLASS:MAMMAL]
        [PETVALUE:300]
        [PREFSTRING:large size]
        [PREFSTRING:broad antlers]
        [GRASSTRAMPLE:0]
        [LARGE_ROAMING]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:1:1]
        [BIOME:FOREST_TAIGA]
        [BIOME:ANY_TEMPERATE_FOREST]
        [BENIGN][MEANDERER][NATURAL][PET_EXOTIC][MOUNT_EXOTIC]
        [MAXAGE:15:25]
        [DIURNAL]
        [HOMEOTHERM:10067]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:471:314:157:1900:2900] 56 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [SWIMS_INNATE]
        [MUNDANE]
        [CASTE:FEMALE]
            [FEMALE]
            [CASTE_NAME:cow moose:cow moose:cow moose]
            [MULTIPLE_LITTER_RARE]
            [BODY:QUADRUPED_NECK_HOOF:TAIL:2EYES:2EARS:NOSE:2LUNGS:HEART:GUTS:ORGANS:THROAT:NECK:SPINE:BRAIN:SKULL:MOUTH:TONGUE:GENERIC_TEETH:RIBCAGE]
            [STANDARD_GRAZER]
            [BODY_SIZE:0:0:31500]
            [BODY_SIZE:1:0:157500]
            [BODY_SIZE:2:0:315000]
        [CASTE:MALE]
            [MALE]
            [CASTE_NAME:bull moose:bull moose:bull moose]
            [BODY:QUADRUPED_NECK_HOOF:TAIL:2EYES:2EARS:NOSE:2LUNGS:HEART:GUTS:ORGANS:THROAT:NECK:SPINE:BRAIN:SKULL:MOUTH:TONGUE:GENERIC_TEETH:RIBCAGE:2HEAD_ANTLER]
            [SET_BP_GROUP:BY_TYPE:LOWERBODY][BP_ADD_TYPE:GELDABLE]
            [ATTACK:HGORE:BODYPART:BY_CATEGORY:HORN]
                [ATTACK_SKILL:BITE]
                [ATTACK_VERB:gore:gores]
                [ATTACK_CONTACT_PERC:100]
                [ATTACK_PREPARE_AND_RECOVER:3:3]
                [ATTACK_FLAG_WITH]
                [ATTACK_PRIORITY:MAIN]
            [STANDARD_GRAZER]
            [BODY_SIZE:0:0:31500]
            [BODY_SIZE:1:0:262500]
            [BODY_SIZE:2:0:525000]
        [SELECT_CASTE:ALL]
            [ATTACK:KICK:BODYPART:BY_CATEGORY:HOOF_FRONT]
                [ATTACK_SKILL:STANCE_STRIKE]
                [ATTACK_VERB:kick:kicks]
                [ATTACK_CONTACT_PERC:100]
                [ATTACK_PREPARE_AND_RECOVER:4:4]
                [ATTACK_PRIORITY:MAIN]
                [ATTACK_FLAG_WITH]
                [ATTACK_FLAG_BAD_MULTIATTACK]
            [ATTACK:KICK:BODYPART:BY_CATEGORY:HOOF_REAR]
                [ATTACK_SKILL:STANCE_STRIKE]
                [ATTACK_VERB:kick:kicks]
                [ATTACK_CONTACT_PERC:100]
                [ATTACK_PREPARE_AND_RECOVER:4:4]
                [ATTACK_PRIORITY:MAIN]
                [ATTACK_FLAG_WITH]
                [ATTACK_FLAG_BAD_MULTIATTACK]
            [ATTACK:BITE:CHILD_BODYPART_GROUP:BY_CATEGORY:HEAD:BY_CATEGORY:TOOTH]
                [ATTACK_SKILL:BITE]
                [ATTACK_VERB:bite:bites]
                [ATTACK_CONTACT_PERC:100]
                [ATTACK_PENETRATION_PERC:100]
                [ATTACK_FLAG_EDGE]
                [ATTACK_PREPARE_AND_RECOVER:3:3]
                [ATTACK_PRIORITY:SECOND]
                [ATTACK_FLAG_CANLATCH]
            [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
                [USE_MATERIAL_TEMPLATE:HOOF:HOOF_TEMPLATE]
                [USE_MATERIAL_TEMPLATE:HORN:HORN_TEMPLATE]
                    [STATE_NAME:ALL_SOLID:antler]
                    [STATE_ADJ:ALL_SOLID:antler]
                    [ANTLER]
            [BODY_DETAIL_PLAN:STANDARD_TISSUES]
                [USE_TISSUE_TEMPLATE:HOOF:HOOF_TEMPLATE]
                [USE_TISSUE_TEMPLATE:HORN:HORN_TEMPLATE]
                    [TISSUE_NAME:antler:NP]
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
            [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
            [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
            [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
            [SET_TL_GROUP:BY_CATEGORY:ALL:HAIR]
                [TL_COLOR_MODIFIER:BROWN:1]
                    [TLCM_NOUN:hair:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
        [TL_COLOR_MODIFIER:BROWN:1:BURNT_UMBER:1:CINNAMON:1:COPPER:1:DARK_BROWN:1:DARK_PEACH:1:DARK_TAN:1:ECRU:1:PALE_BROWN:1:PALE_CHESTNUT:1:PALE_PINK:1:PEACH:1:PINK:1:RAW_UMBER:1:SEPIA:1:TAN:1:TAUPE_PALE:1:TAUPE_SANDY:1]
                    [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:IRIS_EYE_BROWN:1]
                    [TLCM_NOUN:eyes:PLURAL]
