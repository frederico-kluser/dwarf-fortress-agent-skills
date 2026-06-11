# Creature examples

> Fonte: [Creature examples](https://dwarffortresswiki.org/index.php/Creature_examples) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

This page was created to aid those looking to create new creatures. Those familiar with creature raws should feel free to add helpful/obscure information to the lists below to help less-experienced members of the community with their creatures.

## Dummy creatures

Creatures that are not intended to function in general gameplay, but are used as references or in interactions (the latter of which can mostly be found here).

### Material Resource Creature

Sometimes, you will want to use a custom material in an interaction that is not related to any specific creature or stone. Making it an inorganic material with the \[SPECIAL\] tag will prevent it from appearing in almost all places, however there may be some cases where you need to use a dummy creature to store special materials, and reference that creature instead.

    Material resource creature

    [CREATURE:MATERIALS]
        [NAME:creature:creatures:creature]
        [CASTE_NAME:creature:creatures:creature]
        [DESCRIPTION:A living being of unknown description.]
        [ARENA_RESTRICTED]
        [DOES_NOT_EXIST]
        [USE_MATERIAL_TEMPLATE:BLOOD:BLOOD_TEMPLATE][PREFIX:NONE]
        [USE_MATERIAL_TEMPLATE:BURNING:STONE_TEMPLATE][PREFIX:NONE][STATE_NAME_ADJ:SOLID:flame magic][MELTING_POINT:0][BOILING_POINT:1][MAT_FIXED_TEMP:35000][DISPLAY_COLOR:6:0:1]
        [USE_MATERIAL_TEMPLATE:BURNING_STRONG:STONE_TEMPLATE][PREFIX:NONE][STATE_NAME_ADJ:SOLID:flame magic][MELTING_POINT:0][BOILING_POINT:1][MAT_FIXED_TEMP:90000][DISPLAY_COLOR:6:0:1]
        [USE_MATERIAL_TEMPLATE:FREEZING:SWEAT_TEMPLATE][STATE_NAME:ALL:ice magic][STATE_ADJ:ALL:frigid][ENTERS_BLOOD][PREFIX:NONE][STATE_COLOR:ALL:WHITE][DISPLAY_COLOR:7:0:1][EVAPORATES][MELTING_POINT:NONE][BOILING_POINT:4000][HEATDAM_POINT:4001][SPEC_HEAT:1]

### Instantly-evaporating creature

To make a creature instantly "poof" into a fine mist, you can transform them into this.

    Instantly evaporating creature

    [CREATURE:POOF]
        [ARENA_RESTRICTED]
        [DOES_NOT_EXIST]
        [DESCRIPTION:A creature that has evaporated.]
        [NAME:fine mist:fine mists:fine mist]
        [CASTE_NAME:fine mist:fine mists:fine mist]
        [CREATURE_TILE:250][COLOR:0:0:0]
        [NOT_BUTCHERABLE]
        [BODY:BASIC_1PARTBODY]
        [USE_MATERIAL_TEMPLATE:BREAK:CREATURE_EXTRACT_TEMPLATE]
            [STATE_NAME:ALL:mist]
            [STATE_COLOR:ALL:BLACK]
            [MELTING_POINT:0]
            [BOILING_POINT:1]
            [HEATDAM_POINT:NONE]
            [COLDDAM_POINT:NONE]
            [PREFIX:NONE]
        [TISSUE:BREAK]
            [TISSUE_NAME:mist:NP]
            [TISSUE_MATERIAL:LOCAL_CREATURE_MAT:BREAK]
            [CONNECTS]
            [FUNCTIONAL]
            [STRUCTURAL]
            [TISSUE_MAT_STATE:SOLID]
            [TISSUE_SHAPE:LAYER]
            [VASCULAR:50]
        [TISSUE_LAYER:BY_CATEGORY:ALL:BREAK]
        [BLOOD:LOCAL_CREATURE_MAT:BREAK:LIQUID]
        [IMMOBILE]
        [BODY_SIZE:0:0:1]

You can also give it an ITEMCORPSE if you want it to leave an item behind.

### Easily Damaged Creature

This creature can be destroyed by any damage. You can also alter the values easily, if you want to investigate a specific damage type.

    Easily damaged creature

    [CREATURE:BREAKS_ON_ANY_HIT]
        [DESCRIPTION:Something that breaks easily.]
        [NAME:break:breaks:break]
        [CASTE_NAME:break:breaks:break]
        [CREATURE_TILE:'A'][COLOR:4:0:1]
        [NO_THOUGHT_CENTER_FOR_MOVEMENT]
        [PREFSTRING:breaking]
        [BODY:BASIC_1PARTBODY]
        [USE_MATERIAL_TEMPLATE:MUSCLE:MUSCLE_TEMPLATE]
            [IMPACT_YIELD:1]
            [IMPACT_FRACTURE:1]
            [COMPRESSIVE_YIELD:1]
            [COMPRESSIVE_FRACTURE:1]
            [TENSILE_YIELD:1]
            [TENSILE_FRACTURE:1]
            [TORSION_YIELD:1]
            [TORSION_FRACTURE:1]
            [SHEAR_YIELD:1]
            [SHEAR_FRACTURE:1]
            [BENDING_YIELD:1]
            [BENDING_FRACTURE:1]
        [TISSUE:SILK]
            [TISSUE_NAME:flesh:NP]
            [TISSUE_MATERIAL:LOCAL_CREATURE_MAT:MUSCLE]
            [MUSCULAR]
            [FUNCTIONAL]
            [STRUCTURAL]
            [RELATIVE_THICKNESS:1]
            [CONNECTS]
            [TISSUE_SHAPE:LAYER]
        [TISSUE_LAYER:BY_CATEGORY:BODY:SILK]
        [BODY_SIZE:0:0:4000]
        [IMMOBILE]

## Creatures with unusual physiologies

### Creature made of plants

Apart from having a plant-based physiology, this creature also has body parts that are converted into actual plants when butchered. This example uses two types of tissues. You can easily make an entire creature out of different kinds of plants, and the larger body parts will give you more plants. This can be very useful, as plants are used in different kinds of interactions than animal parts are. For example, you can use this trick to get booze or thread from an animal's body parts. You will require both a creature raw file and plant raw file for this to work.

    Plant-based creature (Creature raw)

    [CREATURE:FLEURBERRI_AMT]
        [DESCRIPTION:A large, sun-loving creature, made up of a mixture of plant and animal tissues.  Its heart is a valuable berry.]
        [NAME:fleurberri:fleurberris:fleurberri]
        [CASTE_NAME:fleurberri:fleurberris:fleurberri]
        [CREATURE_TILE:'F'][COLOR:2:0:1]
        [LARGE_ROAMING]
        [NOBONES]
        [NATURAL][BENIGN]
        [MEANDERER]
        [BIOME:GRASSLAND_TEMPERATE]
        [BIOME:SHRUBLAND_TEMPERATE]
        [BIOME:SAVANNA_TEMPERATE]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:3:5]
        [FREQUENCY:50]
        [PREFSTRING:juicy berries]
        [BODY:QUADRUPED:BRAIN:SPINE:2EYES:MOUTH:HEART]
        [BODY_DETAIL_PLAN:STANDARD_HEAD_POSITIONS]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
        [USE_MATERIAL_TEMPLATE:WOOD:WOOD_TEMPLATE]
            [BUTCHER_SPECIAL:WOOD:NONE] <--This will cause the wood body parts to become logs when butchered.
        [TISSUE:CORTEX]
            [TISSUE_NAME:cortex:NP]
            [THICKENS_ON_ENERGY_STORAGE]
            [SCARS]
            [TISSUE_MATERIAL:PLANT_MAT:FLEURBERRI_PLANT_AMT:STRUCTURAL] <--This is the line to make the body part out of plant.  The plant must also have a BUTCHER_SPECIAL:PLANT:NONE tag for this to work.
            [RELATIVE_THICKNESS:1]
            [HEALING_RATE:100]
            [VASCULAR:3]
            [PAIN_RECEPTORS:5]
            [CONNECTS]
            [TISSUE_SHAPE:LAYER]
            [SETTABLE]
            [SPLINTABLE]
        [TISSUE:PLANT]
            [TISSUE_NAME:vascular tissue:NP]
            [THICKENS_ON_ENERGY_STORAGE]
            [SCARS]
            [TISSUE_MATERIAL:PLANT_MAT:FLEURBERRI_PLANT_AMT:STRUCTURAL]
            [RELATIVE_THICKNESS:1]
            [HEALING_RATE:100]
            [VASCULAR:3]
            [PAIN_RECEPTORS:5]
            [CONNECTS]
            [TISSUE_SHAPE:LAYER]
            [SETTABLE]
            [SPLINTABLE]
        [TISSUE:PITH]
            [TISSUE_NAME:pith:NP]
            [ARTERIES]
            [FUNCTIONAL]
            [TISSUE_MATERIAL:LOCAL_CREATURE_MAT:WOOD]
            [RELATIVE_THICKNESS:2]
            [VASCULAR:5]
            [PAIN_RECEPTORS:50]
            [CONNECTS]
            [TISSUE_SHAPE:LAYER]
        [TISSUE:BERRY] <--Define the plant-based tissue here.
            [TISSUE_NAME:berry:NP]
            [FUNCTIONAL]
            [STRUCTURAL]
            [SCARS]
            [TISSUE_MATERIAL:PLANT_MAT:FLEURBERRI_BERRY_AMT:STRUCTURAL] <-- A different kind of plant. Use as many types as you want.
            [RELATIVE_THICKNESS:1]
            [HEALING_RATE:100]
            [VASCULAR:10]
            [PAIN_RECEPTORS:5]
            [CONNECTS]
            [TISSUE_SHAPE:LAYER]
        [BODY_DETAIL_PLAN:VERTEBRATE_TISSUE_LAYERS:CORTEX:NONE:PLANT:PITH:NONE]
        [SELECT_TISSUE_LAYER:ALL:BY_CATEGORY:HEART]
            [SET_LAYER_TISSUE:BERRY] <--This will set the selected layer or layers as the plant-based tissue.
            [TL_MAJOR_ARTERIES]
        [USE_MATERIAL_TEMPLATE:SAP:PLANT_EXTRACT_TEMPLATE]
            [STATE_NAME_ADJ:ALL:sap]
        [BLOOD:LOCAL_CREATURE_MAT:SAP:LIQUID]
        [CREATURE_CLASS:PLANT]
        [BODY_SIZE:0:0:50000]
        [BODY_SIZE:1:0:100000]
        [BODY_SIZE:2:0:400000]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [APPLY_CREATURE_VARIATION:MOUTH_BITE_ATTACK]
        [APPLY_CREATURE_VARIATION:KICK_ATTACK]
        [MAXAGE:10:20]
        [DIURNAL]
        [CASTE:FEMALE]
        [FEMALE]
        [MULTIPLE_LITTER_RARE]
        [CASTE:MALE]
        [MALE]
        [SET_TL_GROUP:BY_CATEGORY:ALL:CORTEX]
            [TL_COLOR_MODIFIER:PINK:1:GREEN:5]
                [TLCM_NOUN:body:SINGULAR]

