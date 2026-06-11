# Polar bear

> Fonte: [Polar bear](https://dwarffortresswiki.org/index.php/Polar_bear) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes polar bears for their strength.**
- **Biome**
- **Glacier Tundra**
- **Variations**
- **Polar bear - Polar bear man - Giant polar bear**
- **Attributes**
- **Steals food · Steals drink · War animals · Hunting animals · Exotic mount**
- **Tamed Attributes**
- **Pet value:** 750
- **Trainable : Hunting War**
- **Size**
- **Birth:** 40,000 cm 3
- **Mid:** 200,000 cm 3
- **Max:** 400,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 20-30
- **Butchering returns ( Value multiplier ×3)**
- **Food items**
- **Meat:** 14-20
- **Fat:** 12-16
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
- **Bones:** 18-22
- **Skull:** 1
- **Teeth:** 2
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge predatory mammal covered in white hair. It hunts the shores along tundra and glaciers.*

**Polar bears** are large, solitary animals found in tundras and glaciers and are the only purely carnivorous bears aside from their savage variants. These predators are over 6 times the size of a dwarf (twice the size of a grizzly bear in comparison) and as such are extremely dangerous to unarmed civilians; on top of that, they're also food and alcohol thieves who are more than eager to steal from your stocks if they get the chance. While they possess a very low frequency rate, the low number of species who inhabit their biomes (especially glaciers) means you'll eventually come across them at some point. Note, however, that no more than 2-3 polar bears will exist in a single region before they're locally extinct. They possess thick fur which provides them with increased insulation compared to most other animals, which helps them survive in the cold, and their infants are called *cubs* like other species of bear.

Polar bears can be captured in cage traps and trained into valuable exotic pets. Given their thieving disposition, food stockpiles can be used as bait to lure them into traps. They can be trained into war and hunting beasts, with their large size making them the best mundane species of bear for the job. Provided you manage to get a breeding pair, polar bears also make great livestock, providing lots of returns when butchered which are worth thrice more than products coming out of more common domestic animals. They're also exotic mounts and can be theoretically used by humans during sieges, but as human settlements rarely, if ever, exist in freezing regions, their civilizations will often not have access to polar bears anyway.

Some dwarves like polar bears for their *strength*.

Admired for its *strength*.

Estimated Polar Bear Size Comparison.

    12 kph

    [CREATURE:BEAR_POLAR]
        [DESCRIPTION:A huge predatory mammal covered in white hair.  It hunts the shores along tundra and glaciers.]
        [NAME:polar bear:polar bears:polar bear]
        [CASTE_NAME:polar bear:polar bears:polar bear]
        [GENERAL_CHILD_NAME:polar bear cub:polar bear cubs]
        [CREATURE_TILE:'B'][COLOR:7:0:1]
        [CREATURE_CLASS:MAMMAL]
        [NATURAL]
        [PETVALUE:750]
        [LARGE_ROAMING]
        [PET_EXOTIC]
        [MOUNT_EXOTIC]
        [TRAINABLE]
        [POPULATION_NUMBER:2:3]
        [CLUSTER_NUMBER:1:1]
        [LARGE_PREDATOR]
        [FREQUENCY:2]
        [CURIOUSBEAST_EATER]
        [CURIOUSBEAST_GUZZLER]
        [MEANDERER]
        [BIOME:GLACIER]
        [BIOME:TUNDRA]
        [GRASSTRAMPLE:0]
        [BONECARN]
        [PREFSTRING:strength]
        [BODY:QUADRUPED_NECK:TAIL:2EYES:2EARS:NOSE:2LUNGS:HEART:GUTS:ORGANS:THROAT:NECK:SPINE:BRAIN:SKULL:5TOES_FQ_REG:5TOES_RQ_REG:MOUTH:TONGUE:GENERIC_TEETH_WITH_LARGE_EYE_TEETH:RIBCAGE]
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
        [BODY_SIZE:0:0:40000]
        [BODY_SIZE:1:0:200000]
        [BODY_SIZE:2:0:400000]
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
        [ATTACK:SCRATCH:CHILD_TISSUE_LAYER_GROUP:BY_TYPE:STANCE:BY_CATEGORY:ALL:NAIL]
            [ATTACK_SKILL:GRASP_STRIKE]
            [ATTACK_VERB:scratch:scratches]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:SECOND]
        [CHILD:1]
        [DIURNAL]
        [HOMEOTHERM:10067]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:657:438:219:1900:2900] 40 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [SWIMS_INNATE]
        [MUNDANE]
        [CASTE:FEMALE]
            [FEMALE]
        [CASTE:MALE]
            [MALE]
            [SET_BP_GROUP:BY_TYPE:LOWERBODY][BP_ADD_TYPE:GELDABLE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:HAIR]
                [TL_COLOR_MODIFIER:WHITE:1]
                    [TLCM_NOUN:hair:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
        [TL_COLOR_MODIFIER:BROWN:1:BURNT_UMBER:1:CINNAMON:1:COPPER:1:DARK_BROWN:1:DARK_PEACH:1:DARK_TAN:1:ECRU:1:PALE_BROWN:1:PALE_CHESTNUT:1:PALE_PINK:1:PEACH:1:PINK:1:RAW_UMBER:1:SEPIA:1:TAN:1:TAUPE_PALE:1:TAUPE_SANDY:1]
                    [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
        [SELECT_MATERIAL:ALL]
            [MULTIPLY_VALUE:3]
