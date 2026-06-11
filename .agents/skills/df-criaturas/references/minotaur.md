# Minotaur

> Fonte: [Minotaur](https://dwarffortresswiki.org/index.php/Minotaur) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes minotaurs for their horns.**
- **Biome**
- **Any Land**
- **Attributes**
- **Building destroyer : Level 2**
- **Semi-megabeast · Learns · Fanciful · Horn · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 10,000 cm 3
- **Mid:** 50,000 cm 3
- **Max:** 220,000 cm 3
- **Age**
- **Child at:** 1
- **Adult at:** 18
- **Max age:** Immortal
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A giant humanoid monster with the head of a bull.*

**Minotaurs** are intelligent humanoids who inhabit labyrinths (marked with a \# on the Travel map). As you explore the labyrinth in adventurer mode, the minotaur will taunt you (*"I'll grind your bones into porridge!' 'I'll eat you whole!"*) until you find and kill it - or it kills you.

Minotaurs are semi-megabeasts which can destroy buildings and are attracted by wealth, just like regular megabeasts and titans. The game will pause and display a warning message when a minotaur appears. They are associated with the spheres of strength, deformity, darkness, chaos, and caverns, and their names will often reflect this.

In fortress mode, they will attack your fortress once it reaches 50 population, 5000 exported wealth, and 50000 created wealth. They can easily overpower normal dwarves, but a well-equipped military should be able to take care of one. They are susceptible to traps and can therefore easily be caught with a cage trap, and then used in a labyrinth of your own.

Compared to other semi-megabeasts, the minotaur is far smaller (less than half the size of a cow, in fact), but it is also an Expert with axes, swords, daggers, pikes "Pike (weapon)"), maces, hammers, whips, and spears, although it tends to show up unarmed. It is also Talented at wrestling, striking, kicking, and dodging; Competent at biting; and a Master observer. If the minotaur happens to have a ranged weapon, it does not carry any ammunition, rendering it only usable as a makeshift bludgeon\[Verify\]. It can still be dangerous to an unarmed civilian, chasing them all over the map before catching up to them, eventually making its kill. However, any amateur hunter can be drafted into the military and be sent to kill the minotaur. Usually, the first hit will mildly disable or knock out the minotaur, allowing the marksdwarf/hunter to repeatedly shoot it to death.

In adventurer mode, a quest may be given to slay a particular minotaur that may have previously killed other adventurers in the history of the world. Upon entering the labyrinth, the butchered corpses of these unfortunate heroes can be found throughout - in worlds with longer histories, minotaurs have a tendency of dying off first, their smaller size compared to other semi-megabeasts catching up with them, as more skilled warriors and larger animal people appear in civilizations.

Exercise caution against minotaurs who have managed to substantially increase their skills, which, by the way, is something no megabeast is able to do.

Some dwarves like minotaurs for their *horns*.

They're not so bad when they're not killing.

    [CREATURE:MINOTAUR]
        [DESCRIPTION:A giant humanoid monster with the head of a bull.]
        [NAME:minotaur:minotaurs:minotaur]
        [CASTE_NAME:minotaur:minotaurs:minotaur]
        [CREATURE_TILE:'M'][COLOR:6:0:0]
        [CREATURE_CLASS:MAMMAL]
        [CREATURE_CLASS:HUMANOID_TRACKING_SYMBOL]
        [FANCIFUL]
        [LARGE_PREDATOR]
        [SEMIMEGABEAST][DIFFICULTY:5]
            [ATTACK_TRIGGER:2:2:2]
        [CAN_LEARN][CAN_SPEAK]
        [CANOPENDOORS]
        [BUILDINGDESTROYER:2]
        [PREFSTRING:horns]
        [BIOME:ANY_LAND]
        [PERSONALITY:BRAVERY:75:90:100]
        [SPHERE:CAVERNS]
        [SPHERE:CHAOS]
        [SPHERE:DARKNESS]
        [SPHERE:DEFORMITY]
        [SPHERE:STRENGTH]
        [BODY:HUMANOID_NECK:2EYES:2EARS:NOSE:2LUNGS:HEART:GUTS:ORGANS:HUMANOID_JOINTS:THROAT:NECK:SPINE:BRAIN:SKULL:2HEAD_HORN:5FINGERS:5TOES:MOUTH:TONGUE:EYELIDS:CHEEKS:TEETH:RIBCAGE]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
            [USE_MATERIAL_TEMPLATE:HORN:HORN_TEMPLATE]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
            [USE_TISSUE_TEMPLATE:HORN:HORN_TEMPLATE]
        [BODY_DETAIL_PLAN:VERTEBRATE_TISSUE_LAYERS:SKIN:FAT:MUSCLE:BONE:CARTILAGE]
        [TISSUE_LAYER:BY_CATEGORY:HEAD:HAIR:NORMAL]
        [USE_TISSUE_TEMPLATE:EYEBROW:EYEBROW_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:HEAD:EYEBROW:ABOVE:BY_CATEGORY:EYE]
        [USE_TISSUE_TEMPLATE:EYELASH:EYELASH_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:EYELID:EYELASH:FRONT]
        [USE_MATERIAL_TEMPLATE:NAIL:NAIL_TEMPLATE]
        [USE_TISSUE_TEMPLATE:NAIL:NAIL_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:FINGER:NAIL:FRONT]
        [TISSUE_LAYER:BY_CATEGORY:TOE:NAIL:FRONT]
        [SELECT_TISSUE_LAYER:HEART:BY_CATEGORY:HEART]
         [PLUS_TISSUE_LAYER:SKIN:BY_CATEGORY:THROAT]
            [TL_MAJOR_ARTERIES]
        [BODY_DETAIL_PLAN:STANDARD_HEAD_POSITIONS]
        [BODY_DETAIL_PLAN:HUMANOID_HEAD_POSITIONS]
        [BODY_DETAIL_PLAN:HUMANOID_RIBCAGE_POSITIONS]
        [BODY_DETAIL_PLAN:HUMANOID_RELSIZES]
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
        [USE_MATERIAL_TEMPLATE:SWEAT:SWEAT_TEMPLATE]
        [USE_MATERIAL_TEMPLATE:TEARS:TEARS_TEMPLATE]
        [USE_MATERIAL_TEMPLATE:SPIT:SPIT_TEMPLATE]
        [SECRETION:LOCAL_CREATURE_MAT:SWEAT:LIQUID:BY_CATEGORY:ALL:SKIN:EXERTION]
        [SECRETION:LOCAL_CREATURE_MAT:TEARS:LIQUID:BY_CATEGORY:EYE:ALL:EXTREME_EMOTION]
        [CAN_DO_INTERACTION:PET_ANIMAL]
            [CDI:ADV_NAME:Pet animal]
            [CDI:USAGE_HINT:GREETING]
            [CDI:BP_REQUIRED:BY_TYPE:GRASP]
            [CDI:VERB:pet:pets:pets]
            [CDI:TARGET:A:SELF_ONLY]
            [CDI:TARGET:B:TOUCHABLE]
            [CDI:TARGET_RANGE:B:1]
            [CDI:MAX_TARGET_NUMBER:B:1]
            [CDI:WAIT_PERIOD:20]
        [CAN_DO_INTERACTION:MATERIAL_EMISSION]
            [CDI:TOKEN:SPIT]
            [CDI:ADV_NAME:Spit]
            [CDI:USAGE_HINT:NEGATIVE_SOCIAL_RESPONSE]
            [CDI:USAGE_HINT:TORMENT]
            [CDI:BP_REQUIRED:BY_CATEGORY:MOUTH]
            [CDI:MATERIAL:LOCAL_CREATURE_MAT:SPIT:LIQUID_GLOB]
            [CDI:VERB:spit:spits:NA]
            [CDI:TARGET:C:LINE_OF_SIGHT]
            [CDI:TARGET_RANGE:C:15]
            [CDI:MAX_TARGET_NUMBER:C:1]
            [CDI:WAIT_PERIOD:30]
        [BODY_SIZE:0:0:10000]
        [BODY_SIZE:1:168:50000]
        [BODY_SIZE:12:0:220000]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [ATTACK:PUNCH:BODYPART:BY_TYPE:GRASP]
            [ATTACK_SKILL:GRASP_STRIKE]
            [ATTACK_VERB:punch:punches]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_FLAG_WITH]
            [ATTACK_PRIORITY:MAIN]
        [ATTACK:GORE:BODYPART:BY_CATEGORY:HORN]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:gore:gores]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_FLAG_WITH]
            [ATTACK_PRIORITY:MAIN]
        [ATTACK:KICK:BODYPART:BY_TYPE:STANCE]
            [ATTACK_SKILL:STANCE_STRIKE]
            [ATTACK_VERB:kick:kicks]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PREPARE_AND_RECOVER:4:4]
            [ATTACK_FLAG_WITH]
            [ATTACK_PRIORITY:SECOND]
            [ATTACK_FLAG_BAD_MULTIATTACK]
        [ATTACK:SCRATCH:CHILD_TISSUE_LAYER_GROUP:BY_TYPE:GRASP:BY_CATEGORY:FINGER:NAIL]
            [ATTACK_SKILL:GRASP_STRIKE]
            [ATTACK_VERB:scratch:scratches]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:SECOND]
        [ATTACK:BITE:CHILD_BODYPART_GROUP:BY_CATEGORY:HEAD:BY_CATEGORY:TOOTH]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:bite:bites]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:SECOND]
            [ATTACK_FLAG_CANLATCH]
        [BABY:1]
        [CHILD:18]
        [EQUIPS]
        [NATURAL_SKILL:WRESTLING:6]
        [NATURAL_SKILL:BITE:3]
        [NATURAL_SKILL:GRASP_STRIKE:6]
        [NATURAL_SKILL:STANCE_STRIKE:6]
        [NATURAL_SKILL:MELEE_COMBAT:8]
        [NATURAL_SKILL:DODGING:6]
        [NATURAL_SKILL:AXE:8]
        [NATURAL_SKILL:SWORD:8]
        [NATURAL_SKILL:DAGGER:8]
        [NATURAL_SKILL:PIKE:8]
        [NATURAL_SKILL:MACE:8]
        [NATURAL_SKILL:HAMMER:8]
        [NATURAL_SKILL:WHIP:8]
        [NATURAL_SKILL:SPEAR:8]
        [NATURAL_SKILL:SITUATIONAL_AWARENESS:12]
        [PHYS_ATT_RANGE:STRENGTH:1000:1100:1150:1250:1350:1550:2250]
        [PHYS_ATT_RANGE:TOUGHNESS:1000:1100:1150:1250:1350:1550:2250]
        [PHYS_ATT_RANGE:AGILITY:1000:1100:1150:1250:1350:1550:2250]
        [PHYS_ATT_RANGE:ENDURANCE:1000:1100:1150:1250:1350:1550:2250]
        [PHYS_ATT_RANGE:RECUPERATION:1000:1100:1150:1250:1350:1550:2250]
        [PHYS_ATT_RANGE:DISEASE_RESISTANCE:1000:1100:1150:1250:1350:1550:2250]
        [MENT_ATT_RANGE:FOCUS:1000:1100:1150:1250:1350:1550:2250]
        [MENT_ATT_RANGE:WILLPOWER:1000:1100:1150:1250:1350:1550:2250]
        [MENT_ATT_RANGE:MEMORY:2000:2100:2150:2250:2350:2550:3250]
        [MENT_ATT_RANGE:SPATIAL_SENSE:2000:2100:2150:2250:2350:2550:3250]
        [MENT_ATT_RANGE:KINESTHETIC_SENSE:1000:1100:1150:1250:1350:1550:2250]
        [LAIR:LABYRINTH:100]
        [LAIR_HUNTER]
        [LAIR_HUNTER_SPEECH:LAIR_HUNTER_MINOTAUR]
        [HABIT_NUM:TEST_ALL]
        [HABIT:GRIND_BONE_MEAL:100]
        [HABIT:EAT_BONE_PORRIDGE:100]
        [HABIT:USE_ANY_MELEE_WEAPON:100]
        [ALL_ACTIVE]
        [LOW_LIGHT_VISION:10000]
        [HOMEOTHERM:10067]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:657:438:219:1900:2900] 40 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [SWIMS_INNATE]
        [CASTE:FEMALE]
            [FEMALE]
            [MULTIPLE_LITTER_RARE]
        [CASTE:MALE]
            [MALE]
            [SET_BP_GROUP:BY_TYPE:LOWERBODY][BP_ADD_TYPE:GELDABLE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:HAIR]
                [TL_COLOR_MODIFIER:BROWN:1]
                    [TLCM_NOUN:hair:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
        [TL_COLOR_MODIFIER:BROWN:1:BURNT_UMBER:1:CINNAMON:1:COPPER:1:DARK_BROWN:1:DARK_PEACH:1:DARK_TAN:1:ECRU:1:PALE_BROWN:1:PALE_CHESTNUT:1:PALE_PINK:1:PEACH:1:PINK:1:RAW_UMBER:1:SEPIA:1:TAN:1:TAUPE_PALE:1:TAUPE_SANDY:1]
                    [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
