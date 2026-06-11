# Cave crocodile

> Fonte: [Cave crocodile](https://dwarffortresswiki.org/index.php/Cave_crocodile) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes cave crocodiles for their strength.**
- **Biome**
- **Underground Depth: 1-2**
- **Attributes**
- **Building destroyer : Level 1**
- **Amphibious · Exotic mount · Egglaying**
- **Tamed Attributes**
- **Pet value:** 750
- **Not hunting/war trainable**
- **Size**
- **Birth:** 70 cm 3
- **Mid:** 300,000 cm 3
- **Max:** 600,000 cm 3
- **Food products**
- **Eggs:** 20-60
- **Age**
- **Adult at:** 3
- **Max age:** 60-100
- **Butchering returns ( Value multiplier ×4)**
- **Food items**
- **Meat:** 18-40
- **Fat:** 17-29
- **Brain:** 1
- **Heart:** 1
- **Lungs:** 2
- **Intestines:** 2
- **Liver:** 1
- **Kidneys:** 1
- **Tripe:** 1
- **Sweetbread:** 1
- **Eyes:** 2
- **Spleen:** 1
- **Raw materials**
- **Bones:** 21-33
- **Skull:** 1
- **Skin:** Scales
- **Gizzard stone:** 1

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge, predatory reptile with pale, colorless scales and red eyes. It lives in caves and ambushes its prey.*

**Cave crocodiles** are massive, subterranean, reptilian predators which can be found in the first two layers of the caverns - the bane of fisherdwarves and fledgling fortresses who breach the underground too early. The largest creatures inhabiting the first cavern level, they'll spawn individually out of the edges of the water and seek for dwarves to attack and wooden buildings to wreck - they are building destroyers and will topple furniture they come across. Cave crocodile hatchlings reach their full size in 2 years, but don't reach adulthood (for breeding purposes) until the end of their 3rd year.

Because of their size (10 times larger than a dwarf) and hostile behavior, cave crocodiles should be engaged with well-equipped military squads or traps. They can also be used as mounts by goblins during sieges, and they will gleefully swim over any water moat you are using as a defense - whether their riders survive the trek is another story.

Cave crocodiles can be captured in cages rather easily, as furniture for them to topple can be used as bait. They can be trained into valuable pets and either butchered for a great amount of returns or kept as livestock. Products made from cave crocodile parts are worth 4 times more than those of common animals. They are the best egg-layers of all subterranean creatures and one of the best in the entire game, making them the go-to animal for a fortress' egg production. Because of how prolific they can be and their many uses, a cave crocodile farm can be extremely profitable as it will give you plenty of food, bones for crafting and a force of giant reptiles to defend your fortress from intruders. Just take measures to ensure crocsplosion doesn't take down the fortress in the process.

Some dwarves like cave crocodiles for their *strength*.

-

  He's young, but already planning something...

-

  Capturing that thing was the "easy" part.\
  *Art by kruggsmash*

\

## In real life

A population of Dwarf(ironically) Crocodiles was found to live entirely in Abanda Caves. These crocodiles feed on bats and cave crickets and do not pose any danger to humans. This discovery was made in 2010, which is well after Cave Crocodiles were added to Dwarf Fortress

    [CREATURE:CROCODILE_CAVE]
        [DESCRIPTION:A huge, predatory reptile with pale, colorless scales and red eyes.  It lives in caves and ambushes its prey.]
        [NAME:cave crocodile:cave crocodiles:cave crocodile]
        [CASTE_NAME:cave crocodile:cave crocodiles:cave crocodile]
        [CHILD:3][GENERAL_CHILD_NAME:cave crocodile hatchling:cave crocodile hatchlings]
        [CREATURE_TILE:'C'][COLOR:7:0:0]
        [PETVALUE:750]
        [PET_EXOTIC]
        [MOUNT_EXOTIC]
        [AMPHIBIOUS]
        [BIOME:SUBTERRANEAN_WATER]
        [UNDERGROUND_DEPTH:1:2]
        [LARGE_ROAMING][DIFFICULTY:2]
        [POPULATION_NUMBER:10:20]
        [CARNIVORE][NATURAL]
        [LARGE_PREDATOR]
        [GRASSTRAMPLE:20]
        [PREFSTRING:strength]
        [BUILDINGDESTROYER:1]
        [BODY:QUADRUPED_NECK:TAIL:2EYES:NOSE:2LUNGS:HEART:GUTS:ORGANS:GIZZARD:THROAT:NECK:SPINE:BRAIN:SKULL:5TOES_FQ_REG:4TOES_RQ_REG:MOUTH:TONGUE:GENERIC_TEETH:RIBCAGE]
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
        [USE_MATERIAL_TEMPLATE:CLAW:NAIL_TEMPLATE]
        [USE_TISSUE_TEMPLATE:CLAW:CLAW_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:TOE:CLAW:FRONT]
        [BODY_DETAIL_PLAN:LEATHERY_EGG_MATERIALS]
        [SELECT_TISSUE_LAYER:HEART:BY_CATEGORY:HEART]
         [PLUS_TISSUE_LAYER:SCALE:BY_CATEGORY:THROAT]
            [TL_MAJOR_ARTERIES]
        [BODY_DETAIL_PLAN:STANDARD_HEAD_POSITIONS]
        [BODY_DETAIL_PLAN:HUMANOID_RIBCAGE_POSITIONS]
        [USE_MATERIAL_TEMPLATE:SINEW:SINEW_TEMPLATE]
        [TENDONS:LOCAL_CREATURE_MAT:SINEW:200]
        [LIGAMENTS:LOCAL_CREATURE_MAT:SINEW:200]
        [HAS_NERVES]
        [EXTRA_BUTCHER_OBJECT:BY_CATEGORY:GIZZARD]
            [EBO_ITEM:SMALLGEM:NONE:ANY_HARD_STONE]
            [EBO_SHAPE:GIZZARD_STONE]
        [USE_MATERIAL_TEMPLATE:BLOOD:BLOOD_TEMPLATE]
        [BLOOD:LOCAL_CREATURE_MAT:BLOOD:LIQUID]
        [CREATURE_CLASS:GENERAL_POISON]
        [GETS_WOUND_INFECTIONS]
        [GETS_INFECTIONS_FROM_ROT]
        [USE_MATERIAL_TEMPLATE:PUS:PUS_TEMPLATE]
        [PUS:LOCAL_CREATURE_MAT:PUS:LIQUID]
        [BODY_SIZE:0:0:70]
        [BODY_SIZE:1:0:300000]
        [BODY_SIZE:2:0:600000]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:60:100]
        [ATTACK:BITE:CHILD_BODYPART_GROUP:BY_CATEGORY:HEAD:BY_CATEGORY:TOOTH]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:bite:bites]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_CANLATCH]
        [ALL_ACTIVE]
        [HOMEOTHERM:10040]
        [LOW_LIGHT_VISION:10000]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:3512:2634:1756:878:4900:6900] 10 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2206:1692:1178:585:3400:4900] 15 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [SWIMS_INNATE]
        [CANNOT_JUMP]
        [CASTE:FEMALE]
            [FEMALE]
            [LAYS_EGGS]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGGSHELL:SOLID]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGG_WHITE:LIQUID]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGG_YOLK:LIQUID]
                [EGG_SIZE:80]
                [CLUTCH_SIZE:20:60]
        [CASTE:MALE]
            [MALE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SCALE]
                [TL_COLOR_MODIFIER:GRAY:1]
                    [TLCM_NOUN:scales:PLURAL]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:RED:1]
                    [TLCM_NOUN:eyes:PLURAL]
        [SELECT_MATERIAL:ALL]
            [MULTIPLY_VALUE:4]
