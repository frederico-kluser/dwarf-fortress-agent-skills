# Antman

> Fonte: [Antman](https://dwarffortresswiki.org/index.php/Antman) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes antmen for their mystery.**
- **Biome**
- **Underground Depth: 1-3**
- **Attributes**
- **Flying · Learns · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 1,000 cm 3
- **Mid:** 5,000 cm 3
- **Max:** 20,000 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 5-8
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A humanoid with the head and body of an ant.*

**Antmen** are one of the many races of underground tribal animal people found living in small groups on any cavern level. They can be thought of as humanoid versions of the common ant, but are not formed in the way of most animal people as variations of their base creatures. The antman is more like the serpent man, reptile man, amphibian man, and rodent man in this regard.

Antmen form worker, soldier, drone and queen castes. Antmen workers are the most common antmen, no larger than a kobold. The all-male drones are the same size as workers and are additionally capable of flight. Soldiers can grow to be almost as large as a dwarf. The queen, as big as a lion, is the only breeding female among antmen. Oddly enough, Antmen queens give live birth instead of laying eggs.

Despite being labelled as hostile in the unit list, antmen initially found in the caverns will ignore your citizens unless provoked. They will usually be observed carrying wooden spears, blowguns and shields, although they are sometimes seen using metal items instead. These can range from copper to steel, and are presumably caused by a bug. Depending on which other subterranean creatures they have access to, their blowdarts will be covered in different poisons, which can vary from mildly annoying cave spider venom to highly dangerous giant cave spider toxins. You can preemptively check for poisons by selecting a blowgunner, looking in their items tab and viewing their blowdarts.

Compared to most humanoids, antmen have an extremely short lifespan, allowing a patient player to simply wait for them to die of old age rather than confront them. As previously mentioned, antmen drones can fly, meaning that they will be able to fly over your walls, or through gaps in your floors and ceilings, so plan your defenses accordingly. This can also make them marginally harder to hit than other creatures of their size.

Some dwarves like antmen for their *mystery*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Although Antmen do not appear to have any notable writing system, humans frequently attempt to get their signatures, citing them as being some sort of great heroes. Records on their supposed escapades are found solely in human codices, often pitted against some sort of Beeman. To date, no Beemen have been discovered by dwarf-kind. Additionally, many humans believe that antmen are capable of shrinking. No evidence of this has been discovered, either.

Still afraid of giant magnifying glasses.\
*Art by Devilingo*

    [CREATURE:ANT_MAN]
        [DESCRIPTION:A humanoid with the head and body of an ant.]
        [NAME:antman:antmen:antman]
        [CREATURE_TILE:'a'][COLOR:0:0:1]
        [LARGE_ROAMING]
        [FREQUENCY:100]
        [FEATURE_ATTACK_GROUP]
        [BIOME:SUBTERRANEAN_CHASM]
        [UNDERGROUND_DEPTH:1:3]
        [CAN_LEARN][CAN_SPEAK]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:5:10]
        [PREFSTRING:mystery]
        [EQUIPS]
        [CANOPENDOORS]
        [LARGE_PREDATOR]
        [ALL_ACTIVE]
        [LOW_LIGHT_VISION:10000]
        [NO_SLEEP]
        [HOMEOTHERM:10040]
        [USE_MATERIAL_TEMPLATE:SINEW:SINEW_TEMPLATE]
        [TENDONS:LOCAL_CREATURE_MAT:SINEW:200]
        [LIGAMENTS:LOCAL_CREATURE_MAT:SINEW:200]
        [HAS_NERVES]
        [USE_MATERIAL_TEMPLATE:ICHOR:ICHOR_TEMPLATE]
        [BLOOD:LOCAL_CREATURE_MAT:ICHOR:LIQUID]
        [CREATURE_CLASS:GENERAL_POISON]
        [GETS_WOUND_INFECTIONS]
        [GETS_INFECTIONS_FROM_ROT]
        [USE_MATERIAL_TEMPLATE:PUS:PUS_TEMPLATE]
        [PUS:LOCAL_CREATURE_MAT:PUS:LIQUID]
        [MAXAGE:5:8]
        [NOBONES]
        [CASTE:WORKER]
            [CASTE_NAME:worker ant woman:worker ant women:worker ant woman]
            Female, but non-breeding.
            [POP_RATIO:10000]
        [CASTE:SOLDIER]
            [CASTE_NAME:soldier ant woman:soldier ant women:soldier ant woman]
            Female, but non-breeding.
            [POP_RATIO:1000]
        [CASTE:DRONE]
            [MALE]
            [CASTE_NAME:drone ant man:drone ant men:drone ant man]
            [POP_RATIO:5]
        [CASTE:QUEEN]
            [FEMALE]
            [CASTE_NAME:queen ant woman:queen ant women:queen ant woman]
            [POP_RATIO:1]
        [SELECT_CASTE:WORKER]
         [SELECT_ADDITIONAL_CASTE:SOLDIER]
         [SELECT_ADDITIONAL_CASTE:QUEEN]
            [BODY:HUMANOID_4ARMS:2EYES:HEART:GUTS:BRAIN:MOUTH]
            [BODYGLOSS:INSECT_UPPERBODY:INSECT_LOWERBODY]
            [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:711:521:293:1900:2900] 30 kph
            [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
            [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [SELECT_CASTE:DRONE]
            [BODY:HUMANOID_4ARMS:2EYES:HEART:GUTS:BRAIN:MOUTH:2WINGS]
            [BODYGLOSS:INSECT_UPPERBODY:INSECT_LOWERBODY]
            [FLIER]
            [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:711:521:293:1900:2900] 30 kph
            [APPLY_CREATURE_VARIATION:STANDARD_FLYING_GAITS:900:711:521:293:1900:2900] 30 kph
            [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
            [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [SELECT_CASTE:ALL]
            [BODY_DETAIL_PLAN:CHITIN_MATERIALS]
            [BODY_DETAIL_PLAN:CHITIN_TISSUES]
            [BODY_DETAIL_PLAN:EXOSKELETON_TISSUE_LAYERS:CHITIN:FAT:MUSCLE]
            [BODY_DETAIL_PLAN:STANDARD_HEAD_POSITIONS]
            [ATTACK:PUNCH:BODYPART:BY_TYPE:GRASP]
                [ATTACK_SKILL:GRASP_STRIKE]
                [ATTACK_VERB:punch:punches]
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
            [ATTACK:BITE:BODYPART:BY_CATEGORY:MOUTH]
                [ATTACK_SKILL:BITE]
                [ATTACK_VERB:bite:bites]
                [ATTACK_CONTACT_PERC:100]
                [ATTACK_PENETRATION_PERC:100]
                [ATTACK_FLAG_EDGE]
                [ATTACK_PREPARE_AND_RECOVER:3:3]
                [ATTACK_PRIORITY:MAIN]
                [ATTACK_FLAG_CANLATCH]
            [SET_TL_GROUP:BY_CATEGORY:ALL:CHITIN]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:chitin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
        [SELECT_CASTE:WORKER]
            [BODY_SIZE:0:0:1000]
            [BODY_SIZE:1:168:5000]
            [BODY_SIZE:2:0:20000]
        [SELECT_CASTE:SOLDIER]
            [BODY_SIZE:0:0:1500]
            [BODY_SIZE:1:168:10000]
            [BODY_SIZE:2:0:50000]
        [SELECT_CASTE:QUEEN]
            [BODY_SIZE:0:0:10000]
            [BODY_SIZE:1:168:50000]
            [BODY_SIZE:2:0:200000]
        [SELECT_CASTE:DRONE]
            [BODY_SIZE:0:0:1000]
            [BODY_SIZE:1:168:5000]
            [BODY_SIZE:2:0:20000]

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
