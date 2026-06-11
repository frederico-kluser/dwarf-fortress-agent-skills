# Blind cave bear

> Fonte: [Blind cave bear](https://dwarffortresswiki.org/index.php/Blind_cave_bear) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes blind cave bears for their drooping ears.**
- **Biome**
- **Underground Depth: 1-2**
- **Attributes**
- **Exotic mount**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 20,000 cm 3
- **Mid:** 100,000 cm 3
- **Max:** 200,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 20-30
- **Butchering returns ( Value multiplier ×3)**
- **Food items**
- **Meat:** 14
- **Fat:** 13
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
- **Bones:** 17
- **Skull:** 1
- **Teeth:** 2
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge emaciated-looking bear with great drooping ears and many sharp teeth. It is found deep underground.*

**Blind cave bears** are large subterranean predators that appear only one at a time to hunt dwarves. Unlike bears of the surface world (black bears, grizzly bears or polar bears), blind cave bears are not attracted by food or drink and cannot be lured into traps with anything less than either blind luck or a strategically placed kitten on a rope. They are not actually blind, at least not really, possessing the [`[EXTRAVISION]`](/index.php/Creature_token#EXTRAVISION "Creature token") tag despite having no eyes - the end result is that (ironically) they cannot be blinded. They are also of the [`[LARGE_PREDATOR]`](/index.php/Creature_token#LARGE_PREDATOR "Creature token") class, which means that they will opportunistically attack any dwarves that approach - unless that dwarf happens to be a great axedwarf in full steel armor, they're not likely to survive the encounter. Compared to most other cavern creatures who can appear in the first cavern layer, blind cave bears are quite uncommon to encounter.

They can be trapped and trained by an animal trainer and make decent pets. They are also useful dead: blind cave bear parts and products are worth three times as much as those of domestic animals, and a single bear will keep a bone carver busy for a while. Goblins have been known to arrive on them during sieges. Unlike most creatures, they can't be spawned in the object testing arena.

Some dwarves like blind cave bears for their *drooping ears*.

*Concept art by Bay 12 Games.*

|  |
|----|
| "Blind cave bear" in other / Languages / Dwarven / : / nural äs uvel / Elven / : / nanotha garetho atha / Goblin / : / ostad omo ron / Human / : / odu ngethac rorec |

    [CREATURE:BLIND_CAVE_BEAR]
        [ARENA_RESTRICTED]
        [DESCRIPTION:A huge emaciated-looking bear with great drooping ears and many sharp teeth.  It is found deep underground.]
        [NAME:blind cave bear:blind cave bears:blind cave bear]
        [CASTE_NAME:blind cave bear:blind cave bears:blind cave bear]
        [CHILD:1][GENERAL_CHILD_NAME:blind cave bear cub:blind cave bear cubs]
        [CREATURE_TILE:'B'][COLOR:7:0:1]
        [CREATURE_CLASS:MAMMAL]
        [PETVALUE:500]
        [PET_EXOTIC]
        [MOUNT_EXOTIC]
        [NATURAL]
        [LARGE_ROAMING][FREQUENCY:10]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:1:1]
        [BIOME:SUBTERRANEAN_CHASM]
        [UNDERGROUND_DEPTH:1:2]
        [LARGE_PREDATOR]
        [MEANDERER]
        [EXTRAVISION]  I wonder if they should still be called eye teeth...  eye socket teeth...
        [PREFSTRING:drooping ears]
        [BODY:QUADRUPED_NECK:TAIL:2EARS:NOSE:2LUNGS:HEART:GUTS:ORGANS:THROAT:NECK:SPINE:BRAIN:SKULL:5TOES_FQ_REG:5TOES_RQ_REG:MOUTH:TONGUE:GENERIC_TEETH_WITH_LARGE_EYE_TEETH:RIBCAGE]
        [BODYGLOSS:PAW]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
        [BODY_DETAIL_PLAN:VERTEBRATE_TISSUE_LAYERS:SKIN:FAT:MUSCLE:BONE:CARTILAGE]
        [USE_MATERIAL_TEMPLATE:NAIL:NAIL_TEMPLATE]
        [USE_TISSUE_TEMPLATE:NAIL:NAIL_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:TOE:NAIL:FRONT]
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
        [BODY_SIZE:0:0:20000]
        [BODY_SIZE:1:0:100000]
        [BODY_SIZE:2:0:200000]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
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
        [ATTACK:SCRATCH:CHILD_TISSUE_LAYER_GROUP:BY_TYPE:STANCE:BY_CATEGORY:ALL:NAIL]
            [ATTACK_SKILL:GRASP_STRIKE]
            [ATTACK_VERB:scratch:scratches]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:SECOND]
        [DIURNAL]
        [HOMEOTHERM:10062]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [SWIMS_INNATE]
        [CASTE:FEMALE]
            [FEMALE]
        [CASTE:MALE]
            [MALE]
            [SET_BP_GROUP:BY_TYPE:LOWERBODY][BP_ADD_TYPE:GELDABLE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
                [TL_COLOR_MODIFIER:WHITE:1]
                    [TLCM_NOUN:skin:SINGULAR]
        [SELECT_MATERIAL:ALL]
            [MULTIPLY_VALUE:3]
