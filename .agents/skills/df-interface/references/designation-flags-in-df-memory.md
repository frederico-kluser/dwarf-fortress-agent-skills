# Designation flags in DF memory

> Fonte: [Designation flags in DF memory](https://dwarffortresswiki.org/index.php/Designation_flags_in_DF_memory) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

00100000001010001000001000000000 <- obsidian, far away from magma flow
       00100000001001101000001000000000 <- obsidian, near magma flow
       11100000001001101000001000000000 <- obsidian, near magma flow
       00100000001010101000000000000000 <- obsidian, near magma flow
       00100000001010001000000000000000 <- obsidian, next to magma flow
       11100000001001101000000000000000 <- obsidian, next to magma flow
       00100000001001101000000000000000 <- obsidian, next to magma flow
       00100100001010010100000000000111 <- obsidian, next to magma flow
       11100100001001110100000000000111 <- obsidian, next to magma flow
       00000000000010101000000000000000 <- damp loam wall, next to murky pool
       00000000000100001000000000000000 <- damp loam wall, next to murky pool
       00000000000000101000000000000000 <- damp loam wall, next to murky pool
       00000000000011001000000000000000 <- damp loam wall, next to murky pool
       11000000000001101000000000000000 <- damp loam wall, next to murky pool
       11000000000001101000001000000000 <- undiscovered loam wall, close to murky pool
       00000000000011001000001000000000 <- undiscovered loam
       00000000000010010100110000000000 <- furrowed silt loam ground, empty space
       11000100000011110100000000000111 <- channel with 7/7 water
       11000100000011110100000000000110 <- murky pool, 6/7
       11000100000010010100000000000110 <- murky pool, 6/7
       11000100000010010100000000000111 <- murky pool, 7/7
       11000100000011110100000000000111 <- murky pool, 7/7
       11000100000010010100000000000111 <- murky pool, 7/7
       11000100000010110100000000000111 <- murky pool, 7/7
       11000100000000110100000000000111 <- murky pool, 7/7
       11000100000001110100000000000111 <- murky pool, 7/7
       00100100001010010100000000000111 <- open space, lava 7/7
       00100100001001110100000000000111 <- open space, lava 7/7
       11100100001001110100000000000111 <- open space, lava 7/7
       00100100001010110100000000000111 <- open space, lava 7/7
       00000000000010101001000000010000 <- rough-hewn claystone wall, desig. for mining
       00000000000010101001000000110000 <- rough-hewn claystone wall, desig. for channeling
       00000000000010101001000001100000 <- rough-hewn claystone wall, desig. for upward stairs
       00000000000010101001000000100000 <- rough-hewn claystone wall, desig. for up/down stairs
       00000000000010101001000001000000 <- rough-hewn claystone wall, desig. for up ramp
       00000000000010101001000001010000 <- rough-hewn claystone wall, desig. for down stairs
       00000000000010101001000010000000 <- rough-hewn claystone wall, desig. for smooth stones
       00000000000000110101000000000000 <- chestnut tree
       00000000000000110101000000010000 <- chestnut tree, designated for chopping
       00000000000000110101000000000000 <- shrub
       00000000000000110101000000010000 <- shrub, designated for gathering
         ^       ^           ^     |^^^
         warm?   warm?       Hidden|Flow Size
            ^            ^^^^
            liquid       Soil/Rock Layer ID
                        ^      ^^^^
                        Light  Desig. for activities (mining/shrubbing/stairing/etc.)
                       ^
                       Sub-terr.
                      ^
                      Outside
                  ^^^^
                  Unknown ID
                ^
                thought to be damp, but isn't
          ^
          Mossy

\

       //DWARF/DUAL MODE DESIGNATIONS
       DESIGNATION_LIQUID_AMOUNT_BIT1 BIT1 //DUAL MODE
       DESIGNATION_LIQUID_AMOUNT_BIT2 BIT2 //DUAL MODE
       DESIGNATION_LIQUID_AMOUNT_BIT3 BIT3 //DUAL MODE
       DESIGNATION_PILE BIT4
       DESIGNATION_DIG_BIT1 BIT5
       DESIGNATION_DIG_BIT2 BIT6
       DESIGNATION_DIG_BIT3 BIT7
       DESIGNATION_DETAIL BIT8
       DESIGNATION_DETAIL_EVENT BIT9
       DESIGNATION_HIDDEN BIT10 //DUAL MODE
       DESIGNATION_MATGLOSS_BIT1 BIT11 //DUAL MODE
       DESIGNATION_MATGLOSS_BIT2 BIT12 //DUAL MODE
       DESIGNATION_MATGLOSS_BIT3 BIT13 //DUAL MODE
       DESIGNATION_MATGLOSS_BIT4 BIT14 //DUAL MODE
       DESIGNATION_OPEN_TO_SUN BIT15 //DUAL MODE
       DESIGNATION_SUBTERRANEAN BIT16 //DUAL MODE
       DESIGNATION_SKY_VIEW BIT17 //DUAL MODE
       DESIGNATION_BIOME_BIT1 BIT18 //DUAL MODE
       DESIGNATION_BIOME_BIT2 BIT19 //DUAL MODE
       DESIGNATION_BIOME_BIT3 BIT20 //DUAL MODE
       DESIGNATION_BIOME_BIT4 BIT21 //DUAL MODE
       DESIGNATION_LIQUID_TYPE_BIT1 BIT22 //DUAL MODE
       DESIGNATION_WATER_TABLE BIT23 //DUAL MODE
       DESIGNATION_RAINED BIT24 //DUAL MODE
       DESIGNATION_TRAFFIC_BIT1 BIT25 //DUAL MODE
       DESIGNATION_TRAFFIC_BIT2 BIT26 //DUAL MODE
       DESIGNATION_FLOW_FORBID BIT27 //DUAL MODE
       DESIGNATION_LIQUID_STATIC BIT28 //DUAL MODE
       DESIGNATION_MOSS BIT29 //DUAL MODE
       DESIGNATION_FEATURE_PRESENT BIT30 //DUAL MODE
       DESIGNATION_LIQUID_CHARACTER_BIT1 BIT31 //DUAL MODE
       DESIGNATION_LIQUID_CHARACTER_BIT2 BIT32 //DUAL MODE

       //ADVENTURE DESIGNATIONS
       //1-3 DUAL USED
       DESIGNATION_LIT BIT4
       DESIGNATION_VISIBLE BIT5
       DESIGNATION_MEM_BUILDING BIT6
       DESIGNATION_MEM_ITEM BIT7
       DESIGNATION_MEM_MONSTER BIT8
       DESIGNATION_ORIGINALCAVE BIT9
       //10-32 DUAL USED
