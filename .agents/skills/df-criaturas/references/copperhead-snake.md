# Copperhead snake

> Fonte: [Copperhead snake](https://dwarffortresswiki.org/index.php/Copperhead_snake) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes copperhead snakes for their attractive scale patterns.**
- **Biome**
- **Temperate Broadleaf Forest Any Temperate Swamp**
- **Variations**
- **Copperhead snake - Copperhead snake man - Giant copperhead snake**
- **Attributes**
- **Syndrome**
- **Tamed Attributes**
- **Pet value:** 50
- **Not hunting/war trainable**
- **Size**
- **Birth:** 50 cm 3
- **Mid:** 300 cm 3
- **Max:** 500 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 10-20
- **Butchering returns ( Value multiplier ×2)**
- **Food items**
- **Raw materials**
- **Skull:** 1

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A tiny venomous snake found in the woods and swamps.*

**Copperhead snakes** are tiny, solitary, venomous creatures who inhabit temperate broadleaf forests and swamps. They can inject a poison that causes nausea and pain, and swelling of the affected area, which wears off after not too much time, though they're typically too small to successfully puncture a dwarf's skin. Like other snakes, they continuously grow through their entire lives, reaching their max size at the age of 20, though some copperheads may die of old age as soon as they reach the age of 10. Even when fully grown, however, they are among the smallest creatures in the game who aren't vermin.

Copperhead snakes can be captured in cage traps and trained into exotic pets. They are born adults and as such can't be fully tamed. They are too small to give anything but a skull when butchered and, unlike most reptiles, they give live birth instead of laying eggs, making them entirely unusable for a meat industry. A totem made out of a copperhead's skull, however, will be twice more valuable than a normal one.

Some dwarves like copperhead snakes for their *attractive scale patterns*.

|  |
|----|
| "Copperhead snake" in other / Languages / Dwarven / : / gusil-ser therleth / Elven / : / canò-íne imaza / Goblin / : / saxo-ostam slorust / Human / : / gugir-aru rosha |

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
All attempts by dwarf-kind to extract the copper in their heads have failed, leading some to believe that copperhead snakes do not contain any copper at all.

Admired for its *attractive scale patterns*.

    1 kph

    Copperhead snakes were sponsored by the generous contributions of the Bay 12 community.

        For Joalton. Because it had to be snakes.

    [CREATURE:COPPERHEAD_SNAKE]
        [DESCRIPTION:A tiny venomous snake found in the woods and swamps.]
        [NAME:copperhead snake:copperhead snakes:copperhead snake]
        [CASTE_NAME:copperhead snake:copperhead snakes:copperhead snake]
        [CREATURE_TILE:'s'][COLOR:6:0:0]
        [CREATURE_CLASS:POISONOUS]
        [PETVALUE:50]
        [PET_EXOTIC]
        [FREQUENCY:30]
        [NATURAL]
        [CARNIVORE]
        [LARGE_ROAMING]
        [BIOME:FOREST_TEMPERATE_BROADLEAF]
        [BIOME:ANY_TEMPERATE_SWAMP]
        [POPULATION_NUMBER:10:25]
        [CLUSTER_NUMBER:1:1]
        [PREFSTRING:attractive scale patterns]
        [BODY:BASIC_1PARTBODY:BASIC_HEAD:TAIL:2EYES:NOSE:2LUNGS:HEART:GUTS:ORGANS:SPINE:BRAIN:SKULL:MOUTH:GENERIC_TEETH_WITH_FANGS:RIBCAGE]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
            [REMOVE_MATERIAL:SKIN]
            [REMOVE_MATERIAL:LEATHER]
            [REMOVE_MATERIAL:PARCHMENT]
            [REMOVE_MATERIAL:HAIR]
            [USE_MATERIAL_TEMPLATE:SCALE:SCALE_TEMPLATE]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
            [REMOVE_TISSUE:SKIN]
            [REMOVE_TISSUE:HAIR]
            [USE_TISSUE_TEMPLATE:SCALE:SCALE_TEMPLATE]
        [BODY_DETAIL_PLAN:VERTEBRATE_TISSUE_LAYERS:SCALE:FAT:MUSCLE:BONE:CARTILAGE]
        [SELECT_TISSUE_LAYER:HEART:BY_CATEGORY:HEART]
         [PLUS_TISSUE_LAYER:SCALE:BY_CATEGORY:THROAT]
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
            [STATE_NAME:ALL_SOLID:frozen copperhead snake venom]
            [STATE_ADJ:ALL_SOLID:frozen copperhead snake venom]
            [STATE_NAME:LIQUID:copperhead snake venom]
            [STATE_ADJ:LIQUID:copperhead snake venom]
            [STATE_NAME:GAS:boiling copperhead snake venom]
            [STATE_ADJ:GAS:boiling copperhead snake venom]
            [PREFIX:NONE]
            [ENTERS_BLOOD]
            [SYNDROME]
                [SYN_NAME:copperhead snake bite]
                [SYN_AFFECTED_CLASS:GENERAL_POISON]
                [SYN_IMMUNE_CREATURE:COPPERHEAD_SNAKE:ALL]
                [SYN_INJECTED]
                [CE_PAIN:SEV:75:PROB:100:RESISTABLE:SIZE_DILUTES:LOCALIZED:VASCULAR_ONLY:START:50:PEAK:500:END:1500]
                [CE_SWELLING:SEV:10:PROB:100:RESISTABLE:SIZE_DILUTES:LOCALIZED:VASCULAR_ONLY:START:50:PEAK:500:END:1500]
                [CE_NAUSEA:SEV:75:PROB:100:RESISTABLE:SIZE_DILUTES:START:50:PEAK:500:END:1500]
        [BODY_SIZE:0:0:50]
        [BODY_SIZE:2:0:300]
        [BODY_SIZE:20:0:500]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [MAXAGE:10:20]
        [MUNDANE]
        [ATTACK:BITE:CHILD_BODYPART_GROUP:BY_CATEGORY:HEAD:BY_CATEGORY:TOOTH]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:bite:bites]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_FLAG_CANLATCH]
            [SPECIALATTACK_INJECT_EXTRACT:LOCAL_CREATURE_MAT:VENOM:LIQUID:100:100]
        [NOCTURNAL]
        [APPLY_CREATURE_VARIATION:STANDARD_WALK_CRAWL_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [SWIMS_INNATE]
        [CANNOT_JUMP]
        [CASTE:FEMALE]
            [FEMALE]
        [CASTE:MALE]
            [MALE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SCALE]
                [TL_COLOR_MODIFIER:COPPER:1] copper stripes
                    [TLCM_NOUN:scales:PLURAL]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
        [SELECT_MATERIAL:ALL]
            [MULTIPLY_VALUE:2]
