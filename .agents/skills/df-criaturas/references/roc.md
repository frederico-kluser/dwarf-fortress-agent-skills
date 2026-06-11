# Roc

> Fonte: [Roc](https://dwarffortresswiki.org/index.php/Roc) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes rocs for their dedication to their young.**
- **Biome**
- **Mountain**
- **Attributes**
- **Flying · Megabeast · Steals food · Steals items · War animals · Hunting animals · Fanciful · Exotic mount · Egglaying**
- **Tamed Attributes**
- **Pet value:** 10,000
- **Trainable : Hunting War**
- **Size**
- **Birth:** 200,000 cm 3
- **Mid:** 5,000,000 cm 3
- **Max:** 20,000,000 cm 3
- **Food products**
- **Eggs:** 1-2
- **Age**
- **Adult at:** 1
- **Max age:** Immortal
- **Butchering returns ( Value multiplier ×15)**
- **Food items**
- **Meat:** 416-949
- **Fat:** 126-262
- **Brain:** 25-34
- **Heart:** 12-17
- **Lungs:** 50-68
- **Intestines:** 77-102
- **Liver:** 27-34
- **Kidneys:** 24-34
- **Tripe:** 27-34
- **Sweetbread:** 13-17
- **Eyes:** 2
- **Spleen:** 12-17
- **Raw materials**
- **Bones:** 258-317
- **Skull:** 1
- **Gizzard stone:** 1

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A bird of prey so large and ferocious it dwarfs many dragons. All beneath its mighty wings should fear the sky.*

Estimated size comparison between a roc and a dwarf.

**Rocs** are gigantic megabeasts taking the form of colossal birds of prey. These creatures reach their max size at only 20 years, and once they hit that age, they become the largest creatures in the game who are capable of flight. As megabeasts, rocs are also found in lairs, stealing items from nearby sites and generally harassing civilizations. Their lair is often littered with the loot they've amassed, as well as a number of nest boxes for them to use. All rocs are born with Talented skill in fighting, biting, kicking, dodging and observing.

Rocs are naturally formidable opponents; they are twice the size of a titan and are able to attack your dwarves from above, quickly turning them into little bearded shreds with their talons. However, when compared to their fellow megabeasts, rocs are arguably the least powerful of the four. Unlike other megabeasts, rocs are susceptible to both pain and over-exertion, and they also lack the danger posed by the fire breath of a dragon, the multi-attacks of a hydra or the inorganic armor of a bronze colossus. That being said, rocs are not to be underestimated, for their sheer size makes them a grave threat to a fortress.

Despite their monstrous size, rocs are just as vulnerable to cage traps as any other creature. In the event the player succeeds in capturing one, they can be trained and turned into war or hunting beasts or, if female, be pastured at a nest box to lay gigantic eggs – rocs lay the largest eggs in the game, each over thrice the size of a dwarf, but egg size currently plays no role. Rocs only lay 1-2 eggs at a time, which would make them subpar targets for egg production along with the size of them making hauling the eggs a time-consuming process, though one may choose to ignore this fact for the bragging rights of having your dwarves dine on the eggs of a colossal mythical bird.

Along with dragons, rocs are one of the megabeasts in possession of the [`[CHILD]`](/index.php/Creature_token#CHILD "Creature token") token, meaning they can become fully domesticated without modding. (Outdated: However, due to being megabeasts, rocs are perpetually hostile to your military squads and must be kept separated from your soldiers, otherwise they will kill each other on sight.Bug:10731) This is almost certainly outdated information according to this Reddit post. Trained or tame rocs likely won't attack friendly creatures, even if they're military, guests etc.

Some dwarves like rocs for their *awe-inspiring size* and their *dedication to their young*.

-

  Admired for its *awe-inspiring size*

-

  DnD inspired ROC Illustration

    [CREATURE:BIRD_ROC]
        [DESCRIPTION:A bird of prey so large and ferocious it dwarfs many dragons.  All beneath its mighty wings should fear the sky.]
        [NAME:roc:rocs:roc]
        [CASTE_NAME:roc:rocs:roc]
        [GENERAL_CHILD_NAME:roc hatchling:roc hatchlings]
        [CREATURE_TILE:'R'][COLOR:7:0:1]
        [PETVALUE:10000]
        [PET_EXOTIC]
        [TRAINABLE]
        [MOUNT_EXOTIC]
        [BIOME:MOUNTAIN]
        [FREQUENCY:5]
        [FANCIFUL]
        [MEGABEAST][DIFFICULTY:10]
            [ATTACK_TRIGGER:3:3:3]
        [SPHERE:SKY]
        [SPHERE:WIND]
        [SPHERE:HUNTING]
        [CURIOUSBEAST_ITEM]
        [CURIOUSBEAST_EATER]
        [NATURAL]
        [LARGE_PREDATOR]
        [FLIER]
        [BONECARN]
        [CHILD:1]
        [ALL_ACTIVE]
        [HOMEOTHERM:10067]
        [LAIR:WILDERNESS_LOCATION:100]
        [HABIT_NUM:TEST_ALL]
        [HABIT:GIANT_NEST:100]
        [NATURAL_SKILL:BITE:6]
        [NATURAL_SKILL:STANCE_STRIKE:6]
        [NATURAL_SKILL:MELEE_COMBAT:6]
        [NATURAL_SKILL:DODGING:6]
        [NATURAL_SKILL:SITUATIONAL_AWARENESS:6]
        [APPLY_CREATURE_VARIATION:STANDARD_FLYING_GAITS:900:528:352:176:1900:2900] 50 kph
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:3512:2634:1756:878:4900:6900] 10 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [SWIMS_INNATE]
        [PREFSTRING:awe-inspiring size]
        [PREFSTRING:dedication to their young]
        [BODY:HUMANOID_ARMLESS_NECK:2WINGS:2EYES:2LUNGS:HEART:GUTS:ORGANS:GIZZARD:HUMANOID_JOINTS:THROAT:NECK:SPINE:BRAIN:SKULL:4TOES:BEAK:TONGUE:RIBCAGE]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
            [REMOVE_MATERIAL:HAIR]
            [USE_MATERIAL_TEMPLATE:FEATHER:FEATHER_TEMPLATE]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
            [REMOVE_TISSUE:HAIR]
            [USE_TISSUE_TEMPLATE:FEATHER:FEATHER_TEMPLATE]
        [BODY_DETAIL_PLAN:VERTEBRATE_TISSUE_LAYERS:SKIN:FAT:MUSCLE:BONE:CARTILAGE]
        [BODY_DETAIL_PLAN:BODY_FEATHER_TISSUE_LAYERS:FEATHER]
        [USE_MATERIAL_TEMPLATE:TALON:NAIL_TEMPLATE]
        [USE_TISSUE_TEMPLATE:TALON:TALON_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:TOE:TALON:FRONT]
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
        [BODY_SIZE:0:0:200000]
        [BODY_SIZE:1:0:5000000]
        [BODY_SIZE:20:0:20000000]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [ATTACK:BITE:BODYPART:BY_CATEGORY:BEAK]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:bite:bites]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_CANLATCH]
        [ATTACK:SCRATCH:CHILD_TISSUE_LAYER_GROUP:BY_TYPE:STANCE:BY_CATEGORY:ALL:TALON]
            [ATTACK_SKILL:STANCE_STRIKE]
            [ATTACK_VERB:snatch at:snatches at]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:SECOND]
            [ATTACK_FLAG_WITH]
        [CASTE:FEMALE]
            [FEMALE]
            [LAYS_EGGS]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGGSHELL:SOLID]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGG_WHITE:LIQUID]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGG_YOLK:LIQUID]
                [EGG_SIZE:201000]
                [CLUTCH_SIZE:1:2]
        [CASTE:MALE]
            [MALE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:FEATHER]
                [TL_COLOR_MODIFIER:WHITE:1]
                    [TLCM_NOUN:feathers:PLURAL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
        [SELECT_MATERIAL:ALL]
            [MULTIPLY_VALUE:15]
