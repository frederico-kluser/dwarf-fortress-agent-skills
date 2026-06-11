# Bugbat

> Fonte: [Bugbat](https://dwarffortresswiki.org/index.php/Bugbat) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes bugbats for their freakish insect heads.**
- **Biome**
- **Underground Depth: 2-3**
- **Attributes**
- **Flying · Humanoid**
- **Tamed Attributes**
- **Pet value:** 20
- **Not hunting/war trainable**
- **Size**
- **Birth:** 1,000 cm 3
- **Mid:** 5,000 cm 3
- **Max:** 10,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 10-20
- **Butchering returns**
- **Food items**
- **Meat:** 10-13
- **Fat:** 10-13
- **Brain:** 1
- **Lungs:** 2
- **Intestines:** 1
- **Liver:** 1
- **Tripe:** 1
- **Raw materials**
- **Bones:** 8-12
- **Skull:** 1
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A small bat-like creature with the head of an insect. It is found deep underground.*

**Bugbats** are small, flying creatures who inhabit the second and third layers of the caverns, appearing in swarms ranging from 5-15 individuals. Only half the size of a kobold, these weird-looking critters will spend their time flying through the underground, fleeing from dwarves who approach them; they are benign and will rarely fight back if confronted. All bugbats are born with Legendary skill in climbing.

Bugbats can be captured in cage traps and trained into low-value pets, reaching their full adult size at 2 years of age, and should be butchered by then for a maximum amount of returns.. They are prolific breeders and appear in large numbers, meaning it's easy to set up a bugbat farm relatively quickly.

Unlike most creatures, they can't be spawned in the object testing arena.

Some dwarves like bugbats for their *freakish insect heads*.

## Gallery

-

  *Art by Quinmael*.

-

  Initially described as being the "size of a fruit bat", though it is much larger in-game.\
  *Concept art by Bay 12 Games.* [1]

-

  Bugbat sprites prior to version 53.07

    [CREATURE:BUGBAT]
        [ARENA_RESTRICTED]
        [DESCRIPTION:A small bat-like creature with the head of an insect.  It is found deep underground.]
        [NAME:bugbat:bugbats:bugbat]
        [CASTE_NAME:bugbat:bugbats:bugbat]
        [CHILD:1][GENERAL_CHILD_NAME:bugbat pup:bugbat pups]
        [CREATURE_TILE:'b'][COLOR:5:0:0]
        [FLIER]
        [PETVALUE:20]
        [PET_EXOTIC]
        [LARGE_ROAMING]
        [POPULATION_NUMBER:20:40]
        [CLUSTER_NUMBER:5:15]
        [BIOME:SUBTERRANEAN_CHASM]
        [UNDERGROUND_DEPTH:2:3]
        [BENIGN]
        [NATURAL]
        [PREFSTRING:freakish insect heads]
        [BODY:HUMANOID_NECK_FLIER:TAIL:2EYES:2LUNGS:HEART:GUTS:ORGANS:THROAT:NECK:SPINE:BRAIN:SKULL:4FINGERS:4TOES:MOUTH:LARGE_MANDIBLES:RIBCAGE]
        [BODYGLOSS:PAW]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
        [BODY_DETAIL_PLAN:VERTEBRATE_TISSUE_LAYERS:SKIN:FAT:MUSCLE:BONE:CARTILAGE]
        [BODY_DETAIL_PLAN:BODY_HAIR_TISSUE_LAYERS:HAIR]
        [USE_MATERIAL_TEMPLATE:NAIL:NAIL_TEMPLATE]
        [USE_TISSUE_TEMPLATE:NAIL:NAIL_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:FINGER:NAIL:FRONT]
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
        [BODY_SIZE:0:0:1000]
        [BODY_SIZE:1:0:5000]
        [BODY_SIZE:2:0:10000]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:10:20]
        [ATTACK:BITE:CHILD_BODYPART_GROUP:BY_CATEGORY:HEAD:BY_CATEGORY:MANDIBLE]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:bite:bites]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_CANLATCH]
        [ALL_ACTIVE]
        [LOW_LIGHT_VISION:10000]
        [HOMEOTHERM:10067]
        [APPLY_CREATURE_VARIATION:STANDARD_FLYING_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:7780:7508:7254:2925:8478:9233] 3 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:7780:7508:7254:2925:8478:9233] 3 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:7780:7508:7254:2925:8478:9233] 3 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:7780:7508:7254:2925:8478:9233] 3 kph
        [NATURAL_SKILL:CLIMBING:15]
        [SWIMS_INNATE]
        [CASTE:FEMALE]
            [FEMALE]
        [CASTE:MALE]
            [MALE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:HAIR]
                [TL_COLOR_MODIFIER:DARK_VIOLET:1]
                    [TLCM_NOUN:hair:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
                [TL_COLOR_MODIFIER:TAUPE_PALE:1]
                    [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
