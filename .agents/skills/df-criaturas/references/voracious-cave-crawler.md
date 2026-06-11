# Voracious cave crawler

> Fonte: [Voracious cave crawler](https://dwarffortresswiki.org/index.php/Voracious_cave_crawler) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes voracious cave crawlers for their scary mouths.**
- **Biome**
- **Underground Depth: 2-3**
- **Attributes**
- **Building destroyer : Level 2**
- **Exotic mount**
- **Tamed Attributes**
- **Pet value:** 1,000
- **Not hunting/war trainable**
- **Size**
- **Birth:** 20,000 cm 3
- **Mid:** 400,000 cm 3
- **Max:** 900,000 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 20-40
- **Butchering returns ( Value multiplier ×4)**
- **Food items**
- **Meat:** 19-28
- **Fat:** 7-9
- **Brain:** 2-3
- **Heart:** 1
- **Intestines:** 7-10
- **Raw materials**
- **Teeth:** 1
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge cave monster with hundreds of feet moving along the bottom of its long body. In place of a head, it has an enormous toothy maw.*

**Voracious cave crawlers** are quite nasty creatures that are seen from time to time in caverns, spawning one at a time and being generally voracious to anything in their path. Although lacking the special abilities of other, more reliable sources of fun, they are among the largest creatures found in caverns and as such, will prove a threat to civilians. Voracious cave crawlers do not possess eyes, but can see around themselves through [`[EXTRAVISION]`](/index.php/Creature_token#EXTRAVISION "Creature token").

When they spawn, these beasts will attempt to travel to buildings and destroy them even if they aren't in its line of sight. Because of this trait it is relatively simple to capture cave crawlers: restrict access to your underground buildings, but allow a way through that has cage traps built in the way. They will path through the cage traps and get caught. They are very valuable exotic pets and can be trained with generally no problem. They can be used as a mount by goblin siegers, and are quite dangerous.[\[1\]](/index.php/v0.34_Talk:Voracious_cave_crawler "v0.34 Talk:Voracious cave crawler")

Being invertebrates, voracious cave crawlers have a vulnerable brain and can be killed with a few lucky blows to the head. Voracious cave crawler products are worth four times more than those of other creatures. Despite their description, they do not actually have any feet or even legs. Unlike most beasts, they can't be spawned in the object testing arena.

Some dwarves like voracious cave crawlers for their *scary mouths*.

## Gallery

-

  Stuff of night terrors.

-

  "Giant, quasi-radial, little feet."\
  *Concept art by Bay 12 Games.*

    [CREATURE:VORACIOUS_CAVE_CRAWLER]
        [ARENA_RESTRICTED]
        [DESCRIPTION:A huge cave monster with hundreds of feet moving along the bottom of its long body.  In place of a head, it has an enormous toothy maw.]
        [NAME:voracious cave crawler:voracious cave crawlers:voracious cave crawler]
        [CASTE_NAME:voracious cave crawler:voracious cave crawlers:voracious cave crawler]
        [CREATURE_TILE:'C'][COLOR:1:0:0]
        [BIOME:SUBTERRANEAN_CHASM]
        [UNDERGROUND_DEPTH:2:3]
        [LARGE_ROAMING][DIFFICULTY:2]
        [POPULATION_NUMBER:10:20]
        [CARNIVORE][NATURAL]
        [PETVALUE:1000]
        [PET_EXOTIC]
        [MOUNT_EXOTIC]
        [LARGE_PREDATOR]
        [GRASSTRAMPLE:20]
        [PREFSTRING:scary mouths]
        [BUILDINGDESTROYER:2]
        [NOBONES]
        [BODY:BASIC_1PARTBODY:BASIC_HEAD:TAIL:HEART:GUTS:BRAIN:MOUTH:GENERIC_TEETH]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
            [REMOVE_MATERIAL:HAIR]
            [REMOVE_MATERIAL:BONE]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
            [REMOVE_TISSUE:HAIR]
            [REMOVE_TISSUE:BONE]
        [BODY_DETAIL_PLAN:EXOSKELETON_TISSUE_LAYERS:SKIN:FAT:MUSCLE]
        [USE_MATERIAL_TEMPLATE:ICHOR:ICHOR_TEMPLATE]
        [BLOOD:LOCAL_CREATURE_MAT:ICHOR:LIQUID]
        [SELECT_TISSUE_LAYER:HEART:BY_CATEGORY:HEART]
        [BODY_DETAIL_PLAN:STANDARD_HEAD_POSITIONS]
        [USE_MATERIAL_TEMPLATE:SINEW:SINEW_TEMPLATE]
        [TENDONS:LOCAL_CREATURE_MAT:SINEW:200]
        [LIGAMENTS:LOCAL_CREATURE_MAT:SINEW:200]
        [EXTRAVISION]
        [HAS_NERVES]
        [CANNOT_JUMP]
        [CREATURE_CLASS:GENERAL_POISON]
        [GETS_WOUND_INFECTIONS]
        [GETS_INFECTIONS_FROM_ROT]
        [USE_MATERIAL_TEMPLATE:PUS:PUS_TEMPLATE]
        [PUS:LOCAL_CREATURE_MAT:PUS:LIQUID]
        [BODY_SIZE:0:0:20000]
        [BODY_SIZE:1:0:400000]
        [BODY_SIZE:2:0:900000]
        [BODY_APPEARANCE_MODIFIER:LENGTH:80:95:98:100:102:105:120]
        [MAXAGE:20:40]
        [ATTACK:BITE:CHILD_BODYPART_GROUP:BY_CATEGORY:HEAD:BY_CATEGORY:TOOTH]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:bite:bites]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_CANLATCH]
        [ALL_ACTIVE]
        [HOMEOTHERM:10040]
        [APPLY_CREATURE_VARIATION:STANDARD_WALK_CRAWL_GAITS:2206:1692:1178:585:3400:4900] 15 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [CASTE:FEMALE]
            [FEMALE]
        [CASTE:MALE]
            [MALE]
        [NO_DIZZINESS]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
                [TL_COLOR_MODIFIER:MIDNIGHT_BLUE:1]
                    [TLCM_NOUN:skin:SINGULAR]
        [SELECT_MATERIAL:ALL]
            [MULTIPLY_VALUE:4]
