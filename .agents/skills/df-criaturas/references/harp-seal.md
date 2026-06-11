# Harp seal

> Fonte: [Harp seal](https://dwarffortresswiki.org/index.php/Harp_seal) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes harp seals for their adorable pups.**
- **Biome**
- **Arctic Ocean**
- **Variations**
- **Harp seal - Harp seal man - Giant harp seal**
- **Attributes**
- **Amphibious**
- **Tamed Attributes**
- **Pet value:** 100
- **Not hunting/war trainable**
- **Size**
- **Birth:** 1,650 cm 3
- **Mid:** 82,500 cm 3
- **Max:** 165,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 20-30
- **Butchering returns**
- **Food items**
- **Meat:** 8-10
- **Fat:** 7
- **Brain:** 1
- **Heart:** 1
- **Lungs:** 2
- **Intestines:** 1
- **Liver:** 1
- **Kidneys:** 2
- **Tripe:** 1
- **Sweetbread:** 1
- **Eyes:** 0-2
- **Spleen:** 1
- **Raw materials**
- **Bones:** 13
- **Skull:** 1
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A small marine mammal. Its young are prized for their white fur.*

**Harp seals** are carnivorous, amphibious mammals located only in arctic oceans. They can sometimes be spotted on shore, in small packs of 3-7 individuals wandering near the coastlines. Harp seals are generally non-aggressive, though they are large, can bite, and they should not be approached by unarmored military. In quantity, they make a decent source of food, especially that they happen in packs. Harp seals, however, do not have any special value modifier, so hunting them for profit is not as profitable as in real life. A harp seal infant is called a *harp seal pup*.

Harp seals can be captured in cage traps and trained as pets, or as non-grazing livestock for a meat industry. It takes five years for a harp seal to reach its full size, significantly longer than other, more common sources of meat.

Some dwarves like harp seals for their *adorable pups*.

Admired for their *adorable pups*.

## Clubbability

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Harp seals, and especially baby harp seals, are ***very*** clubbable. It is a pity that packs of wild animals do not currently include young, just for the possibility of bashing a wild baby harp seal's skull in. Which is, by the way, a rite of passage for any self-respecting morally ambiguous overseer.

Feel free, however, to catch them wild, and toss them in a place from which they cannot escape. Once the babies are born, send in the macedwarves (no edge weapons allowed) and enjoy your genuine, morally questionable baby seal leather boots! ~~Don't~~ tell the elves.

    16 kph

    Harp seals were sponsored by the generous contributions of the Bay 12 community.

    [CREATURE:HARP_SEAL]
        [DESCRIPTION:A small marine mammal.  Its young are prized for their white fur.]
        [NAME:harp seal:harp seals:harp seal]
        [CASTE_NAME:harp seal:harp seals:harp seal]
        [CHILD:1][GENERAL_CHILD_NAME:harp seal pup:harp seal pups]
        [CREATURE_TILE:'H'][COLOR:7:0:0]
        [CREATURE_CLASS:MAMMAL]
        [PETVALUE:100]
        [PET_EXOTIC]
        [LARGE_ROAMING]
        [AMPHIBIOUS][UNDERSWIM]
        [BIOME:OCEAN_ARCTIC]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:3:7]
        [BENIGN][NATURAL]
        [PREFSTRING:adorable pups]
        [BODY:BASIC_2PARTBODY:BASIC_HEAD_NECK:FRONT_BODY_FLIPPERS:REAR_BODY_FLIPPERS:2EYES:NOSE:2LUNGS:HEART:GUTS:ORGANS:THROAT:NECK:SPINE:BRAIN:SKULL:MOUTH:GENERIC_TEETH:RIBCAGE]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
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
        [BODY_SIZE:0:0:1650]
        [BODY_SIZE:2:0:82500]
        [BODY_SIZE:5:0:165000]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:20:30]
        [ATTACK:BITE:CHILD_BODYPART_GROUP:BY_CATEGORY:HEAD:BY_CATEGORY:TOOTH]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:bite:bites]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_CANLATCH]
        [DIURNAL]
        [HOMEOTHERM:10067]
        [APPLY_CREATURE_VARIATION:STANDARD_WALK_CRAWL_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:900:703:505:274:1900:2900] 32 kph
        [SWIMS_INNATE]
        [CANNOT_JUMP]
        [MUNDANE]
        [CASTE:FEMALE]
            [FEMALE]
        [CASTE:MALE]
            [MALE]
            [SET_BP_GROUP:BY_TYPE:LOWERBODY][BP_ADD_TYPE:GELDABLE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
                [TL_COLOR_MODIFIER:GRAY:1]
                    [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:IRIS_EYE_GRAY:1]
                    [TLCM_NOUN:eyes:PLURAL]
