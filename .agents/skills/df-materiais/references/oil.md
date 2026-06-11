# Oil

> Fonte: [Oil](https://dwarffortresswiki.org/index.php/Oil) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

Olive oil is unusual in that it is pressed from the whole olive fruit, rather than from oil-bearing seeds.

**Oil** is an ingredient in cooking and soap making, made by pressing one of the several seed pastes or fruit at a screw press. The press squeezes the material, releasing the oil, which is stored in a liquid-capable jug. The oil can then be used to supplement a fortress's food supply, or can be combined with lye to make soap.

## Oil-producing crops

The following crops produce seeds that can be milled and pressed into oil:

|  |  |  |  |
|----|----|----|----|
| Plant Name | Underground? | Oil Name | Oil Value |
| Quarry bush | Yes | Rock Nut oil | 5☼ |
| Cotton | No | Cottonseed oil | 5☼ |
| Flax | No | Linseed oil | 5☼ |
| Hemp | No | Hempseed oil | 5☼ |
| Kenaf | No | Kenaf seed oil | 5☼ |
| Olive (fruit) | No | Olive oil | 5☼ |

## Value

Oil will be used in the kitchen when 'prepare meal' tasks are queued if it is enabled in the Kitchen tab in the Labor menu y.

Most of the seeds can be cooked directly, but have a base value of 1☼. However, milling the seeds to a paste and pressing them into oil generates a press cake with a value of 1☼ and a unit of oil with a value of 5☼, a 500% value increase for only two labors.

## Bugs

Cooks will only cook oil and other fluids as a last resort, instead preferring to cook solid foods with solid foods. Bug:2393 For more information, see the kitchen page.

|  |
|----|
| "Oil" in other / Languages / Dwarven / : / uzol / Elven / : / ÿivu / Goblin / : / smatspo / Human / : / konli |

    [MATERIAL_TEMPLATE:PLANT_OIL_TEMPLATE]
        [STATE_COLOR:ALL_SOLID:YELLOW]
        [STATE_NAME:ALL_SOLID:frozen vegetable oil]
        [STATE_ADJ:ALL_SOLID:frozen vegetable oil]
        [STATE_COLOR:LIQUID:YELLOW]
        [STATE_NAME:LIQUID:vegetable oil]
        [STATE_ADJ:LIQUID:vegetable oil]
        [STATE_COLOR:GAS:YELLOW]
        [STATE_NAME:GAS:boiling vegetable oil]
        [STATE_ADJ:GAS:boiling vegetable oil]
        [DISPLAY_COLOR:6:0:1]
        [MATERIAL_VALUE:1]
        [SPEC_HEAT:1820] olive oil 1.97, "vegetable oil" 1.67
        [IGNITE_POINT:10588]
        [MELTING_POINT:9978] real world values for different veg oils appear to be all over the map
        [BOILING_POINT:10368]
        [HEATDAM_POINT:NONE]
        [COLDDAM_POINT:NONE]
        [MAT_FIXED_TEMP:NONE]
        [SOLID_DENSITY:920] used liquid value
        [LIQUID_DENSITY:920]
        [MOLAR_MASS:20000]
        [IMPACT_YIELD:10000]
        [IMPACT_FRACTURE:10000]
        [IMPACT_STRAIN_AT_YIELD:100]
        [COMPRESSIVE_YIELD:10000]
        [COMPRESSIVE_FRACTURE:10000]
        [COMPRESSIVE_STRAIN_AT_YIELD:100]
        [TENSILE_YIELD:10000]
        [TENSILE_FRACTURE:10000]
        [TENSILE_STRAIN_AT_YIELD:100]
        [TORSION_YIELD:10000]
        [TORSION_FRACTURE:10000]
        [TORSION_STRAIN_AT_YIELD:100]
        [SHEAR_YIELD:6600] used high salinity ice
        [SHEAR_FRACTURE:6600]
        [SHEAR_STRAIN_AT_YIELD:100]
        [BENDING_YIELD:10000]
        [BENDING_FRACTURE:10000]
        [BENDING_STRAIN_AT_YIELD:100]
        [MAX_EDGE:500]
        [ABSORPTION:100]
        [MATERIAL_REACTION_PRODUCT:SOAP_MAT:LOCAL_PLANT_MAT:SOAP]
        [LIQUID_MISC_PLANT]
