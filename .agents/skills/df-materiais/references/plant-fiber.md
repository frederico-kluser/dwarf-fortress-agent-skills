# Plant fiber

> Fonte: [Plant fiber](https://dwarffortresswiki.org/index.php/Plant_fiber) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Plant fiber** is a resource material that is the precursor to several useful things for running a healthy fortress. Certain plant fibers can be used by brewers in stills to make alcohol, ground up into a paste or slurry at a quern or mill for other products, or by cooks preparing them in a kitchen to make prepared meals, but what sets plant fibers apart from other edible plants is their ability to be made into thread and ultimately cloth. Ergo, a consistent source of plant fibers is essential to a healthy textile industry.

The following plants qualify as plant fiber, having [`[THREAD]`](/index.php/Plant_token#THREAD "Plant token") in their raws:

|  |  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|----|
| Type | **Graphic** | **Value** | **Weight** | **Grows** | **Growable** | **Brewable** | **Millable** | **Cookable** |
| rope reeds |  | 2☼ | 1Γ | Any Season (Wet) | Surface | Yes | Slurry | Yes (Seeds) |
| pig tails |  | 2☼ | 1Γ | Summer/Autumn | Below Ground | Yes | Slurry | Yes (Seeds) |
| hemp |  | 2☼ | 1Γ | Any Season (Wet) | Surface | No | Slurry/Flour | Yes |
| cotton |  | 2☼ | 1Γ | Any Season (Dry) | Surface | No | Slurry | Yes (Seeds) |
| ramie |  | 2☼ | 1Γ | Any Season (Dry) | Surface | No | Slurry | No |
| flax |  | 2☼ | 1Γ | Any Season (Dry) | Surface | No | Slurry/Flour | Yes (Seeds) |
| jute |  | 2☼ | 1Γ | Any Season (Dry) | Surface | No | Slurry | No |
| kenaf |  | 2☼ | 1Γ | Any Season (Dry) | Surface | No | Slurry | Yes (Seeds) |

Ensure that at least one dwarf has the plant processing labor, then designating plants to be gathered with g gather plants option, before designating a rectangular area to harvest by a dwarf with the Plant Gathering labor

By default, fortresses embark with pig tail seeds, which can be grown underground in soft, loamy or muddy ground. The other kinds of plant fibers can be obtained, if the corresponding plants are growing naturally above ground, by assigning a dwarf the plant gathering labor, then designating plants to be gathered in an area with g. Alternatively, to repeatedly gather plants from a specific area, you can set up a plant gathering zone by pressing z, selecting the desired area to be gathered from, and enabling the " Gather fruit" option - in this case, dwarves with the "plant gathering" labor automatically tend to the zone as soon as new naturally-occurring vegetation can be harvested. **Warning!** naturally occurring plant fibers are uncommon; you can try to scope out any of the above plants to find suitable areas to gather from, but it might be more worthwhile to wait until you can trade for their seeds.

To convert plant fiber into thread, you must construct a farmer's workshop and add a "process plants" task. If there is an available plant fiber material, a dwarf with the plant processing labor assigned will take the plant fiber to the farmer's workshop and convert the plant fiber into thread. When this is done, seeds of the processed type of plant fiber are also produced, which allows you to install plant fiber- producing crops in farm plots. Dwarves who perform this task level up their thresher skill, and gain the title of "Thresher" if it is their highest-leveled skill.

Pre-rope material.

## See Also

- Thread
- Cloth
- Dye
- Textile industry
- Silk
- Yarn

    [MATERIAL_TEMPLATE:THREAD_PLANT_TEMPLATE]
        [STATE_COLOR:ALL_SOLID:GRAY]
        [STATE_NAME:ALL_SOLID:fiber]
        [STATE_ADJ:ALL_SOLID:fiber]
        [STATE_COLOR:LIQUID:BLACK]
        [STATE_NAME:LIQUID:none]
        [STATE_ADJ:LIQUID:none]
        [STATE_COLOR:GAS:BLACK]
        [STATE_NAME:GAS:none]
        [STATE_ADJ:GAS:none]
        [DISPLAY_COLOR:7:0:0]
        [MATERIAL_VALUE:1]
        [SPEC_HEAT:420]
        [IGNITE_POINT:10508]
        [MELTING_POINT:NONE]
        [BOILING_POINT:NONE]
        [HEATDAM_POINT:10250]
        [COLDDAM_POINT:9900]
        [MAT_FIXED_TEMP:NONE]
        [SOLID_DENSITY:1520]
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
        [SHEAR_YIELD:600000] used cotton
        [SHEAR_FRACTURE:600000] used cotton
        [SHEAR_STRAIN_AT_YIELD:100000]
        [BENDING_YIELD:10000]
        [BENDING_FRACTURE:10000]
        [BENDING_STRAIN_AT_YIELD:100000]
        [MAX_EDGE:0]
        [ABSORPTION:100]
        [THREAD_PLANT]
        [ITEMS_SOFT]
