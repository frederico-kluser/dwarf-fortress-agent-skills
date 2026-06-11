# Sperm whale

> Fonte: [Sperm whale](https://dwarffortresswiki.org/index.php/Sperm_whale) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes sperm whales for their vengeful nature.**
- **Biome**
- **Any Ocean**
- **Variations**
- **Sperm whale - Sperm whale man - Giant sperm whale**
- **Attributes**
- **Aquatic · Beaching**
- **Cannot be tamed**
- **Size**
- **Birth:** 500,000 cm 3
- **Mid:** 12,500,000 cm 3
- **Max:** 25,000,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 70-80
- **Butchering returns**
- **Food items**
- **Meat:** 660-940
- **Fat:** 140-220
- **Brain:** 55-85
- **Heart:** 25-45
- **Lungs:** 110-160
- **Intestines:** 170-250
- **Liver:** 55-85
- **Kidneys:** 55-85
- **Tripe:** 55-85
- **Sweetbread:** 26-42
- **Eyes:** 2
- **Spleen:** 26-42
- **Raw materials**
- **Bones:** 160-240
- **Skull:** 1
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A giant marine mammal with a toothy jaw.*

**Sperm whales** are colossal aquatic creatures who can be found in any ocean biome, always appearing individually. They are the largest mundane creatures in the game, as massive as an adult dragon and only surpassed in total size by some savage giants. In comparison, a dwarf is 416 times smaller. An infant sperm whale is called a *sperm whale calf*.

Being fully-sized creatures rather than vermin, the only way to fish sperm whales is to trap them on land, typically with the use of a drowning chamber, though they may occasionally beach themselves to death by their own volition. The products of an average sperm whale can feed an entire fortress of dwarves (all 200 of them) for just over a year, making it an enormous boon if you manage to catch one, providing an enormous food surplus and months of work for your bone carvers. If you want to attempt this, be sure to put your butcher's workshop near the beach.

Sperm whales are rarely (1/101 chance) born with white instead of grey skin.

Some dwarves like sperm whales for their *teeth* and their *vengeful nature*.

Admired for its *teeth*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\

The reason why beached whales drown, in defiance of their mammalian nature, is not sufficiently established. It is possible that the stress of the situation causes a spontaneous and fatal swelling of the tissue surrounding the blowhole. Alternatively, they may be committing suicide, as dolphins have been observed to do, to avoid the more horrible death by dehydration, being crushed by their own weight, or drowning in the returning flood. Rumors that the whales, being very proud creatures, hold their breath in protest, and may even be talked out of their stubbornness by a legendary flatterer and animal trainer are baseless lies, however.

Estimated Sperm Whale Size Comparison.

    1 kph

    Sperm whales were sponsored by the generous contributions of the Bay 12 community.

        MUX

    [CREATURE:SPERM_WHALE]
        [DESCRIPTION:A giant marine mammal with a toothy jaw.]
        [NAME:sperm whale:sperm whales:sperm whale]
        [CASTE_NAME:sperm whale:sperm whales:sperm whale]
        [CHILD:1][GENERAL_CHILD_NAME:sperm whale calf:sperm whale calves]
        [CREATURE_TILE:'W'][COLOR:7:0:0]
        [CREATURE_CLASS:MAMMAL]
        [LARGE_ROAMING]
        [AQUATIC][UNDERSWIM][IMMOBILE_LAND][BEACH_FREQUENCY:10]
        [BENIGN][MEANDERER][NATURAL]
        [PETVALUE:1000]
        [BIOME:ANY_OCEAN]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:1:1]
        [PREFSTRING:teeth]
        [PREFSTRING:vengeful nature]
        [CARNIVORE]
        [BODY:BASIC_2PARTBODY:BASIC_HEAD_NECK:SIDE_FLIPPERS:TAIL:2EYES:2LUNGS:HEART:GUTS:ORGANS:NECK:SPINE:BRAIN:SKULL:MOUTH:GENERIC_TEETH:RIBCAGE]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
            [REMOVE_MATERIAL:HAIR]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
            [REMOVE_TISSUE:HAIR]
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
        [BODY_SIZE:0:0:500000]
        [BODY_SIZE:4:0:12500000]
        [BODY_SIZE:10:0:25000000]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:70:80]
        [ATTACK:BITE:CHILD_BODYPART_GROUP:BY_CATEGORY:HEAD:BY_CATEGORY:TOOTH]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:bite:bites]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_CANLATCH]
        [ATTACK:SLAP:BODYPART:BY_CATEGORY:TAIL]
            [ATTACK_SKILL:STANCE_STRIKE]
            [ATTACK_VERB:slap:slaps]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PREPARE_AND_RECOVER:4:4]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_WITH]
            [ATTACK_FLAG_BAD_MULTIATTACK]
        [ALL_ACTIVE]
        [NO_DRINK]
        [HOMEOTHERM:10067]
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:900:711:521:293:1900:2900] 30 kph
        [SWIMS_INNATE]
        [CANNOT_JUMP]
        [MUNDANE]
        [CASTE:FEMALE]
            [FEMALE]
        [CASTE:MALE]
            [MALE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
                [TL_COLOR_MODIFIER:GRAY:100:WHITE:1]
                    [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
