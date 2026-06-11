# Hedgehog

> Fonte: [Hedgehog](https://dwarffortresswiki.org/index.php/Hedgehog) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes hedgehogs for their many spines.**
- **Biome**
- **Temperate Shrubland Temperate Savanna**
- **Variations**
- **Hedgehog - Hedgehog man - Giant hedgehog**
- **Attributes**
- **Pet**
- **Pet value:** 10
- **Active Seasons**
- **Spring Summer Autumn Winter**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A small round mammal whose back is covered in spines. It is nocturnal and feeds on insects. It curls into a ball when startled and is found in temperate regions.*

**Hedgehogs** are a type of above ground vermin found in any grassy temperate area, but not in winter. They can be captured by trappers and turned into pets. Despite the fact that they are members of Eulipotyphla, they have teeth like a rodent.

Some dwarves like hedgehogs for their *many spines*.

|  |
|----|
| "Hedgehog" in other / Languages / Dwarven / : / èfim-tarag / Elven / : / ralila-ÿara / Goblin / : / slësu-snam / Human / : / hob-celo |

Admired for its *many spines*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
There are tales of a hedgehog with blue fur and a \[speed:0\] tag running around, but no proof has been found so far. However, the rumors of some sort of "Hedgehog's dilemma" resulting in dwarves becoming melancholy have been proven false.

    12 kph

    Hedgehogs were sponsored by the generous contributions of the Bay 12 community.

        Hedgehog: Closest thing to a zefie in Vanilla DF. -Sponsored by Strife

    [CREATURE:HEDGEHOG]
        [DESCRIPTION:A small round mammal whose back is covered in spines.  It is nocturnal and feeds on insects.  It curls into a ball when startled and is found in temperate regions.]
        [NAME:hedgehog:hedgehogs:hedgehog]
        [CASTE_NAME:hedgehog:hedgehogs:hedgehog]
        [CREATURE_TILE:249][COLOR:6:0:0]
        [CREATURE_CLASS:MAMMAL]
        [PETVALUE:10]
        [FREQUENCY:100][VERMIN_GROUNDER]
        [BENIGN][SMALL_REMAINS][NATURAL][PET][NO_WINTER]
        [NOT_BUTCHERABLE]
        [BIOME:SHRUBLAND_TEMPERATE]
        [BIOME:SAVANNA_TEMPERATE]
        [POPULATION_NUMBER:250:500]
        [GOBBLE_VERMIN_CLASS:EDIBLE_GROUND_BUG]
        [VISION_ARC:50:310]
        [PREFSTRING:many spines]
        [BODY:QUADRUPED_NECK:TAIL:2EYES:2EARS:NOSE:2LUNGS:HEART:GUTS:ORGANS:THROAT:NECK:SPINE:BRAIN:SKULL:4TOES_FQ_REG:5TOES_RQ_REG:MOUTH:TONGUE:RODENT_TEETH:RIBCAGE]
        [BODYGLOSS:PAW]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
            [USE_MATERIAL_TEMPLATE:SPINE:NAIL_TEMPLATE]
                [STATE_NAME:ALL_SOLID:spine]
                [STATE_ADJ:ALL_SOLID:spine]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
            [USE_TISSUE_TEMPLATE:SPINE:SPINE_TEMPLATE]
        [BODY_DETAIL_PLAN:VERTEBRATE_TISSUE_LAYERS:SKIN:FAT:MUSCLE:BONE:CARTILAGE]
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
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:3512:2634:1756:878:4900:6900] 10 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [USE_MATERIAL_TEMPLATE:BLOOD:BLOOD_TEMPLATE]
        [BLOOD:LOCAL_CREATURE_MAT:BLOOD:LIQUID]
        [CREATURE_CLASS:GENERAL_POISON]
        [GETS_WOUND_INFECTIONS]
        [GETS_INFECTIONS_FROM_ROT]
        [USE_MATERIAL_TEMPLATE:PUS:PUS_TEMPLATE]
        [PUS:LOCAL_CREATURE_MAT:PUS:LIQUID]
        [BODY_SIZE:0:0:800]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:2:3]
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
        [RETRACT_INTO_BP:BY_CATEGORY:BODY_UPPER:roll into a ball:rolls into a ball:unroll:unrolls]
        [ROOT_AROUND:BY_CATEGORY:NOSE:root around in:roots around in]
        [NOCTURNAL]
        [HOMEOTHERM:10067]
        [SWIMS_INNATE]
        [MUNDANE]
        [CASTE:FEMALE]
            [FEMALE]
        [CASTE:MALE]
            [MALE]
            [SET_BP_GROUP:BY_TYPE:LOWERBODY][BP_ADD_TYPE:GELDABLE]
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
