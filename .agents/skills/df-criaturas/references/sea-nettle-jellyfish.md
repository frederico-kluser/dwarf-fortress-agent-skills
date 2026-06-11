# Sea nettle jellyfish

> Fonte: [Sea nettle jellyfish](https://dwarffortresswiki.org/index.php/Sea_nettle_jellyfish) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes sea nettle jellyfish for their beauty.**
- **Biome**
- **Temperate Ocean**
- **Attributes**
- **Aquatic · Fishable**
- **Active Seasons**
- **Spring Summer Autumn Winter**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*An invertebrate found off the coast. It has a sting which can be severe.*

**Sea nettle jellyfish** are a type of aquatic vermin found in temperate oceans year-round, unless the water freezes, in which case they will be wiped out and come back next year. They are a ready source of food when cleaned at a fishery. Sea nettle jellyfish are distinct for being the only species of vermin capable of beaching, though being vermin, this already-rare behaviour is even more difficult to notice.

Some dwarves like sea nettle jellyfish for their *beauty*.

\

Admired for its *beauty*.

    [CREATURE:JELLYFISH_SEA_NETTLE]
        [DESCRIPTION:An invertebrate found off the coast.  It has a sting which can be severe.]
        [NAME:sea nettle jellyfish:sea nettle jellyfish:sea nettle jellyfish]
        [CASTE_NAME:sea nettle jellyfish:sea nettle jellyfish:sea nettle jellyfish]
        [CREATURE_TILE:234][COLOR:6:0:0]
        [PETVALUE:10]
        [AQUATIC][BEACH_FREQUENCY:10]
        [VERMIN_GROUNDER]
        [SMALL_REMAINS][FISHITEM][NOBONES][IMMOBILE_LAND][UNDERSWIM][VERMIN_NOTRAP]
        [NO_THOUGHT_CENTER_FOR_MOVEMENT]
        [NOT_BUTCHERABLE]
        [NATURAL]
        [MUNDANE]
        [BIOME:OCEAN_TEMPERATE]
        [POPULATION_NUMBER:50:100]
        [CLUSTER_NUMBER:5:10]
        [PREFSTRING:beauty]
        [BODY:BASIC_1PARTBODY] *** lazy!
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
            [REMOVE_MATERIAL:HAIR]
            [REMOVE_MATERIAL:BONE]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
            [REMOVE_TISSUE:HAIR]
            [REMOVE_TISSUE:BONE]
        [BODY_DETAIL_PLAN:EXOSKELETON_TISSUE_LAYERS:SKIN:FAT:MUSCLE]
        [HAS_NERVES]
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [BODY_SIZE:0:0:200]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:2:3]
        [ALL_ACTIVE]
        [NO_DRINK]
        [NO_DIZZINESS]
        [NO_FEVERS]
        [SWIMS_INNATE]
        [CANNOT_JUMP]
        [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
            [TL_COLOR_MODIFIER:BROWN:1]
                [TLCM_NOUN:skin:SINGULAR]
