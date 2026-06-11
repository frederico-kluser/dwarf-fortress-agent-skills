# Giant earthworm

> Fonte: [Giant earthworm](https://dwarffortresswiki.org/index.php/Giant_earthworm) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant earthworms for their awesome presence.**
- **Biome**
- **Underground Depth: 1-2**
- **Attributes**
- **Genderless**
- **Cannot be tamed**
- **Size**
- **Birth:** 20,000 cm 3
- **Mid:** 100,000 cm 3
- **Max:** 200,000 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 5-7
- **Butchering returns ( Value multiplier ×2)**
- **Food items**
- **Meat:** 40-41
- **Fat:** 13
- **Brain:** 5-6
- **Heart:** 2-3
- **Intestines:** 17-18
- **Raw materials**
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A gigantic version of its tiny cousin, this long, slimy creature tunnels through the rocks deep underground.*

**Giant earthworms** are massive and fairly rare worms found in the first and second layers of the caverns. As heavy as a grizzly bear, these creatures will attack dwarves who provoke them with push attacks, and they are large enough for such attacks to cause heavy damage to unarmored peasants.

Giant earthworms have a pet value of 500, but lack the necessary tokens to be trainable. They give a significant amount of returns when butchered, and products made from them are twice as valuable as products made with normal animal parts, making giant earthworm hunting a profitable decision for a fortress.

They can't be spawned in the object testing arena.

Some dwarves like giant earthworms for their *awesome presence*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\

Legends tell of an intelligent giant earthworm in ☼masterwork☼ armor traversing the stars with his puppy friend. Some of his adventures include racing an intelligent crow, traversing the circus domain of an evil cat, and fighting a scholar with a monkey for a head.

Despite popular belief, giant earthworms will not exist within the foundation of science research centers in Greenland during 2000 and 2001. They are also not known as "grey rock worms". They are also not infected (nor worshiped) by a mythological hive-mind known as "The Tuurngait".

They will also not approach unsuspecting workers from the bottom of outside terrain, nor will they attempt to swallow them whole. There is a myth regarding such worms attacking workers that "travel to different moons to collect scrap metal". Dwarven scholars have confirmed that this is only a myth, and nothing more.

## Gallery

-

  Some kids still get dared to eat them.

-

  *Concept art by Bay 12 Games.*

    [CREATURE:GIANT_EARTHWORM]
        [ARENA_RESTRICTED]
        [DESCRIPTION:A gigantic version of its tiny cousin, this long, slimy creature tunnels through the rocks deep underground.]
        [NAME:giant earthworm:giant earthworms:giant earthworm]
        [CASTE_NAME:giant earthworm:giant earthworms:giant earthworm]
        [CREATURE_TILE:'W'][COLOR:7:0:0]
        [PETVALUE:500]
        [FREQUENCY:20]
        [NATURAL][NOBONES]
        [LARGE_ROAMING]
        [BIOME:SUBTERRANEAN_CHASM]
        [UNDERGROUND_DEPTH:1:2]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:1:1]
        [PREFSTRING:awesome presence]
        [EXTRAVISION]
        [CANNOT_JUMP]
        [BODY:BODY_WITH_HEAD_FLAG:HEART:GUTS:BRAIN:MOUTH]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
            [REMOVE_MATERIAL:HAIR]
            [REMOVE_MATERIAL:BONE]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
            [REMOVE_TISSUE:HAIR]
            [REMOVE_TISSUE:BONE]
        [BODY_DETAIL_PLAN:EXOSKELETON_TISSUE_LAYERS:SKIN:FAT:MUSCLE]
        [HAS_NERVES]
        [APPLY_CREATURE_VARIATION:STANDARD_WALK_CRAWL_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [USE_MATERIAL_TEMPLATE:ICHOR:ICHOR_TEMPLATE]
        [BLOOD:LOCAL_CREATURE_MAT:ICHOR:LIQUID]
        [CREATURE_CLASS:GENERAL_POISON]
        [GETS_WOUND_INFECTIONS]
        [GETS_INFECTIONS_FROM_ROT]
        [USE_MATERIAL_TEMPLATE:PUS:PUS_TEMPLATE]
        [PUS:LOCAL_CREATURE_MAT:PUS:LIQUID]
        [BODY_SIZE:0:0:20000]
        [BODY_SIZE:1:0:100000]
        [BODY_SIZE:2:0:200000]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [MAXAGE:5:7]
        [ALL_ACTIVE]
        [NO_SLEEP]
        [NO_DIZZINESS]
        [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
            [TL_COLOR_MODIFIER:GRAY:1]
                [TLCM_NOUN:skin:SINGULAR]
        [SELECT_MATERIAL:ALL]
            [MULTIPLY_VALUE:2]
