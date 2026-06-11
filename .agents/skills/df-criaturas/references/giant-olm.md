# Giant olm

> Fonte: [Giant olm](https://dwarffortresswiki.org/index.php/Giant_olm) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant olms for their gills.**
- **Biome**
- **Underground Depth: 1-2**
- **Variations**
- **Olm - Olm man - Giant olm**
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
- **Meat:** 14-15
- **Fat:** 13
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
- **Bones:** 17-18
- **Skull:** 1
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A giant amphibian predator found underground near water.*

**Giant olms** are much larger cousins of the common olm who can be commonly found at the first and second layers of the caverns, where they prowl one at a time. These creatures are over three times heavier than dwarves and are one of the biggest banes of your fisherdwarves, emerging from the water and attacking anything smaller than themselves. Giant olms are aggressive and may deal great damage, if not outright kill unarmed civilians, and if they attack near the edge of the water, expect your dwarves to stupidly dodge into it and drown. They may also be seen being ridden by goblins during sieges, where they will gleefully swim over any moat you are using as a defense - whether their riders survive the trek is another story.

Giant olms are Level 1 building destroyers and will trample furniture in their path, including doors. Because they seek buildings to destroy, they can be easily lured into traps. If captured in cages, they can either be butchered for a good amount of returns or trained into valuable pets. Products made from giant olms are worth 4 times more than those made from common domestic animals. Unlike olms in real life, giant olms do not lay eggs.

Some dwarves like giant olms for their *gills*.

Not comfortable to ride on.\
*Art by Michael Brissie*

    [CREATURE:OLM_GIANT]
        [DESCRIPTION:A giant amphibian predator found underground near water.]
        [NAME:giant olm:giant olms:giant olm]
        [CASTE_NAME:giant olm:giant olms:giant olm]
        [CREATURE_TILE:'O'][COLOR:7:0:1]
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
        [PREFSTRING:gills]
        [BODY:QUADRUPED_NECK:TAIL:2EYES:NOSE:2LUNGS:HEART:GUTS:ORGANS:THROAT:NECK:SPINE:BRAIN:SKULL:MOUTH:TONGUE:RIBCAGE]
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
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2467:1880:1294:627:3700:5300] 14 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [SWIMS_INNATE]
        [CANNOT_JUMP]
        [CASTE:FEMALE]
            [FEMALE]
        [CASTE:MALE]
            [MALE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
                [TL_COLOR_MODIFIER:WHITE:1]
                    [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
        [SELECT_MATERIAL:ALL]
            [MULTIPLY_VALUE:4]
