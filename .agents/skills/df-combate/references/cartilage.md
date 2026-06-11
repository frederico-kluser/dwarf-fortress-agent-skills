# Cartilage

> Fonte: [Cartilage](https://dwarffortresswiki.org/index.php/Cartilage) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

!!UNKNOWN!!  · xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Cartilage** is a body part generated from butchering most animals. It has no use in the meat industry, and can be dumped without a second thought.

Some fish, such as sharks, are notable for having cartilaginous skeletons. These fish do not drop bones, only cartilage.

Note that dwarves consider cartilage useful (like bones), so they will not dump it automatically, even if you have the o-r-dump other option enabled. It does not rot on its own either.

Bodily material between bones.

    [MATERIAL_TEMPLATE:CARTILAGE_TEMPLATE]
        [STATE_COLOR:ALL_SOLID:WHITE]
        [STATE_NAME:ALL_SOLID:cartilage]
        [STATE_ADJ:ALL_SOLID:cartilaginous]
        [STATE_COLOR:LIQUID:WHITE]
        [STATE_NAME:LIQUID:n/a]
        [STATE_ADJ:LIQUID:n/a]
        [STATE_COLOR:GAS:WHITE]
        [STATE_NAME:GAS:n/a]
        [STATE_ADJ:GAS:n/a]
        [DISPLAY_COLOR:7:0:1]
        [MATERIAL_VALUE:1]
        [SPEC_HEAT:420]
        [IGNITE_POINT:10508]
        [MELTING_POINT:NONE]
        [BOILING_POINT:NONE]
        [HEATDAM_POINT:10250]
        [COLDDAM_POINT:9900]
        [MAT_FIXED_TEMP:NONE]
        [SOLID_DENSITY:500]
        [LIQUID_DENSITY:NONE]
        [MOLAR_MASS:NONE]
        [IMPACT_YIELD:10000]
        [IMPACT_FRACTURE:10000]
        [IMPACT_STRAIN_AT_YIELD:25000]
        [COMPRESSIVE_YIELD:10000]
        [COMPRESSIVE_FRACTURE:10000]
        [COMPRESSIVE_STRAIN_AT_YIELD:25000]
        [TENSILE_YIELD:10000]
        [TENSILE_FRACTURE:10000]
        [TENSILE_STRAIN_AT_YIELD:25000]
        [TORSION_YIELD:10000]
        [TORSION_FRACTURE:10000]
        [TORSION_STRAIN_AT_YIELD:25000]
        [SHEAR_YIELD:30000] from net someplace
        [SHEAR_FRACTURE:30000]
        [SHEAR_STRAIN_AT_YIELD:25000]
        [BENDING_YIELD:10000]
        [BENDING_FRACTURE:10000]
        [BENDING_STRAIN_AT_YIELD:25000]
        [MAX_EDGE:0]
        [ABSORPTION:100]
        [IMPLIES_ANIMAL_KILL]
        [CARTILAGE]
