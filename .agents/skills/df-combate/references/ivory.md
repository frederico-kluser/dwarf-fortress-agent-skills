# Ivory

> Fonte: [Ivory](https://dwarffortresswiki.org/index.php/Ivory) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Ivory** and **teeth** are resources used to create or decorate crafts at the craftsdwarf's workshop with the bone carving skill. The exact material category is "ivory/tooth", signifying that either ivory (the tusks of large animals) or sufficiently large teeth are needed for the job.

Ivory tusks are obtained from butchering certain animals at the butcher's shop: elephants, hippos, narwhals, walruses, warthogs, and wild boars. Some intelligent creatures like trolls and gorlaks also have tusks, but dwarves will not butcher them.

Usable teeth may be harvested by butchering many of the largest animals (roughly grizzly bear-size or larger). Although combat may knock teeth loose from the mouths of dwarves, animals and invaders, such knocked-out teeth are almost always too small for crafting. As a rule, if a creature does not drop teeth or ivory when butchered, its teeth are too small for crafting, especially when divided into 30 pieces.

Goblins will often wear jewelry made of troll ivory. Dwarves (and others) may carry "trophies" made from otherwise uncraftable materials (e.g. an elf tooth amulet).

A fine material, but a rare one for carving.

|  |
|----|
| "Ivory" in other / Languages / Dwarven / : / sosad / Elven / : / ciquara / Goblin / : / stuz / Human / : / bemeh |

    [MATERIAL_TEMPLATE:TOOTH_TEMPLATE]
        [STATE_COLOR:ALL_SOLID:IVORY]
        [STATE_NAME:ALL_SOLID:tooth]
        [STATE_ADJ:ALL_SOLID:tooth]
        [STATE_COLOR:LIQUID:IVORY]
        [STATE_NAME:LIQUID:n/a]
        [STATE_ADJ:LIQUID:n/a]
        [STATE_COLOR:GAS:IVORY]
        [STATE_NAME:GAS:n/a]
        [STATE_ADJ:GAS:n/a]
        [DISPLAY_COLOR:7:0:1]
        [MATERIAL_VALUE:1]
        [SPEC_HEAT:1000]
        [IGNITE_POINT:10508]
        [MELTING_POINT:NONE]
        [BOILING_POINT:NONE]
        [HEATDAM_POINT:10250]
        [COLDDAM_POINT:9900]
        [MAT_FIXED_TEMP:NONE]
        [SOLID_DENSITY:500]
        [LIQUID_DENSITY:NONE]
        [MOLAR_MASS:NONE]
        [IMPACT_YIELD:200000] copied bone, no data
        [IMPACT_FRACTURE:200000]
        [IMPACT_STRAIN_AT_YIELD:100]
        [COMPRESSIVE_YIELD:200000]
        [COMPRESSIVE_FRACTURE:200000]
        [COMPRESSIVE_STRAIN_AT_YIELD:100]
        [TENSILE_YIELD:115000]
        [TENSILE_FRACTURE:130000]
        [TENSILE_STRAIN_AT_YIELD:100]
        [TORSION_YIELD:115000]
        [TORSION_FRACTURE:130000]
        [TORSION_STRAIN_AT_YIELD:100]
        [SHEAR_YIELD:115000]
        [SHEAR_FRACTURE:130000]
        [SHEAR_STRAIN_AT_YIELD:100]
        [BENDING_YIELD:115000]
        [BENDING_FRACTURE:130000]
        [BENDING_STRAIN_AT_YIELD:100]
        [MAX_EDGE:1000]
        [ABSORPTION:100]
        [IMPLIES_ANIMAL_KILL]
        [TOOTH]
        [ITEMS_HARD]
