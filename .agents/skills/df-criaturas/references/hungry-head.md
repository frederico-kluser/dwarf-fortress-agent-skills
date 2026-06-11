# Hungry head

> Fonte: [Hungry head](https://dwarffortresswiki.org/index.php/Hungry_head) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes hungry heads for their terrifying features.**
- **Biome**
- **Underground Depth: 3**
- **Attributes**
- **Flying**
- **Cannot be tamed**
- **Size**
- **Birth:** 200 cm 3
- **Mid:** 2,000 cm 3
- **Max:** 5,000 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 10-20
- **Butchering returns**
- **Food items**
- **Meat:** 3
- **Fat:** 3
- **Brain:** 0-1
- **Lungs:** 2
- **Intestines:** 1
- **Liver:** 0-1
- **Tripe:** 0-1
- **Raw materials**
- **Bones:** 2
- **Skull:** 1
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A fearsome, long-toothed mouth the size of a man's head, flying on bat wings. It is found in deep caves.*

**Hungry heads** are flying pests found in the third cavern layer, in groups of 5-10 individuals, and similar to crundles and troglodytes in their abundance and lethality, being different only in that they can fly and have only three outside body-parts (a head and two wings). Despite having no visible eyes, they have full 360° vision. They do not pose much danger to adventurers or decently equipped military, though their ability to fly can make them a job-interrupting nuisance in fortress mode and you may occasionally lose a civilian dwarf to them if you do not take care.

Hungry heads possess a pet value of 50, but lack the necessary tokens to be trainable. All members of the species possess Legendary skill in climbing. They can't be spawned in the object testing arena.

Some dwarves like hungry heads for their *terrifying features*.

|  |
|----|
| "Hungry head" in other / Languages / Dwarven / : / fokásh ser / Elven / : / ume íne / Goblin / : / esno ostam / Human / : / ubac aru |

## Gallery

-

  Admired for its *terrifying features*.\
  *Art by rhesusmacabre*

-

  *Concept art by Bay 12 Games.*

    [CREATURE:HUNGRY_HEAD]
        [ARENA_RESTRICTED]
        [DESCRIPTION:A fearsome, long-toothed mouth the size of a man's head, flying on bat wings.  It is found in deep caves.]
        [NAME:hungry head:hungry heads:hungry head]
        [CASTE_NAME:hungry head:hungry heads:hungry head]
        [CREATURE_TILE:'h'][COLOR:0:0:1]
        [PETVALUE:50]
        [FLIER]
        [LARGE_ROAMING]
        [POPULATION_NUMBER:100:200]
        [CLUSTER_NUMBER:5:10]
        [BIOME:SUBTERRANEAN_CHASM]
        [UNDERGROUND_DEPTH:3:3]
        [LARGE_PREDATOR]
        [NATURAL]
        [EXTRAVISION]
        [CANNOT_JUMP]
        [PREFSTRING:terrifying features]
        [BODY:BODY_HEAD:2WINGS:2LUNGS:HEART:GUTS:ORGANS:BRAIN:SKULL:MOUTH:TONGUE:GENERIC_TEETH_WITH_LARGE_EYE_TEETH]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
        [BODY_DETAIL_PLAN:VERTEBRATE_TISSUE_LAYERS:SKIN:FAT:MUSCLE:BONE:CARTILAGE]
        [BODY_DETAIL_PLAN:BODY_HAIR_TISSUE_LAYERS:HAIR]
        [SELECT_TISSUE_LAYER:HEART:BY_CATEGORY:HEART]
            [TL_MAJOR_ARTERIES]
        [BODY_DETAIL_PLAN:STANDARD_HEAD_POSITIONS]
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
        [APPLY_CREATURE_VARIATION:STANDARD_FLYING_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_WALK_CRAWL_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [STANCE_CLIMBER][NATURAL_SKILL:CLIMBING:15]
        [BODY_SIZE:0:0:200]
        [BODY_SIZE:1:0:2000]
        [BODY_SIZE:2:0:5000]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:10:20]
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
        [CASTE:FEMALE]
            [FEMALE]
        [CASTE:MALE]
            [MALE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:HAIR]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:hair:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:skin:SINGULAR]
