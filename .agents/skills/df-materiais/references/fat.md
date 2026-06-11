# Fat

> Fonte: [Fat](https://dwarffortresswiki.org/index.php/Fat) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Fat** is a low-value yellow animal product obtained by butchering an animal. It is made of globs, but unlike other globs, will not be cleaned by dwarves. In its liquid form, it is named grease. Although it can ignite, fat cannot boil.

|  |
|----|
| "Fat" in other / Languages / Dwarven / : / er / Elven / : / rine / Goblin / : / dusmxu / Human / : / omep |

## Fortress Mode use

Fat can be rendered into tallow in a kitchen. Tallow is used in the production of soap, or can be cooked into meals. A 'process fat' job processes all the available fat into single stacks of tallow at once. By default, "process fat into tallow" jobs are automatically created in kitchens when fat is available.

## Adventure Mode use

In Adventure Mode, fat is a portable solid, though hardly usable in a solid state.

When fat is put in warm temperatures, (usually the fire that surrounds a burning tree/plant) it eventually becomes grease, which is then drinkable for a short while after, before it cools back down into fat. You sometimes may notice a pool of grease being left behind from someone who was burning. However, given the usual weight of fat, you might be better off using other liquids.

## Creatures

Most creatures, notably excepting inorganic ones (such as iron men), have a layer of fat between skin and muscle. Because of its relatively low melting point, the fat is usually the first thing to go if a creature burns.

Creatures may have varying levels of fat, even when of the same species or caste. In a dwarf's description, for example, it may state their relative amount of fat compared to the racial average. Fatter creatures give more fat when butchered than creatures that are skinnier. The amount of fat on a creature is related to its size.

Pre-soap material.

    [MATERIAL_TEMPLATE:FAT_TEMPLATE]
        [STATE_COLOR:ALL_SOLID:YELLOW]
        [STATE_NAME:ALL_SOLID:fat]
        [STATE_ADJ:ALL_SOLID:fatty]
        [STATE_COLOR:LIQUID:YELLOW]
        [STATE_NAME:LIQUID:grease]
        [STATE_ADJ:LIQUID:greasy]
        [STATE_COLOR:GAS:YELLOW]
        [STATE_NAME:GAS:n/a]
        [STATE_ADJ:GAS:n/a]
        [DISPLAY_COLOR:6:0:1]
        [MATERIAL_VALUE:1]
        [SPEC_HEAT:4181]
        [IGNITE_POINT:10338]
        [MELTING_POINT:10078]
        [BOILING_POINT:NONE]
        [HEATDAM_POINT:10250]
        [COLDDAM_POINT:9900]
        [MAT_FIXED_TEMP:NONE]
        [SOLID_DENSITY:900]
        [LIQUID_DENSITY:800]
        [MOLAR_MASS:NONE]
        [IMPACT_YIELD:10000]
        [IMPACT_FRACTURE:10000]
        [IMPACT_STRAIN_AT_YIELD:50000]
        [COMPRESSIVE_YIELD:10000]
        [COMPRESSIVE_FRACTURE:10000]
        [COMPRESSIVE_STRAIN_AT_YIELD:50000]
        [TENSILE_YIELD:10000]
        [TENSILE_FRACTURE:10000]
        [TENSILE_STRAIN_AT_YIELD:50000]
        [TORSION_YIELD:10000]
        [TORSION_FRACTURE:10000]
        [TORSION_STRAIN_AT_YIELD:50000]
        [SHEAR_YIELD:10000] no data
        [SHEAR_FRACTURE:10000]
        [SHEAR_STRAIN_AT_YIELD:50000]
        [BENDING_YIELD:10000]
        [BENDING_FRACTURE:10000]
        [BENDING_STRAIN_AT_YIELD:50000]
        [MAX_EDGE:0]
        [ABSORPTION:100]
        [REACTION_CLASS:FAT]
        [DO_NOT_CLEAN_GLOB]
        [MATERIAL_REACTION_PRODUCT:RENDER_MAT:LOCAL_CREATURE_MAT:TALLOW]
        [IMPLIES_ANIMAL_KILL]
        [STOCKPILE_GLOB]
        [ROTS]
        [GENERATES_MIASMA]
        [BUTCHER_SPECIAL:GLOB:NONE]
