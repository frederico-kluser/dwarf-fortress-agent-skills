# Serpent man

> Fonte: [Serpent man](https://dwarffortresswiki.org/index.php/Serpent_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes serpent men for their impressive tails.**
- **Biome**
- **Underground Depth: 1-3**
- **Attributes**
- **Amphibious · Learns · Syndrome · Egglaying · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 1,500 cm 3
- **Mid:** 10,000 cm 3
- **Max:** 50,000 cm 3
- **Age**
- **Child at:** 1
- **Adult at:** 12
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*For other kinds of snake men, see adder man, anaconda man, black mamba man, bushmaster man, copperhead snake man, king cobra man, kingsnake man, python man, and rattlesnake man.*

*A large white snake with the arms and torso of a man. These creatures are evil and live far underground.*

**Serpent men** are one of the many races of underground tribal creatures (*animal people, per se, but design choices apparently voided them of that status*) found living in small groups on any cavern level. They stand at roughly the size of an adult dwarf.

Despite being labelled as hostile in the unit list, serpent men initially found in the caverns will ignore your citizens unless provoked. They will usually be observed carrying wooden spears, blowguns and shields, although they are sometimes seen using metal items instead. These can range from copper to steel, and are presumably caused by a bug. Depending on which other subterranean creatures they have access to, their blowdarts will be covered in different poisons, which can vary from mildly annoying cave spider venom to highly dangerous giant cave spider toxins. You can preemptively check for poisons by selecting a blowgunner, looking in their items tab and viewing their blowdarts.

Serpent men may launch group attacks on your fort. When this happens, all tribesmen on the map will become hostile, even if they were peaceful minutes prior to the invasion. They may arrive with pets and mounts, some of which will be able to fly or easily catch up to your fleeing civilians. These invaders, unlike their above-ground counterparts, will not leave after some time has passed, even if your fort is completely sealed off from the caverns, nor will they prevent migrants, caravans or other invaders from arriving; including more waves of serpent men. Because of this, several unchallenged assaults from them can quickly cause your game's FPS to drop to single-digit levels, thus making your fort completely unplayable.

Serpent men are amphibious. That means that they can swim through your reservoirs in order to get through your defenses, or lie in wait to ambush your fisherdwarves, so plan your defenses accordingly. Fortunately, it turns out that being in the water washes any blowdarts clean of their venom, meaning that blowgunners that travel aquatically will have their threat level minimized. In addition, serpent men possess a poisonous bite which can cause paralysis, thus making their victims vulnerable to both suffocation as well as attacks from other serpent men. Keep in mind that serpent men themselves are completely immune to all forms of paralysis. Despite their description, they do not possess the [`[EVIL]`](/index.php/Creature_token#EVIL "Creature token") token and are not any more malevolent than any other race of animal people.

If you ssspeak to a ssserpent man in adventure mode, they will talk like thisss, becaussse of the [`[LISP]`](/index.php/Creature_token#LISP "Creature token") token.

Some dwarves like serpent men for their *impressive tails*.

Does a great "steam blowing through pipes" impression.\
*Art by Diogeneezy*

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\

"Reports indicate that a suspicious serpent man has been sneaking around the fort in a wooden bin (or bins made of paper sheets). Does anyone have additional information?" -A confused guard

|  |
|----|
| "Serpent man" in other / Languages / Dwarven / : / shethel udos / Elven / : / relira onino / Goblin / : / olsmu ngorûg / Human / : / ithrat abo |

    [CREATURE:SERPENT_MAN]
        [DESCRIPTION:A large white snake with the arms and torso of a man.  These creatures are evil and live far underground.]
        [NAME:serpent man:serpent men:serpent man]
        [CREATURE_TILE:'s'][COLOR:7:0:1]
        [CREATURE_CLASS:POISONOUS]
        [LARGE_ROAMING]
        [BIOME:SUBTERRANEAN_WATER]
        [UNDERGROUND_DEPTH:1:3]
        [FREQUENCY:100]
        [AMPHIBIOUS][UNDERSWIM]
        [LARGE_PREDATOR]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:5:10]
        [FEATURE_ATTACK_GROUP]
        [CAN_LEARN][CAN_SPEAK][LISP]
        [CANOPENDOORS]
        [CARNIVORE]
        [PARALYZEIMMUNE]
        [PREFSTRING:impressive tails]
        [BODY:HUMANOID_LEGLESS_NECK:TAIL_STANCE:2EYES:NOSE:2LUNGS:HEART:GUTS:ORGANS:HUMANOID_JOINTS:THROAT:NECK:SPINE:BRAIN:SKULL:4FINGERS:MOUTH:FORKED_TONGUE:GENERIC_TEETH_WITH_FANGS:RIBCAGE]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
            [REMOVE_MATERIAL:HAIR]
            [REMOVE_MATERIAL:SKIN]
            [REMOVE_MATERIAL:LEATHER]
            [REMOVE_MATERIAL:PARCHMENT]
            [USE_MATERIAL_TEMPLATE:SCALE:SCALE_TEMPLATE]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
            [REMOVE_TISSUE:HAIR]
            [REMOVE_TISSUE:SKIN]
            [USE_TISSUE_TEMPLATE:SCALE:SCALE_TEMPLATE]
        [BODY_DETAIL_PLAN:VERTEBRATE_TISSUE_LAYERS:SCALE:FAT:MUSCLE:BONE:CARTILAGE]
        [USE_MATERIAL_TEMPLATE:NAIL:NAIL_TEMPLATE]
        [USE_TISSUE_TEMPLATE:NAIL:NAIL_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:FINGER:NAIL:FRONT]
        [BODY_DETAIL_PLAN:LEATHERY_EGG_MATERIALS]
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
        [USE_MATERIAL_TEMPLATE:VENOM:CREATURE_EXTRACT_TEMPLATE]
            [STATE_NAME:ALL_SOLID:frozen serpent man venom]
            [STATE_ADJ:ALL_SOLID:frozen serpent man venom]
            [STATE_NAME:LIQUID:serpent man venom]
            [STATE_ADJ:LIQUID:serpent man venom]
            [STATE_NAME:GAS:boiling serpent man venom]
            [STATE_ADJ:GAS:boiling serpent man venom]
            [PREFIX:NONE]
            [ENTERS_BLOOD]
            [SYNDROME]
                [SYN_NAME:serpent man bite]
                [SYN_AFFECTED_CLASS:GENERAL_POISON]
                [SYN_IMMUNE_CREATURE:SERPENT_MAN:ALL]
                [SYN_INJECTED]
                [CE_PARALYSIS:SEV:100:PROB:100:RESISTABLE:SIZE_DILUTES:START:5:PEAK:10:END:20]
        [BODY_SIZE:0:0:1500]
        [BODY_SIZE:1:168:10000]
        [BODY_SIZE:12:0:50000]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:60:80]
        [ATTACK:PUNCH:BODYPART:BY_TYPE:GRASP]
            [ATTACK_SKILL:GRASP_STRIKE]
            [ATTACK_VERB:punch:punches]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_FLAG_WITH]
            [ATTACK_PRIORITY:SECOND]
        [ATTACK:KICK:BODYPART:BY_TYPE:STANCE]
            [ATTACK_SKILL:STANCE_STRIKE]
            [ATTACK_VERB:lash:lashes]
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
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_FLAG_CANLATCH]
            [SPECIALATTACK_INJECT_EXTRACT:LOCAL_CREATURE_MAT:VENOM:LIQUID:100:100]
        [BABY:1]
        [CHILD:12]
        [EQUIPS]
        [ALL_ACTIVE]
        [LOW_LIGHT_VISION:10000]
        [APPLY_CREATURE_VARIATION:STANDARD_WALK_CRAWL_GAITS:900:750:600:439:1900:2900] 20 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [SWIMS_INNATE]
        [CANNOT_JUMP]
        [HOMEOTHERM:10040]
        [CASTE:FEMALE]
            [CASTE_NAME:serpent woman:serpent women:serpent woman]
            [FEMALE]
            [MULTIPLE_LITTER_RARE]
            [LAYS_EGGS]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGGSHELL:SOLID]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGG_WHITE:LIQUID]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGG_YOLK:LIQUID]
                [EGG_SIZE:1600]
                [CLUTCH_SIZE:1:3]
        [CASTE:MALE]
            [CASTE_NAME:serpent man:serpent men:serpent man]
            [MALE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SCALE]
                [TL_COLOR_MODIFIER:WHITE:1]
                    [TLCM_NOUN:scales:PLURAL]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]

    Entity (
    civilization
    ) Raws

    [ENTITY:SUBTERRANEAN_ANIMAL_PEOPLES]
        [LAYER_LINKED]
        [CREATURE:AMPHIBIAN_MAN]
        [CREATURE:REPTILE_MAN]
        [CREATURE:SERPENT_MAN]
        [CREATURE:RODENT MAN]
        [CREATURE:BAT_MAN]
        [CREATURE:ANT_MAN]
        [CREATURE:OLM_MAN]
        [CREATURE:CAVE_SWALLOW_MAN]
        [CREATURE:CAVE_FISH_MAN]
        [WEAPON:ITEM_WEAPON_SPEAR]
        [WEAPON:ITEM_WEAPON_BLOWGUN]
            [AMMO:ITEM_AMMO_BLOWDARTS]
        [SHIELD:ITEM_SHIELD_SHIELD]
        [SHIELD:ITEM_SHIELD_BUCKLER]
        [WOOD_WEAPONS]
        [WOOD_ARMOR] shields
        [USE_ANY_PET_RACE]
        [INDOOR_WOOD]
        [USE_CAVE_ANIMALS]
        [USE_ANIMAL_PRODUCTS]
        [EQUIPMENT_IMPROVEMENTS]
        [FRIENDLY_COLOR:1:0:1]
        no site or biome or attack info for now
        [MAX_STARTING_CIV_NUMBER:100] all irrelevant right now
        [MAX_POP_NUMBER:10000]
        [MAX_SITE_POP_NUMBER:120]
        [PERMITTED_JOB:CARPENTER]
        [PERMITTED_JOB:WOODCUTTER]
        [PERMITTED_JOB:ANIMAL_CARETAKER]
        [PERMITTED_JOB:ANIMAL_TRAINER]
        [PERMITTED_JOB:HUNTER]
        [PERMITTED_JOB:WOODCRAFTER]
        [PERMITTED_JOB:LEATHERWORKER]
        [PERMITTED_JOB:BONE_CARVER]
        [PERMITTED_JOB:FISHERMAN]
        [PERMITTED_JOB:FISH_CLEANER]
        [PERMITTED_JOB:COOK]
        [PERMITTED_JOB:BUTCHER]
        [PERMITTED_JOB:TANNER]
        [PERMITTED_REACTION:TAN_A_HIDE]
        *** ethics copied from kobolds for now
        [ETHIC:KILL_ENTITY_MEMBER:PUNISH_EXILE]
        [ETHIC:KILL_NEUTRAL:REQUIRED]
        [ETHIC:KILL_ENEMY:REQUIRED]
        [ETHIC:KILL_ANIMAL:ACCEPTABLE]
        [ETHIC:KILL_PLANT:ACCEPTABLE]
        [ETHIC:TORTURE_AS_EXAMPLE:UNTHINKABLE]
        [ETHIC:TORTURE_FOR_INFORMATION:NOT_APPLICABLE]
        [ETHIC:TORTURE_FOR_FUN:ACCEPTABLE]
        [ETHIC:TORTURE_ANIMALS:UNTHINKABLE]
        [ETHIC:TREASON:UNTHINKABLE]
        [ETHIC:OATH_BREAKING:NOT_APPLICABLE]
        [ETHIC:LYING:NOT_APPLICABLE]
        [ETHIC:VANDALISM:NOT_APPLICABLE]
        [ETHIC:TRESPASSING:NOT_APPLICABLE]
        [ETHIC:THEFT:NOT_APPLICABLE]
        [ETHIC:ASSAULT:PERSONAL_MATTER]
        [ETHIC:SLAVERY:UNTHINKABLE]
        [ETHIC:EAT_SAPIENT_OTHER:UNTHINKABLE]
        [ETHIC:EAT_SAPIENT_KILL:UNTHINKABLE]
        [ETHIC:MAKE_TROPHY_SAME_RACE:UNTHINKABLE]
        [ETHIC:MAKE_TROPHY_SAPIENT:UNTHINKABLE]
        [ETHIC:MAKE_TROPHY_ANIMAL:UNTHINKABLE]
        *** later
        [VALUE:LAW:0]
        [VALUE:LOYALTY:0]
        [VALUE:FAMILY:0]
        [VALUE:FRIENDSHIP:0]
        [VALUE:POWER:0]
        [VALUE:TRUTH:0]
        [VALUE:CUNNING:0]
        [VALUE:ELOQUENCE:0]
        [VALUE:FAIRNESS:0]
        [VALUE:DECORUM:0]
        [VALUE:TRADITION:0]
        [VALUE:ARTWORK:0]
        [VALUE:COOPERATION:0]
        [VALUE:INDEPENDENCE:0]
        [VALUE:STOICISM:0]
        [VALUE:KNOWLEDGE:0]
        [VALUE:INTROSPECTION:0]
        [VALUE:SELF_CONTROL:0]
        [VALUE:TRANQUILITY:0]
        [VALUE:HARMONY:0]
        [VALUE:MERRIMENT:0]
        [VALUE:CRAFTSMANSHIP:0]
        [VALUE:MARTIAL_PROWESS:0]
        [VALUE:SKILL:0]
        [VALUE:HARD_WORK:0]
        [VALUE:SACRIFICE:0]
        [VALUE:COMPETITION:0]
        [VALUE:PERSEVERANCE:0]
        [VALUE:LEISURE_TIME:0]
        [VALUE:COMMERCE:0]
        [VALUE:ROMANCE:0]
        [VALUE:NATURE:0]
        [VALUE:PEACE:0]
        [AMBUSHER]
        [STONE_SHAPE:OVAL_CABOCHON]
        [GEM_SHAPE:OVAL_CABOCHON]
