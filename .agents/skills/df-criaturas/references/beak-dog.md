# Beak dog

> Fonte: [Beak dog](https://dwarffortresswiki.org/index.php/Beak_dog) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes beak dogs for their large beaks.**
- **Biome**
- **Temperate Freshwater Marsh Temperate Saltwater Marsh Tropical Freshwater Marsh Tropical Saltwater Marsh Domesticated**
- **Attributes**
- **Alignment:** Evil
- **Mount · Egglaying**
- **Tamed Attributes**
- **Pet value:** 50
- **Not hunting/war trainable**
- **Size**
- **Birth:** 1,500 cm 3
- **Mid:** 50,000 cm 3
- **Max:** 150,000 cm 3
- **Food products**
- **Eggs:** 5-10
- **Age**
- **Adult at:** 1
- **Max age:** 10-20
- **Butchering returns ( Value multiplier ×2)**
- **Food items**
- **Meat:** 11-13
- **Fat:** 11
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
- **Bones:** 16
- **Skull:** 1
- **Skin:** Raw hide
- **Gizzard stone:** 1

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A creature from the evil swamp. It resembles a squat, wingless bird with powerful beak and legs. Its blotchy skin is brightly colored.*

**Beak dogs** are a freakish species of gorilla-sized, bird-like pack hunters found in evil swamplands. They appear in groups of three to seven and occupy the same ecological niche that wolves do in more normal surroundings. In the fortress-embarking flavor screen, you are sometimes warned to strike the earth quickly "ere the wolves get hungry", but in the actual game, wolves are too small to opportunistically attack dwarves, preferring to predate on smaller creatures instead. Beak dogs, by contrast, are not held back by such a deficiency: they are close to four times as large as a wolf (two and a half times the size of an average dwarf), and the [`[LARGE_PREDATOR]`](/index.php/Creature_token#LARGE_PREDATOR "Creature token") token in their raw files that they share with wolves means that they will snack on any dwarves that appear before them, given the chance. This obviously makes them very dangerous.

Beak dogs can be captured in cage traps and trained into pets. They are considered domestic animals in goblin civilizations and as such are always found with them, often being employed as attack animals or mounts during sieges. Raiding a goblin settlement may lead your dwarves to bring numerous tame beak dogs to your fortress as spoils, which is the easiest way to get a hold on the creatures - they serve well on a meat industry and can also be used in egg production, being far larger than any conventional egg-laying livestock. Additionally, their parts are worth twice as much as boring dog parts.

Some dwarves like beak dogs for their *large beaks*, their *hunched backs* and their *chatters and clicks*.

|  |
|----|
| "Beak dog" in other / Languages / Dwarven / : / emuth idar / Elven / : / etini macetha / Goblin / : / gosma anot / Human / : / kes sheka |

## Gallery

-

  A beak dog and its goblin rider, drawn in crayon by Bay 12 Games.

-

  Urist also likes beak dogs for their crushable heads.\
  *Art by kruggsmash*

-

  Another artistic take on the beak dog.\
  *Art by King Agrian*

## Trivia

- Toady One has said that beak dogs are based on a variety of sources.
- In the premium version of the game, beak dogs are depicted with pale, pinkish-gray skin and black spots along their back. This is a notable departure from their other visual and described appearances, including the above drawing by Bay 12 Games, their in-game description string, and the tissue layer for their skin in the RAW files, which all depict beak dogs with rainbow-colored skin. The RAW files specifically set beak dog's skin tissue color as rainbow-colored stripes.

    [CREATURE:BEAK_DOG]
        [DESCRIPTION:A creature from the evil swamp.  It resembles a squat, wingless bird with powerful beak and legs.  Its blotchy skin is brightly colored.]
        [NAME:beak dog:beak dogs:beak dog]
        [CASTE_NAME:beak dog:beak dogs:beak dog]
        [CHILD:1][GENERAL_CHILD_NAME:beak dog pup:beak dog pups]
        [CREATURE_TILE:'B'][COLOR:4:0:0]
        [PETVALUE:50]
        [LARGE_PREDATOR][MEANDERER]
        [LARGE_ROAMING][FREQUENCY:25]
        [BIOME:MARSH_TEMPERATE_FRESHWATER]
        [BIOME:MARSH_TEMPERATE_SALTWATER]
        [BIOME:MARSH_TROPICAL_FRESHWATER]
        [BIOME:MARSH_TROPICAL_SALTWATER]
        [POPULATION_NUMBER:10:20]
        [CLUSTER_NUMBER:3:7]
        [GRASSTRAMPLE:0][EVIL]
        [PET]
        [MOUNT]
        [COMMON_DOMESTIC]
        [BONECARN]
        [PREFSTRING:chatters and clicks]
        [PREFSTRING:hunched backs]
        [PREFSTRING:large beaks]
        [BODY:HUMANOID_ARMLESS_NECK:TAIL:2EYES:2LUNGS:HEART:GUTS:ORGANS:GIZZARD:THROAT:NECK:SPINE:BRAIN:SKULL:BEAK:TONGUE:RIBCAGE:4TOES]
        [BODYGLOSS:PAW]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
            [REMOVE_MATERIAL:HAIR]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
            [REMOVE_TISSUE:HAIR]
        [BODY_DETAIL_PLAN:VERTEBRATE_TISSUE_LAYERS:SKIN:FAT:MUSCLE:BONE:CARTILAGE]
        [USE_MATERIAL_TEMPLATE:NAIL:NAIL_TEMPLATE]
        [USE_TISSUE_TEMPLATE:NAIL:NAIL_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:TOE:NAIL:FRONT]
        [BODY_DETAIL_PLAN:EGG_MATERIALS]
        [SELECT_TISSUE_LAYER:HEART:BY_CATEGORY:HEART]
         [PLUS_TISSUE_LAYER:SKIN:BY_CATEGORY:THROAT]
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
        [BODY_SIZE:0:0:1500]
        [BODY_SIZE:1:0:50000]
        [BODY_SIZE:2:0:150000]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:10:20]
        [ATTACK:BITE:BODYPART:BY_CATEGORY:BEAK]
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
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:900:585:390:195:1900:2900] 45 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [SWIMS_INNATE]
        [CASTE:FEMALE]
            [FEMALE]
            [LAYS_EGGS]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGGSHELL:SOLID]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGG_WHITE:LIQUID]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGG_YOLK:LIQUID]
                [EGG_SIZE:1600]
                [CLUTCH_SIZE:5:10]
        [CASTE:MALE]
            [MALE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
                [TL_COLOR_MODIFIER:STRIPES_RAINBOW:1]
                    [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
        [SELECT_MATERIAL:ALL]
            [MULTIPLY_VALUE:2]
