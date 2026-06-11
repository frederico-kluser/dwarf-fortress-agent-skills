# Blind cave ogre

> Fonte: [Blind cave ogre](https://dwarffortresswiki.org/index.php/Blind_cave_ogre) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes blind cave ogres for their echoing howls.**
- **Biome**
- **Underground Depth: 2-3**
- **Attributes**
- **Alignment:** Evil
- **Building destroyer : Level 2**
- **Learns · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 250,000 cm 3
- **Mid:** 2,500,000 cm 3
- **Max:** 7,000,000 cm 3
- **Age**
- **Child at:** 1
- **Adult at:** 10
- **Max age:** 20-30
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A large cavern-dwelling humanoid monster. It has a gaping mouth with many sharp teeth. It has no eyes and only two digits on each hand and foot.*

**Blind cave ogres** are huge, violent humanoids found in deep caverns. They are highly aggressive and will gleefully destroy anything that isn't a wall or a fortification between them and your dwarves. Blind cave ogres will arrive at your fortress in groups of one to three mayhem-minded individuals, and despite being "blind" they have [`[EXTRAVISION]`](/index.php/Creature_token#EXTRAVISION "Creature token") and thus are quite capable of sensing exactly where your doors are. Incredibly, they are able to swim.

You do **not** want to underestimate these monsters. They are nearly as big as giants, significantly larger than elephants, and can easily kill even the most seasoned of warrior-dwarves in single combat. Engage them with traps, crossbows, and large numbers if possible. The blind cave ogre's propensity for destruction can be used against it. If you would like to capture one for use in a cunning plan, lay down some cage traps in a narrow passage guarding access to your main fortress and the ogres will soon be caught. In addition they have been known to equip weapons and armor from dead bodies. An ogre with weapons and armor is significantly more deadly than one without them.

Blind cave ogres possess a pet value of 500, but lack the necessary tokens to be trainable (and even if modded to be trainable, the fact they are intelligent creatures will lead to strange behavior). They are intelligent enough that dwarves refuse to butcher them, and are able to learn skills at half the rate of a civilized creature, though they are not capable of speech. They can't be spawned in the object testing arena.

Despite being blind, they can still "see" or "sense" bodies nearby.[1]

Some dwarves like blind cave ogres for their *echoing howls*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Blind cave ogres enjoy updating their fashion while brutally smashing their victims. They can grab weapons off your freshly pulverized dwarves, but more often than not, they grab a fashionable glove or pair of trousers. Then, with their new set of duds, they start beating their victims ever more viciously. Sometimes these fashionable ogres will enjoy beating a crippled dwarf for months, leaving your other dwarves in relative peace. At least until their plaything dies.

## Gallery

-

  *Art by Arne.*

-

  "Giant two-toed blind troll-thing." Dwarf for scale.\
  *Concept art by Bay 12 Games.*

-

  Sprites before 53.04.

    [CREATURE:BLIND_CAVE_OGRE]
        [ARENA_RESTRICTED]
        [DESCRIPTION:A large cavern-dwelling humanoid monster.  It has a gaping mouth with many sharp teeth.  It has no eyes and only two digits on each hand and foot.]
        [NAME:blind cave ogre:blind cave ogres:blind cave ogre]
        [CASTE_NAME:blind cave ogre:blind cave ogres:blind cave ogre]
        [CREATURE_TILE:'O'][COLOR:7:0:1]
        [CREATURE_CLASS:MAMMAL]
        [BIOME:SUBTERRANEAN_CHASM]
        [UNDERGROUND_DEPTH:2:3]
        [LARGE_ROAMING]
        [PETVALUE:500]
        [EVIL]
        [DIFFICULTY:4][FREQUENCY:50]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:3]
        [BUILDINGDESTROYER:2]
        [LARGE_PREDATOR][MEANDERER]
        [CAN_LEARN][SLOW_LEARNER]
        [GRASSTRAMPLE:20]
        [BONECARN]
        [EXTRAVISION]
        [PREFSTRING:echoing howls]
        [BODY:HUMANOID_NECK:2EARS:NOSE:2LUNGS:HEART:GUTS:ORGANS:HUMANOID_JOINTS:THROAT:NECK:SPINE:BRAIN:SKULL:2FINGERS:2TOES:MOUTH:TONGUE:FACIAL_FEATURES:TEETH:RIBCAGE]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
        [BODY_DETAIL_PLAN:VERTEBRATE_TISSUE_LAYERS:SKIN:FAT:MUSCLE:BONE:CARTILAGE]
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
        [BODY_SIZE:0:0:250000]
        [BODY_SIZE:1:168:2500000]
        [BODY_SIZE:20:0:7000000]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:20:30]
        [CHILD:10][BABY:1][MULTIPLE_LITTER_RARE]
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
        [ATTACK:BITE:CHILD_BODYPART_GROUP:BY_CATEGORY:HEAD:BY_CATEGORY:TOOTH]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:bite:bites]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_CANLATCH]
        [EQUIPS]
        [CANOPENDOORS]
        [ALL_ACTIVE]
        [HOMEOTHERM:10040]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:730:561:351:1900:2900] 25 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [SWIMS_INNATE]
        [CASTE:FEMALE]
            [FEMALE]
            [MULTIPLE_LITTER_RARE]
        [CASTE:MALE]
            [MALE]
            [SET_BP_GROUP:BY_TYPE:LOWERBODY][BP_ADD_TYPE:GELDABLE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
                [TL_COLOR_MODIFIER:WHITE:1]
                    [TLCM_NOUN:skin:SINGULAR]
