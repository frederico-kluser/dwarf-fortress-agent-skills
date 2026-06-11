# Sea monster

> Fonte: [Sea monster](https://dwarffortresswiki.org/index.php/Sea_monster) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes sea monsters for their horrifying freakish appearance.**
- **Biome**
- **Any Ocean**
- **Attributes**
- **Alignment:** Evil
- **Aquatic · Genderless**
- **Cannot be tamed**
- **Size**
- **Max:** 8,000,000 cm 3
- **Age**
- **Adult at:** 6
- **Max age:** Immortal
- **Butchering returns ( Value multiplier ×5)**
- **Food items**
- **Meat:** 231
- **Fat:** 19-24
- **Brain:** 8-11
- **Heart:** 4-5
- **Lungs:** 16-22
- **Intestines:** 26-31
- **Liver:** 8-11
- **Kidneys:** 8-10
- **Tripe:** 8-11
- **Sweetbread:** 4-5
- **Eyes:** 6
- **Spleen:** 4-5
- **Raw materials**
- **Bones:** 23-32
- **Skin:** Scales

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A giant creature with many eyes and arms to terrify the sea.*

**Sea monsters** are huge, sea dwelling creatures found in evil oceans. They can weigh up to 8 tons and come armed with six tentacles, two pincers and powerful jaws. When butchered, they produce enormous amounts of food, enough to feed a fortress for a year or more. Their butchering returns are also worth five times the standard value.

Though tough, sea monsters are immobile on land. A fishing chamber can air-drown them, making slaughter and recovery significantly easier. An exception occurs in reanimating biomes, as undead marine creatures can freely move out of water, and into your fortress. Sea monsters possess a pet value of 1,000, but lack the necessary tokens to be trainable.

Some dwarves like sea monsters for their *horrifying freakish appearance*.

One interpretation of a sea monster, out of many.

Another interpretation of a sea monster.

|  |
|----|
| "Sea monster" in other / Languages / Dwarven / : / allas ushang / Elven / : / lene nane / Goblin / : / ozob olngö / Human / : / iño slodi |

    [CREATURE:SEA_MONSTER]
        [DESCRIPTION:A giant creature with many eyes and arms to terrify the sea.]
        [NAME:sea monster:sea monsters:sea monster]
        [CASTE_NAME:sea monster:sea monsters:sea monster]
        [CREATURE_TILE:'M'][COLOR:0:0:1]
        [PETVALUE:1000]
        [AQUATIC][IMMOBILE_LAND]
        [POPULATION_NUMBER:1:1]
        [LARGE_ROAMING]
        [BIOME:ANY_OCEAN]
        [NO_DRINK]
        [LARGE_PREDATOR][EVIL]
        [BONECARN]
        [PREFSTRING:horrifying freakish appearance]
        [CHILD:6][CHILDNAME:sea monster hatchling:sea monster hatchlings]
        [BODY:BASIC_2PARTBODY:BASIC_HEAD:UPPERBODY_PINCERS:REAR_BODY_FLIPPERS:TAIL:SIX_TENTACLES:2EYESTALKS:4EYES:2LUNGS:HEART:GUTS:ORGANS:SPINE:BRAIN:MOUTH]
        [BODYGLOSS:MAW]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
            [REMOVE_MATERIAL:SKIN]
            [REMOVE_MATERIAL:LEATHER]
            [REMOVE_MATERIAL:PARCHMENT]
            [REMOVE_MATERIAL:HAIR]
            [USE_MATERIAL_TEMPLATE:SCALE:SCALE_TEMPLATE]
            [USE_MATERIAL_TEMPLATE:NAIL:NAIL_TEMPLATE]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
            [REMOVE_TISSUE:SKIN]
            [REMOVE_TISSUE:HAIR]
            [USE_TISSUE_TEMPLATE:SCALE:SCALE_TEMPLATE]
            [USE_TISSUE_TEMPLATE:NAIL:NAIL_TEMPLATE]
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
        [BODY_SIZE:0:0:8000000]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [ATTACK:BITE:BODYPART:BY_CATEGORY:MOUTH]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:bite:bites]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_CANLATCH]
        [ATTACK:SLAP:BODYPART:BY_CATEGORY:PINCER]
            [ATTACK_SKILL:GRASP_STRIKE]
            [ATTACK_VERB:snatch:snatches]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_CANLATCH]
        [ALL_ACTIVE]
        [HOMEOTHERM:10067]
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:3512:2634:1756:878:4900:6900] 10 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [NATURAL_SKILL:CLIMBING:15]
        [SWIMS_INNATE]
        [CANNOT_JUMP]
        [SET_TL_GROUP:BY_CATEGORY:ALL:SCALE]
            [TL_COLOR_MODIFIER:BLACK:1]
                [TLCM_NOUN:scales:PLURAL]
        [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
            [TL_COLOR_MODIFIER:GREEN:1]
                [TLCM_NOUN:eyes:PLURAL]
        [SELECT_MATERIAL:ALL]
            [MULTIPLY_VALUE:5]
