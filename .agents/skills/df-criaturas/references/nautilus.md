# Nautilus

> Fonte: [Nautilus](https://dwarffortresswiki.org/index.php/Nautilus) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes nautiluses for their many tentacles.**
- **Biome**
- **Any Ocean**
- **Variations**
- **Nautilus - Nautilus man - Giant nautilus**
- **Attributes**
- **Aquatic · Fishable · Shell**
- **Active Seasons**
- **Spring Summer Autumn Winter**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A tiny, mollusk with a large shell and many tentacles.*

**Nautiluses** are a source of food for fortresses located near the ocean. They are also one of the few types of creatures, along with oysters, cave lobsters, mussels, and turtles, that are common sources of shells. After being caught by a fisherdwarf, they require cleaning at a fishery, which produces a usable shell and an edible nautilus.

According to the raws, nautiluses have 90 tentacles and copper-based blood (though the tentacles are not yet implemented as part of their body structure).

Some dwarves like nautiluses for their *shells* and their *many tentacles*.

\

Admired for its *many tentacles*

    32 kph

    Nautiluses were sponsored by the generous contributions of the Bay 12 community.

        Adam Isom

    [CREATURE:NAUTILUS]
        [DESCRIPTION:A tiny, mollusk with a large shell and many tentacles.]
        [NAME:nautilus:nautiluses:nautilus]
        [CASTE_NAME:nautilus:nautiluses:nautilus]
        [CREATURE_TILE:11][COLOR:4:0:1]
        [PETVALUE:10]
        [VERMIN_FISH]
        [FREQUENCY:100]
        [AQUATIC][SMALL_REMAINS][FISHITEM][NOBONES][IMMOBILE_LAND][UNDERSWIM][COOKABLE_LIVE]
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:900:750:600:439:1900:2900] 20 kph, NO DATA
        [SWIMS_INNATE]
        [CANNOT_JUMP]
        [NATURAL]
        [NOT_BUTCHERABLE]
        [BIOME:ANY_OCEAN]
        [NO_DRINK]
        [POPULATION_NUMBER:250:500]
        [PREFSTRING:shells]
        [PREFSTRING:many tentacles]
        [BODY:BASIC_1PARTBODY:BASIC_HEAD:2EYES:SHELL:BEAK] 90 tentacles
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
            [REMOVE_MATERIAL:HAIR]
            [REMOVE_MATERIAL:BONE]
            [REMOVE_MATERIAL:CARTILAGE]
            [USE_MATERIAL_TEMPLATE:CHITIN:CHITIN_TEMPLATE]
            [USE_MATERIAL_TEMPLATE:SHELL:SHELL_TEMPLATE]
                [STATE_COLOR:ALL:STRIPES_BROWN_WHITE]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
            [REMOVE_TISSUE:HAIR]
            [REMOVE_TISSUE:BONE]
            [REMOVE_TISSUE:CARTILAGE]
            [USE_TISSUE_TEMPLATE:CHITIN:CHITIN_TEMPLATE]
            [USE_TISSUE_TEMPLATE:SHELL:SHELL_TEMPLATE]
        [ATTACK:BITE:BODYPART:BY_CATEGORY:BEAK]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:bite:bites]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_CANLATCH]
        [BODY_DETAIL_PLAN:VERTEBRATE_TISSUE_LAYERS:SKIN:FAT:MUSCLE:CHITIN:CHITIN]
        [HAS_NERVES]
        [MUNDANE]
        [USE_MATERIAL_TEMPLATE:BLOOD:BLOOD_TEMPLATE]
            [STATE_COLOR:ALL:BLUE] copper not iron based
        [BLOOD:LOCAL_CREATURE_MAT:BLOOD:LIQUID]
        [CREATURE_CLASS:GENERAL_POISON]
        [GETS_WOUND_INFECTIONS]
        [GETS_INFECTIONS_FROM_ROT]
        [USE_MATERIAL_TEMPLATE:PUS:PUS_TEMPLATE]
        [PUS:LOCAL_CREATURE_MAT:PUS:LIQUID]
        [BODY_SIZE:0:0:500]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:15:20]
        [ALL_ACTIVE]
        [NO_SLEEP]
        [NO_DIZZINESS]
        [CASTE:FEMALE]
            [FEMALE]
        [CASTE:MALE]
            [MALE]
        [SELECT_CASTE:ALL]
        [SET_TL_GROUP:BY_CATEGORY:ALL:SHELL]
            [TL_COLOR_MODIFIER:STRIPES_WHITE_CHESTNUT:1]
                [TLCM_NOUN:shell:SINGULAR]
        [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
            [TL_COLOR_MODIFIER:MOTTLED_WHITE_BROWN:1]
                [TLCM_NOUN:skin:SINGULAR]
