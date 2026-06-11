# Hair

> Fonte: [Hair](https://dwarffortresswiki.org/index.php/Hair) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Hair** is a filament that grows out of a creature's skin that can provide many functions. This can range from providing warmth to acting as feelers, expanding on the sensation of touch. It is handled in two different ways in the game, being attached to a creature, or being detached and made into a useful item.

|  |
|----|
| "Hair" in other / Languages / Dwarven / : / razes / Elven / : / rera / Goblin / : / esmast / Human / : / ad |

## Hair on living creatures

Hair is part of the cosmetic layers that any creature can have. It can also have different colors, turning grey or white as creatures age.

## Hair as an item

Hair is a byproduct of butchering some animals. It can be spun into thread at a farmer's workshop. Hair thread cannot be used to weave cloth, but it can be dyed and used to suture wounds in a hospital or bind books in a craftsdwarf's workshop.

Hair sample.

    [MATERIAL_TEMPLATE:HAIR_TEMPLATE]
        [STATE_COLOR:ALL_SOLID:GRAY]
        [STATE_NAME:ALL_SOLID:hair]
        [STATE_ADJ:ALL_SOLID:hair]
        [STATE_COLOR:LIQUID:GRAY]
        [STATE_NAME:LIQUID:n/a]
        [STATE_ADJ:LIQUID:n/a]
        [STATE_COLOR:GAS:GRAY]
        [STATE_NAME:GAS:n/a]
        [STATE_ADJ:GAS:n/a]
        [DISPLAY_COLOR:7:0:0]
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
        [IMPACT_STRAIN_AT_YIELD:100000]
        [COMPRESSIVE_YIELD:10000]
        [COMPRESSIVE_FRACTURE:10000]
        [COMPRESSIVE_STRAIN_AT_YIELD:100000]
        [TENSILE_YIELD:10000]
        [TENSILE_FRACTURE:10000]
        [TENSILE_STRAIN_AT_YIELD:100000]
        [TORSION_YIELD:10000]
        [TORSION_FRACTURE:10000]
        [TORSION_STRAIN_AT_YIELD:100000]
        [SHEAR_YIELD:60000] from net someplace
        [SHEAR_FRACTURE:120000]
        [SHEAR_STRAIN_AT_YIELD:100000]
        [BENDING_YIELD:10000]
        [BENDING_FRACTURE:10000]
        [BENDING_STRAIN_AT_YIELD:100000]
        [MAX_EDGE:0]
        [ABSORPTION:100]
        [IMPLIES_ANIMAL_KILL]
        [ITEMS_HARD]
        [HAIR]
