# Wolf

> Fonte: [Wolf](https://dwarffortresswiki.org/index.php/Wolf) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes wolves for their cunning.**
- **Biome**
- **Tundra Taiga Any Temperate Forest Temperate Shrubland**
- **Variations**
- **Wolf - Wolf man - Giant wolf**
- **Tamed Attributes**
- **Pet value:** 50
- **Not hunting/war trainable**
- **Size**
- **Birth:** 4,000 cm 3
- **Mid:** 20,000 cm 3
- **Max:** 40,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 10-20
- **Butchering returns ( Value multiplier ×2)**
- **Food items**
- **Meat:** 12-13
- **Fat:** 12-13
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
- **Bones:** 11-12
- **Skull:** 1
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A large canine found in temperate regions. It is territorial and hunts in packs.*

**Wolves** are wild animals found in some temperate biomes, as well as taigas and tundras, where they spawn in packs of 3-7 individuals. Larger than dogs but smaller than dwarves, these carnivorous hunters will attack your livestock as well as your civilians, potentially mauling them to death if they're unarmed. With a very low frequency rate, you may not encounter them often in areas where lots of species live (such as temperate forests), but expect to see a lot more of them if you embark in an area with a low number of species such as a tundra. They possess thick fur which provides them with increased insulation compared to most other animals, and their newborns are referred to as *pups*.

Wolves can be captured in cage traps and trained into exotic pets. They might serve as a substitute to dogs if there are none available, but unlike them, wolves can't be trained for war or hunting. If you butcher them for food, products made from their parts are worth twice as much as those made from more common animal parts.

Some dwarves like wolves for their *cunning*.

## Adventurer Mode

In adventurer mode, wolves are one of the most common enemies encountered when traveling around the world map, along with other large predators such as dingoes. Wolves can ambush the player from the fast travel map. The announcement "Wolves!" will appear on the screen and a pack of them will spawn a short distance away, though they have been known to spawn encircling the player.

However, being equipped with metal armor should make the fight much easier, as teeth can't penetrate steel very easily.

If possible, isolating a single wolf and defeating each one at a time may yield more success than taking on the pack at once. Another school of thought suggests that maiming all of them (by breaking bones in their legs, or piercing vital organs) may be preferable to focusing on one at a time, since this will slow their onslaught. Edged weapons are superior for stopping wolf packs, as they will often hack off a leg, making the crippled wolf much less of a threat.

\

Admired for its *cunning*.

    12 kph

    [CREATURE:WOLF]
        [DESCRIPTION:A large canine found in temperate regions.  It is territorial and hunts in packs.]
        [NAME:wolf:wolves:wolf]
        [CASTE_NAME:wolf:wolves:wolf]
        [CHILD:1][GENERAL_CHILD_NAME:wolf pup:wolf pups]
        [CREATURE_TILE:'w'][COLOR:7:0:0]
        [CREATURE_CLASS:MAMMAL]
        [LARGE_PREDATOR][MEANDERER]
        [LARGE_ROAMING][FREQUENCY:5]
        [BIOME:TUNDRA]
        [BIOME:FOREST_TAIGA]
        [BIOME:ANY_TEMPERATE_FOREST]
        [BIOME:SHRUBLAND_TEMPERATE]
        [POPULATION_NUMBER:10:20]
        [CLUSTER_NUMBER:3:7]
        [GRASSTRAMPLE:0][NATURAL]
        [PETVALUE:50]
        [PET_EXOTIC]
        [BONECARN]
        [PREFSTRING:cunning]
        [BODY:QUADRUPED_NECK:TAIL:2EYES:2EARS:NOSE:2LUNGS:HEART:GUTS:ORGANS:THROAT:NECK:SPINE:BRAIN:SKULL:4TOES_FQ_REG:4TOES_RQ_REG:MOUTH:TONGUE:GENERIC_TEETH_WITH_LARGE_EYE_TEETH:RIBCAGE]
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
        [BODY_SIZE:0:0:4000]
        [BODY_SIZE:1:0:20000]
        [BODY_SIZE:2:0:40000]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:10:20]
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
        [DIURNAL]
        [HOMEOTHERM:10070]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:447:298:149:1900:2900] 59 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [SWIMS_INNATE]
        [MUNDANE]
        [CASTE:FEMALE]
            [FEMALE]
        [CASTE:MALE]
            [MALE]
            [SET_BP_GROUP:BY_TYPE:LOWERBODY][BP_ADD_TYPE:GELDABLE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:HAIR]
                [TL_COLOR_MODIFIER:GRAY:1]
                    [TLCM_NOUN:hair:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
        [TL_COLOR_MODIFIER:BROWN:1:BURNT_UMBER:1:CINNAMON:1:COPPER:1:DARK_BROWN:1:DARK_PEACH:1:DARK_TAN:1:ECRU:1:PALE_BROWN:1:PALE_CHESTNUT:1:PALE_PINK:1:PEACH:1:PINK:1:RAW_UMBER:1:SEPIA:1:TAN:1:TAUPE_PALE:1:TAUPE_SANDY:1]
                    [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:IRIS_EYE_ORANGE:1]
                    [TLCM_NOUN:eyes:PLURAL]
        [SELECT_MATERIAL:ALL]
            [MULTIPLY_VALUE:2]
