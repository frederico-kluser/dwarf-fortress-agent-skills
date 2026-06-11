# Wolverine

> Fonte: [Wolverine](https://dwarffortresswiki.org/index.php/Wolverine) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes wolverines for their tenacity.**
- **Biome**
- **Taiga Mountain**
- **Variations**
- **Wolverine - Wolverine man - Giant wolverine**
- **Tamed Attributes**
- **Pet value:** 25
- **Not hunting/war trainable**
- **Size**
- **Birth:** 2,000 cm 3
- **Mid:** 10,000 cm 3
- **Max:** 20,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 5-15
- **Butchering returns**
- **Food items**
- **Meat:** 7-11
- **Fat:** 7-10
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
- **Bones:** 4-11
- **Skull:** 1
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A small, muscular, weasel-like creature. It is known for its ferocity.*

**Wolverines** are small carnivorous creatures found in mountains and taigas. They are solitary, only appearing one at a time. Slightly larger than a honey badger, they behave in a similar fashion, being prone to rage and randomly going in a violent frenzy for a while, much to the dismay of any dwarf who happens to be at their vicinity when it happens. When not enraged, they are benign and will flee from other creatures instead. A newborn wolverine is called a *wolverine kit*.

Wolverines can be captured in cage traps and trained into cheap exotic pets. They provide equivalent returns to a dog when butchered, making them an emergency source of food if needed. A trained wolverine can serve as a potential distraction against intruders if it rages when they arrive, but don't expect it to survive the encounter.

Some dwarves like wolverines for their *tenacity*.

Admired for its *tenacity*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
The claws of a wolverine are made out of pure adamantine, and produce a distinctive 'snikt' sound when readied.

Be sure to use a powerful ranged weapon when dealing with many wolverines. They have been known to attack the cousins of some dwarves, causing said dwarves to retaliate. I mean... they kept trying to attack their cousins, what the heck would ***you*** do in a situation like that?!

    Wolverines were sponsored by the generous contributions of the Bay 12 community.

        Merry Christmas
        Doug Treder and sons

    [CREATURE:WOLVERINE]
        [DESCRIPTION:A small, muscular, weasel-like creature.  It is known for its ferocity.]
        [NAME:wolverine:wolverines:wolverine]
        [CASTE_NAME:wolverine:wolverines:wolverine]
        [CHILD:1][GENERAL_CHILD_NAME:wolverine kit:wolverine kits]
        [CREATURE_TILE:'w'][COLOR:6:0:0]
        [CREATURE_CLASS:MAMMAL]
        [NATURAL]
        [PETVALUE:25]
        [PET_EXOTIC]
        [LARGE_ROAMING]
        [POPULATION_NUMBER:10:20]
        [CLUSTER_NUMBER:1:1]
        [BIOME:FOREST_TAIGA]
        [BIOME:MOUNTAIN]
        [BONECARN]
        [BENIGN][PRONE_TO_RAGE:10]
        [GRASSTRAMPLE:0]
        [PREFSTRING:tenacity]
        [BODY:QUADRUPED_NECK:TAIL:2EYES:2EARS:NOSE:2LUNGS:HEART:GUTS:ORGANS:THROAT:NECK:SPINE:BRAIN:SKULL:5TOES_FQ_REG:5TOES_RQ_REG:MOUTH:GENERIC_TEETH_WITH_LARGE_EYE_TEETH:RIBCAGE]
        [BODYGLOSS:PAW]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
            [SELECT_TISSUE:HAIR]
                [INSULATION:200]
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
        [BODY_SIZE:0:0:2000]
        [BODY_SIZE:1:0:10000]
        [BODY_SIZE:2:0:20000]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:5:15]
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
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:549:366:183:1900:2900] 48 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [SWIMS_INNATE]
        [MUNDANE]
        [CASTE:FEMALE]
            [FEMALE]
        [CASTE:MALE]
            [MALE]
            [SET_BP_GROUP:BY_TYPE:LOWERBODY][BP_ADD_TYPE:GELDABLE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:BODY_UPPER:HAIR]
             [PLUS_TL_GROUP:BY_CATEGORY:BODY_LOWER:HAIR]
             [PLUS_TL_GROUP:BY_CATEGORY:HEAD:HAIR]
             [PLUS_TL_GROUP:BY_CATEGORY:TAIL:HAIR]
             [PLUS_TL_GROUP:BY_CATEGORY:EAR:HAIR]
                [TL_COLOR_MODIFIER:MOTTLED_BROWN_BLACK:1]
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
