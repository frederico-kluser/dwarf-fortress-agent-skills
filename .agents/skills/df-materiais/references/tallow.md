# Tallow

> Fonte: [Tallow](https://dwarffortresswiki.org/index.php/Tallow) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Tallow** is the rendered form of animal fat, made from fat by the 'render fat' job in a kitchen; fat is obtained from butchering animals. Tallow is used to make soap, and can also be used as a low-value solid ingredient for cooking prepared meals. Since tallow does not have quality levels, rendering fat is a good, but slow, way to train a cook.

The standing orders workshop menu includes "Auto-Kitchen" (enabled by default), which will automatically schedule 'render fat' jobs on any available kitchen. Once your dwarves have produced enough tallow to last for years; you may want to disable the "Auto-Kitchen" task to keep your cooks focused on more important jobs. You may want to save your tallow for making soap. Since tallow is often in the kitchen, it tends to be made into prepared meals before other ingredients. This can be a problem if Auto-Kitchen is enabled and you also have a Prepared Meal job set to repeat. Two ways to prevent this are to forbid your supplies of tallow, or disable it from being a cooking ingredient.

- Note: By default, any tallow produced will be eaten. Make sure to uncheck this as a viable food after producing your first bars, if you want to save it for soap.

It is stored in food stockpiles and found under 'fat'. Tallow can be stored without a container, but if barrels are available, dwarves will fill up to 50 units of random tallow in one barrel.

Tallow has the [`[ROTS]`](/index.php/Material_definition_token#ROTS "Material definition token") material token, but never does rot even if not stored in a stockpile.

For real-life information on tallow, view the Wikipedia page.

In all its fatty goodness.

    [MATERIAL_TEMPLATE:TALLOW_TEMPLATE]
        [STATE_COLOR:ALL_SOLID:CREAM]
        [STATE_NAME:ALL_SOLID:tallow]
        [STATE_ADJ:ALL_SOLID:tallow]
        [STATE_COLOR:LIQUID:CREAM]
        [STATE_NAME:LIQUID:melted tallow]
        [STATE_ADJ:LIQUID:melted tallow]
        [STATE_COLOR:GAS:CREAM]
        [STATE_NAME:GAS:n/a]
        [STATE_ADJ:GAS:n/a]
        [DISPLAY_COLOR:6:0:0]
        [MATERIAL_VALUE:1]
        [SPEC_HEAT:4181]
        [IGNITE_POINT:10338]
        [MELTING_POINT:10078]
        [BOILING_POINT:NONE]
        [HEATDAM_POINT:10250]
        [COLDDAM_POINT:9900]
        [MAT_FIXED_TEMP:NONE]
        [SOLID_DENSITY:500]
        [LIQUID_DENSITY:NONE]
        [MOLAR_MASS:NONE]
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
        [SHEAR_YIELD:10000]
        [SHEAR_FRACTURE:10000]
        [SHEAR_STRAIN_AT_YIELD:100]
        [BENDING_YIELD:10000] no data
        [BENDING_FRACTURE:10000]
        [BENDING_STRAIN_AT_YIELD:100]
        [MAX_EDGE:0]
        [ABSORPTION:100]
        [REACTION_CLASS:TALLOW]
        [MATERIAL_REACTION_PRODUCT:SOAP_MAT:LOCAL_CREATURE_MAT:SOAP]
        [IMPLIES_ANIMAL_KILL]
        [STOCKPILE_GLOB]
        [EDIBLE_VERMIN]
        [EDIBLE_COOKED]
        [ROTS]
