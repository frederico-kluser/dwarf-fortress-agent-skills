# Fine pewter

> Fonte: [Fine pewter](https://dwarffortresswiki.org/index.php/Fine_pewter) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Uses**
- **Metal crafting Construction**
- **Recipe**
- **3 Tin bars 1 Copper bar - or - 3 Cassiterite 1 Copper ore**
- **Properties**
- **Material value 5☼ Impact strength 350 MPa Shear strength 100 MPa Not fire-safe Not magma-safe Melting point 10417 °U Boiling point 14648 °U Ignition point none Solid density 7280 kg/m³ Liquid density 6990 kg/m³ Specific heat 210 J/kg·K Color silver**
- **Not fire-safe:** Not magma-safe

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Fine pewter** is an alloy of tin and copper.

Fine pewter can be made using one of the following recipes:

- 3 Tin bars + 1 Copper bar = 4 Fine pewter bars
- 3 Cassiterite + 1 Native copper, Malachite, or Tetrahedrite = 16 Fine pewter bars

Fine pewter has a material value of 5. This represents a significant increase over its component parts (which all have a value of 2), making fine pewter suitable for creating mid-value furniture and items. If you have an abundance of tin, this is the best form of pewter to make.

Note that bronze uses the same ingredients (though in different proportions), has the same material value, and is also useful as a mid-grade weapons material, while bismuth bronze is more valuable. However, you can produce 16 bars of fine pewter with a single unit of fuel (when smelting from ores), giving fine pewter a slight advantage over bronze if fuel is constrained.

Fine pewter jug.

    [INORGANIC:PEWTER_FINE]
        [USE_MATERIAL_TEMPLATE:METAL_TEMPLATE]
        [STATE_NAME_ADJ:ALL_SOLID:fine pewter]
        [STATE_NAME_ADJ:LIQUID:molten fine pewter]
        [STATE_NAME_ADJ:GAS:boiling fine pewter]
        [DISPLAY_COLOR:7:7:1]
        [BUILD_COLOR:7:7:1]
        [MATERIAL_VALUE:5]
        [SPEC_HEAT:210]
        [MELTING_POINT:10417]
        [BOILING_POINT:14684]
        [SOLID_DENSITY:7280]
        [LIQUID_DENSITY:6990]
        [MOLAR_MASS:118710]
        [IMPACT_YIELD:42000]
        [IMPACT_FRACTURE:350000]
        [IMPACT_STRAIN_AT_YIELD:724]
        [COMPRESSIVE_YIELD:42000]
        [COMPRESSIVE_FRACTURE:350000]
        [COMPRESSIVE_STRAIN_AT_YIELD:724] 58
        [TENSILE_YIELD:12000]
        [TENSILE_FRACTURE:100000]
        [TENSILE_STRAIN_AT_YIELD:24] 50
        [TORSION_YIELD:12000]
        [TORSION_FRACTURE:100000]
        [TORSION_STRAIN_AT_YIELD:66]
        [SHEAR_YIELD:12000]
        [SHEAR_FRACTURE:100000]
        [SHEAR_STRAIN_AT_YIELD:66] 18
        [BENDING_YIELD:12000]
        [BENDING_FRACTURE:100000]
        [BENDING_STRAIN_AT_YIELD:24]
        [MAX_EDGE:10000]
        [ITEMS_HARD]
        [ITEMS_METAL]
        [ITEMS_BARRED]
        [ITEMS_SCALED]
        [STATE_COLOR:ALL_SOLID:SILVER]
