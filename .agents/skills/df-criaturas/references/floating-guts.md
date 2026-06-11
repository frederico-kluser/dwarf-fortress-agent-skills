# Floating guts

> Fonte: [Floating guts](https://dwarffortresswiki.org/index.php/Floating_guts) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes floating guts for their freakish appearance.**
- **Biome**
- **Underground Depth: 2-3**
- **Attributes**
- **Genderless · No Stun**
- **Tamed Attributes**
- **Pet value:** 10
- **Not hunting/war trainable**
- **Size**
- **Max:** 20,000 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 15-30
- **Butchering returns**
- **Food items**
- **Meat:** 1
- **Fat:** 1
- **Heart:** 1
- **Intestines:** 1
- **Raw materials**
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A transparent and amorphous monster that lives underground. It is small in size and is found crawling across the cavern floor. Its organs appear to be floating inside of its body.*

**Floating guts** are disturbing subterranean creatures that appear to be little more than slimes containing a set of organs, found at the second and third layer of the caverns. Because of this lack of body parts, it's extremely easy to damage organs on them, and thus relatively easy to kill. They have no attacks except for the default push, which may sometimes injure unarmored dwarves.

These can be trained as exotic pets with an animal trainer, having a value of 10. They are genderless, though, and live to a maximum of 30 years, so your supply is limited to what you find on embark. Butchering one will give you a small amount of meat items and some raw hide, so they are of very limited use.

Unlike most creatures, they may not be spawned in the object testing arena.

Some dwarves like floating guts for their *freakish appearance*.

## Gallery

-

  *Art by Arne.*

-

  *Concept art by Bay 12 Games.*

    [CREATURE:FLOATING_GUTS]
        [ARENA_RESTRICTED]
        [DESCRIPTION:A transparent and amorphous monster that lives underground.  It is small in size and is found crawling across the cavern floor.  Its organs appear to be floating inside of its body.]
        [NAME:floating guts:floating guts:floating guts]
        [CASTE_NAME:floating guts:floating guts:floating guts]
        [CREATURE_TILE:'%'][COLOR:7:0:0]
        [BIOME:SUBTERRANEAN_CHASM]
        [UNDERGROUND_DEPTH:2:3]
        [PETVALUE:10]
        [PET_EXOTIC]
        [LARGE_ROAMING]
        [FREQUENCY:10]
        [EXTRAVISION][NOBREATHE][NOSTUN][NONAUSEA][NOEMOTION]
        [NOTHOUGHT]
        [NOBONES]
        [NATURAL]
        [CANNOT_JUMP]
        [POPULATION_NUMBER:250:500]
        [PREFSTRING:freakish appearance]
        [BODY:BASIC_1PARTBODY:HEART:GUTS]
        [NO_THOUGHT_CENTER_FOR_MOVEMENT]
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
        [MAXAGE:15:30]
        [ALL_ACTIVE]
        [NO_SLEEP]
        [NO_DIZZINESS]
        [NO_FEVERS]
        [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
            [TL_COLOR_MODIFIER:CLEAR:1]
                [TLCM_NOUN:skin:SINGULAR]
        [SET_TL_GROUP:BY_CATEGORY:ALL:FAT]
            [TL_COLOR_MODIFIER:CLEAR:1]
                [TLCM_NOUN:fat:SINGULAR]
        [SET_TL_GROUP:BY_CATEGORY:ALL:MUSCLE]
            [TL_COLOR_MODIFIER:CLEAR:1]
                [TLCM_NOUN:fat:SINGULAR]
