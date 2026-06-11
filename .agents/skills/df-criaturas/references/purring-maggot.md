# Purring maggot

> Fonte: [Purring maggot](https://dwarffortresswiki.org/index.php/Purring_maggot) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes purring maggots for their comforting whirs.**
- **Biome**
- **Underground Depth: 2-3**
- **Attributes**
- **Exotic pet · Hateable · Milkable**
- **Pet value:** 10
- **Active Seasons**
- **Spring Summer Autumn Winter**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A tiny larva which is prized for its milk.*

**Purring maggots** are a type of cavern-living vermin notable for being the only underground source of milk, known as dwarven milk. They can be obtained by trapping them with animal traps. They are hateable vermin and will inspire an unhappy thought in dwarves that detest them.

To obtain these maggots, you will need to discover the 2nd or 3rd cavern layer, then construct (brt) animal traps on cave moss there, baiting them with meat or fish. A higher quality trap will increase the chances of catching a purring maggot instead of losing the bait.

Some dwarves like purring maggots for their *comforting whirs*.

Sound cuter than they look.\
*Art by Zippy*

## Quirks

- Only **untamed** purring maggots can be milked - if you tame them, they become unmilkable. Bug:3670
- Once you catch a purring maggot, be sure to assign it to a built cage for long-term storage, otherwise it will be left in the workshop after being milked. Bug:3668

## Trivia

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\

In the 28th episode of Dwarf Fortress Talk, an early sprite for dwarven cheese was inspired by Casu Marzu, a Sardinian cheese containing live maggots. The idea was forwarded by Meph, who drew a two-frame animation for it. This sprite was never publicly released, and dwarven cheese uses standard graphics rather than its own [`[CHEESE_GRAPHICS]`](/index.php/Graphics_token#CHEESE_GRAPHICS "Graphics token"), however, a reference to a non-existent 8-tile tilesheet of cheese graphics can still be found within the creature graphics definitions files which might have been the animated cheese.

This in turn spawned a discussion as to where the maggots in the cheese came from, as the milked maggot remains outside the cheese. Do the maggots lay, or contain, smaller maggots? Do they form maggot-chains, or are they like Matryoshka dolls? Maybe the "purring" of the purring maggot is a bunch of maggots inside the maggot, making a purring noise as they move around.

*"The mystery of the purring maggot only grows."* - Toady One

    [CREATURE:MAGGOT_PURRING]
        [DESCRIPTION:A tiny larva which is prized for its milk.]
        [NAME:purring maggot:purring maggots:purring maggot]
        [CASTE_NAME:purring maggot:purring maggots:purring maggot]
        [CREATURE_TILE:'{'][COLOR:7:0:1][ALTTILE:'}']
        [PETVALUE:10]
        [PET_EXOTIC]
        [VERMIN_GROUNDER][VERMIN_NOROAM][VERMIN_HATEABLE]
        [SMALL_REMAINS][NATURAL]
        [NOT_BUTCHERABLE]
        [BIOME:SUBTERRANEAN_CHASM]
        [UNDERGROUND_DEPTH:2:3]
        [POPULATION_NUMBER:250:500]
        [PREFSTRING:comforting whirs]
        [NOBONES]
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
        [USE_MATERIAL_TEMPLATE:GOO:GOO_TEMPLATE]
        [BLOOD:LOCAL_CREATURE_MAT:GOO:LIQUID]
        [BODY_SIZE:0:0:1000]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [ALL_ACTIVE]
        [CANNOT_JUMP]
        [NO_DRINK][NO_EAT][NO_SLEEP]
        [HOMEOTHERM:10067]
        [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
            [TL_COLOR_MODIFIER:GRAY:1]
                [TLCM_NOUN:skin:SINGULAR]
        [USE_MATERIAL_TEMPLATE:MILK:MILK_TEMPLATE]
            [STATE_NAME:ALL_SOLID:frozen dwarven milk]
            [STATE_ADJ:ALL_SOLID:frozen dwarven milk]
            [STATE_NAME:LIQUID:dwarven milk]
            [STATE_ADJ:LIQUID:dwarven milk]
            [STATE_NAME:GAS:boiling dwarven milk]
            [STATE_ADJ:GAS:boiling dwarven milk]
            [PREFIX:NONE]
            [MULTIPLY_VALUE:2]
        [MILKABLE:LOCAL_CREATURE_MAT:MILK:20000]
        [USE_MATERIAL_TEMPLATE:CHEESE:CREATURE_CHEESE_TEMPLATE]
            [STATE_NAME:SOLID:dwarven cheese]
            [STATE_ADJ:SOLID:dwarven cheese]
            [STATE_NAME:SOLID_POWDER:dwarven cheese powder]
            [STATE_ADJ:SOLID_POWDER:dwarven cheese powder]
            [STATE_NAME:LIQUID:melted dwarven cheese]
            [STATE_ADJ:LIQUID:melted dwarven cheese]
            [STATE_NAME:GAS:boiling dwarven cheese]
            [STATE_ADJ:GAS:boiling dwarven cheese]
            [PREFIX:NONE]
            [MULTIPLY_VALUE:2]
