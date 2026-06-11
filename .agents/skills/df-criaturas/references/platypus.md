# Platypus

> Fonte: [Platypus](https://dwarffortresswiki.org/index.php/Platypus) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes platypuses for their large bills.**
- **Biome**
- **Any River**
- **Variations**
- **Platypus - Platypus man - Giant platypus**
- **Attributes**
- **Amphibious · Syndrome · Egglaying**
- **Tamed Attributes**
- **Pet value:** 10
- **Not hunting/war trainable**
- **Size**
- **Birth:** 10 cm 3
- **Mid:** 1,000 cm 3
- **Max:** 2,000 cm 3
- **Food products**
- **Eggs:** 1-3
- **Age**
- **Adult at:** 1
- **Max age:** 10-20
- **Butchering returns**
- **Food items**
- **Meat:** 2
- **Fat:** 2
- **Raw materials**
- **Skull:** 1
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A small semi-aquatic, egg laying mammal with a bill, flat tail and poison spurs.*

**Platypuses** are small, amphibious and somewhat rare creatures found inhabiting rivers, where they spawn one at a time. They are benign and smaller than cats, making them typically harmless to the average dwarf. Males of the species possess venomous spurs on their legs which they can sting enemies with in their kick attacks, leading to swelling and severe pain on the victim, but their benign and timid disposition means they'll rarely, if ever, poison dwarves. A newborn platypus is called a *baby*.

Platypuses can be captured in cage traps and trained into cheap pets. Due to their tiny size, they produce few returns when butchered, and they lay fewer eggs than domestic poultry, making them subpar animals as livestock.

Some dwarves like platypuses for their *bizarre appearance*, their *venomous spurs*, their *flat tails* and their *large bills*.

Admired for its *bizarre appearance*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
The river titan Platypus has come! An enormous beaver. It has a broad duck beak and it undulates rhythmically. Its river otter-like hide is patchy. Beware its poisonous sting!

Some tamed platypuses have been observed sneaking off to missions during the day to fight evil.

    Platypuses were sponsored by the generous contributions of the Bay 12 community.

        Chaos would like to make http://lostsouls.org/ more closely resemble Dwarf Fortress :)
        James Brooker
        Kryten likes black bronze, olivine, olivine and platypuses for their venomous spurs.
        Stuntaneous deems the Platypus worthy of Dwarven .. attention
        "I want electroreceptors for my dwarves brains"
        Matthew Lord

    [CREATURE:PLATYPUS]
        [DESCRIPTION:A small semi-aquatic, egg laying mammal with a bill, flat tail and poison spurs.]
        [NAME:platypus:platypuses:platypus]
        [CASTE_NAME:platypus:platypuses:platypus]
        [CHILD:1][GENERAL_CHILD_NAME:baby platypus:baby platypuses]
        [CREATURE_TILE:'p'][COLOR:6:0:0]
        [CREATURE_CLASS:MAMMAL]
        [CREATURE_CLASS:POISONOUS]
        [PETVALUE:10]
        [PET]
        [NATURAL]
        [AMPHIBIOUS][UNDERSWIM]
        [LARGE_ROAMING]
        [FREQUENCY:10]
        [BIOME:ANY_RIVER]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:1:1]
        [BENIGN]
        [PREFSTRING:bizarre appearance]
        [PREFSTRING:venomous spurs]
        [PREFSTRING:flat tails]
        [PREFSTRING:large bills]
        [BODY:QUADRUPED_NECK:TAIL:2EYES:2EARS:NOSE:2LUNGS:HEART:GUTS:ORGANS:THROAT:NECK:SPINE:BRAIN:SKULL:BILL:RIBCAGE]
        [BODYGLOSS:PAW]
        [GRASSTRAMPLE:0]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
        [BODY_DETAIL_PLAN:VERTEBRATE_TISSUE_LAYERS:SKIN:FAT:MUSCLE:BONE:CARTILAGE]
        [BODY_DETAIL_PLAN:BODY_HAIR_TISSUE_LAYERS:HAIR]
        [BODY_DETAIL_PLAN:LEATHERY_EGG_MATERIALS]
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
        [USE_MATERIAL_TEMPLATE:VENOM:CREATURE_EXTRACT_TEMPLATE]
            [STATE_NAME:ALL_SOLID:frozen platypus venom]
            [STATE_ADJ:ALL_SOLID:frozen platypus venom]
            [STATE_NAME:LIQUID:platypus venom]
            [STATE_ADJ:LIQUID:platypus venom]
            [STATE_NAME:GAS:boiling platypus venom]
            [STATE_ADJ:GAS:boiling platypus venom]
            [PREFIX:NONE]
            [ENTERS_BLOOD]
            [SYNDROME]
                [SYN_NAME:platypus sting]
                [SYN_AFFECTED_CLASS:GENERAL_POISON]
                [SYN_IMMUNE_CREATURE:PLATYPUS:ALL]
                [SYN_INJECTED]
                [CE_PAIN:SEV:100:PROB:100:RESISTABLE:SIZE_DILUTES:LOCALIZED:VASCULAR_ONLY:START:2:PEAK:100:END:1500]
                [CE_SWELLING:SEV:25:PROB:100:RESISTABLE:SIZE_DILUTES:LOCALIZED:VASCULAR_ONLY:START:50:PEAK:500:END:1500]
        [BODY_SIZE:0:0:10]
        [BODY_SIZE:1:0:1000]
        [BODY_SIZE:2:0:2000]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:10:20]
        [ALL_ACTIVE]
        [HOMEOTHERM:10067]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:2990:2257:1525:731:4300:6100] 12 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph, NO DATA
        [SWIMS_INNATE]
        [MUNDANE]
        [CASTE:FEMALE]
            [FEMALE]
            [LAYS_EGGS]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGGSHELL:SOLID]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGG_WHITE:LIQUID]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGG_YOLK:LIQUID]
                [EGG_SIZE:11] couldn't find a precise number, but they are small
                [CLUTCH_SIZE:1:3]
            [ATTACK:BITE:BODYPART:BY_CATEGORY:BEAK]
                [ATTACK_SKILL:BITE]
                [ATTACK_VERB:bite:bites]
                [ATTACK_CONTACT_PERC:100]
                [ATTACK_PENETRATION_PERC:100]
                [ATTACK_FLAG_EDGE]
                [ATTACK_PREPARE_AND_RECOVER:3:3]
                [ATTACK_PRIORITY:MAIN]
                [ATTACK_FLAG_CANLATCH]
        [CASTE:MALE]
            [MALE]
            undescended, not geldable
            [ATTACK:KICK:BODYPART:BY_CATEGORY:FOOT_REAR]
                [ATTACK_SKILL:STANCE_STRIKE]
                [ATTACK_VERB:kick:kicks]
                [ATTACK_CONTACT_PERC:5]
                [ATTACK_PENETRATION_PERC:10]
                [ATTACK_FLAG_EDGE]
                [ATTACK_PREPARE_AND_RECOVER:4:4]
                [ATTACK_PRIORITY:MAIN]
                [ATTACK_FLAG_WITH]
                [ATTACK_FLAG_BAD_MULTIATTACK]
                [SPECIALATTACK_INJECT_EXTRACT:LOCAL_CREATURE_MAT:VENOM:LIQUID:100:100]
            [ATTACK:BITE:BODYPART:BY_CATEGORY:BEAK]
                [ATTACK_SKILL:BITE]
                [ATTACK_VERB:bite:bites]
                [ATTACK_CONTACT_PERC:100]
                [ATTACK_PENETRATION_PERC:100]
                [ATTACK_FLAG_EDGE]
                [ATTACK_PREPARE_AND_RECOVER:3:3]
                [ATTACK_PRIORITY:SECOND]
                [ATTACK_FLAG_CANLATCH]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:HAIR]
                [TL_COLOR_MODIFIER:BROWN:1]
                    [TLCM_NOUN:hair:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
        [TL_COLOR_MODIFIER:BROWN:1:BURNT_UMBER:1:CINNAMON:1:COPPER:1:DARK_BROWN:1:DARK_PEACH:1:DARK_TAN:1:ECRU:1:PALE_BROWN:1:PALE_CHESTNUT:1:PALE_PINK:1:PEACH:1:PINK:1:RAW_UMBER:1:SEPIA:1:TAN:1:TAUPE_PALE:1:TAUPE_SANDY:1]
                    [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
