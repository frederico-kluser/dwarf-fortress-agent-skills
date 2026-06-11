# Cave dragon

> Fonte: [Cave dragon](https://dwarffortresswiki.org/index.php/Cave_dragon) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes cave dragons for their large eyes.**
- **Biome**
- **Underground Depth: 3**
- **Attributes**
- **Alignment:** Evil
- **Building destroyer : Level 2**
- **Fire immune · War animals · Hunting animals · Egglaying**
- **Tamed Attributes**
- **Pet value:** 10,000
- **Trainable : Hunting War**
- **Size**
- **Birth:** 6,000 cm 3
- **Max:** 15,000,000 cm 3
- **Food products**
- **Eggs:** 1-3
- **Age**
- **Adult at:** Birth
- **Max age:** Immortal
- **Butchering returns ( Value multiplier ×4)**
- **Food items**
- **Meat:** 247-622
- **Fat:** 35-195
- **Brain:** 12-15
- **Heart:** 6-8
- **Lungs:** 24-32
- **Intestines:** 37-48
- **Liver:** 12-16
- **Kidneys:** 12-14
- **Tripe:** 12-16
- **Sweetbread:** 6-8
- **Eyes:** 2
- **Spleen:** 6-8
- **Raw materials**
- **Bones:** 174-225
- **Skull:** 1
- **Teeth:** 3
- **Skin:** Scales

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A gigantic monster, once a dragon, now adapted to and polluted by the underground. Its wings fall limp at its side. Its face is full of incredibly long teeth. Its eyes are large to penetrate the darkness.*

**Cave dragons** are gigantic evil beasts which were once dragons, but have now adapted to life underground. Unlike their above-ground brethren, they do not breathe dragonfire, but they do possess an immunity to being set on fire. Happily, they are not immune to the effects of a dwarf's best friend or extreme heat in general. They have wings (which lack the ability to fly) and white scales, but besides this are not nearly as dangerous as their above ground cousins (due to being smaller and not breathing fire). Oddly, despite their description, regular dragons do not have wings, much less functional ones, though cave dragons do. All cave dragons are born with Talented skill in fighting, biting, kicking and dodging.

Cave dragons are one of the more dangerous things you can face in the caverns, due to their immense size and their natural fighting skills, and they will make mincemeat out of any dwarf civilian or recruit unfortunate enough to get in their way. Cave dragons are building destroyers which means, among other things, that doors are useless as defense. They should be disposed of as if they were megabeasts, with a well equipped military squad and preferably high numbers. Cave dragons are very rare in the underground, but a goblin siege can bring several to your fort, which may be a lot more fun than you can handle.

Cave dragons are among the largest creatures in the game and the largest species in the underground (larger even than forgotten beasts), and grow into their adult size of 15,000,000cm³ after 1000 years. The butchery values in the right-hand column assume that an adult is being butchered: worlds younger than 1000 years will only have juvenile cave dragons, which drop far less meat. Also note that non-historical cave dragons (such cave dragons encountered in the wild and in sieges) are always generated with an age between 150 and 300. The only cave dragons you will encounter that are older than 300 years are ones who became historical figures.

Despite their gigantic size, cave dragons are still vulnerable to cage traps. They are trainable, provide an insanely wonderful pet value of 10,000 and are very good war animals, due to their natural skills and sheer size. Cave dragons lay eggs, and are marginally easier to start a breeding program with than standard dragons due to being normally spawning creatures. Provided you're lucky enough to get a pair of opposite-sex specimens, you can breed these monsters for yourself and become the envy of every goblin pit in the land - just don't use the hatchlings in fortress defense, as they're born as small as foxes. Cave dragons are born adults, so their offspring cannot be turned fully tame. Additionally, they can't be spawned in the object testing arena.

Some dwarves like cave dragons for their *large eyes* and their *impressive teeth*.

|  |
|----|
| "Cave dragon" in other / Languages / Dwarven / : / äs måmgoz / Elven / : / garetho vutheni / Goblin / : / omo kusnath / Human / : / ngethac tamun |

## Gallery

-

  The *one* thing that can scare you away from adamantine mining.\
  *Art by YuanShing / Shengism*

-

  *Concept art by Bay 12 Games.*

-

  Estimated Cave Dragon size comparison.

    [CREATURE:CAVE_DRAGON]
        [ARENA_RESTRICTED]
        [DESCRIPTION:A gigantic monster, once a dragon, now adapted to and polluted by the underground.  Its wings fall limp at its side.  Its face is full of incredibly long teeth.  Its eyes are large to penetrate the darkness.]
        [NAME:cave dragon:cave dragons:cave draconic]
        [CASTE_NAME:cave dragon:cave dragons:cave draconic]
        [CREATURE_TILE:'D'][COLOR:7:0:1]
        [PETVALUE:10000]
        [PET_EXOTIC]
        [TRAINABLE]
        [EVIL]
        [LARGE_ROAMING]
        [BIOME:SUBTERRANEAN_CHASM]
        [UNDERGROUND_DEPTH:3:3]
        [POPULATION_NUMBER:2:5][DIFFICULTY:10]
        [CLUSTER_NUMBER:1:1]
        [FREQUENCY:5]
        [FIREIMMUNE_SUPER]
        [LARGE_PREDATOR]
        [NOFEAR]
        [BUILDINGDESTROYER:2]
        [GRASSTRAMPLE:50]
        [BONECARN]
        [PREFSTRING:impressive teeth]
        [PREFSTRING:large eyes]
        [BODY:QUADRUPED_NECK:TAIL:2WINGS:2EYES:NOSE:2LUNGS:HEART:GUTS:ORGANS:THROAT:NECK:SPINE:BRAIN:SKULL:5TOES_FQ_REG:5TOES_RQ_REG:MOUTH:TONGUE:GENERIC_TEETH_WITH_LARGE_EYE_TEETH:RIBCAGE]
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
        [USE_MATERIAL_TEMPLATE:BLOOD:BLOOD_TEMPLATE]
        [BLOOD:LOCAL_CREATURE_MAT:BLOOD:LIQUID]
        [CREATURE_CLASS:GENERAL_POISON]
        [GETS_WOUND_INFECTIONS]
        [GETS_INFECTIONS_FROM_ROT]
        [USE_MATERIAL_TEMPLATE:PUS:PUS_TEMPLATE]
        [PUS:LOCAL_CREATURE_MAT:PUS:LIQUID]
        [BODY_SIZE:0:0:6000]
        [BODY_SIZE:1000:0:15000000]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [ATTACK:BITE:CHILD_BODYPART_GROUP:BY_CATEGORY:HEAD:BY_CATEGORY:TOOTH]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:bite:bites]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_CANLATCH]
        [ATTACK:CLAW:CHILD_TISSUE_LAYER_GROUP:BY_TYPE:STANCE:BY_CATEGORY:ALL:CLAW]
            [ATTACK_SKILL:GRASP_STRIKE]
            [ATTACK_VERB:claw:claws]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:MAIN]
        [ALL_ACTIVE]
        [LOW_LIGHT_VISION:10000]
        [NATURAL_SKILL:BITE:6]
        [NATURAL_SKILL:GRASP_STRIKE:6]
        [NATURAL_SKILL:MELEE_COMBAT:6]
        [NATURAL_SKILL:DODGING:6]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:750:600:439:1900:2900] 20 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [SWIMS_INNATE]
        [HOMEOTHERM:10040]
        [CASTE:FEMALE]
            [FEMALE]
            [LAYS_EGGS]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGGSHELL:SOLID]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGG_WHITE:LIQUID]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGG_YOLK:LIQUID]
                [EGG_SIZE:6100]
                [CLUTCH_SIZE:1:3]
        [CASTE:MALE]
            [MALE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SCALE]
                [TL_COLOR_MODIFIER:WHITE:1]
                    [TLCM_NOUN:scales:PLURAL]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:IRIS_EYE_GREEN:1]
                    [TLCM_NOUN:eyes:PLURAL]
        [SELECT_MATERIAL:ALL]
            [MULTIPLY_VALUE:4]
