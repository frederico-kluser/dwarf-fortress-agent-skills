# Manera

> Fonte: [Manera](https://dwarffortresswiki.org/index.php/Manera) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes maneras for their long arms.**
- **Biome**
- **Underground Depth: 2**
- **Attributes**
- **Alignment:** Evil
- **Learns**
- **Cannot be tamed**
- **Size**
- **Birth:** 2,000 cm 3
- **Mid:** 20,000 cm 3
- **Max:** 60,000 cm 3
- **Age**
- **Adult at:** 2
- **Max age:** 20-30
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A creature that crawls along the cavern ceiling with four long arms. Its body is shaped as the head of a man with a mouth full of shark teeth. It waits for its prey to pass below.*

**Maneras** are rare, evil-aligned, four-armed creatures found in subterranean caverns, exclusively on the second layer and occasionally in sieges. When spawning in the caverns, they spawn one at a time and lurk in the underground, occasionally pathing to your fortress and attacking dwarves who may cross their way. Maneras are the size of a dwarf and may prove a threat to civilians, but an equipped military squad will make quick work of them. All maneras are born with Legendary skill in climbing.

Maneras are intelligent creatures, capable of learning at half the speed of a civilized one, but are not capable of speech. Because of this, dwarves will not butcher them, limiting their use to live training and occupying space in your refuse stockpile. Сivilized maneras may gain non-military professions among goblin society, but can also appear in goblin sieges. They can't be spawned in the object testing arena.

Maneras, along with trolls, ogres, and blizzard men, can act as livestock for evil civilizations with access to them.

Some dwarves like maneras for their *long arms*.

## Gallery

-

  *Art by Kruggsmash*.

-

  *Concept art by Bay 12 Games.*

    [CREATURE:MANERA]
        [ARENA_RESTRICTED]
        [DESCRIPTION:A creature that crawls along the cavern ceiling with four long arms.  Its body is shaped as the head of a man with a mouth full of shark teeth.  It waits for its prey to pass below.]
        [NAME:manera:maneras:manera]
        [CASTE_NAME:manera:maneras:manera]
        [CREATURE_TILE:'m'][COLOR:6:0:0]
        [NATURAL]
        [EVIL]
        [CAN_LEARN][SLOW_LEARNER]
        [LARGE_ROAMING][FREQUENCY:10]
        [POPULATION_NUMBER:20:30]
        [CLUSTER_NUMBER:1:1]
        [BIOME:SUBTERRANEAN_CHASM]
        [UNDERGROUND_DEPTH:2:2]
        [PREFSTRING:long arms]
        [BODY:BODY_HEAD:4ARMS_STANCE:2EYES:2EARS:NOSE:2LUNGS:HEART:GUTS:ORGANS:SPINE:BRAIN:SKULL:MOUTH:TONGUE:5FINGERS:GENERIC_TEETH_WITH_LARGE_EYE_TEETH:RIBCAGE:FACIAL_FEATURES]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
            [REMOVE_MATERIAL:HAIR]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
            [REMOVE_TISSUE:HAIR]
        [BODY_DETAIL_PLAN:VERTEBRATE_TISSUE_LAYERS:SKIN:FAT:MUSCLE:BONE:CARTILAGE]
        [USE_MATERIAL_TEMPLATE:NAIL:NAIL_TEMPLATE]
        [USE_TISSUE_TEMPLATE:NAIL:NAIL_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:FINGER:NAIL:FRONT]
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
        [BODY_SIZE:0:0:2000]
        [BODY_SIZE:1:0:20000]
        [BODY_SIZE:2:0:60000]
        [MAXAGE:20:30]
        [ATTACK:BITE:CHILD_BODYPART_GROUP:BY_CATEGORY:HEAD:BY_CATEGORY:TOOTH]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:bite:bites]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_CANLATCH]
        [ATTACK:SCRATCH:CHILD_TISSUE_LAYER_GROUP:BY_TYPE:GRASP:BY_CATEGORY:FINGER:NAIL]
            [ATTACK_SKILL:GRASP_STRIKE]
            [ATTACK_VERB:scratch:scratches]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:SECOND]
        [CHILD:2]
        [ALL_ACTIVE]
        [LOW_LIGHT_VISION:10000]
        [HOMEOTHERM:10050]
        [APPLY_CREATURE_VARIATION:STANDARD_WALK_CRAWL_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2206:1692:1178:585:3400:4900] 15 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [NATURAL_SKILL:CLIMBING:15]
        [SWIMS_INNATE]
        [CASTE:FEMALE]
            [FEMALE]
        [CASTE:MALE]
            [MALE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
                [TL_COLOR_MODIFIER:BROWN:1]
                    [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:IRIS_EYE_YELLOW:1]
                    [TLCM_NOUN:eyes:PLURAL]