\

    Plant based creature (Plant raw)

    Fleurberri plants and berries: Found inside a FLEURBERRI_AMT creature.
    They work exactly like regular plants, the only difference is that their structural materials have a BUTCHER_SPECIAL tag.
    You can make a creature entirely out of plants.  You can even give the plants meat-like names and make them out of meat to get brewable 'meat'.  (They will still be stockpiled as plants though.)

    [PLANT:FLEURBERRI_PLANT_AMT]
        [NAME:fleurberri strip]
        [NAME_PLURAL:fleurberri strips]
        [ADJ:fleur berry]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
            [MATERIAL_VALUE:1]
            [EDIBLE_VERMIN]
            [EDIBLE_RAW]
            [EDIBLE_COOKED]
            [BUTCHER_SPECIAL:PLANT:NONE] <-- This is the important part!
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [PICKED_TILE:21]
        [PICKED_COLOR:2:0:1]
        [USE_MATERIAL_TEMPLATE:MILL:PLANT_POWDER_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:fleurberri flour]
            [STATE_COLOR:ALL_SOLID:GREEN]
            [DISPLAY_COLOR:2:0:1]
            [MATERIAL_VALUE:20]
            [EDIBLE_VERMIN]
            [EDIBLE_COOKED]
            [PREFIX:NONE]
        [MILL:LOCAL_PLANT_MAT:MILL]
        [WET]
        [DRY]
        [VALUE:5]
        [PREFSTRING:crunch]

    [PLANT:FLEURBERRI_BERRY_AMT]
        [NAME:fleur berry]
        [NAME_PLURAL:fleur berries]
        [ADJ:fleur berry]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
            [MATERIAL_VALUE:10]
            [EDIBLE_VERMIN]
            [EDIBLE_RAW]
            [EDIBLE_COOKED]
            [BUTCHER_SPECIAL:PLANT:NONE] <-- This is the important part!
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [PICKED_TILE:58]
        [PICKED_COLOR:4:0:1]
        [WET]
        [DRY]
        [VALUE:15]
        [USE_MATERIAL_TEMPLATE:DRINK:PLANT_ALCOHOL_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:frozen fleurberri wine]
            [STATE_NAME_ADJ:LIQUID:fleurberri wine]
            [STATE_NAME_ADJ:GAS:boiling fleurberri wine]
            [MATERIAL_VALUE:15]
            [DISPLAY_COLOR:4:0:1]
            [EDIBLE_RAW]
            [EDIBLE_COOKED]
            [PREFIX:NONE]
        [DRINK:LOCAL_PLANT_MAT:DRINK]
        [PREFSTRING:rarity]
