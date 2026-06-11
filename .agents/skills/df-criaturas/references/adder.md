# Adder

> Fonte: [Adder](https://dwarffortresswiki.org/index.php/Adder) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes adders for their warning hisses.**
- **Biome**
- **Temperate Grassland Temperate Savanna Temperate Shrubland Any Temperate Forest Any Temperate Wetland**
- **Variations**
- **Adder - Adder man - Giant adder**
- **Attributes**
- **Syndrome · Egglaying**
- **Tamed Attributes**
- **Pet value:** 50
- **Not hunting/war trainable**
- **Size**
- **Birth:** 15 cm 3
- **Mid:** 75 cm 3
- **Max:** 150 cm 3
- **Food products**
- **Eggs:** 3-10
- **Age**
- **Adult at:** Birth
- **Max age:** 15-20
- **Butchering returns ( Value multiplier ×2)**
- **Food items**
- **Raw materials**
- **Skull:** 1

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*For logical designs related to the addition of numbers, see Adder (Computing) "Adder (Computing)").*

*A tiny snake with ridged scales and a powerful venomous bite.*

**Adders** are venomous snakes found in many temperate biomes. Their bites deliver a venom that can cause immediate strong pain, followed by long-term (but not permanent) nausea, blisters, and swelling. Though the bite itself is not usually fatal, such pain can cause unconsciousness, which *can* lead to fatal complications in combat.

Adders are distinct for being the smallest creatures in the game which aren't vermin.

Adders can be captured in cage traps and trained into cheap exotic pets. They are born adults and as such can't be permanently tamed. Butchering an adder only produces a skull, making them worthless to your meat industry. Female adders are egg-layers, producing 3-10 edible eggs with regularity, and providing significantly more food than would be expected from such a small creature.

Some dwarves like adders for their *warning hisses*.

Admired for its *warning hisses*.

    1 kph

    Adders were sponsored by the generous contributions of the Bay 12 community.

        IL

    [CREATURE:ADDER]
        [DESCRIPTION:A tiny snake with ridged scales and a powerful venomous bite.]
        [NAME:adder:adders:adder]
        [CASTE_NAME:adder:adders:adder]
        [CREATURE_TILE:'a'][COLOR:6:0:0]
        [CREATURE_CLASS:POISONOUS]
        [PETVALUE:50]
        [PET_EXOTIC]
        [FREQUENCY:30]
        [NATURAL]
        [CARNIVORE]
        [LARGE_ROAMING]
        [BIOME:GRASSLAND_TEMPERATE]
        [BIOME:SAVANNA_TEMPERATE]
        [BIOME:SHRUBLAND_TEMPERATE]
        [BIOME:ANY_TEMPERATE_FOREST]
        [BIOME:ANY_TEMPERATE_WETLAND]
        [POPULATION_NUMBER:10:25]
        [CLUSTER_NUMBER:1:1]
        [PREFSTRING:warning hisses]
        [BODY:BASIC_1PARTBODY:BASIC_HEAD:TAIL:2EYES:NOSE:2LUNGS:HEART:GUTS:ORGANS:SPINE:BRAIN:SKULL:MOUTH:GENERIC_TEETH_WITH_FANGS:RIBCAGE]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
            [REMOVE_MATERIAL:SKIN]
            [REMOVE_MATERIAL:LEATHER]
            [REMOVE_MATERIAL:PARCHMENT]
            [REMOVE_MATERIAL:HAIR]
            [USE_MATERIAL_TEMPLATE:SCALE:SCALE_TEMPLATE]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
            [REMOVE_TISSUE:SKIN]
            [REMOVE_TISSUE:HAIR]
            [USE_TISSUE_TEMPLATE:SCALE:SCALE_TEMPLATE]
        [BODY_DETAIL_PLAN:VERTEBRATE_TISSUE_LAYERS:SCALE:FAT:MUSCLE:BONE:CARTILAGE]
        [BODY_DETAIL_PLAN:LEATHERY_EGG_MATERIALS]
        [SELECT_TISSUE_LAYER:HEART:BY_CATEGORY:HEART]
         [PLUS_TISSUE_LAYER:SCALE:BY_CATEGORY:THROAT]
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
        [USE_MATERIAL_TEMPLATE:VENOM:CREATURE_EXTRACT_TEMPLATE]
            [STATE_NAME:ALL_SOLID:frozen adder venom]
            [STATE_ADJ:ALL_SOLID:frozen adder venom]
            [STATE_NAME:LIQUID:adder venom]
            [STATE_ADJ:LIQUID:adder venom]
            [STATE_NAME:GAS:boiling adder venom]
            [STATE_ADJ:GAS:boiling adder venom]
            [PREFIX:NONE]
            [ENTERS_BLOOD]
            [SYNDROME]
                [SYN_NAME:adder bite]
                [SYN_AFFECTED_CLASS:GENERAL_POISON]
                [SYN_IMMUNE_CREATURE:ADDER:ALL]
                [SYN_INJECTED]
                [CE_NAUSEA:SEV:50:PROB:100:RESISTABLE:SIZE_DILUTES:START:400:PEAK:500:END:1200]
                [CE_PAIN:SEV:75:PROB:100:RESISTABLE:SIZE_DILUTES:LOCALIZED:VASCULAR_ONLY:START:10:PEAK:50:END:2400]
                [CE_SWELLING:SEV:25:PROB:100:RESISTABLE:SIZE_DILUTES:LOCALIZED:VASCULAR_ONLY:START:50:PEAK:500:END:1500]
                [CE_BLISTERS:SEV:50:PROB:100:RESISTABLE:SIZE_DILUTES:LOCALIZED:VASCULAR_ONLY:START:50:PEAK:500:END:1500]
        [BODY_SIZE:0:0:15]
        [BODY_SIZE:1:0:75]
        [BODY_SIZE:2:0:150]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [MAXAGE:15:20]
        [ATTACK:BITE:CHILD_BODYPART_GROUP:BY_CATEGORY:HEAD:BY_CATEGORY:TOOTH]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:bite:bites]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_FLAG_CANLATCH]
            [SPECIALATTACK_INJECT_EXTRACT:LOCAL_CREATURE_MAT:VENOM:LIQUID:100:100]
        [ALL_ACTIVE]
        [APPLY_CREATURE_VARIATION:STANDARD_WALK_CRAWL_GAITS:6561:6115:5683:1755:7456:8567] 5 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [SWIMS_INNATE]
        [CANNOT_JUMP]
        [MUNDANE]
        [CASTE:FEMALE]
            [FEMALE]
            [LAYS_EGGS]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGGSHELL:SOLID]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGG_WHITE:LIQUID]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGG_YOLK:LIQUID]
                [EGG_SIZE:16]
                [CLUTCH_SIZE:3:10] 3 to 20
        [CASTE:MALE]
            [MALE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SCALE]
                [TL_COLOR_MODIFIER:MOTTLED_TAN_DARK_BROWN:1]
                    [TLCM_NOUN:scales:PLURAL]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
        [SELECT_MATERIAL:ALL]
            [MULTIPLY_VALUE:2]
