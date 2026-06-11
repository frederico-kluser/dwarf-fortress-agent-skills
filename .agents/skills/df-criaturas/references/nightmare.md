# Nightmare

> Fonte: [Nightmare](https://dwarffortresswiki.org/index.php/Nightmare) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

\

**Nightmares** `Ñ` are procedurally-generated, fanciful night creatures summoned by necromancers and demons\[Verify\] to fight in battle, larger than your standard humanoids, but smaller than titans and forgotten beasts. They are short-lived, and neutral to creatures with [`[NOFEAR]`](/index.php/Creature_token#NOFEAR "Creature token"). Nightmares summoned in fortress mode will be friendly. When summoned, nightmares will possess Talented skill in observing, fighting, wrestling, biting, striking, kicking and dodging. They do not need to sleep, eat or drink, feel no pain (though still have nerves that can be damaged, therefore affecting motor function), cannot be stunned, feel no fear, completely avoid traps, don't need to breathe, or feel dizziness, nausea, have extravision, and never get tired from over-exertion.

Graphically, the sprites that nightmares use will be of black (or sometimes grey), mysterious-looking creatures that resemble the generated appearance they've been given. This same setup is used for other procedurally-generated creatures, such as bogeymen and experiments.

Since they are procedurally-generated, their in-game appearance (which can be seen by spawning them in the object testing arena) will vary by world, but will always end with: "Now you will know why you fear the night." This same quote is associated with bogeymen. By default, there are multiple nightmare types per world, and the number can be set in advanced world generation. Like many procedurally-generated creatures in the game, not only can their appearance be randomized, but the color of their blood.

As with all procedurally generated creatures how much of a threat they are varies greatly, however their large size and innate combat skills along with the possibilities of procedural generation means an adventurer can end up fighting something above a semi-megabeast in threat. A necromancer's ability to summon them is arguably their currently most dangerous ability, though the nightmare may also end up fighting their summoner's undead minions.

All nightmares are linked with the spheres of misery, night, and - unsurprisingly - nightmares.

Some dwarves like nightmares for their *unfathomably horrifying nature.*

\

Too much for the neurons to handle.\
*Art by jlcseiles (John L C Seiles)*

    Example raws (as extracted from world.dat in version 0.47.04)

    [CREATURE:NIGHT_CREATURE_23]
        [NAME:nightmare:nightmares:nightmare]
        [CASTE_NAME:nightmare:nightmares:nightmare]
        [GENERATED]
        [ATTACK_TRIGGER:50:5000:50000]
        [NIGHT_CREATURE_NIGHTMARE]
        [NATURAL_SKILL:WRESTLING:6]
        [NATURAL_SKILL:BITE:6]
        [NATURAL_SKILL:MELEE_COMBAT:6]
        [NATURAL_SKILL:GRASP_STRIKE:6]
        [NATURAL_SKILL:STANCE_STRIKE:6]
        [NATURAL_SKILL:DODGING:6]
        [NATURAL_SKILL:SITUATIONAL_AWARENESS:6]
        [NO_GENDER]
        [CLUSTER_NUMBER:1:1]
        [PHYS_ATT_RANGE:STRENGTH:450:1050:1150:1250:1350:1550:2250]
        [PHYS_ATT_RANGE:TOUGHNESS:450:1050:1150:1250:1350:1550:2250]
        [PHYS_ATT_RANGE:ENDURANCE:450:1050:1150:1250:1350:1550:2250]
        [PHYS_ATT_RANGE:RECUPERATION:450:1050:1150:1250:1350:1550:2250]
        [PHYS_ATT_RANGE:DISEASE_RESISTANCE:700:1300:1400:1500:1600:1800:2500]
        [MENT_ATT_RANGE:ANALYTICAL_ABILITY:1250:1500:1750:2000:2500:3000:5000]
        [MENT_ATT_RANGE:FOCUS:1250:1500:1750:2000:2500:3000:5000]
        [MENT_ATT_RANGE:WILLPOWER:1250:1500:1750:2000:2500:3000:5000]
        [MENT_ATT_RANGE:PATIENCE:0:333:666:1000:2333:3666:5000]
        [MENT_ATT_RANGE:MEMORY:1250:1500:1750:2000:2500:3000:5000]
        [MENT_ATT_RANGE:LINGUISTIC_ABILITY:450:1050:1150:1250:1350:1550:2250]
        [MENT_ATT_RANGE:MUSICALITY:0:333:666:1000:2333:3666:5000]
        [MENT_ATT_RANGE:SOCIAL_AWARENESS:700:1300:1400:1500:1600:1800:2500]
        [PERSONALITY:ANXIETY_PROPENSITY:0:0:0]
        [PERSONALITY:DEPRESSION_PROPENSITY:0:0:0]
        [PERSONALITY:BASHFUL:0:0:0]
        [PERSONALITY:STRESS_VULNERABILITY:0:0:0]
        [PERSONALITY:FRIENDLINESS:0:0:0]
        [PERSONALITY:ASSERTIVENESS:100:100:100]
        [PERSONALITY:DISDAIN_ADVICE:100:100:100]
        [PERSONALITY:CHEER_PROPENSITY:0:0:0]
        [PERSONALITY:GRATITUDE:0:0:0]
        [PERSONALITY:TRUST:0:0:0]
        [PERSONALITY:ALTRUISM:0:0:0]
        [PERSONALITY:SWAYED_BY_EMOTIONS:0:0:0]
        [PERSONALITY:CRUELTY:100:100:100]
        [PERSONALITY:HUMOR:100:100:100]
        [NO_DRINK]
        [NO_EAT]
        [NO_SLEEP]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [LARGE_PREDATOR]
        [EVIL]
        [SUPERNATURAL]
        [FANCIFUL]
        [AMPHIBIOUS]
        [SWIMS_INNATE]
        [NONAUSEA]
        [NOEXERT]
        [NO_DIZZINESS]
        [NOPAIN]
        [NOSTUN]
        [PETVALUE:2000]
        [ALL_ACTIVE]
        [NOFEAR]
        [NO_FEVERS]
        [LARGE_PREDATOR]
        [SPHERE:MISERY]
        [SPHERE:NIGHT]
        [SPHERE:NIGHTMARES]
        [BODY_SIZE:0:0:1000000]
        [GRASSTRAMPLE:20]
        [BUILDINGDESTROYER:2]
        [TRAPAVOID]
        [CREATURE_TILE:165]
        [BODY:RCP_UPPER_BODY:RCP_LOWER_BODY:RCP_NECK:RCP_HEAD:RCP_TWO_PART_ARMS:RCP_TWO_PART_LEGS:RCP_ANTENNAE:RCP_HEART:RCP_GUTS:RCP_BRAIN:RCP_MOUTH]
        [CANOPENDOORS]
        [EQUIPS]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
            [REMOVE_MATERIAL:HAIR]
        [USE_MATERIAL_TEMPLATE:FEATHER:FEATHER_TEMPLATE]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
            [REMOVE_TISSUE:HAIR]
        [USE_TISSUE_TEMPLATE:FEATHER:FEATHER_TEMPLATE]
        [BODY_DETAIL_PLAN:EXOSKELETON_TISSUE_LAYERS:SKIN:FAT:MUSCLE]
        [HAS_NERVES]
        [NOBREATHE]
        [EXTRAVISION]
        [HOMEOTHERM:10040]
        [BODY_DETAIL_PLAN:BODY_FEATHER_TISSUE_LAYERS:FEATHER]
        [SELECT_MATERIAL:FEATHER]
            [STATE_COLOR:ALL_SOLID:SLATE_GRAY]
        [NO_UNIT_TYPE_COLOR]
        [COLOR:0:0:1]
        [SELECT_TISSUE_LAYER:HEART:BY_CATEGORY:HEART]
            [PLUS_TISSUE_LAYER:SCALE:BY_CATEGORY:THROAT]
            [TL_MAJOR_ARTERIES]
        [USE_MATERIAL_TEMPLATE:ICHOR:ICHOR_TEMPLATE]
        [BLOOD:LOCAL_CREATURE_MAT:ICHOR:LIQUID]
        [ATTACK:PUNCH:BODYPART:BY_TYPE:GRASP]
            [ATTACK_SKILL:GRASP_STRIKE]
            [ATTACK_VERB:punch:punches]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PREPARE_AND_RECOVER:2:2]
            [ATTACK_FLAG_WITH]
            [ATTACK_PRIORITY:MAIN]
        [ATTACK:KICK:BODYPART:BY_TYPE:STANCE]
            [ATTACK_SKILL:STANCE_STRIKE]
            [ATTACK_VERB:kick:kicks]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PREPARE_AND_RECOVER:2:2]
            [ATTACK_FLAG_WITH]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_BAD_MULTIATTACK]
        [ATTACK:BITE:BODYPART:BY_CATEGORY:MOUTH]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:bite:bites]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PREPARE_AND_RECOVER:2:2]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_CANLATCH]
        [GAIT:SWIM:Maximum Swim Speed:725:10:3:2175:50:LAYERS_SLOW:STRENGTH:AGILITY:STEALTH_SLOWS:50]
        [GAIT:SWIM:Faster Swim:1450:5:3:2175:10:LAYERS_SLOW:STRENGTH:AGILITY:STEALTH_SLOWS:20]
        [GAIT:SWIM:Fast Swim:2175:NO_BUILD_UP:5:LAYERS_SLOW:STRENGTH:AGILITY:STEALTH_SLOWS:10]
        [GAIT:SWIM:Swim:2900:NO_BUILD_UP:0]
        [GAIT:SWIM:Slow Swim:3900:NO_BUILD_UP:0]
        [GAIT:SWIM:Creeping Swim:5900:NO_BUILD_UP:0]
        [GAIT:WALK:Sprint:225:10:3:675:50:LAYERS_SLOW:STRENGTH:AGILITY:STEALTH_SLOWS:50]
        [GAIT:WALK:Run:450:5:3:675:10:LAYERS_SLOW:STRENGTH:AGILITY:STEALTH_SLOWS:20]
        [GAIT:WALK:Jog:675:NO_BUILD_UP:5:LAYERS_SLOW:STRENGTH:AGILITY:STEALTH_SLOWS:10]
        [GAIT:WALK:Walk:900:NO_BUILD_UP:0]
        [GAIT:WALK:Stroll:1900:NO_BUILD_UP:0]
        [GAIT:WALK:Creep:2900:NO_BUILD_UP:0]
        [GAIT:CRAWL:Scramble:225:10:3:675:50:LAYERS_SLOW:STRENGTH:AGILITY:STEALTH_SLOWS:50]
        [GAIT:CRAWL:Faster Crawl:450:5:3:675:10:LAYERS_SLOW:STRENGTH:AGILITY:STEALTH_SLOWS:20]
        [GAIT:CRAWL:Fast Crawl:675:NO_BUILD_UP:5:LAYERS_SLOW:STRENGTH:AGILITY:STEALTH_SLOWS:10]
        [GAIT:CRAWL:Crawl:900:NO_BUILD_UP:0]
        [GAIT:CRAWL:Slow Crawl:1900:NO_BUILD_UP:0]
        [GAIT:CRAWL:Creep:2900:NO_BUILD_UP:0]
        [GAIT:CLIMB:Scramble:225:10:3:675:50:LAYERS_SLOW:STRENGTH:AGILITY:STEALTH_SLOWS:50]
        [GAIT:CLIMB:Faster Climb:450:5:3:675:10:LAYERS_SLOW:STRENGTH:AGILITY:STEALTH_SLOWS:20]
        [GAIT:CLIMB:Fast Climb:675:NO_BUILD_UP:5:LAYERS_SLOW:STRENGTH:AGILITY:STEALTH_SLOWS:10]
        [GAIT:CLIMB:Climb:900:NO_BUILD_UP:0]
        [GAIT:CLIMB:Slow Climb:1900:NO_BUILD_UP:0]
        [GAIT:CLIMB:Creep:2900:NO_BUILD_UP:0]
        [DESCRIPTION:A very large feathered humanoid.  It has a pair of squat antennae and with singular purpose it seeks to destroy the living.  Its slate gray feathers are fluffed-out.  Now you will know why you fear the night.]
        [PREFSTRING:unfathomably horrifying nature]

    [CREATURE:NIGHT_CREATURE_30]
        [NAME:nightmare:nightmares:nightmare]
        [CASTE_NAME:nightmare:nightmares:nightmare]
        [GENERATED]
        [ATTACK_TRIGGER:50:5000:50000]
        [NIGHT_CREATURE_NIGHTMARE]
        [NATURAL_SKILL:WRESTLING:6]
        [NATURAL_SKILL:BITE:6]
        [NATURAL_SKILL:MELEE_COMBAT:6]
        [NATURAL_SKILL:GRASP_STRIKE:6]
        [NATURAL_SKILL:STANCE_STRIKE:6]
        [NATURAL_SKILL:DODGING:6]
        [NATURAL_SKILL:SITUATIONAL_AWARENESS:6]
        [NO_GENDER]
        [CLUSTER_NUMBER:1:1]
        [PHYS_ATT_RANGE:STRENGTH:450:1050:1150:1250:1350:1550:2250]
        [PHYS_ATT_RANGE:TOUGHNESS:450:1050:1150:1250:1350:1550:2250]
        [PHYS_ATT_RANGE:ENDURANCE:450:1050:1150:1250:1350:1550:2250]
        [PHYS_ATT_RANGE:RECUPERATION:450:1050:1150:1250:1350:1550:2250]
        [PHYS_ATT_RANGE:DISEASE_RESISTANCE:700:1300:1400:1500:1600:1800:2500]
        [MENT_ATT_RANGE:ANALYTICAL_ABILITY:1250:1500:1750:2000:2500:3000:5000]
        [MENT_ATT_RANGE:FOCUS:1250:1500:1750:2000:2500:3000:5000]
        [MENT_ATT_RANGE:WILLPOWER:1250:1500:1750:2000:2500:3000:5000]
        [MENT_ATT_RANGE:PATIENCE:0:333:666:1000:2333:3666:5000]
        [MENT_ATT_RANGE:MEMORY:1250:1500:1750:2000:2500:3000:5000]
        [MENT_ATT_RANGE:LINGUISTIC_ABILITY:450:1050:1150:1250:1350:1550:2250]
        [MENT_ATT_RANGE:MUSICALITY:0:333:666:1000:2333:3666:5000]
        [MENT_ATT_RANGE:SOCIAL_AWARENESS:700:1300:1400:1500:1600:1800:2500]
        [PERSONALITY:ANXIETY_PROPENSITY:0:0:0]
        [PERSONALITY:DEPRESSION_PROPENSITY:0:0:0]
        [PERSONALITY:BASHFUL:0:0:0]
        [PERSONALITY:STRESS_VULNERABILITY:0:0:0]
        [PERSONALITY:FRIENDLINESS:0:0:0]
        [PERSONALITY:ASSERTIVENESS:100:100:100]
        [PERSONALITY:DISDAIN_ADVICE:100:100:100]
        [PERSONALITY:CHEER_PROPENSITY:0:0:0]
        [PERSONALITY:GRATITUDE:0:0:0]
        [PERSONALITY:TRUST:0:0:0]
        [PERSONALITY:ALTRUISM:0:0:0]
        [PERSONALITY:SWAYED_BY_EMOTIONS:0:0:0]
        [PERSONALITY:CRUELTY:100:100:100]
        [PERSONALITY:HUMOR:100:100:100]
        [NO_DRINK]
        [NO_EAT]
        [NO_SLEEP]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [LARGE_PREDATOR]
        [EVIL]
        [SUPERNATURAL]
        [FANCIFUL]
        [AMPHIBIOUS]
        [SWIMS_INNATE]
        [NONAUSEA]
        [NOEXERT]
        [NO_DIZZINESS]
        [NOPAIN]
        [NOSTUN]
        [PETVALUE:2000]
        [ALL_ACTIVE]
        [NOFEAR]
        [NO_FEVERS]
        [LARGE_PREDATOR]
        [SPHERE:MISERY]
        [SPHERE:NIGHT]
        [SPHERE:NIGHTMARES]
        [BODY_SIZE:0:0:800000]
        [GRASSTRAMPLE:20]
        [BUILDINGDESTROYER:2]
        [TRAPAVOID]
        [CREATURE_TILE:165]
        [BODY:RCP_UPPER_BODY:RCP_LOWER_BODY:RCP_NECK:RCP_HEAD:RCP_SIMPLE_FRONT_LEGS:RCP_SIMPLE_REAR_LEGS:RCP_TAIL:RCP_2_HEAD_HORNS:RCP_4_FRONT_TOES:RCP_4_REAR_TOES:RCP_LUNGS:RCP_HEART:RCP_GUTS:RCP_THROAT:RCP_SPINE:RCP_UPPER_SPINE:RCP_BRAIN:RCP_SKULL:RCP_MOUTH:RCP_TONGUE:RCP_TEETH:RCP_RIBS]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
            [REMOVE_MATERIAL:SKIN]
            [REMOVE_MATERIAL:HAIR]
        [USE_MATERIAL_TEMPLATE:SCALE:SCALE_TEMPLATE]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
            [REMOVE_TISSUE:SKIN]
            [REMOVE_TISSUE:HAIR]
        [USE_TISSUE_TEMPLATE:SCALE:SCALE_TEMPLATE]
        [USE_MATERIAL_TEMPLATE:HORN:HORN_TEMPLATE]
        [USE_TISSUE_TEMPLATE:HORN:HORN_TEMPLATE]
        [BODY_DETAIL_PLAN:VERTEBRATE_TISSUE_LAYERS:SCALE:FAT:MUSCLE:BONE:CARTILAGE]
        [BODY_DETAIL_PLAN:STANDARD_HEAD_POSITIONS]
        [BODY_DETAIL_PLAN:HUMANOID_HEAD_POSITIONS]
        [BODY_DETAIL_PLAN:HUMANOID_RIBCAGE_POSITIONS]
        [BODY_DETAIL_PLAN:HUMANOID_RELSIZES]
        [USE_MATERIAL_TEMPLATE:SINEW:SINEW_TEMPLATE]
        [TENDONS:LOCAL_CREATURE_MAT:SINEW:200]
        [LIGAMENTS:LOCAL_CREATURE_MAT:SINEW:200]
        [HAS_NERVES]
        [NOBREATHE]
        [EXTRAVISION]
        [HOMEOTHERM:10040]
        [SELECT_MATERIAL:SCALE]
            [STATE_COLOR:ALL_SOLID:CLEAR]
        [NO_UNIT_TYPE_COLOR]
        [COLOR:0:0:1]
        [SELECT_TISSUE_LAYER:HEART:BY_CATEGORY:HEART]
            [PLUS_TISSUE_LAYER:SCALE:BY_CATEGORY:THROAT]
            [TL_MAJOR_ARTERIES]
        [USE_MATERIAL_TEMPLATE:BLOOD:BLOOD_TEMPLATE]
            [STATE_COLOR:ALL:PLUM]
        [BLOOD:LOCAL_CREATURE_MAT:BLOOD:LIQUID]
        [USE_MATERIAL_TEMPLATE:CLAW:NAIL_TEMPLATE]
        [USE_TISSUE_TEMPLATE:CLAW:CLAW_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:TOE:CLAW:FRONT]
        [ATTACK:KICK:BODYPART:BY_TYPE:STANCE]
            [ATTACK_SKILL:STANCE_STRIKE]
            [ATTACK_VERB:kick:kicks]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PREPARE_AND_RECOVER:2:2]
            [ATTACK_FLAG_WITH]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_BAD_MULTIATTACK]
        [ATTACK:HORN:BODYPART:BY_CATEGORY:HORN]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:gore:gores]
            [ATTACK_CONTACT_PERC:5]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_PREPARE_AND_RECOVER:2:2]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PRIORITY:MAIN]
        [ATTACK:BITE:CHILD_BODYPART_GROUP:BY_CATEGORY:HEAD:BY_CATEGORY:TOOTH]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:bite:bites]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_PREPARE_AND_RECOVER:2:2]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_CANLATCH]
        [ATTACK:TSCRATCH:CHILD_TISSUE_LAYER_GROUP:BY_TYPE:STANCE:BY_CATEGORY:ALL:CLAW]
            [ATTACK_SKILL:STANCE_STRIKE]
            [ATTACK_VERB:scratch:scratches]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_PREPARE_AND_RECOVER:2:2]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_BAD_MULTIATTACK]
        [GAIT:SWIM:Maximum Swim Speed:725:10:3:2175:50:LAYERS_SLOW:STRENGTH:AGILITY:STEALTH_SLOWS:50]
        [GAIT:SWIM:Faster Swim:1450:5:3:2175:10:LAYERS_SLOW:STRENGTH:AGILITY:STEALTH_SLOWS:20]
        [GAIT:SWIM:Fast Swim:2175:NO_BUILD_UP:5:LAYERS_SLOW:STRENGTH:AGILITY:STEALTH_SLOWS:10]
        [GAIT:SWIM:Swim:2900:NO_BUILD_UP:0]
        [GAIT:SWIM:Slow Swim:3900:NO_BUILD_UP:0]
        [GAIT:SWIM:Creeping Swim:5900:NO_BUILD_UP:0]
        [GAIT:WALK:Gallop:225:10:3:675:5:LAYERS_SLOW:STRENGTH:AGILITY:STEALTH_SLOWS:50]
        [GAIT:WALK:Canter:450:5:3:675:3:LAYERS_SLOW:STRENGTH:AGILITY:STEALTH_SLOWS:20]
        [GAIT:WALK:Trot:675:NO_BUILD_UP:0:LAYERS_SLOW:STRENGTH:AGILITY:STEALTH_SLOWS:10]
        [GAIT:WALK:Walk:900:NO_BUILD_UP:0]
        [GAIT:WALK:Stroll:1900:NO_BUILD_UP:0]
        [GAIT:WALK:Creep:2900:NO_BUILD_UP:0]
        [GAIT:CRAWL:Scramble:225:10:3:675:50:LAYERS_SLOW:STRENGTH:AGILITY:STEALTH_SLOWS:50]
        [GAIT:CRAWL:Faster Crawl:450:5:3:675:10:LAYERS_SLOW:STRENGTH:AGILITY:STEALTH_SLOWS:20]
        [GAIT:CRAWL:Fast Crawl:675:NO_BUILD_UP:5:LAYERS_SLOW:STRENGTH:AGILITY:STEALTH_SLOWS:10]
        [GAIT:CRAWL:Crawl:900:NO_BUILD_UP:0]
        [GAIT:CRAWL:Slow Crawl:1900:NO_BUILD_UP:0]
        [GAIT:CRAWL:Creep:2900:NO_BUILD_UP:0]
        [DESCRIPTION:A very large eyeless dimetrodon.  It has two long, curving horns and with singular purpose it seeks to destroy the living.  Its clear scales are round and close-set.  Now you will know why you fear the night.]
        [PREFSTRING:unfathomably horrifying nature]

    [CREATURE:NIGHT_CREATURE_32]
        [NAME:nightmare:nightmares:nightmare]
        [CASTE_NAME:nightmare:nightmares:nightmare]
        [GENERATED]
        [ATTACK_TRIGGER:50:5000:50000]
        [NIGHT_CREATURE_NIGHTMARE]
        [NATURAL_SKILL:WRESTLING:6]
        [NATURAL_SKILL:BITE:6]
        [NATURAL_SKILL:MELEE_COMBAT:6]
        [NATURAL_SKILL:GRASP_STRIKE:6]
        [NATURAL_SKILL:STANCE_STRIKE:6]
        [NATURAL_SKILL:DODGING:6]
        [NATURAL_SKILL:SITUATIONAL_AWARENESS:6]
        [NO_GENDER]
        [CLUSTER_NUMBER:1:1]
        [PHYS_ATT_RANGE:STRENGTH:450:1050:1150:1250:1350:1550:2250]
        [PHYS_ATT_RANGE:TOUGHNESS:450:1050:1150:1250:1350:1550:2250]
        [PHYS_ATT_RANGE:ENDURANCE:450:1050:1150:1250:1350:1550:2250]
        [PHYS_ATT_RANGE:RECUPERATION:450:1050:1150:1250:1350:1550:2250]
        [PHYS_ATT_RANGE:DISEASE_RESISTANCE:700:1300:1400:1500:1600:1800:2500]
        [MENT_ATT_RANGE:ANALYTICAL_ABILITY:1250:1500:1750:2000:2500:3000:5000]
        [MENT_ATT_RANGE:FOCUS:1250:1500:1750:2000:2500:3000:5000]
        [MENT_ATT_RANGE:WILLPOWER:1250:1500:1750:2000:2500:3000:5000]
        [MENT_ATT_RANGE:PATIENCE:0:333:666:1000:2333:3666:5000]
        [MENT_ATT_RANGE:MEMORY:1250:1500:1750:2000:2500:3000:5000]
        [MENT_ATT_RANGE:LINGUISTIC_ABILITY:450:1050:1150:1250:1350:1550:2250]
        [MENT_ATT_RANGE:MUSICALITY:0:333:666:1000:2333:3666:5000]
        [MENT_ATT_RANGE:SOCIAL_AWARENESS:700:1300:1400:1500:1600:1800:2500]
        [PERSONALITY:ANXIETY_PROPENSITY:0:0:0]
        [PERSONALITY:DEPRESSION_PROPENSITY:0:0:0]
        [PERSONALITY:BASHFUL:0:0:0]
        [PERSONALITY:STRESS_VULNERABILITY:0:0:0]
        [PERSONALITY:FRIENDLINESS:0:0:0]
        [PERSONALITY:ASSERTIVENESS:100:100:100]
        [PERSONALITY:DISDAIN_ADVICE:100:100:100]
        [PERSONALITY:CHEER_PROPENSITY:0:0:0]
        [PERSONALITY:GRATITUDE:0:0:0]
        [PERSONALITY:TRUST:0:0:0]
        [PERSONALITY:ALTRUISM:0:0:0]
        [PERSONALITY:SWAYED_BY_EMOTIONS:0:0:0]
        [PERSONALITY:CRUELTY:100:100:100]
        [PERSONALITY:HUMOR:100:100:100]
        [NO_DRINK]
        [NO_EAT]
        [NO_SLEEP]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [LARGE_PREDATOR]
        [EVIL]
        [SUPERNATURAL]
        [FANCIFUL]
        [AMPHIBIOUS]
        [SWIMS_INNATE]
        [NONAUSEA]
        [NOEXERT]
        [NO_DIZZINESS]
        [NOPAIN]
        [NOSTUN]
        [PETVALUE:2000]
        [ALL_ACTIVE]
        [NOFEAR]
        [NO_FEVERS]
        [LARGE_PREDATOR]
        [SPHERE:MISERY]
        [SPHERE:NIGHT]
        [SPHERE:NIGHTMARES]
        [BODY_SIZE:0:0:600000]
        [GRASSTRAMPLE:20]
        [BUILDINGDESTROYER:2]
        [TRAPAVOID]
        [CREATURE_TILE:165]
        [BODY:RCP_CEPHALOTHORAX:RCP_ABDOMEN:RCP_FIRST_SIMPLE_LEGS:RCP_SECOND_SIMPLE_LEGS:RCP_THIRD_SIMPLE_LEGS:RCP_PINCERS:RCP_TAIL:RCP_4_HEAD_HORNS:RCP_2_EYES:RCP_HEART:RCP_GUTS:RCP_BRAIN:RCP_MOUTH:RCP_TAIL_STINGER]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
        [USE_MATERIAL_TEMPLATE:CHITIN:CHITIN_TEMPLATE]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
        [USE_TISSUE_TEMPLATE:CHITIN:CHITIN_TEMPLATE]
        [USE_MATERIAL_TEMPLATE:HORN:HORN_TEMPLATE]
        [USE_TISSUE_TEMPLATE:HORN:HORN_TEMPLATE]
        [BODY_DETAIL_PLAN:EXOSKELETON_TISSUE_LAYERS:CHITIN:FAT:MUSCLE]
        [BODY_DETAIL_PLAN:STANDARD_HEAD_POSITIONS]
        [BODY_DETAIL_PLAN:HUMANOID_HEAD_POSITIONS]
        [BODY_DETAIL_PLAN:HUMANOID_RELSIZES]
        [USE_MATERIAL_TEMPLATE:SINEW:SINEW_TEMPLATE]
        [TENDONS:LOCAL_CREATURE_MAT:SINEW:200]
        [LIGAMENTS:LOCAL_CREATURE_MAT:SINEW:200]
        [HAS_NERVES]
        [NOBREATHE]
        [HOMEOTHERM:10040]
        [BODY_DETAIL_PLAN:BODY_HAIR_TISSUE_LAYERS:HAIR]
        [SELECT_MATERIAL:HAIR]
        [STATE_COLOR:ALL_SOLID:BLACK]
        [NO_UNIT_TYPE_COLOR]
        [COLOR:0:0:1]
        [SELECT_TISSUE_LAYER:HEART:BY_CATEGORY:HEART]
            [PLUS_TISSUE_LAYER:SCALE:BY_CATEGORY:THROAT]
            [TL_MAJOR_ARTERIES]
        [USE_MATERIAL_TEMPLATE:ICHOR:ICHOR_TEMPLATE]
        [BLOOD:LOCAL_CREATURE_MAT:ICHOR:LIQUID]
        [USE_MATERIAL_TEMPLATE:POISON:CREATURE_EXTRACT_TEMPLATE]
            [ENTERS_BLOOD]
            [SYNDROME]
                [SYN_NAME:night sickness]
                [SYN_AFFECTED_CLASS:GENERAL_POISON]
                [SYN_IMMUNE_CREATURE:NIGHT_CREATURE_32:ALL]
                [SYN_INJECTED]
                [SYN_CONTACT]
                [SYN_INHALED]
                [SYN_INGESTED]
                [CE_IMPAIR_FUNCTION:SEV:100:PROB:100:START:470:PEAK:1172:END:3988:BP:BY_CATEGORY:ALL:STOMACH]
                [CE_DROWSINESS:SEV:100:PROB:100:START:788:PEAK:1802:END:3774]
        [ATTACK:PINCER:BODYPART:BY_CATEGORY:PINCER]
            [ATTACK_SKILL:GRASP_STRIKE]
            [ATTACK_VERB:snatch:snatches]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_PREPARE_AND_RECOVER:2:2]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_CANLATCH]
            [ATTACK_FLAG_WITH]
        [ATTACK:KICK:BODYPART:BY_TYPE:STANCE]
            [ATTACK_SKILL:STANCE_STRIKE]
            [ATTACK_VERB:kick:kicks]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PREPARE_AND_RECOVER:2:2]
            [ATTACK_FLAG_WITH]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_BAD_MULTIATTACK]
        [ATTACK:STING:BODYPART:BY_CATEGORY:STINGER]
            [ATTACK_SKILL:STANCE_STRIKE]
            [ATTACK_VERB:sting:stings]
            [ATTACK_CONTACT_PERC:5]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_PREPARE_AND_RECOVER:2:2]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PRIORITY:MAIN]
            [SPECIALATTACK_INJECT_EXTRACT:LOCAL_CREATURE_MAT:POISON:LIQUID:100:100]
        [ATTACK:HORN:BODYPART:BY_CATEGORY:HORN]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:gore:gores]
            [ATTACK_CONTACT_PERC:5]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_PREPARE_AND_RECOVER:2:2]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PRIORITY:MAIN]
        [ATTACK:BITE:BODYPART:BY_CATEGORY:MOUTH]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:bite:bites]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PREPARE_AND_RECOVER:2:2]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_CANLATCH]
        [GAIT:SWIM:Maximum Swim Speed:725:10:3:2175:50:LAYERS_SLOW:STRENGTH:AGILITY:STEALTH_SLOWS:50]
        [GAIT:SWIM:Faster Swim:1450:5:3:2175:10:LAYERS_SLOW:STRENGTH:AGILITY:STEALTH_SLOWS:20]
        [GAIT:SWIM:Fast Swim:2175:NO_BUILD_UP:5:LAYERS_SLOW:STRENGTH:AGILITY:STEALTH_SLOWS:10]
        [GAIT:SWIM:Swim:2900:NO_BUILD_UP:0]
        [GAIT:SWIM:Slow Swim:3900:NO_BUILD_UP:0]
        [GAIT:SWIM:Creeping Swim:5900:NO_BUILD_UP:0]
        [GAIT:WALK:Fastest Walk:225:10:3:675:50:LAYERS_SLOW:STRENGTH:AGILITY:STEALTH_SLOWS:50]
        [GAIT:WALK:Faster Walk:450:5:3:675:10:LAYERS_SLOW:STRENGTH:AGILITY:STEALTH_SLOWS:20]
        [GAIT:WALK:Fast Walk:675:NO_BUILD_UP:5:LAYERS_SLOW:STRENGTH:AGILITY:STEALTH_SLOWS:10]
        [GAIT:WALK:Walk:900:NO_BUILD_UP:0]
        [GAIT:WALK:Slow Walk:1900:NO_BUILD_UP:0]
        [GAIT:WALK:Slowest Walk:2900:NO_BUILD_UP:0]
        [GAIT:CRAWL:Scramble:225:10:3:675:50:LAYERS_SLOW:STRENGTH:AGILITY:STEALTH_SLOWS:50]
        [GAIT:CRAWL:Faster Crawl:450:5:3:675:10:LAYERS_SLOW:STRENGTH:AGILITY:STEALTH_SLOWS:20]
        [GAIT:CRAWL:Fast Crawl:675:NO_BUILD_UP:5:LAYERS_SLOW:STRENGTH:AGILITY:STEALTH_SLOWS:10]
        [GAIT:CRAWL:Crawl:900:NO_BUILD_UP:0]
        [GAIT:CRAWL:Slow Crawl:1900:NO_BUILD_UP:0]
        [GAIT:CRAWL:Creep:2900:NO_BUILD_UP:0]
        [GAIT:CLIMB:Scramble:225:10:3:675:50:LAYERS_SLOW:STRENGTH:AGILITY:STEALTH_SLOWS:50]
        [GAIT:CLIMB:Faster Climb:450:5:3:675:10:LAYERS_SLOW:STRENGTH:AGILITY:STEALTH_SLOWS:20]
        [GAIT:CLIMB:Fast Climb:675:NO_BUILD_UP:5:LAYERS_SLOW:STRENGTH:AGILITY:STEALTH_SLOWS:10]
        [GAIT:CLIMB:Climb:900:NO_BUILD_UP:0]
        [GAIT:CLIMB:Slow Climb:1900:NO_BUILD_UP:0]
        [GAIT:CLIMB:Creep:2900:NO_BUILD_UP:0]
        [DESCRIPTION:A very large hairy scorpion.  It has four broad horns and with singular purpose it seeks to destroy the living.  Its black hair is unkempt.  Now you will know why you fear the night.]
        [PREFSTRING:unfathomably horrifying nature]

    Script

    creatures
    .
    night_creature
    .
    nightmare
    .
    default
    =
    function
    (
    tok
    )

    local

    lines
    =
    {}

    local

    options
    =
    {

    spheres
    =
    {

    NIGHT
    =
    true
    ,

    NIGHTMARES
    =
    true
    ,

    MISERY
    =
    true

    },

    forced_color
    =
    {

    f
    =
    0
    ,

    b
    =
    0
    ,

    br
    =
    1

    },

    no_general_poison
    =
    true
    ,

    blood_color
    =
    function
    (
    cl
    )

    -- DARKER MAGENTA COLORS

    return

    cl
    .
    h
    >=
    260

    and

    cl
    .
    h

    <=

    340

    and

    cl
    .
    v

    <=

    0.5

    and

    cl
    .
    v

    >=

    0.1

    end
    ,

    fallback_pref_str
    =
    "unfathomably horrifying nature"
    ,

    token
    =
    tok

    }

    night_creature_universals
    (
    lines
    ,
    options
    )

    options
    .
    humanoid_only
    =
    false

    options
    .
    cannot_have_antennae
    =
    false

    if

    one_in
    (
    10
    )

    then

    options
    .
    glowing_eyes
    =
    true

    end

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[NIGHT_CREATURE_NIGHTMARE]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[NATURAL_SKILL:WRESTLING:6]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[NATURAL_SKILL:BITE:6]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[NATURAL_SKILL:MELEE_COMBAT:6]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[NATURAL_SKILL:GRASP_STRIKE:6]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[NATURAL_SKILL:STANCE_STRIKE:6]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[NATURAL_SKILL:DODGING:6]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[NATURAL_SKILL:SITUATIONAL_AWARENESS:6]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[NO_GENDER]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[CLUSTER_NUMBER:1:1]"

    --[[******************************* BOGEY

            --atts

        lines[#lines+1]="[PHYS_ATT_RANGE:STRENGTH:450:1050:1150:1250:1350:1550:2250]"

        lines[#lines+1]="[PHYS_ATT_RANGE:TOUGHNESS:450:1050:1150:1250:1350:1550:2250]"

        lines[#lines+1]="[PHYS_ATT_RANGE:ENDURANCE:450:1050:1150:1250:1350:1550:2250]"

        lines[#lines+1]="[PHYS_ATT_RANGE:RECUPERATION:450:1050:1150:1250:1350:1550:2250]"

        lines[#lines+1]="[PHYS_ATT_RANGE:DISEASE_RESISTANCE:700:1300:1400:1500:1600:1800:2500]"

        lines[#lines+1]="[MENT_ATT_RANGE:ANALYTICAL_ABILITY:1250:1500:1750:2000:2500:3000:5000]"

        lines[#lines+1]="[MENT_ATT_RANGE:FOCUS:1250:1500:1750:2000:2500:3000:5000]"

        lines[#lines+1]="[MENT_ATT_RANGE:WILLPOWER:1250:1500:1750:2000:2500:3000:5000]"

        lines[#lines+1]="[MENT_ATT_RANGE:PATIENCE:0:333:666:1000:2333:3666:5000]"

        lines[#lines+1]="[MENT_ATT_RANGE:MEMORY:1250:1500:1750:2000:2500:3000:5000]"

        lines[#lines+1]="[MENT_ATT_RANGE:LINGUISTIC_ABILITY:450:1050:1150:1250:1350:1550:2250]"

        lines[#lines+1]="[MENT_ATT_RANGE:MUSICALITY:0:333:666:1000:2333:3666:5000]"

        lines[#lines+1]="[MENT_ATT_RANGE:SOCIAL_AWARENESS:700:1300:1400:1500:1600:1800:2500]"

    MENTAL_ATTRIBUTE_CREATIVITY,

    MENTAL_ATTRIBUTE_INTUITION,

    MENTAL_ATTRIBUTE_SPATIAL_SENSE,

    MENTAL_ATTRIBUTE_KINESTHETIC_SENSE,

    MENTAL_ATTRIBUTE_EMPATHY,

        ]]

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[PERSONALITY:ANXIETY_PROPENSITY:0:0:0]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[PERSONALITY:DEPRESSION_PROPENSITY:0:0:0]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[PERSONALITY:BASHFUL:0:0:0]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[PERSONALITY:STRESS_VULNERABILITY:0:0:0]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[PERSONALITY:FRIENDLINESS:0:0:0]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[PERSONALITY:ASSERTIVENESS:100:100:100]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[PERSONALITY:DISDAIN_ADVICE:100:100:100]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[PERSONALITY:CHEER_PROPENSITY:0:0:0]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[PERSONALITY:GRATITUDE:0:0:0]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[PERSONALITY:TRUST:0:0:0]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[PERSONALITY:ALTRUISM:0:0:0]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[PERSONALITY:SWAYED_BY_EMOTIONS:0:0:0]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[PERSONALITY:CRUELTY:100:100:100]"

    --lines[#lines+1]="[PERSONALITY:PRIDE:100:100:100]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[PERSONALITY:HUMOR:100:100:100]"

    add_regular_tokens
    (
    lines
    ,
    options
    )

    populate_sphere_info
    (
    lines
    ,
    options
    )

    local

    rcp
    =
    get_random_creature_profile
    (
    options
    )

    add_body_size
    (
    lines
    ,
    math.max
    (
    rcp
    .
    min_size
    ,
    100000
    +
    trandom
    (
    11
    )
    *
    100000
    ),
    options
    )

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[CREATURE_TILE:165]"

    --Ñ

    options
    .
    custom_desc_func
    =
    function
    (
    options
    )

    return

    "with singular purpose it seeks to destroy the living"

    end

    build_procgen_creature
    (
    rcp
    ,
    lines
    ,
    options
    )

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[GO_TO_START]"

    local

    name_str
    =
    "nightmare:nightmares:nightmare]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[NAME:"
    ..
    name_str

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[CASTE_NAME:"
    ..
    name_str

    return

    {
    raws
    =
    lines
    ,
    weight
    =
    1
    }

    end
