# Giant cave toad

> Fonte: [Giant cave toad](https://dwarffortresswiki.org/index.php/Giant_cave_toad) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant cave toads for their strength.**
- **Biome**
- **Underground Depth: 1-2**
- **Attributes**
- **Building destroyer : Level 1**
- **Amphibious · Exotic mount**
- **Tamed Attributes**
- **Pet value:** 750
- **Not hunting/war trainable**
- **Size**
- **Birth:** 20,000 cm 3
- **Mid:** 100,000 cm 3
- **Max:** 200,000 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 60-100
- **Butchering returns ( Value multiplier ×4)**
- **Food items**
- **Meat:** 13-14
- **Fat:** 12
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
- **Bones:** 16-17
- **Skull:** 1
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*Not to be confused with regular giant toads.*

*A giant amphibian predator found underground.*

**Giant cave toads** are large creatures found in caverns, inhabiting the first and second layers. They spawn one at a time, wandering the underground all while terrorizing crundles and harassing dwarves who they encounter in their path, sometimes causing heavy damage in the process - giant cave toads are over three times larger than the average dwarf and are very aggressive, though they generally do not fare well when facing a squad of equipped military dwarves.

Giant cave toads are building destroyers and will attempt to topple furniture they come across, which can be exploited to easily lure them into traps. They may also be seen being ridden by goblins during sieges, where they will gleefully swim over any moat you are using as a defense - whether their riders survive the trek is another story.

Giant cave toads can be captured with cage traps and trained into valuable pets. If a breeding pair is obtained, they can be used for a fortress' meat industry as they produce a steady supply of meat, bones, fat and prepared organs, with their products being worth 4 times more than those of standard animals. Unlike toads in real life, giant cave toads do not lay eggs. Giant cave toads reach their full size in 2 years, and should preferably be butchered at that age for optimal product returns.

Some dwarves like giant cave toads for their *strength*.

Warning: Hopping may rattle nearby foundation. Badly.\
*Art by kruggsmash*

    [CREATURE:TOAD_GIANT_CAVE]
        [DESCRIPTION:A giant amphibian predator found underground.]
        [NAME:giant cave toad:giant cave toads:giant cave toad]
        [CASTE_NAME:giant cave toad:giant cave toads:giant cave toad]
        [CREATURE_TILE:'T'][COLOR:7:0:0]
        [PETVALUE:750]
        [PET_EXOTIC]
        [MOUNT_EXOTIC]
        [AMPHIBIOUS][UNDERSWIM]
        [LARGE_PREDATOR]
        [CARNIVORE]
        [BUILDINGDESTROYER:1]
        [NATURAL]
        [GRASSTRAMPLE:20]
        [BIOME:SUBTERRANEAN_WATER]
        [UNDERGROUND_DEPTH:1:2]
        [LARGE_ROAMING][DIFFICULTY:2]
        [POPULATION_NUMBER:10:20]
        [PREFSTRING:strength]
        [BODY:QUADRUPED_NECK:2EYES:NOSE:2LUNGS:HEART:GUTS:ORGANS:THROAT:NECK:SPINE:BRAIN:SKULL:MOUTH:TONGUE:RIBCAGE]
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
        [BODY_SIZE:0:0:20000]
        [BODY_SIZE:1:0:100000]
        [BODY_SIZE:2:0:200000]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:60:100]
        [ATTACK:BITE:BODYPART:BY_CATEGORY:MOUTH]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:bite:bites]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_CANLATCH]
        [ALL_ACTIVE]
        [HOMEOTHERM:10040]
        [LOW_LIGHT_VISION:10000]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:4732:4026:3327:1097:5922:7567] 8 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [SWIMS_INNATE]
        [CASTE:FEMALE]
            [FEMALE]
        [CASTE:MALE]
            [MALE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
                [TL_COLOR_MODIFIER:TAUPE_GRAY:1]
                    [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
        [SELECT_MATERIAL:ALL]
            [MULTIPLY_VALUE:4]
